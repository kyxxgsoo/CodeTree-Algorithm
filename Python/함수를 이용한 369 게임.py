def func1(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if str(i).find("3") != -1 or str(i).find("6") != -1 or str(i).find("9") != -1 or i % 3 == 0:
            cnt += 1
    return cnt

a, b = map(int, input().split())

print(func1(a, b))
