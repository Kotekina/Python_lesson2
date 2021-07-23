# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

my_dict = {1: 'winter', 2: 'winter',3: 'spring',4: 'spring',5: 'spring',6: 'summer',7: 'summer',8: 'summer',9:
    'autumn',10: 'autumn',11: 'autumn',12: 'winter'}
my_list = ('winter', 'spring', 'summer', 'autumn')
print(my_dict[1])
month = int(input("ВВедите целое число от 1 до 12:"))
if month == 1 or month == 2  or month == 12:
    print(my_dict.get(1))
    print(my_list[0])
elif month == 3 or month == 4  or month == 5:
    print(my_dict.get(3))
    print(my_list[1])
elif month == 6 or month == 7  or month == 8:
    print(my_dict.get(6))
    print(my_list[2])
elif month == 9 or month == 10  or month == 11:
    print(my_dict.get(9))
    print(my_list[3])

else:
    print('Введите верное значение..от 1 до 12:')