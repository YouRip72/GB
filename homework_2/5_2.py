my_reit = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_reit}")
reit = int(input("Введите число (111 - выход) "))
while reit != 111:
    for el in range(len(my_reit)):
        if my_reit[el] == reit:
            my_reit.insert(el + 1, reit)
            break
        elif my_reit[0] < reit:
            my_reit.insert(0, reit)
        elif my_reit[-1] > reit:
            my_reit.append(reit)
        elif my_reit[el] > reit and my_reit[el + 1] < reit:
            my_reit.insert(el + 1, reit)
    print(f"текущий список - {my_reit}")
    reit = int(input("Введите число "))