def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b

if __name__ == "__main__":
    print("--- Calculadora Simples ---")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador (+, -, /): ")

        if operador == '+':
            resultado = soma(num1, num2)
        elif operador == '-':
            resultado = subtracao(num1, num2)
        elif operador == '/':
            resultado = divisao(num1, num2)
        if operador == '*':
            resultado = multiplicacao(num1, num2)
        else:
            resultado = "Operador inválido."

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, digite números.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")