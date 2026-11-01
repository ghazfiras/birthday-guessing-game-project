while True:
    birthday = 0
    set_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    print(set_1)
    answer = int(input("Is your birthday included in this set? (Enter 1 for Yes and 0 for No): "))
    if answer == 1:
        birthday = birthday + set_1[0]
    set_2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
    print(set_2)
    answer = int(input("Is your birthday included in this set? (Enter 1 for Yes and 0 for No): "))
    if answer == 1:
        birthday = birthday + set_2[0]
    set_3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
    print(set_3)
    answer = int(input("Is your birthday included in this set? (Enter 1 for Yes and 0 for No): "))
    if answer == 1:
        birthday = birthday + set_3[0]
    set_4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
    print(set_4)
    answer = int(input("Is your birthday included in this set? (Enter 1 for Yes and 0 for No): "))
    if answer == 1:
        birthday = birthday + set_4[0]
    set_5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    print(set_5)
    answer = int(input("Is your birthday included in this set? (Enter 1 for Yes and 0 for No): "))
    if answer == 1:
        birthday = birthday + set_5[0]
    print("Your birthday is:", birthday)
