from funções import add
from funções import see 
from funções import att 
from funções import fav
from funções import contatoFavorito
from funções import delete
contatos = []

while True:
    print("\nMenu de Contatos.")
    print("1. Adcionar um contato")
    print("2. Visualizar a lista de contatos")
    print("3. Atualizar um contato")
    print("4. Marcar ou desmarcar um contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Excluir um contato")
    print("7. Sair")

    choice = input("Digite sua escolha: ") 
    if choice == "1":
       name = input("Digite o nome do contato que deseja adcionar: ")
       phone = input("Digite o número do contato: ")
       add(contatos, name, phone)

    elif choice == "2":
       see(contatos)
      
    elif choice == "3":
       see(contatos)
       IndiceContato = input("Digite o indice do contato que deseja alterar: ")
       novoNome= input("Digite o novo nome do contato: ")
       att(contatos, IndiceContato, novoNome)
      
    elif choice == "4":
       see(contatos)
       IndiceContato = input("Digite o indice do contato que deseja favoritar ou remover de favorito: ")
       favorito = input("Deseja 'adicionar' ou 'remover' da lista de favoritos? ")  
       fav(contatos, IndiceContato, favorito)          
       print("Alteração feita com sucesso!")

    elif choice == "5":
       contatoFavorito(contatos)

    elif choice == "6":
       see(contatos)
       IndiceContato = input("Digite o indice do contato que você deseja excluir: ")
       delete(contatos, IndiceContato)

    elif choice == "7":
     break

