
import timeit

# List speed test
print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', number=10000000))

# Tuple speed test

print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', number=10000000))

# Tuples are faster wow