#!/usr/bin/env python3
"""
This module provides a measure_time function to measure the average runtime
of the wait_n coroutine over n asynchronous tasks.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns the average time per task.

    Args:
        n (int): The number of asynchronous tasks to execute.
        max_delay (int): The maximum delay for each task.

    Returns:
        float: The average time per task.
    """
    start_time = time.time()  # Record the start time
    
    # Run the wait_n coroutine inside an event loop
    asyncio.run(wait_n(n, max_delay))
    
    end_time = time.time()  # Record the end time
    
    # Calculate the total elapsed time
    total_time = end_time - start_time
    
    # Return the average time per task
    return total_time / n
