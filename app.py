import streamlit as st

from main import (
    extract_invoice_text,
    clean_invoice_text,
    extract_invoice_fields,
    validate_invoice,
    save_invoice_json
)

st.title("AI Invoice Processing System")
st.write("Upload an invoice PDF to extract and validate its details.")

uploaded_file = st.file_uploader("Choose an invoice PDF", type=["pdf"])

if st.button("Process Invoice"):
    if uploaded_file is not None:
        with open("uploaded_invoice.pdf", "wb") as file:
            file.write(uploaded_file.getbuffer())
        text = extract_invoice_text("uploaded_invoice.pdf")
        clean_lines = clean_invoice_text(text)
        invoice_data = extract_invoice_fields(clean_lines)
        validation_result = validate_invoice(invoice_data)
        st.subheader("Validation Results")
        st.json(validation_result)
        st.subheader("Extracted Invoice Details")
        st.json(invoice_data)
    else:
        st.warning("Please upload an invoice PDF first.")


