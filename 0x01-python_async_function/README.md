# Python Async Function Project

This project explores asynchronous programming in Python using the `asyncio` library. It includes several modules to demonstrate how coroutines, tasks, and asynchronous functions work. The goal is to implement functions that execute asynchronously and efficiently handle multiple I/O-bound tasks.

## Project Structure

The project contains the following files:

### 1. `0-basic_async_syntax.py`
- **Purpose**: This file contains the `wait_random` coroutine, which asynchronously waits for a random delay between 0 and a specified maximum delay (`max_delay`) and returns the actual delay.
- **Function**:
  ```python
  async def wait_random(max_delay: int) -> float
