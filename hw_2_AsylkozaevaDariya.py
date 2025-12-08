a = input('Фамилия пациента')
b = input('Имя пациента')
c = int (input('Год рождения'))
d = int (input('Месяц рождения'))
e = int (input('День рождения'))
g = input('Диагноз')
h = input('Статус')

# в целом пайплайн решения верный, но есть несколько ошибок
# есть синтаксическая ошибка при инициализации списка: разделителем в списке являются запятие, а не точки с запятой
# то есть правильно вот так:
patient_data=['Фамилия пациента','Имя пациента','Год рождения','Месяц рождения','День рождения','Диагноз','Статус'] 

# здесь тоже ошибка: у списков нет метода split(), он есть только у строк
# parts = patient_data.split(';')

# тем не менее, список patient_data не нужен, так как он не участвует в решении самой задачи: 

if h.startswith("активный") or h.startswith("ремиссия") or h.startswith("выписан"):
    print("True")
if g.startswith("A") or g.startswith("B") or g.startswith("C") and g[-1].isdigit():
    print("True")
if e<=31:
    print("True")
if d<=12:
    print("True")
if len("c")==4:
    print("True") 
# В этой проверке нет смысла, так как переменные c, d, e имеют тип int, а у объектов типа int нету метода isdigit()
# if c.isdigit() and d.isdigit() and e.isdigit(): 
#     print("True")      
if a.isalpha() and b.isalpha():
    print("True")
else:
    print(False)
