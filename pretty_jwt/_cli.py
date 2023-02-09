from __future__ import annotations

import datetime
import json
import sys
from typing import Any

from ._colorizer import Color, colorize
from .pretty_jwt import ParceError, parce as parce


def print_colorized(data: str, color: Color) -> None:
    print(colorize(data, color))


def dict_prettify(data: dict[str, object]) -> str:
    return json.dumps(data, indent=4)


def try_print_timestamp(timestamp: Any, claim_name: str) -> None:
    if not timestamp:
        return

    try:
        timestamp_converted = int(timestamp)
    except ValueError:
        return

    datetime_str = datetime.datetime.fromtimestamp(timestamp_converted)
    print_colorized(f"{claim_name}\t: {datetime_str}", Color.MAGENTA)


def entrypoint() -> None:
    args = sys.argv
    if len(args) != 2:
        print_colorized("Invalid or empty JWT", Color.RED)
        print("\nUsage:\npjwt <JWT>\n")
        sys.exit(1)

    try:
        jwt = parce(args[1])
    except ParceError as e:
        print_colorized(f"Invalid jwt, {e}", Color.RED)
        sys.exit(2)

    print_colorized("Header:", Color.GREEN)
    print(dict_prettify(jwt.header))
    print_colorized("Payload:", Color.GREEN)
    print(dict_prettify(jwt.payload))
    print_colorized("Signature:", Color.GREEN)
    print(jwt.signature)

    exp = jwt.payload.get("exp")
    iat = jwt.payload.get("iat")
    nbf = jwt.payload.get("nbf")

    if any((exp, iat, nbf)):
        print()

    try_print_timestamp(exp, "Expiration Time")
    try_print_timestamp(iat, "Issued At")
    try_print_timestamp(nbf, "Not Before")


if __name__ == "__main__":
    entrypoint()
