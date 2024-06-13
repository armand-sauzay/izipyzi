from izipyzi.time import time_function_by_tries, time_function_by_duration
import pytest


@pytest.fixture
def func():
    def func():
        return 1

    return func


def test_time_function_by_tries(func):
    times = time_function_by_tries(func, tries=3)
    assert len(times) == 3
    assert all(isinstance(time, float) for time in times)


def test_time_function_by_duration(func):
    times = time_function_by_duration(func, duration=0.1)
    assert all(isinstance(time, float) for time in times)
    assert sum(times) > 0
