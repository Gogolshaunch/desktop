import tkinter as tk
import random
import sqlite3
database = sqlite3.connect('../pass.db')
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (password TEXT, ID TEXT)""")
database.commit()
window = tk.Tk()
window.title('Генератор паролей')
kh = 0
name = None


def click_button():
    global kh, name
    a = []
    ok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    s = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z,'
    num = s.split(',')
    for i in range(8):
        a.append(random.choice(ok))

    for i in range(8):
        a.append(random.choice(num))

    shuffled_list = sorted(a, key=lambda x: random.random())
    ls = " ".join(map(str, shuffled_list))
    pas = ls.replace(" ", "")

    cursor.execute(f"SELECT password FROM users WHERE password = '{pas}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (pas, pas))
        if name is None:
            name = tk.Label(
                text=pas,
                width=20,
                height=2)
            name.pack()
        if kh == 1:
            kh = 0
            name.pack_forget()
            name = None
        else:
            kh += 1
    else:
        for i in range(8):
            a.append(random.choice(ok))

        for i in range(8):
            a.append(random.choice(num))

        shuffled_list = sorted(a, key=lambda x: random.random())
        ls = " ".join(map(str, shuffled_list))
        pas = ls.replace(" ", "")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO users VALUES (?, ?)", (pas, pas))
            database.commit()
            if name is None:
                name = tk.Label(
                    text=pas,
                    width=20,
                    height=2)
                name.pack()
            if kh == 1:
                kh = 0
                name.pack_forget()
                name = None
            else:
                kh += 1


label = tk.Label(
    text="Генератор паролей!",
    width=20,
    height=2)

button = tk.Button(
    text="Сгенерировать",
    command=click_button,
    width=25,
    height=5)


label.pack()
button.pack()
window.mainloop()
