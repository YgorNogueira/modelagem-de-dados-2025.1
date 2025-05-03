"""
    https://colab.research.google.com/drive/1yAykkCQC3jn1DKjIQttBc7GomJlUTptB
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

import pandas as pd

# Carregar o arquivo CSV enviado
file_path = "/mnt/data/database-clean.csv"
df_raw = pd.read_csv(file_path, sep=";", encoding="utf-8", low_memory=False)

# Exibir as primeiras linhas e colunas do dataframe
df_raw.head(), df_raw.columns.tolist()

from google.colab import files
uploaded = files.upload()

# Remover duplicatas antes de separar os dataframes
df_raw.drop_duplicates(inplace=True)

# Tabela: Pacientes
df_pacientes = df_raw[[
    'NU_NOTIFIC', 'DT_NASC', 'NU_IDADE_N', 'CS_SEXO',
    'CS_GESTANT', 'CS_RACA', 'CS_ESCOL_N'
]].copy()

# Tabela: Notificações
df_notificacoes = df_raw[[
    'NU_NOTIFIC', 'TP_NOT', 'ID_AGRAVO', 'DT_NOTIFIC', 'SEM_NOT', 'NU_ANO',
    'SG_UF_NOT', 'ID_MUNICIP', 'ID_REGIONA', 'ID_UNIDADE', 'DT_SIN_PRI', 'SEM_PRI'
]].copy()

# Tabela: Sinais e Sintomas
sintomas_cols = [
    'NU_NOTIFIC', 'FEBRE', 'MIALGIA', 'CEFALEIA', 'EXANTEMA', 'VOMITO', 'NAUSEA',
    'DOR_COSTAS', 'CONJUNTVIT', 'ARTRITE', 'ARTRALGIA', 'PETEQUIA_N',
    'LEUCOPENIA', 'LACO', 'DOR_RETRO'
]
df_sintomas = df_raw[sintomas_cols].copy()

# Tabela: Doenças Pré-existentes
doencas_cols = [
    'NU_NOTIFIC', 'DIABETES', 'HEMATOLOG', 'HEPATOPAT', 'RENAL', 'HIPERTENSA',
    'ACIDO_PEPT', 'AUTO_IMUNE'
]
df_doencas = df_raw[doencas_cols].copy()

# Tabela: Resultados de Exames
exames_cols = [
    'NU_NOTIFIC', 'DT_CHIK_S1', 'DT_CHIK_S2', 'DT_PRNT', 'RES_CHIKS1',
    'RES_CHIKS2', 'RESUL_PRNT', 'DT_SORO', 'RESUL_SORO', 'DT_NS1', 'RESUL_NS1',
    'DT_VIRAL', 'RESUL_VI_N', 'DT_PCR', 'RESUL_PCR_', 'SOROTIPO'
]
df_exames = df_raw[exames_cols].copy()

# Tabela: Hospitalização
df_hospitalizacao = df_raw[[
    'NU_NOTIFIC', 'HOSPITALIZ', 'DT_INTERNA', 'UF', 'MUNICIPIO', 'HOSPITAL',
    'DDD_HOSP', 'TEL_HOSP'
]].copy()

# Tabela: Evolução do Caso
df_evolucao = df_raw[[
    'NU_NOTIFIC', 'CLASSI_FIN', 'CRITERIO', 'DOENCA_TRA', 'CLINC_CHIK', 'EVOLUCAO',
    'DT_OBITO', 'DT_ENCERRA'
]].copy()

# Tabela: Alertas e Gravidade
alerta_cols = ['NU_NOTIFIC'] + [col for col in df_raw.columns if col.startswith('ALRM_') or col.startswith('GRAV_')] + ['DT_ALRM', 'DT_GRAV']
df_alertas = df_raw[alerta_cols].copy()

# Tabela: Local de Infecção
df_infeccao = df_raw[[
    'NU_NOTIFIC', 'TPAUTOCTO', 'COUFINF', 'COPAISINF', 'COMUNINF', 'CODISINF',
    'CO_BAINF', 'NOBAIINF'
]].copy()

# Tabela: Endereço
df_endereco = df_raw[[
    'NU_NOTIFIC', 'SG_UF', 'ID_MN_RESI', 'ID_RG_RESI', 'ID_DISTRIT', 'ID_BAIRRO',
    'NM_BAIRRO', 'ID_LOGRADO', 'NM_LOGRADO', 'NU_CEP', 'CS_ZONA', 'ID_PAIS'
]].copy()

# Confirmar criação
df_pacientes.head(2), df_notificacoes.head(2), df_sintomas.head(2)

save_path = "/mnt/data/"  # No Colab, salva na aba lateral "Files"

# Salvar cada tabela como CSV
df_pacientes.to_csv(save_path + "pacientes.csv", index=False)
df_notificacoes.to_csv(save_path + "notificacoes.csv", index=False)
df_sintomas.to_csv(save_path + "sintomas.csv", index=False)
df_doencas.to_csv(save_path + "doencas.csv", index=False)
df_exames.to_csv(save_path + "exames.csv", index=False)
df_hospitalizacao.to_csv(save_path + "hospitalizacao.csv", index=False)
df_evolucao.to_csv(save_path + "evolucao.csv", index=False)
df_alertas.to_csv(save_path + "alertas.csv", index=False)
df_infeccao.to_csv(save_path + "infeccao.csv", index=False)
df_endereco.to_csv(save_path + "endereco.csv", index=False)

!pip install ydata-profiling
from google.colab import files
import pandas as pd
from ydata_profiling import ProfileReport

uploaded = files.upload()
df = pd.read_csv('pacientes.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('pacientes.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('endereco.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('infeccao.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('alertas_gravidade.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('evolucao.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('hospitalizado.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('resultado_exames.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('sintomas.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

uploaded = files.upload()
df = pd.read_csv('notificacoes.csv')

# Cria o relatório
profile = ProfileReport(df, title="Profiling Report")

# Exibe no notebook
profile.to_notebook_iframe()

