# Importando a biblioteca pandas
import pandas as pd

def processdata():    # Carregando o arquivo .csv
   df = pd.read_csv('chipotle_stores.csv', delimiter = ',')    # Convertendo o conteúdo do arquivo em uma lsita
   df = df.to_dict(orient = 'records')
   print(df) # Exibindo a lista criada
   return df
