from pybox.stats import calculate_statistics


def test_calculate_statistics():
    numbers = [0.1, 0.2, 0.15, 0.12, 0.18]
    statistics = calculate_statistics(numbers)
    assert statistics["mean"] > 0
    assert statistics["confidence_interval"][0] < statistics["confidence_interval"][1]
