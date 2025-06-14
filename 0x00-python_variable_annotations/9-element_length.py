#!/usr/bin/env python3
"""Type-annotated function that returns element lengths"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    containing each sequence and its length.
    
    Args:
        lst: An iterable of sequences (strings, lists, tuples, etc.)
        
    Returns:
        A list of tuples where each tuple contains:
        - The original sequence
        - The length of that sequence as an integer
    """
    return [(i, len(i)) for i in lst]
