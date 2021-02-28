import re
import csv
file = open('raw.data' , 'r' , encoding="utf-8")
text = file.read()

'''
p - pattern
t - text
'''

name_of_com_p = r"\nФилиал.(?P<Name_Com>.+)"
name_of_com_t = re.search(name_of_com_p , text).group("Name_Com")

bin_p = r"\nБИН.*(?P<BIN>\b[0-9]+)"
bin_t = re.search(bin_p , text).group("BIN")

date_adress_p = r"\nВремя:.(?P<Date>.+)\n(?P<Adress>.+)"
date_t = re.search(date_adress_p , text).group("Date")
adress_t = re.search(date_adress_p , text).group("Adress")

item_p = r"\n(?P<Title>.+)\n(?P<Count>.+)\n(?P<Unit_Price>.+)\n(?P<Total_Price>.+)\nСтоимость\n.*"
item_t = re.compile(item_p)

items = [["Название компании" , "БИН" , "Наименование товара" , "Количество" , "Цена за еденицу" , "Общая сумма" , "Дата" , "Адрес"]]

for n in re.finditer(item_p , text):
    items.append([name_of_com_t , bin_t , n.group("Title") , n.group("Count") , n.group("Unit_Price") , n.group("Total_Price") , date_t , adress_t])

    with open('file.csv' , 'w' , newline='') as f:
        writer = csv.writer(f)
        writer.writerow(items)
    
    file.close()