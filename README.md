# 🧠 Text Analyzer — Program 1

Program ini digunakan untuk menganalisis teks dari file `.txt` dan menampilkan berbagai informasi seperti jumlah kata, kalimat, paragraf, karakter, rata-rata panjang kata, serta 10 kata yang paling sering muncul.  
Selain itu, program ini juga menampilkan **visualisasi data** dalam bentuk grafik batang menggunakan library `matplotlib`.

---

## ✨ Fitur Utama
1. Menghitung total kata, kalimat, paragraf, dan karakter.  
2. Menghitung rata-rata panjang kata.  
3. Menampilkan 10 kata yang paling sering muncul.  
4. Menampilkan grafik batang frekuensi kata (Top 10 words).

---

## ⚙️ Instalasi & Persiapan

Sebelum menjalankan program, pastikan kamu sudah memiliki **Python 3.8+** terpasang.  
Kemudian lakukan langkah-langkah berikut di terminal atau VSCode:

``bash
# 1. Aktifkan virtual environment (jika ada)
.\.venv\Scripts\activate

## CARA MENJALANKAN PROGRAM

# 1. Masuk ke folder tempat file berada
cd text-analyzer

# 2. Jalankan program dengan file teks
python text-analyzer.py artikel.txt
# 2. Instal library yang dibutuhkan
pip install matplotlib python-docx
