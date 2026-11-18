"""Núcleo do sistema: leitura, limpeza, processamento e gráficos."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorVendas:
    """Encapsula toda a inteligência sobre a base Video Game Sales."""

    COLUNAS_VENDAS = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

    def __init__(self, caminho_csv="data/vgsales.csv"):
        self.df = pd.read_csv(caminho_csv)
        self.linhas_originais = len(self.df)
        self._limpar()
        sns.set_theme(style="whitegrid")

    # ---------- Limpeza ----------
    def _limpar(self):
        """Remove nulos e duplicatas e corrige tipos."""
        self.df = self.df.dropna().drop_duplicates()
        self.df["Year"] = self.df["Year"].astype(int)
        self.df = self.df.reset_index(drop=True)

    def info_limpeza(self):
        removidas = self.linhas_originais - len(self.df)
        return (f"Linhas originais: {self.linhas_originais} | "
                f"Após limpeza: {len(self.df)} | Removidas: {removidas}")

    # ---------- Processamento ----------
    def visao_geral(self):
        return self.df.head(10)

    def estatisticas_globais(self):
        return self.df["Global_Sales"].agg(["mean", "median", "std", "min", "max"]).round(3)

    def vendas_por_genero(self):
        return (self.df.groupby("Genre")["Global_Sales"].sum()
                .sort_values(ascending=False).round(2))

    def vendas_por_ano(self):
        return self.df.groupby("Year")["Global_Sales"].sum().round(2)

    def media_por_plataforma(self):
        return (self.df.groupby("Platform")["Global_Sales"].mean()
                .sort_values(ascending=False).round(3))

    def top_jogos(self, n=10):
        return self.df.nlargest(n, "Global_Sales")[["Name", "Platform", "Year", "Genre", "Global_Sales"]]

    def filtrar_por_plataforma(self, plataforma):
        filtro = self.df[self.df["Platform"].str.upper() == plataforma.upper()]
        return filtro[["Name", "Year", "Genre", "Global_Sales"]]

    def plataformas_disponiveis(self):
        return sorted(self.df["Platform"].unique())

    # ---------- Gráficos ----------
    def grafico_linha_vendas_ano(self):
        dados = self.vendas_por_ano()
        plt.figure(figsize=(10, 5))
        plt.plot(dados.index, dados.values, marker="o", color="teal")
        plt.title("Vendas Globais de Games por Ano de Lançamento")
        plt.xlabel("Ano")
        plt.ylabel("Vendas Globais (milhões de unidades)")
        plt.tight_layout()
        plt.show()

    def grafico_barras_genero(self):
        dados = self.vendas_por_genero()
        plt.figure(figsize=(10, 5))
        sns.barplot(x=dados.index, y=dados.values, hue=dados.index, palette="viridis", legend=False)
        plt.title("Vendas Globais por Gênero")
        plt.xlabel("Gênero")
        plt.ylabel("Vendas Globais (milhões de unidades)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def grafico_histograma_vendas(self):
        plt.figure(figsize=(10, 5))
        sns.histplot(self.df[self.df["Global_Sales"] < 5]["Global_Sales"], bins=40, color="coral")
        plt.title("Distribuição das Vendas Globais (jogos abaixo de 5 mi)")
        plt.xlabel("Vendas Globais (milhões de unidades)")
        plt.ylabel("Quantidade de Jogos")
        plt.tight_layout()
        plt.show()

    def grafico_dispersao_regioes(self):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=self.df, x="NA_Sales", y="EU_Sales", alpha=0.5)
        plt.title("Vendas na América do Norte vs Europa")
        plt.xlabel("Vendas América do Norte (milhões)")
        plt.ylabel("Vendas Europa (milhões)")
        plt.tight_layout()
        plt.show()

    def grafico_heatmap_correlacao(self):
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.df[self.COLUNAS_VENDAS].corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlação entre Vendas por Região")
        plt.xlabel("Região")
        plt.ylabel("Região")
        plt.tight_layout()
        plt.show()
