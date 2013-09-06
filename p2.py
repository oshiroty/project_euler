def fibonacci(max_num):
    (x, y) = (1, 2)
    while x <= max_num:
        yield x
        (x, y) = (y, x + y)

def even(gen):
    for i, num in enumerate(gen):
        if not (i + 2) % 3:
            yield num

print sum(even(fibonacci(4000000)))
