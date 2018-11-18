import random, sys, copy, time, timeit, matplotlib, os
import matplotlib.pyplot as plt
import threading



def find_smallest(a_list):
    smallest = a_list[0]
    smallest_i = 0
    for i, num in enumerate(a_list):
        if num < smallest:
            smallest = num
            smallest_i = i
    return smallest_i


def find_kth_smallest_O_n(a_list, k):
    count = 0
    while count < (k - 1):
        a_list.pop(find_smallest(a_list))
        count += 1
    return a_list.pop(find_smallest(a_list))


def find_kth_smallest_O_nlogn(a_list, k):
    a_list.sort()
    return a_list[k - 1]



class time_algorithm(threading.Thread):
    def __init__(self, values, timer, *args, **kwargs):
        super().__init__()
        self.timer = timer
        self.values = values
        self.times = list()
        self.progress = 0

    def run(self):
        for i, size in enumerate(self.values, start=1):
            self.progress = i
            self.a_list = [ random.randint(0,1000) for i in range(size) ]
            self.times.append(self.timer.timeit(number=10))
        


k = 3

x_axis = list(range(1000, 1000000, 10000))

O_n_timer = timeit.Timer('find_kth_smallest_O_n(threads[0].a_list, k)',
                         'from __main__ import threads, k, find_kth_smallest_O_n')

O_nlogn_timer = timeit.Timer('find_kth_smallest_O_nlogn(threads[1].a_list, k)',
                             'from __main__ import threads, k, find_kth_smallest_O_nlogn')

threads = [time_algorithm(x_axis, O_n_timer), time_algorithm(x_axis, O_nlogn_timer)]

for i, t in enumerate(threads, start=1):
    print(f'starting thread {i}')
    t.start()

fig, ax = plt.subplots()

while True:
    print(u'\u001b[2A\u001b[1000D', end='')
    
    at_least_1_alive = False

    for i, t in enumerate(threads, start=1):
        if t.progress == len(x_axis):
            print(f'Thread {i} complete     ', ' '*len(str(t.progress)),
                   '    ', ' '*len(str(len(x_axis))), '[', '='*101, ']\n',
                   sep='', end='')
        else:
            bars = int((t.progress / len(x_axis))*100) - 1
            spaces = 100 - bars
            print(f'Thread {i} running test {t.progress} of {len(x_axis)} [',
                   '='*bars, '>', ' '*spaces, ']\n', sep='', end='')
        
        if i == len(threads):
            time.sleep(0.5)
        
        if t.is_alive():
            at_least_1_alive = True
    
    if not at_least_1_alive:
        break

print('plotting data...')
ax.plot(x_axis, threads[0].times)
ax.plot(x_axis, threads[1].times)
plt.show()
