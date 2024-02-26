# пара чисел - два подряд идущих числа. Нужно определить количество элементов в
# котором один из двух делится на 9 и один элемент меньше среднего арифметического всех чётных
# элементов последовательности.
f = open('17.2.txt')
a = [int(s) for s in f]
sum_par = []
chet = [y for y in a if y%2==0]
sred_arifmet = sum(chet)/len(chet)
for i in range(len(a)-1):
    if (((a[i]%9==0 and a[i+1]%9!=0) or (a[i]%9!=0 and a[i+1]%9==0)) and (a[i]<sred_arifmet or a[i+1]<sred_arifmet)):
        sum_par.append(a[i]+a[i+1])
print(len(sum_par), max(sum_par))