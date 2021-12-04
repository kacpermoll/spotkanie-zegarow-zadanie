from datetime import datetime
import czytanie

# returns the time in seconds
def total_seconds(list):
    for i in range(0, czytanie.set_of_three_clocks):
        for j in range(0, czytanie.cloks_number):
            time = datetime.strptime(list[i][j][0], "%H:%M")
            time_in_seconds = time.minute * 60 + time.hour * 3600
            list[i][j][0] = time_in_seconds
    return list


def sort_by_delay(list):
    for i in range(0, czytanie.set_of_three_clocks):
        # reverse = True ---> sorts in descending order
        list[i] = sorted(list[i], key=lambda l: int(l[1]), reverse=True)
    return list


def time_to_meet(list):
    minutes = []
    for i in range(0, czytanie.set_of_three_clocks):
        minutes.append(0)
        clock1_time = list[i][0][0]
        clock1_delay = list[i][0][1]
        clock2_time = list[i][1][0]
        clock2_delay = list[i][1][1]
        clock3_time = list[i][2][0]
        clock3_delay = list[i][2][1]

        if (
            int(clock1_delay) == int(clock2_delay)
            or int(clock1_delay) == int(clock3_delay)
            or int(clock3_delay) == int(clock2_delay)
        ):
            minutes[i] = "Zegary sie nigdy nie spotkaja"

        else:
            while not (clock1_time == clock2_time == clock3_time):
                clock1_time += 60 + int(clock1_delay)
                clock2_time += 60 + int(clock2_delay)
                clock3_time += 60 + int(clock3_delay)
                minutes[i] += 1
    return minutes


seconds_array3D = total_seconds(czytanie.array3D)
sorted_seconds_array3D = sort_by_delay(seconds_array3D)
seconds_to_meet = time_to_meet(sorted_seconds_array3D)

myFile = open("daneWyjsciowe.txt", "w")
myFile.write("")
myFile.close()

myFile = open("daneWyjsciowe.txt", "a")
for i in range(len(seconds_to_meet)):
    if seconds_to_meet[i] == "Zegary sie nigdy nie spotkaja":
        myFile.write(seconds_to_meet[i] + "\n")
    else:
        myFile.write(str(seconds_to_meet[i] * 60) + "s\n")
myFile.close()

print("\nProgam zostal pomyslnie wykonany! \n")
