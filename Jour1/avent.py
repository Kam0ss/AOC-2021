fichier = open('C:\\Users\\AN28170\\Documents\\ZUnivers\\Avent\\Jour1\\Input.txt')
inputs = fichier.readlines()
inputs = [int(i) for i in inputs]
j=0
prev_somme = sum(inputs[0:3])
for i in range(1,len(inputs)-2):
    #if inputs[i+1] > inputs[i]:
    #    j += 1
    somme = sum(inputs[i:i+3])
    if somme > prev_somme:
        j += 1
    prev_somme = somme
print(j)