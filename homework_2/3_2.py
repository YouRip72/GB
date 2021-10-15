month = input('Введите месяц цифрами: ')
a, b, c, d  = 'winter', 'spring', 'summer', 'autumn'
seasons_dict = {'1': a, '2': a, '3': b, '4': b, '5': b, '6': c, '7': c, '8': c, '9': d, '10': d, '11': d, '12': a}
print(seasons_dict[month])
seasons_list = [a, a, b, b, b, c, c, c, d, d, d, a]
print(seasons_list[int(month) - 1])