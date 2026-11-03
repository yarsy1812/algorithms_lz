#создаем список из ста чисел с рандомными значениями от 1 до 1 млн
import random 
#задаем пустой список
nesort = []
for i in range(100):
    a = random.randint(0, 1000000)
    #добавляем найденное значение в список
    nesort.append(a)
    #выводим список
print(nesort)

#задаем счетчик итераций
b=0
#создаем второй список
sort = nesort
#добавляем флаг чтобы остановить цикл
stop = True
while stop is True:
    stop = False
    for i in range(0, len(sort) - 1):
        if sort[i] < sort[i + 1]:
            #если выполняется условие меняем местами элементы
            swap = sort[i]
            sort[i] = sort[i + 1]
            sort[i + 1] = swap
            #прибавлем в счетчик одну итерацию
            b=b+1
            stop = True
            #выводим промежуточное значение списка при пузырьке
        print(sort)

#задаем счетчик итераций
c=0
#создаем второй список
sortv = nesort
sortv = []
#начинаем цикл итераций
while len(nesort) > 0:
    max = nesort[0]
    for i in range(0, len(nesort)):
        if nesort[i] > max:
            max = nesort[i]
    sortv.append(max)
    nesort.remove(max)
    #прибавлем в счетчик одну итерацию
    c=c+1
    #выводим промежуточное значение списка при выборке
    print(sortv)

#выводим список 
print("сортированный пузырьком список",sort)
#выводим кол-во сравнений пузырька
print("кол-во сравнений пузырька",b)
#выводим кол-во сравнений выборки
print("кол-во сравнений выборки",c)