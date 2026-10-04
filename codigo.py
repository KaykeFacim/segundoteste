#titulo do site
#seção cadastras vendas 
    #campo data
    #campo vendedor - Ana, Bruno, Carla,
    #produto - notbook, fone, celular
    #campo quantidade
    #campo valor
    #campo cadastrar vendas
        #quando eu clicar o botao -> adiciona a venda na tela
#seção de vendas cadastradas
    #tabela com as vendas
#seção com dashbord
    #card/metrica -> faturamento total
    #gafico de barra/coluna -> venda por vendedor
    #grafico de pizza -> vendas por produto

#utilizaremos pandas, streamlit e plotly

#dica: primeiro colocar a carcaça do site, ou seja, graficos, titulos etc, mesmo q n funcionem
#aos poucos tu vai adicionando as funcionalidades e deixando o site inteligente

#codigo para rodas o streamlit: 
#python -m streamlit run codigo.py



import streamlit as st
#stremlit pode ser utilizado para rodar automações, por exemplo, colocando o codigo da primeira aula em um botao do streamlit, pode rodar o codigo todo so clicando ele
#o q é uma mao na roda, posso criar um  monte de coisa, deixar rodando e so ativar o que precisar quando precisar


import pandas as pd
import plotly.express as px    #lembrar d trazer assim pq ele ja traz prontos os graficos 

tabela_vendas = pd.read_csv("vendas.csv")

#sempre que for escrever na tela: ]
st.write("# Sistema de vendas")



#esse sidebar faz as coisas aparecerem na lateral da tela, independente do tamanho, 
#sempre colocar logo dps do "st" e antes do q a função deve fazer
st.sidebar.write("## Cadastrar vendas") 
data = st.sidebar.date_input("data") #seleciona a data
vendedor = st.sidebar.selectbox("vendedor", ["Ana", "Bruno", "Carla"]) #lista de vendedores
produto = st.sidebar.selectbox("produto", ["Notebook", "Celular", "Fone"]) #lista de produtos
quantidade = st.sidebar.number_input("quantidade", step=1) #entra numero,
valor = st.sidebar.number_input("valor") #entra numero
botao_cadastrar = st.sidebar.button("cadastrar vendas") #botao para enviar



#logica de cadastro 
if botao_cadastrar:     

    #aqui nessa parte poderia criar condições com laços para garantir q ta td preenhido certin, q nem o do guanabara
    #tambem nessa parte poderia deixar os campos obrigatorios com condições tabem,
    #teria de usar o comando st.warning("mensagem aqui") para mostrar na tela em vermelho e destacado
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    #o pandas le a td como texto, por isso deixar a data como texto tbm
    st.sidebar.success("Venda Cadastrada")
    tabela_vendas.to_csv("vendas.csv", index=False)
st.write("## Vendas cadastradas")
#oq é um dataframe? tabela do pandas, só uma tabela
st.dataframe(tabela_vendas) #mostra uma tabela, e ja vem cm funcionalidades para filtar etc


st.write("## Dashbord")
#card 
faturamento = tabela_vendas["valor"].sum() 
#para tirar so a coluna valor da tabela, e o sum() soma td, 
st.metric("faturamento total",f"R$: {faturamento}")
#monta o cardzinho da metrica la, onde mostra o faturamento total

#grafico de barras
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1) #esse codigo joga o codigdo no site q ta rodando

#grafico de pizza (Torta)
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2) #esse codigo injeta no site o nosso grafico