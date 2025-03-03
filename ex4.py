X, Y, N = input().split()
R = int(N) * int(X) + (int(Y) * int(N)) // 100
K = (int(Y) * int(N)) % 100

print(f"{R} руб. {K} коп.")