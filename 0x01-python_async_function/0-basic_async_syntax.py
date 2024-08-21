#!/usr/bin/env python3

import random
import asyncio
from typing import float

async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (float): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
