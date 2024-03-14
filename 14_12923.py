def solve():
    r = 3 * 3125 ** 9 + 2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
    s = ''
    count = 0
    while r > 0:
        if r % 25 == 0:
            count += 1
        s += str(r % 25)
        r //= 25

    print(s[::-1])
    print(count)


if __name__ == '__main__':
    solve()
