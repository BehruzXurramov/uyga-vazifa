from os import system
system("cls || clear")

n = input("N = ")
soni = 0
for i in n:
    if i == '0':
        soni += 1
    else:
        break
print("Nollar:", soni)