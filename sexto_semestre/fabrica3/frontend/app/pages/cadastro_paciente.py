import streamlit as st
from controllers.paciente_controller import cadastrar_paciente
from controllers.medo_controller import cadastrar_medo  # Corrigido para app


def cadastro_paciente():
    st.title("Cadastro de Paciente")

    with st.form("cadastro_paciente_form"):
        nome = st.text_input("Nome")
        # selecionar até 100 anos atrás
        # data_nascimento = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
        # StreamlitAPIException: DateInput min should either be a date/datetime or None
        data_nascimento = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        email = st.text_input("E-mail")
        endereco = st.text_area("Endereço")
        observacao = st.text_area("Observações")
        
        # Relacionado ao medo
        st.subheader("Medo Relacionado")
        nome_medo = st.text_input("Nome do Medo")
        grau_medo = st.slider("Grau do Medo", 0, 10)

        submit_button = st.form_submit_button("Cadastrar")

    if submit_button:
        paciente_data = {
            "nome": nome,
            "data_nascimento": str(data_nascimento),
            "cpf": cpf,
            "telefone": telefone,
            "email": email,
            "endereco": endereco,
            "observacao": observacao
        }
        cadastrar_paciente(paciente_data)
        cadastrar_medo(nome_medo, grau_medo)
