# Walkthrough

The `feed` package provides useful tools when building small scale streaming operations. The primary reason for using this package is to help build the mechanisms that generate observations from an environment. Therefore, it is fitting that their primary location of use is in the `Observer` component. The `Stream` API provides the granularity needed to connect specific data sources to the `Observer`.

## What is a `Stream`?
A `Stream` is the basic building block for the `DataFeed`, which is also a stream itself. Each stream has a name and a data type and they can be set after the stream is created.  Streams can be created through the following mechanisms:
* generators
* iterables
* sensors
* direct implementation of `Stream`

For example, if you wanted to make a stream for a simple counter. We will make it such that it will start at 0 and increment by 1 each time it is called and on `reset` will set the count back to 0. The following code accomplishes this functionality through creating a generator function.

```py
from feed import Stream

def counter():
    i = 0
    while True:
        yield i
        i += 1

s = Stream.source(counter)
```

In addition, you can also use the built-in `count` generator from the `itertools` package.

```py
from itertools import count

s = Stream.source(count(start=0, step=1))
```

These will all create infinite streams that will keep incrementing by 1 to infinity. If you wanted to make something that counted until some finite number you can use the built in `range` function.

```py
s = Stream.source(range(5))
```

This can also be done by giving in a `list` directly.

```py
s = Stream.source([1, 2, 3, 4, 5])
```

The direct approach to stream creation is by sub-classing `Stream` and implementing the `forward`, `has_next`, and `reset` methods. If the stream does not hold stateful information, then `reset` is not required to be implemented and can be ignored.

```py
class Counter(Stream):

    def __init__(self):
        super().__init__()
        self.count = None

    def forward(self):
        if self.count is None:
            self.count = 0
        else:
            self.count += 1
        return self.count

    def has_next(self):
        return True

    def reset(self):
        self.count = None

s = Counter()
```


## Using Data Types
The purpose of the data type of a stream, `dtype`, is to add additional functionality and behavior to a stream such that it can be aggregated with other streams of the same type in an easy and intuitive way.

Since the most common data type is `float` in these tasks, the following is a list of supported special operations for it:
* Let `s`, `s1`, `s2` be streams.
* Let `c` be a constant.
* Let `n` be a number.
* Unary:
    * `-s`, `s.neg()`
    * `abs(s)`, `s.abs()`
    * `s**2`, `pow(s, n)`
* Binary:
    * `s1 + s2`, `s1.add(s2)`, `s + c`, `c + s`
    * `s1 - s2`, `s1.sub(s2)`, `s - c`, `c - s`
    * `s1 * s2`, `s1.mul(s2)`, `s * c`, `c * s`
    * `s1 / s2`, `s1.div(s2)`, `s / c`, `c / s`


There are many more useful functions that can be utilized, too many to list in fact. You can find all of the. however, in the API reference section of the documentation.
