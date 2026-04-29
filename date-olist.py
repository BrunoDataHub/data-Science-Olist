import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Usando uma função para limpar o texto (Padronizando ele em minúsculo)
def limpar_texto(df, coluna):
    df[coluna] = df[coluna].str.strip().str.lower()
    return df
## Usando uma função para remover duplicatas
def remover_duplicata(df, subset_colunas = None):
    # 1. Contar quantas linhas existem antes
    linhas_antes = df.shape[0]
    
    # 2. Aplicar a remoção
    df_limpo = df.drop_duplicates(subset=subset_colunas)
    
    # 3. Contar quantas linhas sobraram
    linhas_depois = df_limpo.shape[0]
    
    # 4. Calcular a diferença
    total_duplicadas = linhas_antes - linhas_depois
    
    # 5. Exibir a mensagem para você no console
    if total_duplicadas > 0:
        print(f"Foram encontradas e removidas {total_duplicadas} duplicatas.")
    else:
        print("Não existem duplicatas nesta base.")
        
    return df_limpo
## usando uma função para converter para datatime
def converter_para_data(df, colunas):
    for coluna in colunas:
        df[coluna] = pd.to_datetime(df[coluna])
    return df



# # ## Importando a base de dados : olist_customers_dataset
# df_customers = pd.read_csv('olist_customers_dataset.csv')

# ## Fazendo uma copia da base original
# df_customers_limpo = df_customers.copy()

# # ## Verificando se existe valores nulos da base:olist_customers_dataset
# # print (df_customers.isnull().sum())

#  ## Removendo espaço e padronizando os textos da base : olist_customers_dataset usando a função Limpar texto
#df_customers_limpo = limpar_texto(df_customers_limpo, 'customer_city')
# print(df_customers_limpo)

# # Removendo duplicatas
# df_customers_limpo = remover_duplicata(df_customers_limpo,['customer_id', 'customer_unique_id', 'customer_zip_code_prefix']  )
# print(df_customers_limpo)








## Importanto a base de dados :olist_geolocation_dataset
# df_geolocation = pd.read_csv('olist_geolocation_dataset.csv')

# ## Criando uma copia da base original
# df_geolocation_limpo = df_geolocation.copy()

# print(df_geolocation_limpo)

# ## Verificando se existe valores nulos da base:olist_geolocation_dataset
# #print (df_geolocation_limpo.isnull().sum())

#  ## Removendo espaço e padronizando os textos da base : olist_geolocation_dataset usando a função Limpar texto
# df_geolocation_limpo = limpar_texto(df_geolocation_limpo, 'geolocation_city')
# print(df_geolocation_limpo)






## Importanto a base de dados :olist_order_items_dataset
df_order_items = pd.read_csv('olist_order_items_dataset.csv')


## Criando uma copia da base original
df_order_items_limpo = df_order_items.copy()

# # ## Verificando se existe valores nulos da base:order_items
#print (df_order_items_limpo.isnull().sum())

# # Removendo duplicatas
#df_order_items_limpo = remover_duplicata(df_order_items_limpo,['order_id', 'product_id', 'seller_id']  )
#print( df_order_items_limpo)

## Convertendo data
#df_order_items_limpo = converter_para_data(df_order_items_limpo,'shipping_limit_date')






# ## Importanto a base de dados :olist_order_payments_dataset
# df_olist_order_payments= pd.read_csv('olist_order_payments_dataset.csv')

# ## Criando uma copia da base original
# df_olist_order_payments_limpo = df_olist_order_payments.copy()

# # # ## Verificando se existe valores nulos da base:order_items
# print (df_olist_order_payments_limpo.isnull().sum())

# #  ## Removendo espaço e padronizando os textos da base : df_olist_order_payments_limpo  usando a função Limpar texto
# df_olist_order_payments_limpo = limpar_texto(df_olist_order_payments_limpo, 'payment_type')
# print(df_olist_order_payments_limpo)

# # # Removendo duplicatas
# df_olist_order_payments_limpo = remover_duplicata(df_olist_order_payments_limpo,'order_id'  )
# print( df_olist_order_payments_limpo)




## Importanto a base de dados :olist_order_reviews_dataset
df_olist_order_reviews = pd.read_csv('olist_order_reviews_dataset.csv')


## Criando uma copia da base original
df_olist_order_reviews_limpo = df_olist_order_reviews.copy()

##Verificando se existe valores nulos na base ; olist_order_reviews_limpo
print (df_olist_order_reviews_limpo.isnull().sum())

## Removendo duplicatas
df_olist_order_reviews_limpo = remover_duplicata(df_olist_order_reviews_limpo,['review_id','order_id'])

## Convertendo data
df_olist_order_reviews_limpo = converter_para_data(df_olist_order_reviews_limpo,['review_creation_date','review_answer_timestamp'])