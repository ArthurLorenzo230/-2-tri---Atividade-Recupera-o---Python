# Programa com menu interativo

while True:
    print("\n=== MENU ===")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("👋 Olá! Seja bem-vindo!")
    elif opcao == "2":
        print("ℹ️ Para usar o programa, escolha uma das opções do menu.")
    elif opcao == "3":
        print("🚪 Saindo do programa... Até logo!")
        break
    else:
        print("⚠️ Opção inválida! Tente novamente.")
