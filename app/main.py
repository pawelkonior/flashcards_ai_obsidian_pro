from typing import Any, cast


def add(a: int, b: int) -> Any:
    return None if a > 42 else 42


x: float = cast(float, add(1, 2))

result: Any = x + 42