from os import system
system("cls || clear")

file = open("matn.txt", "r")
matn = file.read()

chapda = "zaqxswcdevfrbgtZAQXSWCDEVFRBGT12345!@#$%"
ongda = "nhymjukilopNHYMJUKILOP67890-=^&*()_+,./;'[]{<>?:}"

chap = 0
ong = 0
for i in matn:
    if i in chapda:
        chap += 1
    elif i in ongda:
        ong += 1

print("O'ngda bosilgan:", ong)
print("Chapda bosilgan:", chap)

file.close()