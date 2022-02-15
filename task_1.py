while True:
    number_temp = input("Пожалуйста, введите число: ")
    try:
        number = int(number_temp)
        if number > 7:
            print("Привет")
        break
    except ValueError:
        try:
            number = float(number_temp)
            if number > 7:
                print("Привет")
            break
        except ValueError:
            print("Вы ввели не число")
                