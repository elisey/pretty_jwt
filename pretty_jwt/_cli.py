from __future__ import annotations

import json
import sys

from ._colorizer import Color, colorize
from .pretty_jwt import ParceError, parce as parce


def print_colorized(data: str, color: Color) -> None:
    print(colorize(data, color))


def dict_prettify(data: dict[str, object]) -> str:
    return json.dumps(data, indent=4)


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


if __name__ == "__main__":
    entrypoint()
