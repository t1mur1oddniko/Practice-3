x, y = input().split()
x = int(x)
y = int(y)

print((x % y == 0 or y % x == 0) * 1 + (x % y != 0 and y % x != 0) * 2)