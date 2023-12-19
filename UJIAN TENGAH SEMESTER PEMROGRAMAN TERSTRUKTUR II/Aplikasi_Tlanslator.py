from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Pasang Label dengan warna teks
        Label(mainFrame, text='Masukkan teks:', foreground='blue').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Inggris:', foreground='red').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Korea:', foreground='purple').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Japang:', foreground='purple').grid(row=8, column=0,
            sticky=W, padx=5, pady=5)

        # Pasang textbox dengan latar belakang berwarna
        self.txtSumber = Entry(mainFrame, width=50, bg='lightgray') 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)


        self.txtHasil2 = Entry(mainFrame, width=50, bg='lightblue') 
        self.txtHasil2.grid(row=4, column=1, padx=5, pady=5)

        self.txtHasil3 = Entry(mainFrame, width=50, bg='lightgreen') 
        self.txtHasil3.grid(row=6, column=1, padx=5, pady=5)

        self.txtHasil4 = Entry(mainFrame, width=50, bg='lightblue') 
        self.txtHasil4.grid(row=8, column=1, padx=5, pady=5)

        # Pasang Button dengan warna latar belakang
        self.btnTranslate = Button(mainFrame, text='Translate!', bg='orange',
            command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menghapus hasil terjemahan sebelumnya
        self.txtHasil2.delete(0, END)
        self.txtHasil3.delete(0, END)
        self.txtHasil4.delete(0, END)

        # menterjemahkan
        hasil2 = penterjemah.translate(self.txtSumber.get(), src='id', dest='en') 
        hasil3 = penterjemah.translate(self.txtSumber.get(), src='id', dest='ko') 
        hasil4 = penterjemah.translate(self.txtSumber.get(), src='id', dest='ja') 

        # menampilkan hasil terjemahan
        self.txtHasil2.insert(END, hasil2.text)
        self.txtHasil3.insert(END, hasil3.text)
        self.txtHasil4.insert(END, hasil3.text)

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()