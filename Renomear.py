#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


lista_de_arquivos = pd.read_excel('Operações suprimento 2020.xls', sheet_name= 'Vendas')


# In[3]:


novo_nome_df = lista_de_arquivos.copy()


# In[4]:


novo_nome_df = novo_nome_df[['Código Boleta', 'Contraparte', 'Cód. BBCE']]


# In[5]:


novo_nome_df['Código Boleta'] = novo_nome_df.iloc[: , 0].astype(str)
novo_nome_df['Cód. BBCE'] = novo_nome_df.iloc[: , 2].fillna(' ')


# In[6]:


novo_nome_df['nome'] = novo_nome_df['Código Boleta'] + '_' + novo_nome_df['Contraparte'] + '_' + novo_nome_df['Cód. BBCE']


# In[7]:


novo_nome_df = novo_nome_df.rename(columns={'Código Boleta': 'boleta', 'Contraparte': 'contraparte', 'Cód. BBCE': 'bbce', 'nome': 'nome'})


# In[ ]:





# In[8]:


cont = -1
operacao = []
for nome in os.listdir('./amostra_de_arquivos'):
    cont = cont + 1
    dados = str(nome).split(".")
    for i in novo_nome_df["bbce"]:
        if i == dados[0]:
            novo_nome = novo_nome_df['nome'].loc[cont]
            novo_nome = novo_nome + ".pdf"
            
            os.rename("./amostra_de_arquivos/"+nome, "./amostra_de_arquivos/"+novo_nome)
            print("arquivo " + nome + " alterado para " + novo_nome)


# In[ ]:



            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




