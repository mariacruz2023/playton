def cadastro():
  """
  Pede para o usuário cadastrar um nome de usuário e uma senha.
  A senha precisa ter no mínimo 6 caracteres.
  """
  while True:
    usuario = input("Crie seu nome de usuário: ")
    senha = input("Crie sua senha (mínimo de 6 caracteres): ")

    if len(senha) >= 6:
      print("Cadastro concluído!")
      return usuario, senha
    else:
      print("A senha precisa ter pelo menos 6 caracteres. Tente novamente.")

def login(usuario_cadastrado, senha_cadastrada):
  """
  Pede para o usuário fazer login e verifica se as credenciais estão corretas.
  """
  while True:
    usuario_login = input("\nDigite seu nome de usuário: ")
    senha_login = input("Digite sua senha: ")

    if usuario_login == usuario_cadastrado and senha_login == senha_cadastrada:
      print("Login bem-sucedido! Bem-vindo.")
      return True
    else:
      print("Usuário ou senha incorretos. Tente novamente.")

usuario, senha = cadastro()
login(usuario, senha)
