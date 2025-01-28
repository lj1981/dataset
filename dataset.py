import pandas as pd
import random
from datetime import datetime, timedelta

# Configurações gerais do dataset
n_linhas = 1000  # Definindo o número de linhas
ids = list(range(101, 101 + n_linhas))

# Dados possíveis para gerar aleatoriamente com proporções ajustadas
idades = [random.randint(18, 60) for _ in range(n_linhas)]
generos = random.choices(["Feminino", "Masculino"], weights=[60, 40], k=n_linhas)
cidades = random.choices(
    ["Fortaleza", "São Paulo", "Rio de Janeiro", "Salvador", "Belo Horizonte"],
    weights=[20, 30, 25, 15, 10],  # Ajustando proporções de clientes por cidade
    k=n_linhas
)
estados = {
    "Fortaleza": "Ceará",
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Salvador": "Bahia",
    "Belo Horizonte": "Minas Gerais",
}

# Produtos com categorias e pesos para gerar variedade
produtos_variados = {
    "Vestuário": ["Tênis", "Meia", "Camiseta", "Jaqueta", "Calça", "Boné", "Chinelo"],
    "Acessórios": ["Relógio", "Óculos", "Mochila", "Carteira"],
    "Serviços": ["Assinatura", "Transporte"]
}
produtos_pesos = {
    "Vestuário": 50,  # Vestuário é o mais comum
    "Acessórios": 30,
    "Serviços": 20
}

avaliacoes = ["Excelente", "Boa", "Neutra", "Ruim", "Péssimo"]
avaliacoes_pesos = [30, 40, 20, 7, 3]  # Mais clientes avaliam como "Boa" ou "Excelente"
pagamentos = ["Pix", "Crédito", "Débito", "Dinheiro"]
pagamentos_pesos = [40, 30, 20, 10]  # Pix é o mais utilizado

# Gerar nomes fictícios
nomes_masculinos = ["Luiz", "João", "Carlos", "Pedro", "Lucas", "Ricardo", "Fernando", "Mateus", "Henrique", "Tiago"]
nomes_femininos = ["Carla", "Maria", "Ana", "Clara", "Fernanda", "Juliana", "Patrícia", "Bianca", "Camila", "Larissa"]
nomes_clientes = [random.choice(nomes_masculinos) if genero == "Masculino" else random.choice(nomes_femininos) for genero in generos]

# Expandir os dados para ter cada produto e seu respectivo valor em linhas separadas com avaliações e pagamentos diferentes
expanded_data = []
for i in range(n_linhas):
    cliente_id = ids[i]
    nome = nomes_clientes[i]
    idade = idades[i]
    genero = generos[i]
    cidade = cidades[i]
    estado = estados[cidade]

    # Gerar um número aleatório de produtos que o cliente comprou
    num_produtos = random.randint(1, 6)
    categorias_escolhidas = random.choices(
        list(produtos_variados.keys()),
        weights=[produtos_pesos[cat] for cat in produtos_variados.keys()],
        k=num_produtos
    )
    produtos_comprados = [
        random.choice(produtos_variados[categoria]) for categoria in categorias_escolhidas
    ]
    valores = [round(random.uniform(10, 500), 2) for _ in produtos_comprados]  # Valores mais realistas
    data_inicial = datetime(2023, 1, 1)
    datas_compras = [data_inicial + timedelta(days=random.randint(0, 365)) for _ in produtos_comprados]

    avaliacoes_aleatorias = random.choices(avaliacoes, weights=avaliacoes_pesos, k=len(produtos_comprados))
    pagamentos_aleatorios = random.choices(pagamentos, weights=pagamentos_pesos, k=len(produtos_comprados))

    for produto, valor, data_compra, avaliacao, pagamento in zip(
        produtos_comprados, valores, datas_compras, avaliacoes_aleatorias, pagamentos_aleatorios
    ):
        expanded_data.append({
            "Nome": nome,
            "ID": cliente_id,
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
