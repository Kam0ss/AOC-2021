def calcul_bin(x,p):
    return x*pow(2,p)

def test(i,j):
    if list(lines[i])[0] == j:
        liste_co2.append(lines[i])
    else:
        liste_oxygen.append(lines[i])

def garde(k,j,liste_test,liste2):
    for i in range(len(liste_test)):
        if liste_test[i][k] == j:
            liste2.append(liste_test[i])

def list_co2(k,liste_test,liste2):
    for i in range(len(liste_test)):
        liste = list(liste_test[i])
        for j in range(len(liste)-1):
            if int(liste[j]) == 0:
                nb0[j] += 1
            else:
                nb1[j] += 1

    if nb0[k] > nb1[k]:
        garde(k,'0',liste_test,liste2)
    else:
        garde(k,'1',liste_test,liste2)

def list_oxygen(k,liste_test,liste2):
    for i in range(len(liste_test)):
        liste = list(liste_test[i])
        for j in range(len(liste)-1):
            if int(liste[j]) == 0:
                nb0[j] += 1
            else:
                nb1[j] += 1

    if nb0[k] > nb1[k]:
        garde(k,'0',liste_test,liste2)
    else:
        garde(k,'1',liste_test,liste2) 

file = open("C:\\Users\\Camille\\Documents\\ZUnivers\\AOC\\Jour3\\input.txt","r")
lines = file.readlines()
int_gamma = 0
int_epsilon = 0
gamma = ''
epsilon = ''
nb0 = [0,0,0,0,0,0,0,0,0,0,0,0]
nb1 = [0,0,0,0,0,0,0,0,0,0,0,0]
liste_oxygen = []
liste_co2 = []
for i in range(len(lines)):
    liste = list(lines[i])
    for j in range(len(liste)-1):
        if int(liste[j]) == 0:
            nb0[j] += 1
        else: 
            nb1[j] += 1

for j in range(len(liste)):
    if nb0[j] > nb1[j]:
        int_gamma += calcul_bin(0,len(liste)-1-j)
        gamma += '0'
        epsilon += '1'
        int_epsilon += calcul_bin(1,len(liste)-1-j)

    else:
        int_gamma += calcul_bin(1,len(liste)-1-j)
        gamma += '1'
        epsilon += '0'
        int_epsilon += calcul_bin(0,len(liste)-1-j)

print(f'gamma : {gamma}   epsilon : {epsilon}')
print(f'gamma : {int_gamma}   epsilon : {int_epsilon}')
print(f'total : {int_gamma*int_epsilon}')



for i in range(len(lines)):
    if nb0[0] < nb1[0]:
        test(i,'0')
    else:
        test(i,'1')

for k in range(len(nb0)):
    nb0 = [0,0,0,0,0,0,0,0,0,0,0,0]
    nb1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    liste_oxygen2 = []
    list2(k,liste_oxygen,liste_oxygen2)
    liste_oxygen = liste_oxygen2


    nb0 = [0,0,0,0,0,0,0,0,0,0,0,0]
    nb1 = [0,0,0,0,0,0,0,0,0,0,0,0]
    liste_co22 = []
    list2(k,liste_co2,liste_co22)
    liste_co2 = liste_co22

print(f'oxygen : {liste_oxygen}    co2 : {liste_co2}')

liste = list(liste_oxygen[0])
oxygen = 0
co2 = 0
for i in range(len(liste)-1):
    oxygen += calcul_bin(int(list(liste_oxygen[0])[i]),len(liste)-2-i)
    co2 += calcul_bin(int(list(liste_co2[0])[i]),len(liste)-2-i)

print(f'oxygen : {oxygen}    co2 : {co2}')
print(f'total : {oxygen*co2}')