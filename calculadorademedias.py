print("===== Calculadora de Médias Acadêmicas =====")

while True:
    disciplina = input("\nDigite o nome da disciplina (ou 'sair' para encerrar): ")
    if disciplina.lower() == 'sair':
        print("Programa encerrado. Bons estudos!")
        break

    soma_notas = 0
    qtd_notas = 0

    while True:
        try:
            nota = float(input(f"Digite a nota {qtd_notas + 1} de {disciplina} (ou -1 para finalizar): "))
            if nota == -1:
                break
            if 0 <= nota <= 10:
                soma_notas += nota
                qtd_notas += 1
            else:
                print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número válido.")

    if qtd_notas == 0:
        print("⚠️ Nenhuma nota foi inserida para esta disciplina.")
        continue

    media = soma_notas / qtd_notas
    print(f"\n🔹 Média da disciplina {disciplina}: {media:.2f}")

    if media >= 7:
        print("✅ Resultado: Aprovado!")
    elif 5 <= media < 7:
        print("⚠️ Resultado: Recuperação.")
    else:
        print("❌ Resultado: Reprovado.")
