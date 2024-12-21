import streamlit as st

# Halaman Utama CV
def main():
    st.title("Curriculum Vitae")

    # Foto
    st.image("foto.png", width=150, caption="Foto Saya")  # Ganti 'foto.jpg' dengan file foto Anda

    # Biodata
    st.header("Biodata")
    st.write("""
    **Nama**: John Doe  
    **Tanggal Lahir**: 1 Januari 1990  
    **Alamat**: Jl. Contoh No. 1, Jakarta  
    **Email**: johndoe@example.com  
    **Nomor Telepon**: +62 812-3456-7890  
    """)

    # Pendidikan
    st.header("Pendidikan")
    st.write("""
    - **S1 Teknik Informatika** - Universitas ABC (2010-2014)  
    - **SMA Negeri 1 Jakarta** (2007-2010)  
    """)

    # Pengalaman Kerja
    st.header("Pengalaman Kerja")
    st.write("""
    - **Software Engineer** - PT Teknologi Maju (2015-2020)  
      Pengembangan aplikasi berbasis web dan mobile.  
    - **Data Analyst** - PT Data Insights (2020-Sekarang)  
      Analisis data menggunakan Python dan SQL.  
    """)

    # Pengalaman Organisasi
    st.header("Pengalaman Organisasi")
    st.write("""
    - **Ketua** - Himpunan Mahasiswa Teknik Informatika (2013-2014)  
    - **Anggota** - Komunitas Data Science Indonesia (2020-Sekarang)  
    """)

    # Pengalaman Pelatihan
    st.header("Pengalaman Pelatihan")
    st.write("""
    - Bootcamp Data Science - XYZ Academy (2019)  
    - Pelatihan Machine Learning - ABC Institute (2021)  
    """)

    # Skill
    st.header("Skill yang Berhubungan")
    st.write("""
    - Pemrograman: Python, JavaScript, SQL  
    - Analisis Data: Pandas, NumPy, Matplotlib  
    - Framework: Streamlit, Flask, Django  
    """)

if __name__ == "__main__":
    main()
