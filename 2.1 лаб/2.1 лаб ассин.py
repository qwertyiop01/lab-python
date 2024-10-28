def recoder(text_ru):
    text_en = ""
    dictA= {
    "й": "j", "ц": "c", "у": "u", 
    "к": "k", "е": "e", "н": "n",     
    "г": "g", "ш": "sh", "щ": "shh", 
    "з": "z", "х": "h", "ъ": "#",     
    "ф": "f", "ы": "y", "в": "v", 
    "а": "a", "п": "p", "р": "r",  
    "о": "o", "л": "l", "д": "d", 
    "ж": "zh", "э": "je", "я": "ya",    
    "ч": "ch", "с": "s", "м": "m", 
    "и": "i", "т": "t", "ь": "'",     
    "б": "b", "ю": "ju", "ё": "jo"
    }
    for i in text_ru:
        if i in dictA.keys():
            text_en= text_en+ dictA[i]
        else:
            text_en=text_en+i
            
    return text_en
      


with open ("C:\\Users\\_qwertyiop_\\OneDrive\\Рабочий стол\\5сем\\ассин прог\\2.1 лаб\\cyrillic.txt", "r", encoding="utf-8") as file:
        text_ru= file.read()

text= recoder(text_ru)

with open ("C:\\Users\\_qwertyiop_\\OneDrive\\Рабочий стол\\5сем\\ассин прог\\2.1 лаб\\transliteration.txt", "w", encoding="utf-8") as f:
     f.write(text)
