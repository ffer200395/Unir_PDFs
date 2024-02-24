import PyPDF2
import streamlit as st

def page_pdf():
    output_pdf = "documents/pdf_final.pdf"

    def unir_pdfs(output_path, documents):
        pdf_final = PyPDF2.PdfMerger()

        for document in documents:
            pdf_final.append(document)
            pdf_final.write(output_path)

    st.image("assets/combine-pdf.png")
    st.header("Unir PDF")
    st.subheader("Adjuntar pdfs para unir")
    print(st.session_state['autenticado'])
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

    # Botón de cierre de sesión
    if st.button("Cerrar sesión"):
        #del st.session_state['autenticado']
        #del st.session_state['usuario']
        # Verificar si la clave existe antes de intentar eliminarla
        if 'autenticado' in st.session_state:
            del st.session_state['autenticado']
        if 'usuario' in st.session_state:
            del st.session_state['usuario']
        st.experimental_rerun()