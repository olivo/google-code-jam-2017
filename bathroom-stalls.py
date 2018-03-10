import heapq
import math

def split_interval(interval):

    res = interval >> 1

    if interval % 2 == 0:
        return (res, res - 1)
    else:
        return (res, res)

file = open("C-large-practice.in", "r")

num_tests = int(file.readline().strip())

for test in range(num_tests):
    N, K = file.readline().strip().split()
    N = int(N)
    K = int(K)

    q = []
    occurrences = dict()
    occurrences[N] = 1
    filled_stalls = 0
    pending_intervals = set([N])

    heapq.heappush(q, (N, N))

    while True:
        largest_interval = heapq.heappop(q)[1]
        pending_intervals.remove(largest_interval)

        large_subinterval, small_subinterval = split_interval(largest_interval)
        filled_stalls += occurrences[largest_interval]

        if filled_stalls >= K:
            print("Case #" + str(test + 1) + ": " + str(large_subinterval) + " " + str(small_subinterval))
            break
        else:
            if large_subinterval not in pending_intervals:
                heapq.heappush(q, (-large_subinterval, large_subinterval))
                pending_intervals.add(large_subinterval)

            if small_subinterval not in pending_intervals:
                heapq.heappush(q, (-small_subinterval, small_subinterval))
                pending_intervals.add(small_subinterval)

            occurrences[large_subinterval] = occurrences.get(large_subinterval, 0) + occurrences[largest_interval]
            occurrences[small_subinterval] = occurrences.get(small_subinterval, 0) + occurrences[largest_interval]