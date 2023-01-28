def f():
    return 42


print(f())


def f1():
    pass


print(f1())


def f(a, b, c='C'): # c está como valor default
    print(a, b, c)


f('A', 'B', 'C')
f(a='A', b='B', c='C')
f('A', 'B')


def f(a, b, c='C', *args): # nome args é convenção (tupla que agrupa os argumentos sem correspondência)
    print(a, b, c, args)


f('A', 'B', 'C', 'E', 'F')


def f(a, b, c='C', **kwargs): # nome kwargs é convenção (passa quantidade indeterminada parâmetros nomeados)
    print(a, b, c, kwargs)


f(c='C', z='Z', a='A', b='B', g='G')


def f(a, b, c='C', *args, x=42, y=51, **kwargs):  # kwargs - quantidade infinita de parâmetros posicionais
    print(a, b, c, x, y, args, kwargs)


f('A', 'B', 'C', 'D', 'E', x= 2, y =1, z='Z', w='W')
# output: 'ABC' posicionais, 'DE' posicionais na tupla args e o 'WZ' nomeados no dicionário Kwargs.


# keyword only arguments - pode vir entre o args e o kwargs. ex(x=42, y=51)
# precisa obrigatoriamente passar argumentos nomeados


""" lookups - o django não chama de kwargs e sim lookups"""


def filter(**lookups):
    for k, v in lookups.items():
        print(k.split('__'), v)


filter(name__startswith='Hen', age__lt=30,
       city__endswith='rói')


def teste(*args, **kwargs):
    print(args, kwargs)


t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

teste(t, d)  # output - ficou tudo no args e {} no kwargs
teste(*t, **d)  # output - especificando *t(parâmetro posicional) **d(unpacked de parâmetro nomeado)


















