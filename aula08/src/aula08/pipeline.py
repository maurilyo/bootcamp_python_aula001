from pathlib import Path
from etl import pipeline_calcular_kpi_de_vendas_consolidado

BASE_DIR = Path(__file__).resolve().parents[2]
path_arquivo = BASE_DIR / "data"

formatos_saida = ["csv","json"]

pipeline_calcular_kpi_de_vendas_consolidado(path_arquivo, formatos_saida)