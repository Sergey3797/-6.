#Задание №1 c помощью цикла while
N = int(input("Введите количество чисел"))
cnt = 0
i = 0
while i < N:
  number = int(input("Введите числа"))
  if number == 0:
    cnt += 1
  i += 1
print(cnt)    



# Задание №1 с помощью цикла for
N = int(input("Введите количество целых чисел:"))
cnt = 0

for i in range(1,N+1):
  i = int(input())
  if i == 0:
    cnt += 1
print(cnt)
  


# Задание №2 c помощью цикла while
X = int(input("Введите натуральное число X"))
cnt_divisor = 0
i = 1

while i <= X:
  if X % i == 0:
    cnt_divisor += 1 
  i += 1

print("Количество делителей числа X:",cnt_divisor)  



# Задание № 2 с помощью цикла for 
X = int(input("Введите натуральное чсило X"))
cnt_divisor = 0 

for i in range(1,X+1):
  if X % i == 0:
    cnt_divisor += 1
print("Количество делителей числа X",cnt_divisor)



#Задание №3 с помощью цикла while

A = int(input())
B = int(input())

if A % 2 != 0: 
  A += 1
while A <= B:
    print(A)
    A += 2



#Задание №3 с помощью цикла for
A = int(input())
B = int(input())

for i in range(A,B+1):
  if i % 2 == 0:
    print(i)    
