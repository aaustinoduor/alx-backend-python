#!/usr/bin/env python3
"""advanced type annotated function"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """More annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
