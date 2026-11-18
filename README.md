[README.md](https://github.com/user-attachments/files/35031449/README.md)
# 🎮 Analisador de Vendas de Video Games (CLI)

## 👥 Integrantes da Equipe

* [João Paulo Arruda Corrêa] 
* [Isabela Oliveira Rezende] 
  

## 🗂️ Sobre o Dataset Escolhido

* **Tema Geral:** Vendas globais de video games (mercado de jogos eletrônicos).
* **Fonte de Dados (URL):** https://www.kaggle.com/datasets/gregorut/videogamesales
* **Motivação:** A base reúne mais de 16 mil jogos com ano de lançamento, gênero, plataforma, publisher e vendas (em milhões de unidades) na América do Norte, Europa, Japão, outras regiões e no mundo. Queríamos descobrir quais gêneros e épocas concentram mais vendas e se o comportamento de compra varia entre as regiões.

## 🏗️ Arquitetura e Estruturação (O que vocês codaram)

```
projeto/
├── data/              # vgsales.csv (baixado do Kaggle)
├── src/
│   ├── __init__.py
│   └── analisador.py  # Classe AnalisadorVendas
├── main.py            # Menu interativo (CLI)
├── requirements.txt   # pandas, matplotlib, seaborn
└── README.md
```

* **Módulos / Classes Criadas:** A classe `AnalisadorVendas`, em `src/analisador.py`, é o núcleo do sistema. Ela é responsável por:
  * ler o `.csv` e fazer a limpeza no construtor (`__init__`);
  * processar os dados com métodos específicos: estatísticas globais (média, mediana, desvio padrão, mínimo e máximo), agrupamentos com `.groupby()` (vendas por gênero, por ano e média por plataforma), ranking dos 10 jogos mais vendidos e filtro por plataforma;
  * gerar os gráficos com Matplotlib e Seaborn.

  O `main.py` contém apenas o menu (`while True` com `try/except` para entradas inválidas) e as chamadas aos métodos da classe.
* **Limpeza de Dados:** A base original possui valores nulos, principalmente nas colunas `Year` (ano de lançamento) e `Publisher`. Na rotina `_limpar()` aplicamos `.dropna()` para remover as linhas incompletas, `.drop_duplicates()` para eliminar repetições e convertemos `Year` de decimal para inteiro. Como o volume removido é pequeno frente ao total, a análise não perde representatividade. A opção 1 do menu mostra quantas linhas existiam antes e depois da limpeza.

## 📊 Gráficos Desenvolvidos

1. **Visão 1 – Gráfico de Linha (opção 8):** mostra a soma das vendas globais de jogos por ano de lançamento. Permite ver a evolução do mercado ao longo do tempo, com o crescimento até o fim dos anos 2000 e a queda posterior. Eixo X: ano; eixo Y: vendas globais (milhões de unidades).
2. **Visão 2 – Gráfico de Barras (opção 9):** compara o total de vendas globais por gênero, em ordem decrescente, o que evidencia quais gêneros (como Action e Sports) dominam o mercado. Eixo X: gênero; eixo Y: vendas globais (milhões de unidades).
3. **Visão 3 – Histograma (opção 10):** exibe a distribuição das vendas globais dos jogos abaixo de 5 milhões de unidades, mostrando que a grande maioria dos títulos vende pouco e poucos viram grandes sucessos. Eixo X: vendas globais; eixo Y: quantidade de jogos.

**Visualizações extras:**
* **Dispersão (opção 11):** relaciona as vendas da América do Norte com as da Europa, indicando se um jogo que vende bem em uma região tende a vender bem na outra.
* **Heatmap (opção 12):** mostra a correlação entre as vendas de cada região e as vendas globais.

## ▶️ Como Executar

1. Baixe o `vgsales.csv` no link do Kaggle acima e salve-o na pasta `data/`.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o sistema: `python main.py`
