#!/usr/bin/env python3
"""list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of all nums inside a list"""
    a: float = 0.0
    for j in input_list:
        a += j
    return a
