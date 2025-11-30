#задание по строкам
n = ('Иванов;Анна;1985-03-22;A15.0;активный')
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
    

    
