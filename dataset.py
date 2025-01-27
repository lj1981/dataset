import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações gerais do dataset
n_linhas = 400  # Definindo o número de linhas
ids = list(range(101, 101 + n_linhas))

# Dados possíveis para gerar aleatoriamente
idades = [random.randint(18, 60) for _ in range(n_linhas)]
generos = [random.choice(["Masculino", "Feminino"]) for _ in range(n_linhas)]
cidades = [random.choice(["Fortaleza", "São Paulo", "Rio de Janeiro", "Salvador", "Belo Horizonte"]) for _ in
           range(n_linhas)]
estados = {
    "Fortaleza": "Ceará",
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Salvador": "Bahia",
    "Belo Horizonte": "Minas Gerais",
}
produtos_variados = [
    "Tênis", "Meia", "Camiseta", "Assinatura", "Transporte", "Jaqueta",
    "Relógio", "Calça", "Boné", "Chinelo", "Óculos", "Mochila", "Carteira"
]
avaliacoes = ["Excelente", "Boa", "Neutra", "Ruim", "Péssimo"]
pagamentos = ["Pix", "Crédito", "Débito", "Dinheiro"]

# Expandir os dados para ter cada produto e seu respectivo valor em linhas separadas com avaliações e pagamentos diferentes
expanded_data = []
for i in range(n_linhas):
    cliente_id = ids[i]
    idade = idades[i]
    genero = generos[i]
    cidade = cidades[i]
    estado = estados[cidade]

    # Gerar um número aleatório de produtos que o cliente comprou, mas não maior que a quantidade de produtos disponíveis
    num_produtos = random.randint(1, min(6,
                                         len(produtos_variados)))  # O máximo de produtos será 6 ou o número total de produtos

    # Gerar os produtos e valores conforme o número aleatório de produtos
    produtos_comprados = random.sample(produtos_variados, num_produtos)
    valores = [round(random.uniform(5, 200), 2) for _ in produtos_comprados]
    data_inicial = datetime(2023, 1, 1)  # Data inicial para compras
    datas_compras = [data_inicial + timedelta(days=random.randint(0, 365)) for _ in produtos_comprados]

    # Garantir que o número de avaliações aleatórias não seja maior que a quantidade disponível
    avaliacoes_aleatorias = random.sample(avaliacoes, min(len(produtos_comprados), len(avaliacoes)))

    pagamentos_aleatorios = random.choices(pagamentos, k=len(produtos_comprados))

    for produto, valor, data_compra, avaliacao, pagamento in zip(
            produtos_comprados, valores, datas_compras, avaliacoes_aleatorias, pagamentos_aleatorios
    ):
        expanded_data.append({
            "ID_Cliente": cliente_id,
            "Idade": idade,
            "Gênero": genero,
            "Cidade": cidade,
            "Estado": estado,
            "Produto": produto,
            "Valor": f"R${valor:.2f}",
            "Data_Compra": data_compra.strftime("%Y-%m-%d"),
            "Avaliacao": avaliacao,
            "Pagamento": pagamento
        })

# Criar um novo DataFrame com os dados atualizados
df_expanded = pd.DataFrame(expanded_data)

# Definir o caminho do arquivo onde você deseja salvar
file_path = "/home/luiz/Downloads/Projetos One/Analise de comportamento/dataset_clientes_final.csv"

# Salvar o DataFrame em um arquivo CSV no diretório específico
df_expanded.to_csv(file_path, index=False, encoding="utf-8")

print(f"Arquivo CSV salvo em: {file_path}")
