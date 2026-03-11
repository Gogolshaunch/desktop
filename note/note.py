import sys
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import askyesnocancel, askyesno

window = Tk()
window.configure(bg="white")
window.geometry("600x700")
window.title("Блокнот")
window.resizable(False, False)

frame_tasks = Frame(window)
frame_tasks.pack()

text_fild = Text(frame_tasks,
                 bg='white',
                 fg='black',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=590,
                 font='Arial 14 normal roman'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(frame_tasks, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)
Font_tuple = ['Arial', '14', 'normal', 'roman']


def close():
    result = askyesno(title="Warning!", message="Вы точно хотите закрыть программу?")
    if result:
        sys.exit()
    else:
        pass


def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path).read())


def light():
    text_fild['bg'] = 'white'
    text_fild['fg'] = 'black'


def dark():
    text_fild['bg'] = 'black'
    text_fild['fg'] = 'white'


def aril():
    Font_tuple[0] = "Arial"
    text_fild['font'] = Font_tuple


def cour():
    Font_tuple[0] = "Courier"
    text_fild['font'] = Font_tuple


def comic():
    Font_tuple[0] = "Comic Sans MS"
    text_fild['font'] = Font_tuple


def hel():
    Font_tuple[0] = "Helvetica"
    text_fild['font'] = Font_tuple


def times():
    Font_tuple[0] = "Times"
    text_fild['font'] = Font_tuple


def yellow():
    text_fild['fg'] = 'yellow'


def darkyellow():
    text_fild['fg'] = 'darkyellow'


def lightyellow():
    text_fild['fg'] = 'lightyellow'


def white():
    text_fild['fg'] = 'white'


def red():
    text_fild['fg'] = 'red'


def darkred():
    text_fild['fg'] = 'darkred'


def black():
    text_fild['fg'] = 'black'


def purple():
    text_fild['fg'] = 'purple'


def pink():
    text_fild['fg'] = 'pink'


def orange():
    text_fild['fg'] = 'orange'


def green():
    text_fild['fg'] = 'green'


def darkgreen():
    text_fild['fg'] = 'darkgreen'


def lightgreen():
    text_fild['fg'] = 'lightgreen'


def blue():
    text_fild['fg'] = 'blue'


def darkblue():
    text_fild['fg'] = 'darkblue'


def lightblue():
    text_fild['fg'] = 'lightblue'


def grey():
    text_fild['fg'] = 'grey'


def darkgrey():
    text_fild['fg'] = 'darkgrey'


def lightgrey():
    text_fild['fg'] = 'lightgrey'


def brown():
    text_fild['fg'] = 'brown'


def save_file():
    try:
        file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        f = open(file_path, 'a+', encoding='utf-8')
        text = text_fild.get('1.0', END)
        f.write(text)
        f.close()
    except:
        pass


def new_fail():
    result = askyesnocancel(title="Warning!", message="Сохранить файл перед закрытием?")
    if result == None:
        pass
    elif result:
        save_file()
        text_fild.delete('1.0', END)
    else:
        text_fild.delete('1.0', END)


def eight():
    Font_tuple[1] = "8"
    text_fild['font'] = Font_tuple


def ten():
    Font_tuple[1] = "10"
    text_fild['font'] = Font_tuple


def twelve():
    Font_tuple[1] = "12"
    text_fild['font'] = Font_tuple


def fourteen():
    Font_tuple[1] = "14"
    text_fild['font'] = Font_tuple


def sixteen():
    Font_tuple[1] = "16"
    text_fild['font'] = Font_tuple


def eighteen():
    Font_tuple[1] = "18"
    text_fild['font'] = Font_tuple


def twenty():
    Font_tuple[1] = "20"
    text_fild['font'] = Font_tuple


def twentytwo():
    Font_tuple[1] = "22"
    text_fild['font'] = Font_tuple


def twentyfour():
    Font_tuple[1] = "24"
    text_fild['font'] = Font_tuple


def twentysix():
    Font_tuple[1] = "26"
    text_fild['font'] = Font_tuple


def twentyeight():
    Font_tuple[1] = "28"
    text_fild['font'] = Font_tuple


def threety():
    Font_tuple[1] = "30"
    text_fild['font'] = Font_tuple


def threetytwo():
    Font_tuple[1] = "32"
    text_fild['font'] = Font_tuple


def threetyfour():
    Font_tuple[1] = "34"
    text_fild['font'] = Font_tuple


def threetysix():
    Font_tuple[1] = "36"
    text_fild['font'] = Font_tuple


def threetyeight():
    Font_tuple[1] = "38"
    text_fild['font'] = Font_tuple


def sorok():
    Font_tuple[1] = "40"
    text_fild['font'] = Font_tuple


def soroktwo():
    Font_tuple[1] = "42"
    text_fild['font'] = Font_tuple


def sorokfour():
    Font_tuple[1] = "44"
    text_fild['font'] = Font_tuple


