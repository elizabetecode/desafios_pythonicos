"""
01. donuts

Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""


# primeira solucao

# def donuts(count):
#     if count >= 10:
#         print('Number of counts: many')
#     else:
#         print('Number of counts:', count)
#     return


#segunda solução, após fazer o exercício 02_both_ends.py
# def donuts(count):
#     return f'Number of donuts: {count}' if count < 10 else f'Number of donuts: many'


def donuts(count):
    if count >= 10:
        number = f'Number of donuts: many'
    else:
        number = f'Number of donuts: {count}'
    return number


# def donuts(count):
#     return f'Number de donuts: many' if count >= 10 else f'Number of counts:', count


donuts(4)
donuts(9)
donuts(10)
donuts(22)


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(donuts, 4, 'Number of donuts: 4')
    test(donuts, 9, 'Number of donuts: 9')
    test(donuts, 10, 'Number of donuts: many')
    test(donuts, 99, 'Number of donuts: many')










