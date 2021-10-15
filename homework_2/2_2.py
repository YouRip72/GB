uzer_input = input('Введите элементы списка: ')
uzer_list = uzer_input.split()
list_len = len(uzer_list)

start = 0
if list_len > 1:
    while start < list_len - 1:
        uzer_list[start], uzer_list[start + 1] = uzer_list[start + 1], uzer_list[start]
        start = start + 2

        print(uzer_list)
