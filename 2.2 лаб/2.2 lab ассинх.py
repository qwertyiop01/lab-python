def read (filename: str):
    try:
        with open(filename, "r") as file:
            data= file.read()
            if not data.strip():
                print("Указанный файл пуст")
                return None
            
            numbers=data.split()
            valid_numbers=[]

            for num in numbers:
                try:
                    valid_numbers.append(int(num))
                except ValueError:
                    print("Файл содержит некорректные данные")
                    return None
            return valid_numbers
    except FileNotFoundError:
            print("Указанный файл не существует")
            return None
    
filename= input("Введите путь до файла:" + '\n')
#C:\\Users\\_qwertyiop_\\OneDrive\\Рабочий стол\\5сем\\ассин прог\\2.2 лаб\\documentik.txt
data= read(filename)


def write(data):
    data.sort()
    minimum=data[0]
    maximum=data[-1]
    l=len(data)
    summa= sum(data)
    medium= int((summa / l) * 100) / 100
    with open ("C:\\Users\\_qwertyiop_\\OneDrive\\Рабочий стол\\5сем\\ассин прог\\2.2 лаб\\out.txt", "w", encoding='utf-8') as file:
        file.write(f"Максимальное значение: {maximum} \n")
        file.write(f"Минимальное значение: {minimum} \n")
        file.write(f"Среднее значение: {medium} \n")
    return "Данные записаны в out.txt"
result = write(data)
print(result)

            
            


