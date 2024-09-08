entrada_idade = ''

while entrada_idade != 0:
    try:
        entrada_idade = int(input('Digite um número qualquer ou 0 para sair: '))
        print('Número digitado:', entrada_idade)
    except ValueError:
        print('Entrada inválida! Digite um número inteiro.')

print('Fim do loop WHILE')