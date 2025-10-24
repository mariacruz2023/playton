# --- Calculadora de IMC Simples ---

# Solicita o peso e a altura do usuário
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em cm (ex: 175): "))

# Converte a altura de cm para metros
altura_metros = altura / 100

# Calcula o IMC
imc = peso / (altura_metros ** 2)

# Exibe o resultado do IMC com 2 casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Classifica e exibe o resultado
if imc < 18.5:
    print("Classificação: Baixo peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Excesso de peso (pré-obesidade)")
elif 30 <= imc < 35:
    print("Classificação: Obesidade de Classe I")
elif 35 <= imc < 40:
    print("Classificação: Obesidade de Classe II")
else:
    print("Classificação: Obesidade de Classe III")