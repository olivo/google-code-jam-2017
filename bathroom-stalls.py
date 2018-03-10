import heapq
import math

def split(value):

    n = value >> 1

    return (n, n-1) if value % 2 == 0 else (n, n)

file = open("C-large-practice.in", "r")

num_tests = int(file.readline().strip())

for test in range(num_tests):
    N, K = file.readline().strip().split()
    N = int(N)
    K = int(K)

    q = []
    C = dict()
    C[N] = 1
    P = 0
    S = set([N])

    heapq.heappush(q, (N, N))

    while True:
        #print("Intervals: " + str(q))

        x = heapq.heappop(q)[1]
        S.remove(x)

        x0, x1 = split(x)
        #x0 = math.ceil((x - 1) / 2)
        #x1 = math.floor((x - 1) / 2)
        P += C[x]

        if P >= K:
            print("Case #" + str(test + 1) + ": " + str(x0) + " " + str(x1))
            break
        else:
            if x0 not in S:
                heapq.heappush(q, (-x0, x0))
                S.add(x0)

            if x1 not in S:
                heapq.heappush(q, (-x1, x1))
                S.add(x1)

            C[x0] = C.get(x0, 0) + C[x]
            C[x1] = C.get(x1, 0) + C[x]