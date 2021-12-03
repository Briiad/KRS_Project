# Nama  : Brian Aditya Dharmatirta
# NIM   : 2015150301111010
# Kelas : Pemlan B

from tkinter import *
from tkinter import ttk

# FUNCTIONS


def add_matkul(kode_matkul, mata_kuliah, sks):
    print('huhu hihe')


# Main Program
if __name__ == '__main__':
    # Initialize
    app = Tk()
    app.geometry("500x500")
    app.title("APLIKASI RENCANA STUDI")

    heading = Label(app, text="Form KRS", bg='grey', width='500', height='3').pack()

    # User Data Module
    Label(app, text='Nama : ').place(x='10', y='60')
    Label(app, text='NIM  : ').place(x='10', y='90')
    Label(app, text='IPS  : ').place(x='10', y='120')

    u__name = Text(app, height=1, width=20).place(x='60', y='60')
    u__nim = Text(app, height=1, width=20).place(x='60', y='90')
    u__ips = Text(app, height=1, width=20).place(x='60', y='120')

    # KRS Input Module
    krs = ttk.Treeview(app)
    Label(app, text='Pilihan Mata Kuliah').place(x='10', y='160')

    krs['columns'] = ("Kode Matkul", "Mata Kuliah", "SKS")

    krs.column('#0', width='0')
    krs.column('Kode Matkul', width='120', anchor=CENTER)
    krs.column('Mata Kuliah', width='120', anchor=CENTER)
    krs.column('SKS', width='120', anchor=CENTER)

    krs.heading('Kode Matkul', text='Kode Matkul', anchor=CENTER)
    krs.heading('Mata Kuliah', text='Mata Kuliah', anchor=CENTER)
    krs.heading('SKS', text='SKS', anchor=CENTER)

    krs.insert(parent='', index='end', iid=0, values=("AAAA", "Sistem Linear", 3))
    krs.insert(parent='', index='end', iid=1, values=("BBBB", "Sistem Digital", 3))
    krs.insert(parent='', index='end', iid=2, values=("CCCC", "Pemrograman 1", 3))
    krs.insert(parent='', index='end', iid=3, values=("DDDD", "Pemrograman 2", 4))
    krs.insert(parent='', index='end', iid=4, values=("EEEE", "Kewirausahaan", 2))
    krs.insert(parent='', index='end', iid=5, values=("FFFF", "Pemrosesan Sinyal", 3))
    krs.insert(parent='', index='end', iid=6, values=("GGGG", "Sistem Operasi", 3))
    krs.insert(parent='', index='end', iid=7, values=("HHHH", "Aerial Robotic", 4))
    krs.insert(parent='', index='end', iid=8, values=("IIII", "Matematika 1", 2))
    krs.insert(parent='', index='end', iid=9, values=("JJJJ", "Bahasa Inggris", 3))

    krs.place(x='10', y='200')

    # KRS INPUT BUTTON MODULE
    add_btn = PhotoImage(file='green_btn.png')

    Label(app, text='Button Tambah').place(x='393', y='200')

    btn__0 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('AAAA', 'Sistem Linear', 3)).place(x='430', y='225.5')
    btn__1 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('BBBB', 'Sistem Digital', 3)).place(x='430', y='246.5')
    btn__2 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('CCCC', 'Pemrograman 1', 3)).place(x='430', y='267')
    btn__3 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('DDDD', 'Pemrograman 2', 4)).place(x='430', y='288')
    btn__4 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('EEEE', 'Kewirausahaan', 2)).place(x='430', y='309')
    btn__5 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('FFFF', 'Pemrosesan Sinyal', 3)).place(x='430', y='330')
    btn__6 = Button(app, image=add_btn, width=10, height=6, command=lambda: add_matkul('AAAA', 'Sistem Operasi', 3)).place(x='430', y='351')
    btn__7 = Button(app, image=add_btn, width=10, height=6).place(x='430', y='367.5')
    btn__8 = Button(app, image=add_btn, width=10, height=6).place(x='430', y='385.7')
    btn__9 = Button(app, image=add_btn, width=10, height=6).place(x='430', y='407.7')

    app.mainloop()
