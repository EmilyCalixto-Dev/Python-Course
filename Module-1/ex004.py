n = input('Digite algo: ')
if (n.isnumeric()):
    print('{} é inteiro'.format(n))
if (n.isalpha()):

    print('{} é uma string'.format(n))
if (n.isdecimal()):
    print('{} é um float'.format(n))


