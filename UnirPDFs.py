import streamlit as st 
import PyPDF2

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

# Interfaz de Streamlit
def main():
    # Título
    st.title("Sistema de XXX con Autenticación")

    # Verificar si el usuario está autenticado
    if 'autenticado' not in st.session_state or not st.session_state['autenticado']:
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
            else:
                st.error("Credenciales incorrectas.")
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
"""
output_pdf = "documents/pdf_final.pdf"

def unir_pdfs(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)
        pdf_final.write(output_path)

st.image("assets/combine-pdf.png")
st.header("Unir PDF")
st.subheader("Adjuntar pdfs para unir")

pdf_adjuntos = st.file_uploader(label="", accept_multiple_files=True)

unir = st.button(label= "Unir PDFs")

if unir:
    if len(pdf_adjuntos) <= 1:
        st.warning("Debes adjuntar más de un PDF")
    else:
        unir_pdfs(output_pdf, pdf_adjuntos)
        st.success("Desde aquí puede descargar el PDF final")
        with open(output_pdf, 'rb') as file:
            pdf_data=  file.read()
        st.download_button(label="Descargar PDF final", data=pdf_data, file_name="pdf_final.pdf")
"""