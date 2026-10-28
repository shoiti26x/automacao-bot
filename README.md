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
└── README.md
```

A planilha `produtos.csv` tem as colunas `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo` e `obs` (observação, opcional).

---

## 🚀 Como rodar

**1. Instale as dependências**

```bash
pip install pandas pyautogui
```

**2. Ajuste o login**

No início do `automacao_bot.py`, preencha as variáveis `EMAIL` e `SENHA` com os dados de acesso do site.

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

> 🛑 **Para interromper**, leve o mouse rapidamente até o canto superior esquerdo da tela. É uma proteção do próprio PyAutoGUI.

---

## ⚠️ Limitações

- Feito para **Windows** com o **Microsoft Edge** (o bot abre o navegador pela tecla Windows).
- Depende da **posição dos elementos na tela**, então mudanças de resolução, zoom ou layout do site exigem ajuste.
- Usa **tempos de espera fixos**: se o site demorar mais do que o esperado para carregar, o bot pode digitar antes da hora.

## 🗺️ Próximas melhorias

- [ ] Trocar o PyAutoGUI por **Selenium** ou **Playwright**, que encontram os campos pelo código da página e não pela posição na tela
- [ ] Ler o login de um arquivo `.env`, fora do código
- [ ] Gerar um relatório no final com os produtos cadastrados e os que deram erro
