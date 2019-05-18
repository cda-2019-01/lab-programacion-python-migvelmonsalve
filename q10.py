##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
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
resultado = []
for letra in text4:
    x=0
    for line in text:
        if line.split(':')[0] == letra:
            x = x + 1
    resultado.append('{},{}'.format(letra,x))
resultado = '\n'.join(resultado)
print(resultado)
