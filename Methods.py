import datetime
import json
import os

def outJson(number, name, text):
    fileName = f'{number}-{name}'
    timeNote = (f'{datetime.datetime.today().strftime("%d.%m.%Y")}-'
                f'{datetime.datetime.today().strftime("%H.%M.%S")}')
    data = {'ID': number, 'Name': name, 'Time': timeNote, "Text": text}
    with open(f"D:\\Works\\IT\\IntermediateTest\\DirNotes\\{fileName}.json", "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    return
def listNote():
    directory = 'D:\\Works\\IT\\IntermediateTest\\DirNotes'
    for filename in os.listdir(directory):
        print(filename)
    return
def selectNumber(number):
    directory = 'D:D:\\Works\\IT\\IntermediateTest\\DirNotes'
    arr = []
    res = True
    for filename in os.listdir(directory):
        arr.append(int(filename.split('-')[0]))
    if number in arr:
        res = False
    return res

def selectFile():
    print('Введите номер зaметки: ')
    flag = True
    res = None
    while flag:
        ch = int(input())
        if selectNumber(ch) == True:
            print('Тaкой зaметки нет, выберите другую: ')
            continue
        else:
            directory = 'D:\\Works\\IT\\IntermediateTest\\DirNotes'
            for filename in os.listdir(directory):
                temp = filename.split('-')
                if int(temp[0]) == ch:
                    res = filename
                    flag = False
                    break
    return res
def creatNotes():
    print('Введите порядковый номер зaметки')
    while True:
        number = int(input())
        if selectNumber(number) == False:
            print('Такой номер уже есть, введите другой: ')
            continue
        else: break
    print('введите имя зaметки: \n')
    name = str(input())
    
    print('введите текст зaметки: \n')
    text = str(input())

    outJson(number, name, text)
    return
def editNote():
    with open(f"D:\\Works\\IT\\IntermediateTest\\DirNotes\\{selectFile()}") as json_file:
        jFile = json.load(json_file)
        print('Текст зaметки:')
        print(jFile['Text'])
        print('Изменить текст зaметки: y - дa, n - нет')
        while True:
            choice = input().lower()
            if choice == 'n':
                # flag = False
                break
            elif choice == 'y':
                print('Введите новый текст зaметки')
                jFile['Text'] = input()
                outJson(jFile['ID'], jFile['Name'], jFile['Text'])
                # flag = False
                break
            else:
                print('Не корректный выбор, повторите')
                continue
    return

def delNote():
    os.remove(f"D:\\Works\\IT\\IntermediateTest\\DirNotes\\{selectFile()}")
    return