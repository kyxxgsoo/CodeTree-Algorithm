def func1(y, m, d):
    # 윤년일 때
    maxDay1 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 윤년이 아닐 때
    maxDay2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 윤년일 때
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        if 0 < maxDay1[m] and maxDay1[m] < d:
            return False
    else:
        if 0 < maxDay2[m] and maxDay2[m] < d:
            return False
    return True

y, m, d = map(int, input().split())
if func1(y, m, d):
    if 3 <= m and m <= 5:
        print("Spring")
    elif 6 <= m and m <= 8:
        print("Summer")
    elif 9 <= m and m <= 11:
        print("Fall")
    elif m == 12 or m == 1 or m == 2:
        print("Winter")
else:
    print(-1)