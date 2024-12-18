import streamlit as st
import json
import os
import bcrypt

# Fungsi untuk memuat data pengguna dari file JSON
def load_users():
    if os.path.exists("users.json"):  # Cek apakah file JSON sudah ada
        with open("users.json", "r") as file:
            return json.load(file)
    else:
        return {}  # Jika file belum ada, kembalikan dictionary kosong

# Fungsi untuk menyimpan data pengguna ke file JSON
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

# Fungsi untuk membuat hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Fungsi untuk memverifikasi password
def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Muat data pengguna saat aplikasi dijalankan
if "users" not in st.session_state:
    st.session_state.users = load_users()

# Tampilan utama
st.title("Login and Sign-Up System")

# Pilihan: Login atau Sign Up
menu = st.radio("Menu", ["Login", "Sign Up"])

# Input untuk username dan password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if menu == "Sign Up":
    st.subheader("Sign Up")
    if st.button("Register"):
        if username in st.session_state.users:
            st.warning("Username sudah terdaftar.")
        elif len(username) == 0 or len(password) == 0:
            st.warning("Username dan password tidak boleh kosong.")
        else:
            # Hash password dan simpan akun baru
            hashed_password = hash_password(password)
            st.session_state.users[username] = hashed_password
            save_users(st.session_state.users)
            st.success("Sign up berhasil! Silakan login.")

elif menu == "Login":
    st.subheader("Login")
    if st.button("Login"):
        if username in st.session_state.users and verify_password(password, st.session_state.users[username]):
            st.success(f"Login berhasil! Selamat datang, {username}.")
        else:
            st.error("Username atau password salah.")

# Debug (Opsional): Tampilkan semua data pengguna (hanya untuk pengembangan)
if st.checkbox("Show Registered Users (Debug)"):
    st.json(st.session_state.users)

