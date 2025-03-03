n, c, k = map(int, input().split())
entries_per_page = n * c
page = (k - 1) // entries_per_page + 1
position_on_page = (k - 1) % entries_per_page
row = (position_on_page % n) + 1  
column = (position_on_page // n) + 1

print(f"Страница: {page}, Столбец: {column}, Строка: {row}")