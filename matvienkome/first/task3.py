"""Ввести 2 числа, вивести числа між ними, що діляться на 3"""

a=int(input("enter 1:"))
b=int(input("enter 2:"))
for n in range(a,b+1):
    if n % 3==0:
        print(n)