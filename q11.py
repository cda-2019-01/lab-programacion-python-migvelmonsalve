##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line[:-1] for line in text]
text = [line.split('\t') for line in text]

resultado = []

for line in text:
    resultado.append('{},{},{}'.format(line[0],len(line[3].split(',')),len(line[4].split(','))))
    
resultado = '\n'.join(resultado)
print(resultado)