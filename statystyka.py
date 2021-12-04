from typing import Counter, Text


f = open("daneWyjsciowe.txt", "r")
text = f.readlines()
f.close()

# removing suffix "\n"
text1 = []
for i in text:
    text1.append(i.removesuffix("\n"))

result = 0
counter = 0
for i in text1:
    if i == "Zegary sie nigdy nie spotkaja":
        continue
    else:
        result += int(i)
        counter += 1

mean_average = result / counter
f = open("statystyka.txt", "w")
f.write(str(mean_average))
f.close()
