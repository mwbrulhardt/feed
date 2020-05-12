
from feed.core.base import Stream

from feed.api.boolean import Boolean


@Boolean.register(["invert"])
def invert(s: "Stream[bool]") -> "Stream[bool]":
    return s.apply(lambda x: not x).astype("bool")
