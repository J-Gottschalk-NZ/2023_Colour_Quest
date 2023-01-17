import csv
from tkinter import *


class GetColors:

    def __init__(self):
        # get all colours
        color_list = self.get_all_colours()

        self.color_frame = Frame(padx=10, pady=10)
        self.color_frame.grid()

        for item in color_list[201:]:
            color_name = item[0]
            score = item[1]
            fg_color = item[2]
            color_label = "{} ({})".format(color_name, score)
            self.color_label = Label(self.color_frame, text=color_label,
                                     fg=fg_color, bg=color_name)
            self.color_label.grid(row=color_list.index(item)//10,
                                  column=color_list.index(item) % 10)

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
