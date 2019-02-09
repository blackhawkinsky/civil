import math
''' hello guys this is file to design a square column '''
while True:
    load = float(input("load in kN = "))
    Fy = float(input("tell me steel bar type = "))
    Fc = float(input("Give concrete grade in MPa = "))
    p = load * 1.5
    x = 0
    print("Factored load = ",p," kN (Safety factored is 1.5)","\nIt is assumed that exmin and eymin bith are less than 0.05D so","\np = 0.4*Fck*Ac+0.67*Fy*As","\nLets assume that side of column is D and steel  quantity is 1% of total area")

    e = math.sqrt((p * 1000) / ((0.4 * Fc * 0.99) + (0.67 * Fy * 0.01)))
    def mod(a):
        b = round(a)
        while True:
            c = b % 10
            if c == 0:
                return b
                break
            else:
                b = b + 1
                continue
    D = mod(e)
    #print(D)
    As = int(0.01*D*D)
    Ac = int(0.99*D*D)
    def round_off(n):
        c = n * 100000
        k = int(round(n)) * 100000
        # print(k)
        if int(k) << int(c):
                    k = k / 100000
                    k = k + 1
                    return k
        # elif float(k) == int(c):
        #	k = k/100000
        #	print(k)
        else:
            k = k / 100000
            return k
            print(k)
    while True:
        d = float(input("What dia of steel you have? tell me in mm = "))
        n = float((As * 4) / (3.1416 * d * d))
        print(n)
        n = round_off(int(n))


        def max_tie_dia():
            if d / 4 > 6:
                t = d / 4
                T = round_off(t)
                print("Dia of tie bar is = ",T," mm")
            else:
                T = 6

        def min_spacing():
            if 16 * d < 300:
                if 16*c<<D:
                    s = 16 * d
                    s = mod(s)
                else:
                    s =D
                    s =mos(s)
            else:
                s = 300
            print("Spacing for tie bar = ", s, " mm with clear cover of 40 mm")

        print("Side of column = ", D, " mm","\nno of bar ", n,"\nDia of main bar = ", d, " mm")
        max_tie_dia()
        min_spacing()
        sat = input()
        if sat == "y":
            break
        else:
            continue
    break


