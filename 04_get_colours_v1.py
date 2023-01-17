import csv

file = open("00_colour_list_hex_v3.csv", "r")
all_colors = list(csv.reader(file, delimiter=","))
file.close()

all_colors.pop(0)
print(all_colors[:50])

print("Length: {}".format(len(all_colors)))
