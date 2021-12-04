# this file is responsible for loading data from a file
# and then assigning them to a 3D list accordingly
import pprint


def ThreeD(a, b, c):
    lst = [[[None for col in range(a)] for col in range(b)] for row in range(c)]
    return lst


# reading from file
myFile = open("daneWejsciowe.txt")
text = myFile.read()
myFile.close()

# spliting the file content into lines
ls_lines = text.split("\n")

# clock = 2 because each clock consists of two pieces of information:
#  - the time
#  - the duration of one minute
clock = 2

# cloks_number = 3 because we are considering a situation with three clocks
cloks_number = 3

# set_of_three_clocks is equal number of lines in the file
set_of_three_clocks = len(ls_lines)

# creating a 3D list
array3D = ThreeD(clock, cloks_number, set_of_three_clocks)


ls_each_clock = []
ls_three_clocks = []


for i in ls_lines:
    ls_three_clocks = i.split("||", 2)
    for j in ls_three_clocks:
        ls_each_clock += j.split("|", 1)


for i in range(0, set_of_three_clocks):  # row times
    for j in range(0, cloks_number):  # three times
        for k in range(0, clock):  # two times
            array3D[i][j][k] = ls_each_clock.pop(0)

# deleting unnecessary data from memory
ls_lines.clear()
ls_three_clocks.clear()
