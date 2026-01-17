# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Instala pyautogui para automação de mouse e teclado
# Terminal: pip install pyautogui

import pandas as pd
import pyautogui
import time

# pyautogui.write -> escreve texto no campo ativo
# pyautogui.press -> aperta uma tecla (enter, tab, etc)
# pyautogui.click -> clica em coordenadas X,Y da tela
# pyautogui.hotkey -> combinação teclas (Ctrl+C)

# Define pausa de 0.3 segundos entre todas as ações do mouse/teclado (evita cliques rápidos demais)
pyautogui.PAUSE = 0.3 

# Abrir o navegador (chrome)
pyautogui.press("win")  # Simula pressionar tecla Windows (abre menu Iniciar)
pyautogui.write("chrome")  # Digita "chrome" no campo de busca do Windows
pyautogui.press("enter")  # Aperta Enter para abrir o Chrome

# Entrar no link
# Digita URL completa no Chrome
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# Aperta Enter para navegar até página de login
pyautogui.press("enter")
# Pausa 3 segundos esperando página carregar
time.sleep(3)


# Passo 2: Fazer login
# Selecionar o campo de email

pyautogui.click(x=685, y=451) # Move mouse para posição X=685,Y=451 e clica (campo email)
pyautogui.write("pythonimpressionador@gmail.com") # Escrever o seu email
pyautogui.press("tab")  # Passando pro próximo campo
pyautogui.write("sua senha") # Digita senha no campo de senha agora ativo
pyautogui.click(x=955, y=638)  # Clica no botao de login
time.sleep(3) # Espera 3s para login processar e página carregar

# Passo 3: Importar a base de produtos pra cadastrar

# Lê arquivo CSV contendo todos os produtos para cadastro
tabela = pd.read_csv("produtos.csv")
# Verificar dados carregados
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:  # Loop percorre cada linha/index da tabela (cada produto)
    # clicar no campo de código
    pyautogui.click(x=653, y=294)  # Clica no campo "código" do formulário web
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]  # Extrai valor da coluna "codigo" da linha atual
    # preencher o campo
    pyautogui.write(str(codigo))  # Converte código para texto e digita no campo
    # passar para o proximo campo
    pyautogui.press("tab")  # Tab move para próximo campo (marca)
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))  # Digita marca do produto da linha atual
    pyautogui.press("tab")  # Tab move para campo tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))  # Digita tipo do produto
    pyautogui.press("tab")  # Tab move para campo categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))  # Digita categoria
    pyautogui.press("tab")  # Tab move para campo preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))  # Digita preço unitário
    pyautogui.press("tab")  # Tab move para campo custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))  # Digita custo do produto
    pyautogui.press("tab")  # Tab move para campo observações
    obs = tabela.loc[linha, "obs"]  # Pega valor da coluna "obs" da linha atual
    if not pd.isna(obs):  # Verifica se observação não é NaN/vazia
        pyautogui.write(str(tabela.loc[linha, "obs"]))  # Digita observação se existir
    pyautogui.press("tab")  # Tab move para botão cadastrar
    pyautogui.press("enter")  # cadastra o produto (botao enviar)  # Enter aciona botão "Cadastrar"
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)  # Rola página 5000 pixels para cima (reseta formulário)
    # Passo 5: Repetir o processo de cadastro até o fim  # Loop repete para todos produtos da tabela