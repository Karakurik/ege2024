def solve():
    word = 'КОНЕЦ'
    set1 = set()

    for x1 in word:
        for x2 in word:
            for x3 in word:
                for x4 in word:
                    for x5 in word:
                        set1.add(x1 + x2 + x3 + x4 + x5)

    word = 'ДРАКОН'
    set2 = set()

    for x1 in word:
        for x2 in word:
            for x3 in word:
                for x4 in word:
                    for x5 in word:
                        set2.add(x1 + x2 + x3 + x4 + x5)

    union = set1.union(set2)
    result = union - set1.intersection(set2)

    print(len(result))

solve()
