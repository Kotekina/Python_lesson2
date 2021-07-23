# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
number_input = int(input('Введите новый элемент рейтинга:'))
count = my_list.count(number_input)
for element in my_list:
    if count > 0:
        i = my_list.index(number_input)
        my_list.insert(i+count, number_input)
        break
    else:
        if number_input > element:
            j = my_list.index(element)
            my_list.insert(j, number_input)
            break
        elif number_input < element:
            my_list.append(number_input)
            break
print(my_list)

