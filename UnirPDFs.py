#Importamos streamlit

import streamlit as st 

#importamos biblioteca de PDFs
#Félix

import PyPDF2

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