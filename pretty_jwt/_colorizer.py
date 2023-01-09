import enum


class Color(enum.Enum):
    RED = enum.auto()
    GREEN = enum.auto()
    YELLOW = enum.auto()
    BLUE = enum.auto()
    MAGENTA = enum.auto()
    CYAN = enum.auto()


def colorize(message: str, color: Color) -> str:
    color_codes = {
        Color.RED: "\033[1;31m",
        Color.GREEN: "\033[1;32m",
        Color.YELLOW: "\033[1;33m",
        Color.BLUE: "\033[1;34m",
        Color.MAGENTA: "\033[35m",
        Color.CYAN: "\033[1;36m",
    }
    color_end_code = "\033[0m"

    return color_codes[color] + message + color_end_code
