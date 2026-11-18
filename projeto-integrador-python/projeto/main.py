"""Ponto de entrada: apenas menu interativo e chamadas à classe."""
from src.analisador import AnalisadorVendas

MENU = """
===== ANALISADOR DE VENDAS DE VIDEO GAMES =====
 1 - Resumo da limpeza dos dados
 2 - Primeiras linhas da base
 3 - Estatísticas das vendas globais
 4 - Vendas por gênero (groupby)
 5 - Média de vendas por plataforma (groupby)
 6 - Top 10 jogos mais vendidos
 7 - Filtrar jogos por plataforma
 8 - Gráfico de LINHA: vendas por ano
 9 - Gráfico de BARRAS: vendas por gênero
10 - HISTOGRAMA: distribuição das vendas
11 - DISPERSÃO: América do Norte x Europa
12 - HEATMAP: correlação entre regiões
 0 - Sair
"""


def main():
    try:
        analisador = AnalisadorVendas("data/vgsales.csv")
    except FileNotFoundError:
        print("Arquivo data/vgsales.csv não encontrado. Baixe-o no Kaggle e salve na pasta data/.")
        return

    while True:
        print(MENU)
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite apenas o número da opção.")
            continue

        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break
        elif opcao == 1:
            print(analisador.info_limpeza())
        elif opcao == 2:
            print(analisador.visao_geral())
        elif opcao == 3:
            print(analisador.estatisticas_globais())
        elif opcao == 4:
            print(analisador.vendas_por_genero())
        elif opcao == 5:
            print(analisador.media_por_plataforma())
        elif opcao == 6:
            print(analisador.top_jogos())
        elif opcao == 7:
            print("Plataformas:", ", ".join(analisador.plataformas_disponiveis()))
            plataforma = input("Digite a plataforma: ").strip()
            resultado = analisador.filtrar_por_plataforma(plataforma)
            print(resultado.head(20) if not resultado.empty else "Nenhum jogo encontrado.")
        elif opcao == 8:
            analisador.grafico_linha_vendas_ano()
        elif opcao == 9:
            analisador.grafico_barras_genero()
        elif opcao == 10:
            analisador.grafico_histograma_vendas()
        elif opcao == 11:
            analisador.grafico_dispersao_regioes()
        elif opcao == 12:
            analisador.grafico_heatmap_correlacao()
        else:
            print("Opção inexistente. Escolha um número do menu.")


if __name__ == "__main__":
    main()
