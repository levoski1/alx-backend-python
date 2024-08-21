#!/usr/bin/env python3
"""
This module provides a function task_wait_random that returns an asyncio.Task.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio Task that wraps the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to be passed to wait_random.

    Returns:
        asyncio.Task: The task created to run wait_random.
    """
    # Schedule the wait_random coroutine as an asyncio Task
    task = asyncio.create_task(wait_random(max_delay))
    
    return task

