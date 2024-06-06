import pandas as pd
import json

# Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
arquivo_excel = 'dados.xlsx'

# Lê o arquivo Excel
df = pd.read_excel(arquivo_excel)

# Seleciona a primeira coluna
primeira_coluna = df.iloc[:, 0]

# Lista para armazenar os dados processados
dados_processados = []

# Processa cada linha da primeira coluna
for item in primeira_coluna:
    if isinstance(item, str):  # Verifica se o item é uma string
        try:
            # Converte a string JSON em um dicionário
            json_data = json.loads(item)
            # Adiciona o dicionário à lista de dados processados
            dados_processados.append(json_data)
        except json.JSONDecodeError:
            print(f"Erro ao decodificar JSON: {item}")
    else:
        print(f"Ignorando valor não string: {item}")

# Converte a lista de dicionários em um DataFrame do pandas
df_processado = pd.json_normalize(dados_processados)

# Verifica se a coluna 'Indicators' existe no DataFrame processado
if 'Indicators' in df_processado.columns:
    # Lista para armazenar os dados processados da coluna 'Indicators'
    indicators_processados = []

    # Processa cada linha da coluna 'Indicators'
    for item in df_processado['Indicators']:
        if isinstance(item, str):  # Verifica se o item é uma string
            try:
                # Converte a string JSON em um dicionário
                json_data = json.loads(item)
                # Adiciona o dicionário à lista de dados processados
                indicators_processados.append(json_data)
            except json.JSONDecodeError:
                print(f"Erro ao decodificar JSON: {item}")
                indicators_processados.append({})
        else:
            print(f"Ignorando valor não string: {item}")
            indicators_processados.append({})

    # Converte a lista de dicionários em um DataFrame do pandas
    df_indicators = pd.json_normalize(indicators_processados)

    # Concatena o DataFrame original com o DataFrame processado da coluna 'Indicators'
    df_final = pd.concat([df_processado.drop(columns=['Indicators']), df_indicators], axis=1)
else:
    df_final = df_processado

# Imprime todas as colunas do DataFrame final
print("Colunas do DataFrame final:")
print(df_final.columns)

# Salva o DataFrame final em um novo arquivo Excel
novo_arquivo_excel = 'tes.xlsx'
df_final.to_excel(novo_arquivo_excel, index=False)