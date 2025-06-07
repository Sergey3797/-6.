# задание 1
N = int(input("Введите количество чисел: "))
count_zero = 0

for i in range(N):
  num = int(input(f"Введите число {i + 1}: "))
  if num == 0:
    count_zero += 1

print(f"Количество чисел, равных нулю: {count_zero}")


# задание 2

X = int(input("Введите натуральное число X: "))
count = 0
sqrt_X = int(X ** 0.5)  

for i in range(1, sqrt_X + 1):
  if X % i == 0:
    if i * i == X:  
      count += 1
    else:
      count += 2  

print(f"Количество натуральных делителей числа {X}: {count}")


# задание 3

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

first = True  
for num in range(A, B + 1):
  if num % 2 == 0:
    if not first:
      print(" ", end="")  
    print(num, end="")
    first = False  

print()  
