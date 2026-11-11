# Projeto Final — Analisador de Dados Titanic

Sistema interativo via terminal para leitura, limpeza e análise do dataset **Titanic**. O dataset é uma cópia do conjunto público tradicionalmente distribuído no Kaggle como **Titanic: Machine Learning from Disaster**.

## Estrutura

```text
projeto_final/
├── data/
│   └── titanic.csv
├── src/
│   ├── __init__.py
│   └── analisador.py
├── main.py
├── requirements.txt
└── README.md
```

## Como executar

```bash
cd projeto_final
python3 -m pip install -r requirements.txt
python3 main.py
```

O construtor de `AnalisadorTitanic` lê o CSV com `pandas.read_csv()`, padroniza as colunas categóricas e remove registros nulos das colunas essenciais usando `dropna(subset=...)`, preservando a coluna opcional `Cabin`. A classe concentra médias, estatísticas, `groupby`, filtros e gráficos.

## Opções do menu

- Amostra e estatísticas numéricas;
- Médias de idade, tarifa e familiares;
- Agrupamento por classe do passageiro;
- Filtro de sobreviventes por sexo (aceita Feminino/Masculino ou Female/Male);
- Gráfico de linha da taxa de sobrevivência por classe;
- Gráfico de barras de sobreviventes por sexo;
- Histograma da distribuição de idades.

A entrada do usuário é convertida dentro de `try/except`, evitando que letras ou opções inválidas encerrem o programa inesperadamente.

## Fonte

Dataset público: [Titanic Dataset — Kaggle](https://www.kaggle.com/competitions/titanic/data). O arquivo local em `data/titanic.csv` foi incluído para que o projeto funcione sem download adicional durante a apresentação.
