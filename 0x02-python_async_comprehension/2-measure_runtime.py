#!/usr/bin/env python3
"""runs async_compehension 4 times"""
import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures total runtime of running
    async_comprehension 4 times in parallel.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
