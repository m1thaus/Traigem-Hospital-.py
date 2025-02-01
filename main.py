import json

def coletar_dados_paciente():
    print("=== PONTUÁRIO DE TRIAGEM ===")
    
    paciente = {
        "Nome": input("Digite seu nome: "),
        "Idade": input("Digite sua idade: "),
        "Sexo": input("Digite seu sexo (M/F): "),
        "Telefone": input("Digite seu telefone: "),
        "Sintomas": input("Descreva seus sintomas: ")
    }
    
    return paciente

def exibir_dados_paciente(paciente):
    print("\n=== DADOS DO PACIENTE ===")
    for chave, valor in paciente.items():
        print(f"{chave}: {valor}")

def main():
    paciente = coletar_dados_paciente()
    exibir_dados_paciente(paciente)

if __name__ == "__main__":
    main()