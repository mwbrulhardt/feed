

from feed.core import Stream

from tests.utils.ops import assert_op


def test_reduce_sum():

    s1 = Stream.source([1, 2, 3, 4, 5, 6, 7], dtype="float").rename("s1")
    s2 = Stream.source([7, 6, 5, 4, 3, 2, 1], dtype="float").rename("s2")

    w = Stream.reduce([s1, s2]).sum().rename("w")

    expected = [8, 8, 8, 8, 8, 8, 8]

    assert_op([w], expected)
