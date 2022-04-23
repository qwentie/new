lst = [int(a) for a in input().split()]
n2 = [i for i in lst if i % 2 == 0]
n3 = [i for i in lst if i % 2 == 1]
print(len(n2), len(n3))
