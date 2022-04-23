def a(n):
    return n % 2

lst = [int(i) for i in input().split()]
lst_a = list(map(a, lst))
print(lst_a.count(0), lst_a.count(1))
