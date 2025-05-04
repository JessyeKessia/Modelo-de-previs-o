import csv

# Dados de exemplo para o CSV
dados = [
    ["Data", "Temperatura (°C)", "Vendas (unidades)"],
    ["2025-04-01", 28, 150],
    ["2025-04-02", 30, 160],
    ["2025-04-03", 25, 120],
    ["2025-04-04", 35, 180],
    ["2025-04-05", 32, 175],
    ["2025-04-06", 27, 130],
    ["2025-04-07", 33, 170],
    ["2025-04-08", 26, 110],
    ["2025-04-09", 31, 165],
    ["2025-04-10", 29, 155],
]

# Caminho para salvar o CSV
caminho_csv = "data/sorvete_temperatura_vendas.csv"

# Criar o CSV
with open(caminho_csv, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

caminho_csv
