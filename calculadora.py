import streamlit as st
#projeto calculadora

with  st.form('Programadores') as form:
    st.title('Calculadora')

    with st.sidebar:
        '''
        configurações
        '''
        seletor = st.selectbox('Calculadora',['Soma','Subtração','Multiplicação','Divisão'],placeholder='Selecione uma opção',index=None)

    numero1 = st.number_input('Numero1',step=1)
    numero2 = st.number_input('Numero2',step=1)

    if seletor == 'Soma':
        st.write(f'O resultado e igual a {numero1+numero2}')
    elif seletor == 'Subtração':
        st.write(f'O resultado e igual a {numero1-numero2}')
    
    elif seletor == 'Multiplicação':
        st.write(f'O resultado e igual a {numero1*numero2}')
    
    elif seletor == 'Divisão':
        st.write(f'O resultado e igual a {numero1/numero2}')
    

    
    #index=none inicializa a caixa com nada
    st.write('Opção selecionada:',seletor)
    
    submit_button = st.form_submit_button('Calcular')
