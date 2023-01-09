import base64
import binascii
import dataclasses
import json
from json import JSONDecodeError


class ParceError(Exception):
    pass


@dataclasses.dataclass
class ParcedJwt:
    header: dict[str, object]
    payload: dict[str, object]
    signature: str


def _decode_base64(raw: str) -> str:
    raw_bytes = raw.encode("utf-8")
    rem = len(raw_bytes) % 4
    if rem > 0:
        raw_bytes += b"=" * (4 - rem)
    try:
        result = base64.b64decode(raw_bytes).decode("utf-8")
    except binascii.Error as e:
        raise ParceError(f"Error decode base64 data. {e}")
    return result


def _from_json(json_str: str) -> dict[str, object]:
    try:
        result: dict[str, object] = json.loads(json_str)
    except JSONDecodeError as e:
        raise ParceError(f"Error parce JSON. {e}")
    return result


def parce(jwt: str) -> ParcedJwt:
    try:
        header_raw, payload_raw, signature = jwt.split(".")
    except ValueError:
        raise ParceError("Invalid JWT format")
    header = _from_json(_decode_base64(header_raw))
    payload = _from_json(_decode_base64(payload_raw))

    return ParcedJwt(header, payload, signature)
