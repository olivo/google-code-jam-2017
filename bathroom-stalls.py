import heapq

file = open("C-large-practice.in", "r")

num_tests = int(file.readline().strip())

for test in range(num_tests):
    N, K = file.readline().strip().split()
    N = int(N)
    K = int(K)

    q = []


    heapq.heappush(q, ((N, 1), (1, N)))

    for i in range(K):
        #print("Intervals: " + str(q))

        q_element = heapq.heappop(q)[1]

        interval_len = q_element[1] - q_element[0] + 1
        current_left_ls = 0
        current_right_ls = 0

        #print("Interval: " + str(q_element))
        #print("Interval length: " + str(interval_len))

        if interval_len > 1:
            midpoint = (q_element[0] + q_element[1]) // 2
            #print("Start: " + str(q_element[0]))
            #print("End: " + str(q_element[1]))
            #print("Midpoint: " + str(midpoint))

            if q_element[0] < midpoint:
                heapq.heappush(q, ((-(midpoint - q_element[0]), q_element[0]),(q_element[0], midpoint - 1)))
                current_left_ls = midpoint - q_element[0]
            if q_element[1] > midpoint:
                heapq.heappush(q, ((-(q_element[1] - midpoint), midpoint + 1),(midpoint + 1, q_element[1])))
                current_right_ls = q_element[1] - midpoint

    print("Case #" + str(test + 1) + ": " + str(max(current_left_ls, current_right_ls)) \
                                          + " " + str(min(current_left_ls, current_right_ls)))