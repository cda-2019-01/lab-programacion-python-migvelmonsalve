##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()

text = [line[:-1] for line in text]
text = [line.split('\t')[4] for line in text]
text = ','.join(text)
text = text.split(',')
text2 = [line.split(':')[0] for line in text]
text3 = [line.split(':')[1] for line in text]
text4 = list(set(text2))
text4.sort()
for letra in text4:
    x=int(text3[text2.index(letra)])
    y=int(text3[text2.index(letra)])
    for line in text:
        if line.split(':')[0] == letra:
            if int(line.split(':')[1]) > x:
                x = int(line.split(':')[1])
            elif int(line.split(':')[1]) < y:
                y = int(line.split(':')[1])
    print('{},{},{}'.format(letra,y,x))