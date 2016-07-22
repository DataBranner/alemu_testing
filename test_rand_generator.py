import rand_generator as RG

def test_always_larger():
    """Test that second number is always larger than first"""
    g = RG.larger_random()
    first = next(g)
    second = next(g)
    assert second > first


def test_in_range_0_1():
    """Test that output is always in range (0, 1)"""
    g = RG.larger_random()
    assert 0 <= next(g) <= 1

def test_never_same():
    """Test that in 20 calls there are no duplicates"""
    g = RG.larger_random()
    hundred_calls = set([next(g) for _ in range(20)])
    assert len(hundred_calls) == 20
