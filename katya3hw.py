#задание на кортежи
analysis_history = (
    ("Общий_анализ_крови_лейкоциты", 20240315, 9.8),
    ("Мочевина", 20240315, 6.2),
    ("Креатинин", 20240322, 88),
    ("Общий_анализ_крови_лейкоциты", 20240322, 7.3),
)

def compare_analysis(patient_history, type_analysis):
    list = [analysis for analysis in patient_history if analysis[0] == type_analysis] # смекалка 100/100, хорошее преобразование кортежа в список через comrehension
    sorted_list = sorted(list, key = lambda x: x[1]) # лямбда-функции ещё не проходили, так что респект за продвинутую сортировку
    print(f'Анализы {type_analysis}:')
    for i in sorted_list:
        name, data, result = i # переменная name далее не используется; в таких случая можно написать нижнее подчёркивание: _, data, result = i (для того чтобы не резервировать полезное слово name)
        data_str = str(data)
        format_data = f'{data_str[:4]} - {data_str[4:6]} - {data_str[6:]}'
        print(f' - {format_data}: {result}')
    r1 = sorted_list[0][2]
    r2 = sorted_list[-1][2]
    if type_analysis == "Общий_анализ_крови_лейкоциты":
       if (4 <= r1 <= 9 and 4 <= r2 <= 9 and r1 > r2) or (4 <= r2 <= 9 and not 4 <= r1 <= 9):
           print('Показатель улучшился')
       elif (4 <= r1 <= 9 and 4 <= r2 <= 9 and r1 < r2) or (4 <= r1 <= 9 and not 4 <= r2 <= 9):
           print('Показаель ухудшился')
       else:
           print('Показатель не изменился')
    elif type_analysis == "Мочевина":
       if (2,5 <= r1 <= 8,3 and 2,5 <= r2 <= 8,3 and r1 > r2) or (2,5 <= r2 <= 8,3 and not 2,5 <= r1 <= 8,3):
           print('Показатель улучшился')
       elif (2,5 <= r1 <= 8,3 and 2,5 <= r2 <= 8,3 and r1 < r2) or (2,5 <= r1 <= 8,3 and not 2,5 <= r2 <= 8,3):
           print('Показаель ухудшился')
       else:
           print('Показатель не изменился')
    elif type_analysis == "Креатинин":
       if r1 > r2:
           print('Показатель улучшился')
       elif r1 < r2:
           print('Показаель ухудшился')
       else:
           print('Показатель не изменился')
       
compare_analysis(patient_history= analysis_history, type_analysis= 'Общий_анализ_крови_лейкоциты') 


#задание на кортежи и словари
lab_norm_glycoza = ('Глюкоза натощак', 3.3, 5.5, 'ммоль/л')
lab_norm_gem = ('Гемоглобин', 120, 160, 'г/л')
lab_norm_leic = ('Лейкоциты', 4, 9, '/л')
patient_analysis = {'Гемоглобин': 115, 'Глюкоза натощак': 4.8, 'Лейкоциты': 10.2}
def check_analysis(analysis, lab_norm):
    # внутри функции тоже можно прописать нормальные значения 
    if lab_norm[1] > analysis.get(lab_norm[0]):
        print(f'{lab_norm[0]}: {analysis.get(lab_norm[0])} {lab_norm[3]} - ниже нормы')
    elif lab_norm[2] >= analysis.get(lab_norm[0]) or lab_norm[1] == analysis.get(lab_norm[0]):
        print(f'{lab_norm[0]}: {analysis.get(lab_norm[0])} {lab_norm[3]} - в норме')
    else:
        print(f'{lab_norm[0]}: {analysis.get(lab_norm[0])} {lab_norm[3]} - выше нормы')
check_analysis(analysis = patient_analysis, lab_norm = lab_norm_glycoza)
check_analysis(analysis = patient_analysis, lab_norm = lab_norm_gem)
check_analysis(analysis = patient_analysis, lab_norm = lab_norm_leic)
