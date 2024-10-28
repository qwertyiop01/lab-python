import csv
def exam(data):
    key=['lastname', 'firstname','res1','res2','res3','res']    
    data= data.split()

    if len(data)==5:
        try:
            data[2] = int(data[2])
            data[3] = int(data[3])
            data[4] = int(data[4])
            data.append(data[2]+data[3]+data[4])
            line={k:v for k,v in zip(key, data)}
            return line

        except ValueError:
            print("Вы ввели не те значения")
            return None

def write(): 
    
    print("Введите Фамилию, Имя, результат за 1, 2 и 3 экзамен через пробел")
    print("Для завершения введите 0 ")
    with open ('C://Users//_qwertyiop_//OneDrive//Рабочий стол//5сем//ассин прог//2.4 лаб//exam.csv', mode= "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['lastname', 'firstname', 'res1', 'res2', 'res3', 'res'])
        while True:
            data= input()
            if data=='0':
                break

            line=exam(data)
             
            if line:
                writer.writerow(line.values())   
write()                    

        


   

        
    
        
    


