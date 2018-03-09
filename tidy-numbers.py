file = open("B-large-practice.in", "r")

num_tests = int(file.readline().strip())

for test in range(num_tests):
    N = [int(x) for x in list(file.readline().strip())]

    if len(N) != 1:
        for i in range(len(N) - 1):
            if N[i] > N[i+1]:
                for j in range(i + 1, len(N)):
                    N[j] = 9
                for k in range(i, -1, -1):
                    if k - 1 >= 0 and N[k - 1] == N[k]:
                        N[k] = 9
                    else:
                        N[k] -= 1
                        break

                break

        k = 0
        while k < len(N) and N[k] == 0:
            k += 1

        if k == len(N):
            N = [0]
        else:
            N = N[k:]

    res = ''.join([str(x) for x in N])
    print("Case #" + str(test + 1) + ": " + res)