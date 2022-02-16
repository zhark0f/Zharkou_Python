try:
    my_list = [int(i) for i in input("Введите числа в строку через пробел(ы): ").split()]
    my_new_list = list(filter(lambda x: x % 3 == 0, my_list))
    if len(my_new_list) == 0:
        print("Нет чисел, кратных 3")
    else:
        print("Числа кратные 3: ", *my_new_list)
except:
    print("Вы ввели не только числа")