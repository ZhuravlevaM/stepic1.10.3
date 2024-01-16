n = int(input())
numbers = []
Even = [] #четное
Odd = [] #нечетное
finaly_numbers = []
while n >0: #цикл где мы вводим числа определяем принадлежность и добавляем в нужный список
    num = int(input())
    numbers.append(num)
    if num%2 == 0:
        Even.append(num)
    else:
        Odd.append(num)
    n -= 1
#min_Even = min(Even)# определяем минимальное значение в каждом списке
#min_Odd = min(Odd)
if len(Even) == 0:
    min_Even = 0
else:
    min_Even = min(Even)
if len(Odd) == 0:
    min_Odd = 0
else:
    min_Odd = min(Odd)
sum_min_even_min_odd = min_Even + min_Odd #сумму минимального нечетного и минимального четного элементов
for i in numbers: # цикл для вывода конечного списка
    if i < sum_min_even_min_odd:
        finaly_numbers.append(i + sum_min_even_min_odd)#увеличьте все элементы набора, меньшие M, на M
    elif i > sum_min_even_min_odd:
        finaly_numbers.append(i)
print(*finaly_numbers, sep=' ')#Выведите элементы обработанного набора чисел через пробел.
