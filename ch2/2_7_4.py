import random, sys, copy, time, timeit, matplotlib, os, threading
import matplotlib.pyplot as plt


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
    def __init__(self, values, timer, name, *args, **kwargs):
        super().__init__()
        self.name = name
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

threads = [time_algorithm(x_axis, O_n_timer, 'O(n)'),
           time_algorithm(x_axis, O_nlogn_timer, 'O(nlog(n))')]

num_threads = len(threads)
len_x_axis = len(x_axis)
len_str_len_x_axis = len(str(len_x_axis)
for i, t in enumerate(threads, start=1):
    print(f'Starting thread {i} of {num_threads}: {t.name}\n')
    t.start()
    while True:
        print(u'\u001b[A\u001b[1000D', end='')
        
        if t.progress == len_x_axis:
            print(f'Thread {i} complete      ', ' '*len(str(t.progress)),
                   '    ', ' '*len_str_len_x_axis, '[', '='*101, ']\n',
                   sep='', end='')
        else:
            bars = int((t.progress / len_x_axis)*100) - 1
            spaces = 100 - bars
            print(f'Thread {i} running test {t.progress} of {len(x_axis)} [',
                   '='*bars, '>', ' '*spaces, ']\n', sep='', end='')
        
      
        t.join(timeout=0.5)
        
        if not t.is_alive():
            break

print('plotting data...')
fig, ax = plt.subplots()
ax.set_xlabel('n (list size)')
ax.set_ylabel('execution time (seconds)')
ax.set_title('kth smallest item in a list')
ax.plot(x_axis, threads[0].times, 'r')
ax.plot(x_axis, threads[1].times, 'b')
ax.legend([threads[0].name, threads[1].name])
# fig.savefig('kth_smallest_fig.png')
plt.show()
