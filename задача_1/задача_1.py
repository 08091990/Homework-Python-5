# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def recursion(a, b):
    if b==0:
        return 1
    elif b < 0:
        return 1 / recursion(a, -b)
    elif b % 2 == 0:
        return recursion(a, b//2)**2
    else:
        return a * recursion(a, b - 1)
    
a = 2
b = 5   
result = recursion(a, b)
print(f"{a} в степени {b} = {result}")