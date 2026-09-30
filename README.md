# Bot de Automação de Cadastro de Produtos

## Sobre o projeto
Bot em Python que automatiza o cadastro de produtos em um site, eliminando a necessidade de digitar manualmente cada item um por um.

## Problema
Cadastrar produtos manualmente em um site, item por item, é repetitivo, lento e sujeito a erro de digitação — principalmente quando há muitos produtos (dezenas ou centenas) para cadastrar.

## O que o projeto faz
- Lê os dados dos produtos de um arquivo CSV (código, marca, tipo, categoria, preço unitário, custo, observações)
- Usa PyAutoGUI para simular a digitação e navegação no site, preenchendo os campos automaticamente
- Usa Pandas para organizar e tratar os dados antes do cadastro
- Cadastra cada produto do CSV automaticamente, sem intervenção manual

## Tecnologias usadas
Python
Pandas
PyAutoGUI

## Como rodar
pip install pandas pyautogui
python automacao_bot.py

Coloque o arquivo produtos.csv na mesma pasta do script.

## Resultado
Transforma um processo manual e repetitivo em uma tarefa automática — o que levaria minutos por produto cadastrado manualmente passa a ser feito em segundos, sem risco de erro de digitação.

