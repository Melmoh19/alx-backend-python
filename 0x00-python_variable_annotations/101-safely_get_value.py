#!/usr/bin/env python3
"""
Type annotations with TypeVar for safely_get_value function
"""
import typing

T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default: typing.Union[T, None] = None) -> typing.Union[typing.Any, T]:
    """
    Safely gets a value from a mapping with a default fallback.
    
    Args:
        dct: A mapping (dict-like object)
        key: The key to look up (can be any type)
        default: Default value to return if key not found
        
    Returns:
        The value from the mapping or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
