from os import system
system("cls || clear")

n = int(input("N = "))

soni = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while n > 0:
    soni[n % 10] += 1
    n //= 10

for i in range(10):
    if soni[i]:
        print(f"{i} - {soni[i]}")