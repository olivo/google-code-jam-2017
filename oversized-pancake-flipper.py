file = open("A-large-practice.in", "r")

num_tests = int(file.readline().strip())

for test in range(num_tests):
    pancakes, k = file.readline().strip().split(" ")
    pancakes = list(pancakes)
    k = int(k)

    num_flips = 0
    premature_ending = False

    for i in range(len(pancakes)):
        if pancakes[i] == '-':
            num_flips += 1

            for j in range(i, i + k):
                if j >= len(pancakes):
                    premature_ending = True
                    break

                pancakes[j] = '+' if pancakes[j] == '-' else '-'

        if premature_ending:
            break

    if not premature_ending:
        print("Case #" + str(test + 1) + ": " + str(num_flips))
    else:
        print("Case #" + str(test + 1) + ": IMPOSSIBLE")