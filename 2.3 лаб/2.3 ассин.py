import csv

def start(school, grade):
    results = []
    with open('C://Users//_qwertyiop_//OneDrive//Рабочий стол//5сем//ассин прог//2.3 лаб//rez.csv', mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        
        for record in reader:       
            data=(record['user_name'] + " " + record['Score']).split(" ")[1:]
                
            if data[0] == school and data[1] == grade:
                results.append((data[2], data[4]))
    return results

school= input("Введите номер школы: ")
grade= input("Введите номер класса: ")

result = start(school, grade)
if result:
    for r in result:
        print(f"{r[0]} {r[1]}")
else:
    print("Ничего не найдено")
        