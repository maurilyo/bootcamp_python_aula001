import pandas as pd
import os
import glob
from pathlib import Path

# 1. No topo do seu arquivo .py (fora de qualquer função, em MAIÚSCULAS)
OPCOES_EXPORTACAO = {
    "csv": {"index": False},
    "parquet": {"index": False},
    "json": {"orient": "records", "lines": True}
}

# uma funcao de extract que le e consolida no json
def extract_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    """
    Extrai e consolida arquivos JSON em um DataFrame.    
    Args: pasta (str): Caminho para a pasta contendo os arquivos JSON.        
    Returns: pd.DataFrame: DataFrame consolidado com os dados dos arquivos JSON.
    """
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    
    return df_total

# uma função de tranformação
def calcular_kpi_de_total_de_vendas(df_novo: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o KPI de total de vendas e adiciona uma nova coluna ao DataFrame.    
    Args: df_novo (pd.DataFrame): DataFrame contendo os dados de vendas.        
    Returns: pd.DataFrame: DataFrame atualizado com a coluna "Total" calculada.
    """
    df_novo["Total"] = df_novo["Quantidade"] * df_novo["Venda"]
    return df_novo

def carregar_dados_para_csv(df_novo: pd.DataFrame, pasta: str, formato_saida: list) -> None:
    """
    Carrega os dados do DataFrame para um arquivo CSV.    
    Args: df_novo (pd.DataFrame): DataFrame contendo os dados a serem salvos.        
          pasta (str): Caminho para a pasta onde o arquivo CSV será salvo.        
          nome_arquivo (str): Nome do arquivo CSV a ser criado.
    """
    for formato in formato_saida:
        nome_arquivo = "dados_consolidados." + formato
        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        # Pega o método "to_csv" ou "to_parquet" dinamicamente e já o executa
        # equivalente a: df_novo.to_csv(caminho_arquivo, index=False) ou df_novo.to_parquet(caminho_arquivo, index=False)
        # df_novo.to_json(caminho_arquivo, orient='records', lines=True)
        # 3. Executa dinamicamente desempacotando os argumentos com **
        getattr(df_novo, f"to_{formato}")(caminho_arquivo, **OPCOES_EXPORTACAO.get(formato, {}))

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formatos_saida: list) -> None:
    """
    Executa o pipeline completo de extração, transformação e carregamento (ETL) dos dados de vendas.    
    Args: pasta (str): Caminho para a pasta contendo os arquivos JSON.        
          formatos_saida (list): Lista de formatos de saída desejados (ex: ["csv", "parquet", "json"]).
    """
    df_consolidado = extract_dados_e_consolidar(pasta)
    df_calculado = calcular_kpi_de_total_de_vendas(df_consolidado)
    carregar_dados_para_csv(df_calculado, pasta, formatos_saida)



