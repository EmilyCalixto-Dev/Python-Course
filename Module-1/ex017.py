import math
catop = float(input('Qual é o comprimento do cateto oposto? '))
catadj = float(input('Qual é o comprimento do cateto adjacente? '))
hipotenusa = math.hypot(catop, catadj)
print('A hipotenusa vai medir: {:.2f}'.format(hipotenusa))
