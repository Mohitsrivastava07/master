import streamlit as st
import random
import qrcode
from PIL import Image

# Database (temporary – memory based)
if "records" not in st.session_state:
    st.session_state.records = {
        "Name": ["Mohit", "Naitik", "Ayush"],
        "Pass": ["123@", "1234@", "12345@"],
        "acc": [10242, 21457, 45876],
        "bal": [1024.45, 1028.46, 1030.48]
    }

records = st.session_state.records

st.set_page_config(page_title="Bank Management System", layout="centered")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Account Creation",
        "Deposit",
        "Withdraw",
        "Balance Inquiry",
        "Generate QR Code"
    ]
)

# ---------------- ACCOUNT CREATION ----------------
if menu == "Account Creation":
    st.subheader("Create New Account")

    name = st.text_input("Enter Name")
    pin = st.text_input("Enter PIN", type="password")

    if st.button("Create Account"):
        if name and pin:
            if name not in records["Name"]:
                acc = random.randint(10000, 99999)
                records["Name"].append(name)
                records["Pass"].append(pin)
                records["acc"].append(acc)
                records["bal"].append(0.0)

                st.success("Account Created Successfully 🎉")
                st.write("Account Number:", acc)
                st.write("Balance: 0.0")
            else:
                st.error("User already exists!")
        else:
            st.warning("Please fill all fields")

# ---------------- DEPOSIT ----------------
elif menu == "Deposit":
    st.subheader("Deposit Money")

    name = st.text_input("Name")
    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Deposit"):
        if name in records["Name"]:
            i = records["Name"].index(name)
            if records["Pass"][i] == pin and records["acc"][i] == acc:
                records["bal"][i] += amount
                st.success("Amount Deposited ✅")
                st.write("Updated Balance:", records["bal"][i])
            else:
                st.error("Wrong PIN or Account Number")
        else:
            st.error("User not found")

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    name = st.text_input("Name")
    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Withdraw"):
        if name in records["Name"]:
            i = records["Name"].index(name)
            if records["Pass"][i] == pin and records["acc"][i] == acc:
                if amount <= records["bal"][i]:
                    records["bal"][i] -= amount
                    st.success("Withdrawal Successful 💸")
                    st.write("Remaining Balance:", records["bal"][i])
                else:
                    st.error("Insufficient Balance")
            else:
                st.error("Wrong PIN or Account Number")
        else:
            st.error("User not found")

# ---------------- BALANCE ----------------
elif menu == "Balance Inquiry":
    st.subheader("Check Balance")

    name = st.text_input("Name")
    acc = st.number_input("Account Number", step=1)
    pin = st.text_input("PIN", type="password")

    if st.button("Check Balance"):
        if name in records["Name"]:
            i = records["Name"].index(name)
            if records["Pass"][i] == pin and records["acc"][i] == acc:
                st.success(f"Balance: {records['bal'][i]}")
            else:
                st.error("Wrong credentials")
        else:
            st.error("User not found")

# ---------------- QR CODE ----------------
elif menu == "Generate QR Code":
    st.subheader("Generate Account QR Code")

    name = st.text_input("Enter Username")

    if st.button("Generate QR"):
        if name in records["Name"]:
            i = records["Name"].index(name)
            data = f"""
                Name: {records['Name'][i]}
                Account: {records['acc'][i]}
                Balance: {records['bal'][i]}
                """

            qr = qrcode.make(data)
            qr.save("user_qr.png")

            img = Image.open("user_qr.png")
            st.image(img, caption="Account QR Code")
            st.success("QR Code Generated ✅")
        else:
            st.error("User not found")
