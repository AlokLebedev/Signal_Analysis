'''
text = input()
cnt = 0
control = text.split(';')
if control[0].isalpha() and control[1].isalpha():
    cnt += 1
date = control[2].split('-')
if date[0].isdigit() and len(date[0])==4 and date[1].isdigit() and date[2].isdigit() and len(date[1])==len(date[2])==2 and 0<int(date[1])<13 and 0<int(date[2])<32:
    cnt +=1
if control[3].startswith(('A','B', 'C')):
    mkb = control[3].replace(control[3][0], '')
    if '.' in mkb:
        if mkb.split('.', 1)[0].isdigit() and mkb.split('.', 1)[1].isdigit():
            cnt += 1
    else:
        if mkb.isdigit() and 2 <= len(mkb) <= 3:
            cnt +=1
if control[4] in ['активный', 'ремиссия','выписан']:
    cnt+=1
print(True if cnt == 4 else False)
'''

temperatures = [36.6, 36.7, 36.8, 36.9, 37.1, 37.3, 37.5, 37.4, 37.2, 37.0, 36.9, 36.8]
hours = ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00' ]
cnt = 0
print(f'Максимальная температура: { max(temperatures)} в {hours[temperatures.index(max(temperatures))]}')
for i in range(12):
    if temperatures[i] >= 37.1:
        cnt +=1
        print(f'- {temperatures[i]} °C в {hours[i]}')
print(f'Количество измерений выше 37.0°C: {cnt}')
print('Вердикт:', end=' ')
print('ПОДОЗРЕНИЕ НА АКТИВНЫЙ ТУБЕРКУЛЁЗ' if cnt>2 else 'Температурный режим в пределах нормы')
