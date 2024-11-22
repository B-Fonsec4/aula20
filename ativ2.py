import pandas as pd
import numpy as np 
try:
    print('Obtendo dados...')
    ENDERECO_DADOS ='https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    #Encondings: utf-8 iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estel = df_ocorrencias[['mes_ano','estelionato','munic']]
    df_estel = df_estel.groupby(['mes_ano']).sum(['estelionato']).reset_index()
    print(df_estel.head(12))
    print('Dados obtidos com sucesso!')


except Exception as e:
    print(f' ERRO {e}')
    exit()

try:
        # somando o total de estelionatos
    df_total_estelionato = np.array(df_estel['estelionato'])
    # print(df_total_estelionato)
    media_estelionato = np.mean(df_total_estelionato)
    mediana_estelionato = np.median(df_total_estelionato)
    distancia = abs((media_estelionato - mediana_estelionato)/mediana_estelionato)
    # mexendo com quartis
    q1 = np.quantile(df_total_estelionato, 0.25, method='weibull')
    q2 = np.quantile(df_total_estelionato, 0.50, method='weibull')
    q3 = np.quantile(df_total_estelionato, 0.75, method='weibull')
    print('Q1 (25%): ',q1)
    print('Q2 (50%): ',q2)
    print('Q3 (75%): ',q3)
    # filtrando o numero de casos
    df_estel_acima_q3 = df_estel[df_estel['estelionato'] > q3]
    df_estel_abaixo_q1 = df_estel[df_estel['estelionato'] < q1]

    # printando media/mediana
    print(f'essa é a media {media_estelionato:.2f}')
    print(f'essa é a mediana {mediana_estelionato:.2f}')
    print(f'Temos em media {mediana_estelionato:.2f} casos de estelionato no estado.')

    print(df_estel_acima_q3.head(10 ).sort_values(by='estelionato',ascending=False))
    print(df_estel_abaixo_q1.head(10).sort_values(by='estelionato'))
  
except Exception as e:
    print(f' ERRO {e}')
    exit()