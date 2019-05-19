##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
text = []
with open('data.csv', 'rt') as f:
        text += f.readlines()
        
text = [line.split('\t') for line in text]
text2 = [line[3] for line in text]
text2 = ','.join(text2)
text2 = text2.split(',')
text4 = list(set(text2))
text4.sort()
for letra in text4:
    x=0
    for line in text:
        if line[3].split(',').count(letra) > 0:
            x = x + int(line[1])
    print('{},{}'.format(letra,x))