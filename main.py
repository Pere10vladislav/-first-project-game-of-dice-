from tkinter import *
import random, time


def bros():
    x = random.choice(['b.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png']) #Рандомный выбор картинки

    return x

def img(event):
    global b1, b2
    for i in range(10):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update() #Обнавление окна
        time.sleep(0.1)

def main():
    global lab1, lab2, root

    root = Tk() #Определяем главное окно
    root.geometry('400x200') #Размер окна
    root.title('Игра в кости!') #Название окна
    root.resizable(height=False, width=False) #Запретить разтягивание окна
    root.iconphoto(True, PhotoImage(file=('iconka.png'))) #Добавить иконку формата png с помощью встроенного класса PotoImage
    font = PhotoImage(file=('holst.png'))
    Label(root, image=font).pack() #Создать элемент и разместить его в окне

    lab1 = Label(root) #Создать элемент через переменную
    lab1.place(relx=0.3, rely=0.5, anchor=CENTER) #Разместить элемент в окне
    lab2 = Label(root) #Создать элемент через переменную
    lab2.place(relx=0.7, rely=0.5, anchor=CENTER) #Разместить элемент в окне

    root.bind('<1>', img) #Обработчик событий (Нажатие на левую кнопку мыши)
    img('event')

    root.mainloop() #Цикл для показа окна


if __name__ == '__main__':
    main()

