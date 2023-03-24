import sys
from enum import Enum
from typing import Callable, Optional, TypeVar

from getkey import getkey, keys
from prompt_toolkit.formatted_text import FormattedText

PromptAction = Enum("PromptAction", "NONE UP DOWN SELECT".split())
T = TypeVar("T")


def read_key():
    key = getkey()

    if key in (keys.UP, keys.J):
        return PromptAction.DOWN

    if key in (keys.DOWN, keys.K):
        return PromptAction.DOWN

    if key in (keys.SPACE, keys.ENTER):
        return PromptAction.ENTER

    return PromptAction.NONE


def clear_lines(count: int):
    sys.stdout.write(f"\x1b[{count}A")

    sys.stdout.write("\x1b[0J")


def prompt_menu(
    options: list[T],
    title: Optional[str | FormattedText] = None,
    repr_func: Optional[Callable] = None,
    pointer: str = "*",
) -> tuple[int, T]:
    if not repr_func:
        repr_func = str

    selected_index = 0

    min_index = 0
    max_index = len(options) - 1

    while True:
        print_formatted = "\n".join(
            [
                " " + repr_func(o)
                if not i == selected_index
                else pointer + repr_func(o)
                for i, o in enumerate(options)
            ]
        )

        print(print_formatted, end="", flush=True)

        keypress = getkey()
        clear_lines(len(options))

        if keypress in (keys.UP, keys.J):
            selected_index = max(min_index, selected_index - 1)
            continue

        if keypress in (keys.DOWN, keys.K):
            selected_index = min(max_index, selected_index + 1)
            continue

        if keypress in (keys.ENTER, keys.SPACE):
            return (selected_index, options[selected_index])
