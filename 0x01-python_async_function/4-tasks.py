#!/usr/bin/env python3
"""
This module provides a task_wait_n function which is similar to wait_n but uses task_wait_random.
"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawns n tasks using task_wait_random and returns a list of delays
    in ascending order.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay for each task.

    Returns:
        list[float]: List of delays in ascending order.
    """
    # Create a list of asyncio Tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Gather all tasks and await their completion
    delays = await asyncio.gather(*tasks)
    
    # Return the sorted list of delays
    return sorted(delays)
