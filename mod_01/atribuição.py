table = (('Bete', 'Santos', 41, 1.65),
         ('Vinicius', 'Santarém', 39, 1.78))


for row in table:
    nome, cidade, idade, altura = row
    print(row)


# (*_ signifca o resto das informações, em vez do underscore, poderia ser usado na frente de *nome também.
for nome, *_ in table:
    print(nome, _)



def f(t):
    nome, *_ = t
    print(nome, _)



#if __name__ == '__main__': # entry point
    #f(row)






