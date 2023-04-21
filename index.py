n = int(input("Qual tabuada você deseja realizar? "))
p = 1
while p < 11:
    t = n * p
    print("{} x {} = {}".format(n, p, t))
    p = p + 1
