#!/usr/bin/env python3
"""basic async syntax"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    implements async and wait a random number of minutes
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
