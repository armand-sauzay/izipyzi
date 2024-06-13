import izipyzi.stats


def test_calculate_statistics():
    numbers = [0.1, 0.2, 0.15, 0.12, 0.18]
    statistics = izipyzi.stats.calculate_statistics(numbers)
    assert statistics["mean"] > 0
    assert statistics["confidence_interval"][0] < statistics["confidence_interval"][1]
