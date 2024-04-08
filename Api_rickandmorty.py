import requests
import json
import streamlit as st

with st.form('Rick and Morty',clear_on_submit=False):
    IdPersonagem = st.number_input('Digite o id do personagem',step=1,min_value=1)
    try:
        requisicao = requests.get(f'https://rickandmortyapi.com/api/character/{IdPersonagem}')
    except:
        st.write('Personagem não encontrado')
    requisicao = requisicao.json()
    foto = requisicao['image']
    image = st.image(foto)
    nome = requisicao['name']
    status = requisicao['status']
    especie = requisicao['species']
    genero = requisicao['gender']
    locadidade = requisicao['location']['name']
    st.write('Nome:',nome)
    st.write('Status:',status)
    st.write('Especie:',especie)
    st.write('Genero:',genero)
    st.write('Localidade:',locadidade)
    #Monstra todos os dados correspondentes sobre o personagem escolido
    submit_button = st.form_submit_button('Ver personagem')