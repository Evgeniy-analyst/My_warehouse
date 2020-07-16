# По номеру года найти число дней в этом году
# (вывести 365, если это не високосный год,
# или 366, если високосный).
#
# put your python code here
# 2020 - 366
# 2025 - 365
i = int(input())

if i <= 1582:
    print("error")
else:
    g = (i % 4)  # visokosn
    s = i % 100  # iskl
    s_1 = i % 400  # iskl_2
    if (g == 0) and (s != 0) or (s_1 == 0):
        print(366)
    elif g != 0:
        print(365)