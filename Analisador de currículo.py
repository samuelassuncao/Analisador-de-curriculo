print('Olá! Meu nome é Sam, e eu vou analisar o seu currículo hoje.')
pontuacao = 0
nome = str(input('Primeiro, nos diga seu nome! ')).capitalize()
idade = int(input(f'Muito Prazer, {nome}, qual é a sua idade? '))
if idade < 18:
    print(f'Perdão, {nome}, nesta vaga só aceitamos maiores de idade! ')
else:
    experiencia = int(input('Quanto tempo de experiência na área de programação? '
                            '\nPor favor, responda "0" para 0 a 6 meses, "1" para 1 a 2 anos ou "2" para mais de 2 anos '))
    if experiencia == 0:
        pontuacao += 1
    elif experiencia == 1:
        pontuacao += 2
    elif experiencia == 2:
        pontuacao += 3
    else:
        while experiencia not in [0, 1, 2] :
            experiencia = int(input('RESPOSTA INVÁLIDA'
                      '\nPor favor, responda "0" para menos de 1 ano, "1" para 1 a 2 anos ou "2" para mais de 2 anos ')) #NÃO ESTÁ FUNCIONANDO
            if experiencia == 0:
                pontuacao += 1
            elif experiencia == 1:
                pontuacao += 2
            elif experiencia == 2:
                pontuacao += 3
    projetos = int(input('Quantos projetos você tem publicados no GitHub? '
                        '\nPor favor, responda "0" para 0 a 10 projetos, "1" para 11 a 20 projetos ou "2" para mais de 20 projetos '))
    if projetos == 0:
        pontuacao += 1
    elif projetos == 1:
            pontuacao += 2
    elif projetos == 2:
            pontuacao += 3
    else:
        while projetos not in [0, 1, 2]:
            projetos = int(input('RESPOSTA INVÁLIDA'
                    '\nPor favor, responda "0" para 0 a 6 meses, "1" para 1 a 2 anos ou "2" para mais de 2 anos '))  # NÃO ESTÁ FUNCIONANDO
            if projetos == 0:
                pontuacao += 3
            elif projetos == 1:
                pontuacao += 4
            elif projetos == 2:
                pontuacao += 5
    python = str(input('Você tem conhecimento com a linguagem python? (S/N) ')).upper()
    if python == 'S':
        pontuacao += 1
    elif python == 'N':
        pontuacao += 0
    else:
        while python not in 'SsNn':
            python = str(input('Você tem conhecimento com a linguagem python? (S/N) ')).upper()
            if projetos == 'S':
                pontuacao += 1
            elif python == 'N':
                pontuacao += 0
    javascript = str(input('Você tem conhecimento com a linguagem javascript? (S/N) ')).upper()
    if javascript == 'S':
        pontuacao += 1
    elif javascript =='N':
        pontuacao += 0
    else:
        while javascript not in 'SsNn':
            javascript = str(input('Você tem conhecimento com a linguagem javascript? (S/N) ')).upper()
            if javascript == 'S':
                pontuacao += 1
            elif javascript == 'N':
                pontuacao += 0
    php = str(input('Você tem conhecimento com a linguagem php? (S/N) ')).upper()
    if php == 'S':
        pontuacao += 1
    elif php == 'N':
        pontuacao += 0
    else:
        while php not in 'SsNn':
            php = str(input('Você tem conhecimento com a linguagem php? (S/N) ')).upper()
            if php == 'S':
                pontuacao += 1
            elif php == 'N':
                pontuacao += 0
    csharp = str(input('Você tem conhecimento com a linguagem C#? (S/N) ')).upper()
    if csharp == 'S':
        pontuacao += 1
    elif csharp == 'N':
        pontuacao += 0
    else:
        while csharp not in 'SsNn':
            csharp = str(input('Você tem conhecimento com a linguagem php? (S/N) ')).upper()
            if csharp == 'S':
                pontuacao += 1
            elif csharp == 'N':
                pontuacao += 0
    print(f'Muito obrigado pelas respostas, {nome}! Sua pontuação no nosso teste foi {pontuacao}! Assim que possível entraremos em contato com você. Boa sorte!')
