#задание по строкам
n = input()
def validate_patient_record(n: str) -> bool:
    parts = n.split(';')
    if len(parts) != 5:
        return False
    if not (parts[0].isalpha() and parts[1].isalpha()):
        return False
    if len(parts[2])!=10:
        return False
    if not (parts[2][0:4].isdigit() and parts[2][5:7] and parts[2][8:10]):
        return False
    m = int(parts[2][5:7])
    if not  1<= int(parts[2][5:7]) <= 12:
        return False
    if not 3<= len(parts[3]) <= 5:
        return False
    if not (parts[3].startswith('A') or parts[3].startswith('B') or parts[3].startswith('C')):
        return False
    m = parts[3][1:].replace('.','1')
    if not m.isdigit():
        return False
    allowed = ['активный','выписан','ремиссия']
    if not parts[4] in allowed:
        return False
    return True
a = validate_patient_record(n = n)
print(a)


#задание по спискам
temperatures = [36.6, 36.7, 36.8, 36.9, 37.1, 37.3, 37.5, 37.4, 37.2, 37.0, 36.9, 36.8]
maxtemp = max(temperatures)
hours = 2*temperatures.index(maxtemp)
hours_str = str(hours)
min = ':00'
time = hours_str + min
print(f'Максимальная температура: {maxtemp} в {time}')
count = 0 
for i in temperatures:
    if i > 37.0:
        count+=1
print(f'Количество измерений выше 37.0: {count}')
print('Подозрительные измерения:')
for i in temperatures:
    if i >= 37.1:
        h = 2 * temperatures.index(i)
        h_str = str(h)
        tm = h_str + min
        print(f'- {i} в {tm}')
if count >= 3:
    print('Вердикт: ПОДОЗРЕНИЕ НА АКТИВНЫЙ ТУБЕРКУЛЕЗ')
else:
    print('Вердикт: Темературный режим в пределах нормы') 



#задание по спискам 2
import statistics
pressure_group1 = [120, 127, 125, 130, 135, 132, 128]
pressure_group2 = [140, 142, 145, 150, 138, 143, 147]
avg1 = statistics.mean(pressure_group1)
print(f"Среднее первой группы: {avg1}") 
mediana1 = statistics.median(pressure_group1)
print(f"Медиана первой группы: {mediana1}")
stdev1 = statistics.stdev(pressure_group1)
print(f"Стандартное отклонение первой группы: {stdev1}")
variance1 = statistics.variance(pressure_group1)
print(f"Дисперсия первой группы: {variance1}")
avg2 = statistics.mean(pressure_group2)
print(f"Среднее второй группы: {avg2}")
mediana2 = statistics.median(pressure_group2)
print(f"Медиана второй группы: {mediana2}")
stdev2 = statistics.stdev(pressure_group2)
print(f"Стандартное отклонение второй группы: {stdev2}")
variance2 = statistics.variance(pressure_group2)
print(f"Дисперсия второй группы: {variance2}")


# задание по списка 2, сделанное с помощью функции:

#задание по спискам 2
import statistics
pressure_group1 = [120, 127, 125, 130, 135, 132, 128]
pressure_group2 = [140, 142, 145, 150, 138, 143, 147]

def get_desriptive_statistics(pressure_list: list):
    '''
    возврщает описательные статистики выборки (передаваемого списка)

    pressure_list: список АД пациентов (list)

    return:
        mean, median, standard deviation, variance
    '''
    avg = statistics.mean(pressure_list)
    median = statistics.median(pressure_list)
    stdev = statistics.stdev(pressure_list)
    variance = statistics.variance(pressure_list)

    output = f"\n ################ \n Average: {avg}, \n Median: {median}, \n St.deviation: {stdev}, \n Variance: {variance} \n ################ \n "

    return output


out_1 = get_desriptive_statistics(pressure_group1)
out_2 = get_desriptive_statistics(pressure_group2)

print(out_1, out_2)
