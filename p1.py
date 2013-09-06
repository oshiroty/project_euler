def multiples_of_3_and_5(max_num):
    return (n for n in xrange(max_num) if not (n % 3 and n % 5))

print sum(multiples_of_3_and_5(1000))
