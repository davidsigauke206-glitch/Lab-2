import csv
import random
from xml.dom import minidom


# Задание 1: названия длиннее 30 символов
def task1():
    with open("books-en.csv", encoding="cp1252") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        count = 0
        for row in reader:
            title = row[1]
            if len(title) > 30:
                count = count + 1
    print("Названий длиннее 30 символов:", count)


# Задание 2: поиск по автору (1991–1995)
def task2():
    author = input("Введите автора: ")
    with open("books-en.csv", encoding="cp1252") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        found = 0
        for row in reader:
            if row[2] == author and row[3].isdigit():
                year = int(row[3])
                if 1991 <= year <= 1995:
                    print(row[1], "-", year)
                    found = found + 1
    print("Найдено книг:", found)


# Задание 3: 20 библиографических ссылок
def task3():
    with open("books-en.csv", encoding="cp1252") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        books = list(reader)

    chosen = random.sample(books, 20)

    with open("references.txt", "w", encoding="utf-8") as out:
        number = 1
        for row in chosen:
            out.write(f"{number}. {row[2]}. {row[1]} - {row[3]}\n")
            number = number + 1
    print("Сохранено 20 ссылок в файл references.txt")


# Задание 4: CharCode валют с Nominal = 10 или 100
def task4():
    doc = minidom.parse("currency.xml")
    valutes = doc.getElementsByTagName("Valute")
    codes = []
    for v in valutes:
        nominal = v.getElementsByTagName("Nominal")[0].firstChild.data
        code = v.getElementsByTagName("CharCode")[0].firstChild.data
        if nominal == "10" or nominal == "100":
            codes.append(code)
    print("CharCode с номиналом 10 или 100:", codes)


    #publishers without repeats
def task5():
    with open("books-en.csv", encoding="cp1252") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        publishers = set()
        for row in reader:
            publishers.add(row[4])

    for p in sorted(publishers):
        print(p)
    print("Всего издательств без повторений:", len(publishers))


    #top 20 books by downloads
def task6():
    with open("books-en.csv", encoding="cp1252") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        books = list(reader)

    top = sorted(books, key=lambda row: int(row[5]), reverse=True)[:20]

    number = 1
    for row in top:
        print(f"{number}. {row[1]} — {row[2]} ({row[5]} загрузок)")
        number = number + 1


# Запуск
choice = input("Какое задание? (1, 2, 3, 4, 5, 6): ")

if choice == "1":
    task1()
elif choice == "2":
    task2()
elif choice == "3":
    task3()
elif choice == "4":
    task4()
elif choice == "5":
    task5()
elif choice == "6":
    task6()
else:
    print("Нет такого задания")