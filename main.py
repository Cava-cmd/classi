from ContoBancario import ContoBancario
import random, math

p1 = ContoBancario("persona 1", " ", 0)
p2 = ContoBancario("persona 2", " ", 1)
p3 = ContoBancario("persona 3", " ", 2)

for i in range(13):
    somma = math.floor(random.random()*10)
    if(i == 3 or i == 6 or i == 9 or i == 12):
        p1.versa(somma)
        p2.preleva(somma)
    elif(i == 1 or i == 4 or i == 7 or i == 10):
        p2.versa(somma)
        p3.preleva(somma)
    elif(i == 2 or i == 5 or i == 8 or i == 11):
        p1.versa(somma)
        p3.preleva(somma)

print(p1.getSaldo())
print(p2.getSaldo())
print(p3.getSaldo())