import cv2
import os
import platform
import time

CLEAR_CMD = 'cls'

""" Данная программа выводит видео в ascii формате она работает что-то типа как пирога
ASCII-картинка вытянется в одну горизонтальную линию, а затем 2, затем 3 и т.д, что в итоге
превращается в единное видео """

currect_os_command = platform.system()
path_os_command = platform.system()
    
string = " ,./';[]+-!@#$%^&*()*"
coef = 255 / (len(string) - 1)

if currect_os_command == 'windows':
    pass
else:
    CLEAR_CMD = 'clear' 

currect_os_command = input("Введите название вашей ОС (по типу Linux, Windows и т.д): ").lower()

if currect_os_command == 'windows':
    path_os_command = input("введи путь к папке: ")
    if os.path.isfile(path_os_command):
        path = path_os_command
        print(path_os_command)
    else:
        print("Такой папки нету. Перепроверьте путь.")
   
elif currect_os_command == 'linux':
    path_os_command = input("введи путь к папке: ")
    if os.path.isfile(path_os_command):
        path = path_os_command
        print(path_os_command)
    else:
        print("Такой папки нету. Перепроверьте путь.")

video = cv2.VideoCapture(path)

fps = video.get(cv2.CAP_PROP_FPS) # запрашиваем сколько fps файла
frame_fps = 1.0 / fps # программа понимает, скаким интервалом нужно вводить текст на экран

while True:

    start_time = time.perf_counter() # запускаем высокоточный сукундомер в самом начале обработки

    ret, frame = video.read()   # ret - это логическая переменная, а в frame наше видео считает покадрово
    if not ret or frame is None: #is проверяет двые переменные на один и тот адрес памяти 
        break                   # проверка условия, если ret нет или же frame нету идентичной переменной, 
                                    # то цикл заканчивается

    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # делает из видео в черно-белый оттенок
    height, width = gray_video.shape #frame.shape возращает 2 значение
    spisok = []
    for y in range(0, height - 1, 5): # шаг 5 мы делям для сжатие видео и компенсации форма шрифта
        s = ""
        for x in range(0, width - 1, 3): #шаг 5 мы делям для сжатие видео и компенсации форма шрифта
            s += string[len(string) - int(gray_video[y, x] / coef) - 1]
        if len(s) != 0:
            spisok.append(s)
    os.system(CLEAR_CMD)
    print(f'\n''\033[37m'.join(spisok), flush=True) #flush немедленно заставляет вывести наш список

    elapsed_time = time.perf_counter() - start_time # текущее время - время старта, мы находим разницу
    sleep_time = frame_fps - elapsed_time # вычитываем время из идеалной длительности кадров

    if sleep_time > 0:
        time.sleep(sleep_time) # засыпаем ровно на остаток, чтобы с сумме получилось 0,033 c 
    
video.release() # для освобождение ОЗУ и камеры, чтобы она после программы дальше 
                    # не работала