import pyautogui
import time
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# dados de login do site de teste (troque pelos seus)
EMAIL = "seu-email@exemplo.com"
SENHA = "sua-senha"

# passo 1: entrar no sistema da empresa
# abrir o navegador
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

time.sleep(2)

pyautogui.hotkey("ctrl", "l") #seleciona a barra de endereco
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)



# passo 2: fazer login
pyautogui.press("tab")
pyautogui.write(EMAIL)
pyautogui.press("tab") #passar para o botao
pyautogui.write(SENHA)
pyautogui.press("tab") #passar para o botao
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=386, y=1334)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
