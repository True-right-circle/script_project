from tkinter import *
from tkinter import font
import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("400x600+750+200")
DataList = []

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="실시간 항공운항 App")
    MainText.pack()
    MainText.place(x=20)
def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=180, y=45)
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=20, height=1, borderwidth=12, relief='ridge')

    SearchListBox.insert(1, "  시간대별 국내선 ")
    SearchListBox.insert(2, "  시간대별 국제선 ")
    SearchListBox.insert(3, "  공항별 국내선 ")
    SearchListBox.insert(4, " 정기 국내선 스케쥴 ")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)


InitTopText()
InitSearchListBox()
g_Tk.mainloop()
