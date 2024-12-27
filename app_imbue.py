from tkinter import *
import tkinter as ttk

imbuement_list = [
                  'Critical', 'Vampirism', 'Void',
                  'Bash', 'Blockade', 'Epiphany',
                  'Precision', 'Slash', 'Featherweight',
                  'Swiftness', 'Vibrancy', 'Electrify',
                  'Frost', 'Reap', 'Scorch','Venom',
                  'Cloud Fabric', 'Demon Presence',
                  'Dragon Hide', 'Lich Shroud', 'Quara Scale',
                  'Snake Skin'
                  ]

root = Tk()
imbuement = StringVar()
imbuement.set(imbuement_list[0])

class Funcs():
    def botao_limpar(self):
        self.basic_entry.delete(0, END)
        self.intricate_entry.delete(0, END)
        self.powerful_entry.delete(0, END)

class App(Funcs):
    def __init__(self):
        self.root = root
        self.window()
        self.frames()
        self.buttons()
        root.mainloop()
    def window(self):
        self.root.title("Imbuiment Calculator")
        self.root.iconbitmap("calculator_icon.ico")
        self.root.configure(background = '#292929')
        Label(root, background='#292929', foreground='#ffffff', text ="IMBUEMENT:", font='Helvetica 11').place(x=27, y=40)
        Label(root, background='#292929', foreground='#ffffff', text ="VALOR ITENS BASIC:", font='Helvetica 11').place(x=27, y=100)
        Label(root, background='#292929', foreground='#ffffff', text ="VALOR ITENS INTRICATE:", font='Helvetica 11').place(x=27, y=160)                               
        Label(root, background='#292929', foreground='#ffffff', text ="VALOR ITENS POWERFUL:", font='Helvetica 11').place(x=27, y=220)  
        Label(root, background='#292929', foreground='#ffffff', text ="TOTAL:", font='Helvetica 11').place(x=120, y=280)           
        self.root.geometry("300x600")
        self.root.resizable(False, False)
    def frames(self):
        self.basic_entry = Entry(root, width=20, font="Helvetica 16", textvariable = "a")
        self.basic_entry.place(x=30,y=120)
        self.intricate_entry = Entry(root, width=20, font="Helvetica 16",  textvariable = "b")
        self.intricate_entry.place(x=30,y=180)
        self.powerful_entry = Entry(root, width=20, font="Helvetica 16",  textvariable = "")
        self.powerful_entry.place(x=30,y=240)            
    def buttons(self):
        self.bt_imbue = OptionMenu(self.root, imbuement, *imbuement_list)
        self.bt_imbue.place(x=30, y=60)
        self.bt_calcular = Button(self.root, text = 'Calcular!', bd=4, font='Helvetica 11 bold', command = self.getImbue)
        self.bt_calcular.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.1)
        self.bt_limpar = Button(self.root, text = 'Limpar!', bd=4, font='Helvetica 11 bold', command = self.botao_limpar)
        self.bt_limpar.place(relx=0.1, rely=0.81, relwidth=0.8, relheight=0.1)
    def getImbue(self):
        im = imbuement.get()
        match im:
            case "Critical":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*25 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320)       
            case "Vampirism":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320)       
            case "Void":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)       
            case "Bash":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*10 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)       
            case "Blockade":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*25 + int(self.powerful_entry.get())*25 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)       
            case "Epiphany":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*15 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)       
            case "Precision":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*20 + int(self.powerful_entry.get())*10 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)       
            case "Slash":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*25 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)       
            case "Featherweight":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*10 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                  
            case "Swiftness":
                total = round(int(self.basic_entry.get())*15 + int(self.intricate_entry.get())*25 + int(self.powerful_entry.get())*20 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)            
            case "Vibrancy":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Electrify":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*5 + int(self.powerful_entry.get())*1 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Frost":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*10 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Reap":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*20 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Scorch":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Venom":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*20 + int(self.powerful_entry.get())*2 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Cloud Fabric":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*15 + int(self.powerful_entry.get())*10 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                    
            case "Demon Presence":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*25 + int(self.powerful_entry.get())*20 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Dragon Hide":
                total = round(int(self.basic_entry.get())*20 + int(self.intricate_entry.get())*10 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Lich Shroud":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*20 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Quara Scale":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*20 + int(self.powerful_entry.get())*5 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                      
            case "Snake Skin":
                total = round(int(self.basic_entry.get())*25 + int(self.intricate_entry.get())*20 + int(self.powerful_entry.get())*10 + 250000)
                total = total/1000
                Label(root, background='#292929', foreground='#ffffff', font="Helvetica 12", text=(f"{total:.1f}K")).place(x=120, y=320,)                       
            case _:
                print("Valor inserido inválido.")
App()