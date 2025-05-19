def get_even_numbers(numbers):
    even=[]
    for num in numbers:
        if num%2==0:
            even.append(num)
    return even

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
           if num > max_num:
             max_num = num
    return max_num

def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def quick_sort(numbers):
    if len(numbers) <=1:
        return numbers
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

numbers = []
enter = input("Введите список чисел через запятую: ")
for num in enter.split(','):
        numbers.append(int(num.strip()))

print(f"Четные числа: {get_even_numbers(numbers)}")
print(f"Максимальное число: {find_max(numbers)}")
print(f"Минимальное число: {find_min(numbers)}")
print(f"Отсортированный список: {quick_sort(numbers)}")
