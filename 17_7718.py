def solve():
    with open('17_7718.txt') as file:
        l = []
        for line in file.readlines():
            l.append(int(line))

        ans = []
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                x = l[i]
                y = l[j]

                if ((x + y) % 18 == 0) ^ (y * x % 18 == 0):
                    ans.append(x + y)

        print(len(ans), max(ans))


if __name__ == '__main__':
    solve()

