import random 
list = []
while len(list) < 100:
    a = random.randint(0, 1000000)
    
    if a not in list:
        list.append(a)
list.sort()
print(list)

a=0
print("введите значение")
element=int(input())
for i in range(1,len(list)):
    if list[i]==element:
     a+=1
     print(i)
     break
if a==0 :print("элемент не находится в списке")



