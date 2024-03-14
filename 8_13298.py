def solve():
    mas = sorted('ПРИВЫЧКА')
    target = {'П', 'Р', 'В', 'Ч', 'К'}
    cou = 0
    real_cou = 0
    for x1 in mas:
        for x2 in mas:
            for x3 in mas:
                for x4 in mas:
                    for x5 in mas:
                        cou += 1

                        if cou % 5 != 0:
                            real_cou += 1
                            s = {x1, x2, x3, x4, x5}
                            if len(s) == 5 and all(x in s for x in target):
                                print(real_cou)
                                return


if __name__ == '__main__':
    solve()
