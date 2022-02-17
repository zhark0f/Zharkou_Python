my_line = input("Введите числа в строку через пробел(ы): ").split()
my_list = []
for i in my_line:
    try:
        temp_number = int(i)
        if temp_number % 3 == 0:
            my_list.append(temp_number)
    except ValueError:
        pass
if len(my_list) == 0:
    print("Нет чисел, кратных 3")
else:
    print("Числа кратные 3: ", *my_list)