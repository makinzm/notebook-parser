
from nparse.tmp import tmp


def test_basic():
    result_0: int = tmp(0)
    assert result_0 == 1
    result_1: int = tmp(1)
    assert result_1 == 0
