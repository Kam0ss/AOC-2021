file = open("C:\\Users\\Camille\\Documents\\ZUnivers\\AOC\\Jour2\\input.txt","r")
lines = file.readlines()
horizontal = 0
profondeur = 0
aim = 0
for i in range(len(lines)):
    if 'down' in lines[i]:
        aim += int(lines[i].split()[1])
    elif 'up' in lines[i]:
        aim -= int(lines[i].split()[1])
    else:
        horizontal += int(lines[i].split()[1])
        profondeur += aim*int(lines[i].split()[1])
print(horizontal*profondeur)