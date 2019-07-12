# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir_path = os.getcwd()
dir_name = (dir_path+'\\'+'dir_'+str(i) for i in range(1,10))
dir_new = list(dir_name)

def mk_your_dir():
    '''
    Функция создаёт произвольную папку в текущей директории
    :return:
    '''
    try:
        os.mkdir((dir_path+'\\'+input('Введите название директории для создания: \n')))
        print('Успешно создано')
    except Exception:
        print('Невозможно создать')

def rm_your_dir():
    '''
    Функция удаляет произвольную папку в текущей директории
    :return:
    '''
    try:
        os.rmdir((dir_path+'\\'+input('Введите название директории для удаления: \n')))
        print('Успешно удалено')
    except Exception:
        print('Невозможно удалить')

def mk_dir():
    '''
    Функция создаёт заранее подготовленный список каталогов
    :return:
    '''
    for var in dir_new:
        os.mkdir(var)

def rm_dir():
    '''
    Функция удаляет заранее подготовленный список каталогов
    :return:
    '''
    for var in dir_new:
        os.rmdir(var)

def ls_dir():
    '''
    Функция покзаывает папки текущей директории
    :return:
    '''
    folder = []
    for i in os.walk('.'):
        folder.append(i)
    print(folder[0][1])

def cd_dir():
    '''
    Функция по переходу в другую директорию
    :return:
    '''
    try:
        os.chdir((input('Введите полное название директории куда перейти: \n')))
        print('Успешно перешел')
    except Exception:
        print('Невозможно перейти')


#Создание директории dir_1 - dir_9
#mk_dir()
#Удаление директории dir_1 - dir_9
#rm_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#print("current dir = ", os.getcwd())
#print(os.listdir(path="."))
#print(list(os.walk('.')))

import os
folder = []
for i in os.walk('.'):
    folder.append(i)
print(folder[0][1])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
shutil.copy2(__file__,__file__[:-3]+'_copy'+__file__[-3:])