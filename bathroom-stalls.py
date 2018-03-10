file = open("C-small-practice-2.in", "r")

num_tests = int(file.readline().strip())

for test in range(num_tests):
    N, K = file.readline().strip().split()
    N = int(N)
    K = int(K)

    stalls = [(0, 0, 0) for x in range(N + 2)]

    stalls[0] = (1, 0, 0)
    stalls[N + 1] = (1, 0, 0)

    for i in range(1, N + 1):
        stalls[i] = (0, i - 1, N - i)

    #if test == 0:
    #    print("\n\nTest: " + str(test))
    for i in range(K):
        #if test == 0:
        #    print(stalls)
        best_val = -1
        best_index = -1

        for j in range(1, N + 1):
            if stalls[j][0] == 0 and best_val < min(stalls[j][1], stalls[j][2]):
                best_val = min(stalls[j][1], stalls[j][2])
                best_index = j

        candidate_slots = []

        for j in range(1, N + 1):
            if min(stalls[j][1], stalls[j][2]) == best_val:
                candidate_slots.append((j, stalls[j]))

        best_val = -1
        best_index = -1

        for index, stall in candidate_slots:
            if max(stall[1], stall[2]) > best_val and stall[0] == 0:
                best_val = max(stall[1], stall[2])
                best_index = index

        stalls[best_index] = (1, stalls[best_index][1], stalls[best_index][2])

        if i == K - 1:
            max_val = max(stalls[best_index][1], stalls[best_index][2])
            min_val = min(stalls[best_index][1], stalls[best_index][2])
            break

        for left_index in range(best_index - 1, -1, -1):
            stalls[left_index] = (stalls[left_index][0],
                                  stalls[left_index][1],
                                  min(best_index - left_index - 1, stalls[left_index][2]))
            if stalls[left_index][0] == 1:
                break

        for right_index in range(best_index + 1, N + 1):
            stalls[right_index] = (stalls[right_index][0],
                                   min(right_index - best_index - 1, stalls[right_index][1]),
                                   stalls[right_index][2])
            if stalls[right_index][0] == 1:
                break

    print("Case #" + str(test + 1) + ": " + str(max_val) + " " + str(min_val))