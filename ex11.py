angle = float(input())
hours = int(angle // 30)
minutes = int((angle % 30) * 2)

print(f"{hours} часов {minutes} минут")