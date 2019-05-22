primos = [2]
numero_max = 1000
for x in range (2,numero_max):
    for i in range (2,x):
        if x%i !=0:
            continue
        else:
            break
    else: print ('%d'%x)
