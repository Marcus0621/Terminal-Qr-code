import streamlit as st
import qrcode
from io import BytesIO

# Streamlit UI
st.title("QR Code Generator")
merchant_code = st.text_input("Enter Merchant Code:")
terminal_code = st.text_input("Enter Terminal Code:")

def generate_qr(merchant, terminal):
    timestamp = str(int(st.time()))  # Ensures a fresh request
    qr_url = f"https://svcservice.hywebgt.com:8443/MalaRestful/QrCodeImage/{merchant}/{terminal}?nocache={timestamp}"
    qr = qrcode.make(qr_url)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    return buf

if st.button("Generate QR Code"):
    if merchant_code and terminal_code:
        qr_image = generate_qr(merchant_code, terminal_code)
        st.image(qr_image, caption="Generated QR Code")
        st.write("[Click here to open]({})".format(qr_image))
    else:
        st.warning("Please enter both Merchant and Terminal codes.")

