from tkinter import * # Импортируем все элементы с модуля Ткинтер
from tkinter.scrolledtext import ScrolledText # Импортируем модуль для текста

root = Tk() # Вызываем обьект класса Ткинтер
root.title("Форматирование по шаблону") # Название програмы
root.iconbitmap("iconka.ico") # Добавление иконки
root["bg"] = "gray" # Цвет
root.geometry("500x300+450+200") # Размер окна
# root.resizable(False,False) # Запрет на изменения параметров окна

def _onKeyRelease(event): # Русская, Украинская раскладка
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==65 and  ctrl and event.keysym.lower() != "a":
        event.widget.event_generate("<<SelectAll>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")
root.bind("<Control-KeyPress>", _onKeyRelease)

def get_text1(): # Функция приема_Формат: (',')
    p = s_text.get("1.0", "end") # Получает текст
    l = p.split() # Переобразует в лист
    s1 = "', '".join(l)
    s2 = ("('"+s1+"')")
    root.clipboard_clear() # Очистка буфера обмена
    root.clipboard_append(s2) # Копирование в бефу

def get_text2(): # Функция приема_Формат: пробел
    p = s_text.get("1.0", "end") # Получает текст
    l = p.split() # Переобразует в лист
    root.clipboard_clear() # Очистка буфера обмена
    root.clipboard_append(l) # Копирование в бефу

def delete_all(): # Функция очистки текста 
    s_text.delete("1.0", "end")


s_text = ScrolledText(root, width=10,  height=10, bg = "silver") # Атрибуты текста
s_text.pack(fill=BOTH, side=TOP, expand=True) # Вывод в графику

btf1 = Button(text="Формат: (',')", command=get_text1) # Кнопка формат 1
btf2 = Button(text="Формат: пробел", command=get_text2) # Кнопка формат 2
bto = Button(text="Очистить", command=delete_all)  # Кнопка формат 2

btf2.pack(side=LEFT) # Вывод в графику
btf1.pack(side=LEFT) # Вывод в графику
bto.pack(side=RIGHT)# Вывод в графику

root.mainloop() # Бесконечный цыкл (Запуск)