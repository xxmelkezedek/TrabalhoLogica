# Variável de controle para saída
saida = ''

# Função para soma
def adicao(a, b):
    return a + b

# Função para subtração
def subtracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    if operacao in ('+', 'soma'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtracao'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multiplicacao'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço principal
while saida.lower() != 'n':
    try:
        # Solicita os números e a operação ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ").strip().lower()

        # Calcula o resultado
        resultado = calculadora(num1, num2, operacao)

        # Exibe o resultado
        print(f"Resultado da operação: {resultado}")

        # Pergunta se o usuário deseja continuar
        saida = input("Deseja continuar? Digite S para sim ou N para não: ").strip().lower()
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números e operações válidas.")
