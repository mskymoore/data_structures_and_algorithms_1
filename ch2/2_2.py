import random, time, sys

# timing decorator
def timeit(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'elapsed time for {func.__name__}: {t2 - t1:4.6f}')
        return result
    return wrapper


# assuming no negtive numbers

@timeit
def linear(a_list):
    smallest = a_list[0] 
    for num in a_list:
        if num < smallest:
            smallest = num
    return smallest, a_list.index(smallest)


@timeit
def n_squared(a_list):
    smallest = a_list[0]
    for num_a in a_list:
        for num_b in a_list:
            if num_a < num_b and num_a < smallest:
                smallest = num_a
    return smallest, a_list.index(smallest)


# accept list size from cmd line, or default to 100
if len(sys.argv) == 2 and sys.argv[1].isdecimal():
    size = int(sys.argv[1])
else:
    size = 100

# generate list of size random ints from 0 to 100
a_list = [random.randint(0, 100) for i in range(size)]

# print the generated list in rows of 10
print('index:   0   1   2   3   4   5   6   7   8   9',end='')
for i, num in enumerate(a_list, start=1):
    if (i - 1) % 10 == 0:
        print()
        print(f'{i-1:2d}-{i+8:2d}: ', end='')
    print(f'{num:3d} ', end='')

print()
lin_res = linear(a_list)
print(f'smallest: {lin_res[0]}, index: {lin_res[1]}')
n_sq_res = n_squared(a_list)
print(f'smallest: {n_sq_res[0]}, index: {n_sq_res[1]}')


