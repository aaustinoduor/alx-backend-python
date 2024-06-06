#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return a sum of all nums inside a list"""
    a: float = 0.0
    for k in mxd_lst:
        a += k
    return a
