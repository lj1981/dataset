# Guia Detalhado para o Código de Geração de Dataset

Este guia documenta o funcionamento do código para gerar um dataset sintético. O objetivo é facilitar a compreensão e o uso do código por outras pessoas. Ao final, o arquivo gerado será salvo como um CSV, contendo informações detalhadas sobre clientes fictícios e suas compras.

## Descrição Geral do Código

O código gera dados fictícios de clientes, incluindo informações como nome, idade, gênero, cidade, estado, produtos comprados, valor das compras, data das compras, avaliações, e método de pagamento. Esses dados são organizados e salvos em um arquivo CSV.

---

## Estrutura do Código

1. **Importação de Bibliotecas Necessárias**

   ```python
   import pandas as pd
   import random
   from datetime import datetime, timedelta
   ```

   - `pandas`: Usado para manipulação e armazenamento dos dados.
   - `random`: Para geração de valores aleatórios.
   - `datetime` e `timedelta`: Para manipulação de datas.

2. **Configuração Inicial do Dataset**

   - Define o número de registros (linhas) do dataset e cria IDs únicos para cada cliente.
     ```python
     n_linhas = 1000  # Definindo o número de linhas
     ids = list(range(101, 101 + n_linhas))
     ```

3. **Geração de Dados Aleatórios**

   - Idades, gêneros, cidades e estados são gerados com distribuição controlada por pesos.
     ```python
     idades = [random.randint(18, 60) for _ in range(n_linhas)]
     generos = random.choices(["Feminino", "Masculino"], weights=[60, 40], k=n_linhas)
     cidades = random.choices(
         ["Fortaleza", "São Paulo", "Rio de Janeiro", "Salvador", "Belo Horizonte"],
         weights=[20, 30, 25, 15, 10],
         k=n_linhas
     )
     estados = {
         "Fortaleza": "Ceará",
         "São Paulo": "São Paulo",
         "Rio de Janeiro": "Rio de Janeiro",
         "Salvador": "Bahia",
         "Belo Horizonte": "Minas Gerais",
     }
     ```

4. **Geração de Nomes**

   - Nomes são escolhidos aleatoriamente com base no gênero do cliente.
     ```python
     nomes_masculinos = ["Luiz", "João", "Carlos", "Pedro", "Lucas", "Ricardo", "Fernando", "Mateus", "Henrique", "Tiago"]
     nomes_femininos = ["Carla", "Maria", "Ana", "Clara", "Fernanda", "Juliana", "Patrícia", "Bianca", "Camila", "Larissa"]
     nomes_clientes = [
         random.choice(nomes_masculinos) if genero == "Masculino" else random.choice(nomes_femininos)
         for genero in generos
     ]
     ```

5. **Expansão dos Dados para Produtos e Compras**

   - Cada cliente pode comprar de 1 a 6 produtos, escolhidos aleatoriamente.
   - Cada produto tem um valor aleatório, uma data de compra, uma avaliação e um método de pagamento.
     ```python
     produtos_variados = {
         "Vestuário": ["Tênis", "Meia", "Camiseta", "Jaqueta", "Calça", "Boné", "Chinelo"],
         "Acessórios": ["Relógio", "Óculos", "Mochila", "Carteira"],
         "Serviços": ["Assinatura", "Transporte"]
     }
     produtos_pesos = {"Vestuário": 50, "Acessórios": 30, "Serviços": 20}

     avaliacoes = ["Excelente", "Boa", "Neutra", "Ruim", "Péssimo"]
     avaliacoes_pesos = [30, 40, 20, 7, 3]
     pagamentos = ["Pix", "Crédito", "Débito", "Dinheiro"]
     pagamentos_pesos = [40, 30, 20, 10]
     ```
     - Expansão dos dados:
       ```python
       for i in range(n_linhas):
           cliente_id = ids[i]
           nome = nomes_clientes[i]
           idade = idades[i]
           genero = generos[i]
           cidade = cidades[i]
           estado = estados[cidade]

           num_produtos = random.randint(1, 6)
           categorias_escolhidas = random.choices(
               list(produtos_variados.keys()),
               weights=[produtos_pesos[cat] for cat in produtos_variados.keys()],
               k=num_produtos
           )
           produtos_comprados = [
               random.choice(produtos_variados[categoria]) for categoria in categorias_escolhidas
           ]
           valores = [round(random.uniform(10, 500), 2) for _ in produtos_comprados]
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
                   "Gêmera": genero,
                   "Cidade": cidade,
                   "Estado": estado,
                   "Produto": produto,
                   "Valor": f"R${valor:.2f}",
                   "Data_Compra": data_compra.strftime("%Y-%m-%d"),
                   "Avaliacao": avaliacao,
                   "Pagamento": pagamento
               })
       ```

6. **Criação do DataFrame**

   - O DataFrame é criado a partir dos dados expandidos.
     ```python
     df_expanded = pd.DataFrame(expanded_data)
     ```

7. **Salvamento do Dataset**

   - O dataset é salvo como um arquivo CSV em um caminho especificado.
     ```python
     file_path = "/home/luiz/Downloads/Projetos One/Analise de comportamento/dataset_clientes_final.csv"
     df_expanded.to_csv(file_path, index=False, encoding="utf-8")
     print(f"Arquivo CSV salvo em: {file_path}")
     ```

---

## Como Utilizar o Código

1. Instale as dependências necessárias:

   ```bash
   pip install pandas
   ```

2. Execute o script em um ambiente Python (como Jupyter Notebook ou diretamente pelo terminal).

3. Certifique-se de que o caminho para salvar o arquivo (`file_path`) seja válido no seu sistema.

4. Após a execução, o arquivo CSV contendo o dataset estará disponível no diretório especificado.

---

## Sugestões de Uso

- O dataset gerado pode ser usado para análise de comportamento de compra, teste de algoritmos de machine learning, ou outros estudos.
- Você pode ajustar os parâmetros, como o número de linhas, produtos ou pesos, para personalizar o dataset conforme suas necessidades.

---

## Possíveis Melhorias

- Adicionar mais produtos ou categorias.
- Tornar os nomes e dados demográficos mais realistas.
- Permitir a entrada de parâmetros pelo usuário, como o número de registros e o período de datas.




