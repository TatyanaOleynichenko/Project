import random
list=[random.randint(0,9) for i in range(8)]
print(list)
number=int(input("сколько цифр"))
a=0
for i in list:
    if i==number:
        a+=1
if a>=1:
    print("Количество", number, "=", a)
if a<1:
    print("такого числа в списке нет")