def add(contatos, name, phone):
    contato = {"Nome do contato":name, "Numero do contato": phone, "favorito": False}
    contatos.append(contato)
    print(f"Contato {name} foi adicionado com sucesso!")
    return

def see(contatos):
   print("\nLista de Contatos:")
   for indice, contato in enumerate(contatos, start= 1):
      status = "★" if contato.get("favorito", False) else " "
      name = contato["Nome do contato"]
      phone = contato["Numero do contato"]
      print(f"{indice}. [{status}] {name} - {phone}")

def att(contatos, IndiceContato, novoNome):
   IndiceAjustado = int(IndiceContato) -1 
   if IndiceAjustado >= 0 and IndiceAjustado <= len(contatos):
      contatos[IndiceAjustado]["Nome do contato"] = novoNome
      print(f"Contato {IndiceContato} foi atualizado para {novoNome}")
   else:
      print("Indice de contato inválido.")
      return

def fav(contatos, IndiceContato, favorito):
   IndiceAjustado = int(IndiceContato) - 1
   if favorito.lower() == "adicionar":  # Transforma em minúsculas para evitar erros de digitação
    contatos[IndiceAjustado]["favorito"] = True        
    print(f"Contato {IndiceContato} marcado como favorito.")
   elif favorito.lower() == "remover":
       contatos[IndiceAjustado]["favorito"] = False
       print(f"Contato {IndiceContato} removido dos favoritos.")
   else:
      print("Comando inválido!")

def contatoFavorito(contatos):
   print("\nLista de Contatos Favoritos:")
   favoritos = [contato for contato in contatos if contato.get("favorito", False)]

   if not favoritos:
      print("Contato não encontrado.")

   else: 
      for indice, contato in enumerate(favoritos, start= 1):
         name = contato["Nome do contato"]
         phone = contato["Numero do contato"]
         print(f"{indice}. [★] {name} - {phone}")

def delete(contatos, IndiceContato):
      IndiceAjustado = int(IndiceContato) -1 
      del contatos[IndiceAjustado]
      print("Contato removido com sucesso!")
