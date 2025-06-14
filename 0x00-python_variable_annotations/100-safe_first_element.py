#!/usr/bin/env python3
"""
Duck-typed annotations for safe_first_element function
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise None.
    
    Args:
        lst: A sequence of any type of elements
        
    Returns:
        The first element of the sequence or None if empty
    """
    if lst:
        return lst[0]
    else:
        return None
