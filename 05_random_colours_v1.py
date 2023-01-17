import csv
from tkinter import *
import random


class GetColors:

    def __init__(self):
        # get all colours
        color_list = self.get_all_colours()

        self.choice_frame = Frame(padx=10, pady=10)
        self.choice_frame.grid()



    def get_all_colours(self):
        print("You chose to get all the colours!")

        file = open("00_colour_list_hex_v3.csv", "r")
        all_colors = list(csv.reader(file, delimiter=","))
        file.close()

        all_colors.pop(0)
        return all_colors


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    GetColors()
    root.mainloop()
