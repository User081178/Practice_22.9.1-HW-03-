
# Функция сортировки чисел по возрастанию

def num_sorting(numbers):
    n = 1
    while n < len(numbers):
        
        for i in range(len(numbers) - 1):
           if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
        n += 1
    return numbers

# Функция поиска позиции 

def bin_search(numbers, num, left, right):
    position = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] < num:
            left = mid + 1
        elif numbers[mid] >= num:
            position = mid
            right = mid - 1

    if position != -1 and position <= len(numbers) - 1:
        return position
    else:
        return -1


while True:
    num_list= input("Введите последовательность чисел (не менее 2-х), разделенных пробелом: ")
    try:
        numbers = list(map(int, num_list.split()))
        
        if len(numbers) < 2:
            print("Ошибка ввода! Пожалуйста, введите как минимум 2 числа.")
            print('----------------------------------')
        else:
            break
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите числа через пробел.")
        print('----------------------------------')

# Сортируем список 
numbers = num_sorting(numbers)


#  Ввод числа пользователем 
while True:
    try:
        num = float(input("Введите любое число: "))
        break
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

index = bin_search(numbers, num, 0, len(numbers) - 1)

 
# Вывод результата обработки данных

if (index - 1) < 0:
    print(f"Введенное число '{num}' не соответвет заданному условию !")
else:
     print(f'Номер позиции элемента списка : [{index - 1}], меньше введенного пользователем числа: {num} в списке {numbers}.')
     print(f"Элемент, больший или равный введенному числу {num}, находится в списке на позиции : [{index}].")
       
   
     
   