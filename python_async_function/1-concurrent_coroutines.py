#!/usr/bin/env python3
"""add - sum a and b"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function to add operator ..................................."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
