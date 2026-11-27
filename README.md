# 🤖 Bot de Automação de Cadastro de Produtos

Bot em **Python** que cadastra produtos automaticamente em um sistema web. Ele lê uma planilha de produtos e controla o mouse e o teclado do computador para preencher o formulário do site, item por item, sem digitação manual.

---

## 📌 O problema

Cadastrar produtos à mão em um sistema, um por um, é repetitivo, lento e sujeito a erros de digitação. Com dezenas ou centenas de itens, uma tarefa simples passa a tomar horas.

## ✅ A solução

O bot faz o mesmo trabalho que uma pessoa faria, só que sozinho e sem errar a digitação:

1. Abre o navegador e entra no site do sistema.
2. Faz login.
3. Lê a planilha `produtos.csv` com o **Pandas**.
4. Para cada produto, preenche todos os campos do formulário e clica em enviar.
5. Volta para o topo da página e repete até o último produto.

Com a base de exemplo, são **292 produtos** cadastrados sem nenhuma digitação manual.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| PyAutoGUI | Controla o mouse e o teclado para preencher o formulário |
| Pandas | Lê e organiza os dados da planilha de produtos |

---

## 📂 Estrutura do projeto

```text
automacao-bot/
│
├── automacao_bot.py    # o bot: abre o site, faz login e cadastra os produtos
├── pegar_posicao.py    # utilitário para descobrir a posição de um campo na tela
├── produtos.csv        # base de produtos a cadastrar
├── requirements.txt    # bibliotecas necessárias
├── .gitignore          # arquivos temporários que não vão para o GitHub
└── README.md
```

A planilha `produtos.csv` tem as colunas `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo` e `obs` (observação, opcional).

---

## 🚀 Como rodar

**1. Instale as dependências**

```bash
pip install -r requirements.txt
```

**2. Ajuste o login**

O bot lê o login de duas variáveis de ambiente, para a senha não ficar escrita no código. No PowerShell, antes de rodar:

```powershell
$env:BOT_EMAIL = "seu-email@exemplo.com"
$env:BOT_SENHA = "sua-senha"
```

Elas valem só para aquela janela do terminal. Se não forem definidas, o bot usa os valores de exemplo do código.

**3. Ajuste a posição do primeiro campo (se precisar)**

O bot clica no campo "código" usando a posição dele na tela, que muda conforme a resolução do monitor. Para descobrir a posição na sua tela:

```bash
python pegar_posicao.py
```

Você tem 10 segundos para colocar o mouse em cima do campo. O script mostra as coordenadas `x` e `y`. Atualize esses valores na linha do `pyautogui.click(...)` no `automacao_bot.py`.

**4. Rode o bot**

```bash
python automacao_bot.py
```

Depois de iniciar, **não mexa no mouse nem no teclado** até o bot terminar, porque ele está usando os dois.

Enquanto roda, o terminal mostra o progresso (`Produto 1 de 292 cadastrado`...) e, no fim, mostra quantos produtos foram cadastrados e quanto tempo levou.

> 🛑 **Para interromper**, leve o mouse rapidamente até o canto superior esquerdo da tela. É uma proteção do próprio PyAutoGUI.

---

## ⚙️ Ajustando a velocidade

No `automacao_bot.py`, dois valores controlam o ritmo do bot:

| Valor | O que faz | Padrão |
|---|---|---|
| `pyautogui.PAUSE` | Pausa depois de cada ação (digitar, apertar Tab...) | `0.15` s |
| `time.sleep(...)` depois do Enter | Tempo para o site processar cada cadastro | `0.5` s |

Valores menores deixam o bot mais rápido, mas, se o site não acompanhar, os dados podem cair no campo errado. Se isso acontecer, aumente os valores aos poucos.

---

## 🩺 Problemas comuns

| Sintoma | Causa provável | Solução |
|---|---|---|
| Os dados caem no campo errado | A posição do clique não bate com a sua tela | Rode o `pegar_posicao.py` de novo e atualize o `pyautogui.click(...)` |
| Pula campos ou digita antes da hora | O site está mais lento que o bot | Aumente o `pyautogui.PAUSE` ou o `time.sleep` depois do Enter |
| "Arquivo produtos.csv nao encontrado" | O terminal está em outra pasta | Entre na pasta do projeto antes de rodar |
| Preciso parar no meio | — | Leve o mouse até o canto superior esquerdo da tela |

---

## ⚠️ Limitações

- Feito para **Windows** com o **Microsoft Edge** (o bot abre o navegador pela tecla Windows).
- Depende da **posição dos elementos na tela**, então mudanças de resolução, zoom ou layout do site exigem ajuste.
- Usa **tempos de espera fixos**: se o site demorar mais do que o esperado para carregar, o bot pode digitar antes da hora.

## 🗺️ Próximas melhorias

- [ ] Trocar o PyAutoGUI por **Selenium** ou **Playwright**, que encontram os campos pelo código da página e não pela posição na tela
- [x] Ler o login de fora do código (variáveis de ambiente)
- [ ] Gerar um relatório no final com os produtos cadastrados e os que deram erro
