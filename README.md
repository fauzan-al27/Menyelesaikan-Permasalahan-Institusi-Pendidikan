# Menyelesaikan-Permasalahan-Institusi-Pendidikan

## 1. Business Understanding

Jaya Jaya Institut menghadapi permasalahan tingginya angka **dropout siswa** yang berpengaruh pada reputasi dan kinerja institusi. Tujuan dari proyek ini adalah untuk mengidentifikasi faktor-faktor yang berkontribusi terhadap kemungkinan dropout dan membangun sistem prediksi serta dashboard monitoring performa siswa secara berkala.

## 2. Data Understanding

Data yang digunakan merupakan data internal dari Jaya Jaya Institut yang berisi informasi siswa

Link CSV: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

## 3. Data Preparation

- Encoding kategori ke numerik
- Normalisasi fitur numerik
- Membagi data menjadi fitur dan label

## 4. Modeling

Model machine learning yang digunakan adalah **Random Forest Classifier** yang dipilih karena kemampuannya menangani data tabular dengan baik. Model dilatih untuk memprediksi apakah seorang siswa akan Dropout, Enrolled, atau Graduate.

### Hasil Evaluasi Model:
- Akurasi: 76.61%
- Precision / Recall / F1-score untuk tiap kelas
- Confusion Matrix

## 5. Dashboard

Dashboard dibuat menggunakan **Tableau Public** untuk menampilkan data statistik dan performa siswa secara visual.

📊 **Link dashboard Tableau**:
👉 [Dashboard Tableau - Monitoring Siswa](https://public.tableau.com/app/profile/muhammad.fauzan.alkhairi/viz/Dashboard_17478160134210/Dashboard1)

## 6. Rekomendasi Tindak Lanjut

### Rekomendasi Tindak Lanjut:
a. Analisis lebih lanjut pada siswa “Enrolled”:
- Pertimbangkan teknik resampling seperti SMOTE atau undersampling.
- Tinjau kemungkinan adanya label ambiguity pada siswa yang masih aktif (belum dropout/lulus).

b. Penguatan intervensi pada siswa berisiko tinggi:
- Siswa yang berusia lebih tua dan memiliki utang berpotensi tinggi mengalami dropout.
- Intervensi finansial dan dukungan akademik bisa difokuskan pada kelompok ini.
