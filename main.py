import pandas as pd
import pivottablejs as piv
import webbrowser
from tkinter import *


class Pivoncjusz:
    def __init__(self = None):

        root = Tk()
        root.geometry("400x200")
        root.title("Pivoncjusz Tabeliusz")


        l1 = Label(root, text="What csv file you want open? ")
        l1.config(font=("Courier", 10))
        l1.pack()

        inputer_file_text = StringVar()
        inputer_file = Entry(root, width=10, textvariable=inputer_file_text)
        inputer_file.pack()


        l2 = Label(root, text="What symbol (character) is the separator in your file? ")
        l2.config(font=("Coutier", 10))
        l2.pack()

        inputer_separator_text = StringVar()
        inputer_separator = Entry(root, width=10, textvariable=inputer_separator_text)
        inputer_separator.pack()

        def funcer_creator():
            df = pd.read_csv(f"{inputer_file_text.get()}.csv", sep=f"{inputer_separator_text.get()}")
            piv.pivot_ui(df)
            return webbrowser.open("pivottablejs.html")


        Button1 = Button(root, height=2,
                         width=20,
                         text="Show",
                         command= funcer_creator)
        Button1.pack()


        mainloop()


Pivoncjusz()