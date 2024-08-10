from os import system
from json import dumps
system("cls || clear")

def market(l: list, n: int) ->list:
    lst = list()
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j]["price"] > l[i]["price"]:
                l[i], l[j] = l[j], l[i]
    for i in range(n):
        lst.append(l[i])
    return lst

l = [
    {"name":"go'sht", "price":100},
    {"name":"asal", "price":138},
    {"name":"guruch", "price":22},
    {"name":"olma", "price":5},
]

n = int(input("Qimmatroq = "))

lst = market(l, n)
print(dumps(lst, indent=2))