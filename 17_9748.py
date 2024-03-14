def solve():
    with open('17_9748.txt') as file:
        l = []
        for line in file.readlines():
            l.append(int(line))
        # print(l)

        mx = 0
        for m in l:
            if m % 100 == 15:
                mx = max(mx, m)

        ans = []
        for i in range(len(l) - 2):
            x = l[i]
            y = l[i + 1]
            z = l[i + 2]

            cou = 0
            if len(str(x)) == 4:
                cou += 1

            if len(str(y)) == 4:
                cou += 1

            if len(str(z)) == 4:
                cou += 1

            sm = x + y + z
            if sm > mx and cou == 1:
                ans.append(sm)

        print(len(ans), end=' ')
        print(max(ans))


if __name__ == '__main__':
    solve()
