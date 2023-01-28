"""
06. not_bad
Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.
Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""


def not_bad(s):
    if 'not' and 'bad' in s:
        start = s.index('not')
        end = s.index('bad')
        if start < end:
            return s.replace(s[start:end+3], 'good')
    return s


def not_bad_2(s):
    if 'not' and 'bad' in s:
        if s.index('not') < s.index('bad'):
            return s.replace(s[s.index('not'):s.index('bad')+3], 'good')
    return s


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
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
    # TESTE DA SEGUNDA VERSÃO
    test(not_bad_2, 'This movie is not so bad', 'This movie is good')
    test(not_bad_2, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad_2, 'This tea is not hot', 'This tea is not hot')
    test(not_bad_2, "It's bad yet not", "It's bad yet not")



