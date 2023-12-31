#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def recursion_sum(a, b):
    if b == 0:
        return a
    else:
        return recursion_sum(a + 1, b - 1) 
    
print(recursion_sum(2, 2))    
print(recursion_sum(5, 17))