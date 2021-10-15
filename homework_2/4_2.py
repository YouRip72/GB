uzer_strock = input('Введите строку: ')
uzer_list = uzer_strock.split()
for num, list in enumerate(uzer_list):
    print(f'#{num} - {list[: 10]}')