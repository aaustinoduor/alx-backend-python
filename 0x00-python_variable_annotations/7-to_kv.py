#!/usr/bin/env python3
"""type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns tuple of a string and a float"""
    t = v ** 2
    return (k, t)
