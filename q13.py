##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line[:-1] for line in text]
text = [line.split('\t') for line in text]

for line in text:
    column5 = line[4].split(',')
    x=0
    for line2 in column5:
        x = x + int(line2.split(':')[1])
    print('{},{}'.format(line[0],x))