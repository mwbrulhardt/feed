
# Quickstart


### Installation
Install `canapi` from PyPi using:
```bash
pip install feed-stream
```

### Make a Feed
The following example shows how to make a streaming Fibonacci Sequence:

```py
from feed import Stream, DataFeed

s = Stream.source(range(1000), dtype="float").rename("natural_numbers")
f1 = s.lag(1).rename("f(n-1)")
f2 = s.lag(1).rename("f(n-2)")

f = (f1 + f2).rename("fibonacci")

feed = DataFeed([s])
```

If you would like to know more go through our more thorough walkthrough!
