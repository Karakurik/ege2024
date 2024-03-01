def solve():
    M = 1_000_000

    mas = []
    for n in range(M + 1):
        b = f'{n:b}{n % 4:b}'
        r = int(b, 2)
        mas.append(r)
    mas.sort()

    pref = [0]
    for x in mas:
        while (len(pref) < x):
            pref.append(pref[-1])
        pref.append(pref[-1] + 1)

    ans = 0
    for x in range(65, M + 1):
        ans = max(ans, pref[x] - pref[x-65])

    print(ans)

solve()
