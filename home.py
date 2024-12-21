import streamlit as st

# Halaman Utama CV
def main():
    st.title("Curriculum Vitae")

    # Fotogit
    st.image("foto.png", width=150, caption="Foto Saya")  # Ganti 'foto.jpg' dengan file foto Anda

    # Biodata
    st.header("Biodata")
    st.write("""
    **Nama**: Septian Rizqi Arifandi 
    **Tanggal Lahir**: 4 Januari 2002  
    **Alamat**: East Pondok Kacang, South Tangerang City, Banten 
    **Email**: septianhkc@gmail.com  
    **Nomor Telepon**: +62 822-1325-2152  
    """)

    # Pendidikan
    st.header("Pendidikan")
    st.write("""
    - **S1 Teknik Industri** - Universitas Telkom (Under Graduate)  
    - **Madrasah Aliyah Negri 4 Jakarta**  
    """)

    # Pengalaman Organisasi
    st.header("Pengalaman Organisasi")
    st.write("""
    - **Asisten** - Laboratorium Pengembanga Produk   
    - **Asisten** - Penelitian Proyek Dosen 
    - **Anggota** - Field Officer kepanitiaan orientasi kampus
    - **Anggota** - Lembaga Zakat Universitas Telkom
    - **Anggota** - Central Computer Improvemnet
    """)

    # Pengalaman Pelatihan
    st.header("Pengalaman Pelatihan")
    st.write("""
    - Bootcamp Fullstack Data Science - Sanber x ITB  
    - Bootcamp Data Science - Sanbercode
    - Sertifikasi SAP - Universitas Telkom
    """)

    # Skill
    st.header("Skill yang Berhubungan")
    st.write("""
    - Pemrograman: Python, JavaScript, SQL  
    - Analisis Data: Pandas, NumPy, Matplotlib  
    - Framework: Streamlit
    """)

if __name__ == "__main__":
    main()