def soroksix():
    Font_tuple[1] = "46"
    text_fild['font'] = Font_tuple


def sorokvosem():
    Font_tuple[1] = "48"
    text_fild['font'] = Font_tuple


def fifty():
    Font_tuple[1] = "50"
    text_fild['font'] = Font_tuple


def dele():
    result = askyesno(title="Warning!", message="Вы точно хотите очистить файл?")
    if result:
        text_fild.delete('1.0', END)
    else:
        pass


def bold():
    Font_tuple[2] = "bold"
    text_fild['font'] = Font_tuple


def italic():
    Font_tuple[3] = "italic"
    text_fild['font'] = Font_tuple


def delbold():
    Font_tuple[2] = "normal"
    text_fild['font'] = Font_tuple


def delitalic():
    Font_tuple[3] = "roman"
    text_fild['font'] = Font_tuple


def normal():
    Font_tuple[3] = "roman"
    text_fild['font'] = Font_tuple
    Font_tuple[2] = "normal"
    text_fild['font'] = Font_tuple


menu = Menu(window)
window.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="Открыть", command=open_file)
filemenu.add_command(label="Очистить", command=dele)
filemenu.add_command(label="Новый файл", command=new_fail)
filemenu.add_command(label="Сохранить...", command=save_file)
filemenu.add_command(label="Закрыть", command=close)


helpmenu = Menu(menu, tearoff=0)

tema = Menu(helpmenu, tearoff=0)
tema.add_command(label='Arial', command=aril)
tema.add_command(label='Courier', command=cour)
tema.add_command(label='Comic Sans MS', command=comic)
tema.add_command(label='Helvetica', command=hel)
tema.add_command(label='Times', command=times)

ok = Menu(helpmenu, tearoff=0)
ok.add_command(label='Светлая', command=light)
ok.add_command(label='Темная', command=dark)

num = Menu(helpmenu, tearoff=0)
num.add_command(label='Жёлтый', command=yellow)
num.add_command(label='Ярко-Жёлтый', command=lightyellow)
num.add_command(label='Тёмно-Красный', command=darkred)
num.add_command(label='Красный', command=red)
num.add_command(label='Светло-Голубой', command=lightblue)
num.add_command(label='Голубой', command=blue)
num.add_command(label='Чёрный', command=black)
num.add_command(label='Тёмно-Голубой', command=darkblue)
num.add_command(label='Белый', command=white)
num.add_command(label='Серый', command=grey)
num.add_command(label='Светло-Серый', command=lightgrey)
num.add_command(label='Тёмно-Серый', command=darkgrey)
num.add_command(label='Светло-Зелёный', command=lightgreen)
num.add_command(label='Тёмно-Зелёный', command=darkgreen)
num.add_command(label='Зелёный', command=green)
num.add_command(label='Фиолетовый', command=purple)
num.add_command(label='Розовый', command=pink)
num.add_command(label='Оранжевый', command=orange)
num.add_command(label='Коричневый', command=brown)


mai = Menu(helpmenu, tearoff=0)
mai.add_command(label='8', command=eight)
mai.add_command(label='10', command=ten)
mai.add_command(label='12', command=twelve)
mai.add_command(label='14', command=fourteen)
mai.add_command(label='16', command=sixteen)
mai.add_command(label='18', command=eighteen)
mai.add_command(label='20', command=twenty)
mai.add_command(label='22', command=twentytwo)
mai.add_command(label='24', command=twentyfour)
mai.add_command(label='26', command=twentysix)
mai.add_command(label='28', command=twentyeight)
mai.add_command(label='30', command=threety)
mai.add_command(label='32', command=threetytwo)
mai.add_command(label='34', command=threetyfour)
mai.add_command(label='36', command=threetysix)
mai.add_command(label='38', command=threetyeight)
mai.add_command(label='40', command=sorok)
mai.add_command(label='42', command=soroktwo)
mai.add_command(label='44', command=sorokfour)
mai.add_command(label='46', command=soroksix)
mai.add_command(label='48', command=sorokvosem)
mai.add_command(label='50', command=fifty)

my = Menu(helpmenu, tearoff=0)
my.add_command(label='Стандартный шрифт', command=normal)
my.add_command(label='Жирный шрифт', command=bold)
my.add_command(label='Курсивный шрифт', command=italic)
my.add_command(label='Убрать жирный шрифт', command=delbold)
my.add_command(label='Убрать курсив', command=delitalic)

helpmenu.add_cascade(label="Тема...", menu=ok)
helpmenu.add_cascade(label="Шрифт...", menu=tema)
helpmenu.add_cascade(label="Цвет текста...", menu=num)
helpmenu.add_cascade(label="Размер шрифта...", menu=mai)
helpmenu.add_cascade(label="Начертание...", menu=my)

menu.add_cascade(label="Файл", menu=filemenu)
menu.add_cascade(label="Вид", menu=helpmenu)

window.mainloop()
