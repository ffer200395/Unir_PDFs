import streamlit as st 
#from streamlit_extras.switch_page_button import switch_page
from pages.unir_pdfs import *

# Función de verificación de credenciales
def verificar_credenciales(usuario, password):
    # Cargo la lista de usuarios y contraseñas
    ls_users = st.secrets["USERS"]
    ls_pwd = st.secrets["PWD"]
    # Compruebo si el usuario existe en la bbdd
    if usuario in ls_users:
        idx_user = ls_users.index(usuario)
        valid_pwd = ls_pwd[idx_user]
        return valid_pwd==password
    return False

def login():
    # Título
    st.title("Sistema de XXX con Autenticación")
    # Solicitar usuario y contraseña
    usuario = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    # Botón para iniciar sesión
    if st.button("Iniciar sesión"):
        # Verificación de credenciales
        if verificar_credenciales(usuario, password):
            st.session_state['autenticado'] = True
            st.session_state['usuario'] = usuario
            st.success("Has iniciado sesión correctamente.")
            #switch_page("unir_pdfs")
            #page_pdf()
            return True
        else:
            st.error("Credenciales incorrectas.")

# Interfaz de Streamlit
def main():
    # Verificar si el usuario está autenticado
    if 'autenticado' not in st.session_state or not st.session_state['autenticado']:
        if login():
            page_pdf()
    else:
        # Usuario autenticado
        st.success(f"Bienvenido de nuevo, {st.session_state['usuario']}")

        # Contenido protegido (ejemplo)
        st.markdown("## Aquí va el contenido protegido de la aplicación de facturación")

        # Botón de cierre de sesión
        if st.button("Cerrar sesión"):
            del st.session_state['autenticado']
            del st.session_state['usuario']
            st.experimental_rerun()

if __name__ == "__main__":
    main()