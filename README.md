# Menyelesaikan-Permasalahan-Institusi-Pendidikan

## 1. Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang tengah menghadapi tantangan serius terkait tingginya tingkat dropout (putus studi) mahasiswa. Hal ini berdampak langsung pada reputasi, kinerja institusi, dan kepercayaan masyarakat terhadap kualitas akademik yang ditawarkan. Oleh karena itu, diperlukan sebuah sistem yang mampu memprediksi potensi dropout sejak dini dan memberikan dasar bagi pengambilan keputusan yang lebih tepat sasaran.

## 2. Permasalahan Bisnis
Permasalahan utama yang dihadapi institusi adalah:

- Tingginya tingkat mahasiswa yang keluar (dropout).
- Kurangnya sistem monitoring performa siswa yang dapat memberikan peringatan dini.
- Sulitnya mengidentifikasi siswa yang berisiko tinggi untuk diberi intervensi lebih awal.

## 3. Cakupan Proyek
- Menganalisis data siswa untuk memahami faktor-faktor yang memengaruhi status dropout.
- Mengembangkan model machine learning untuk memprediksi status siswa (Dropout, Enrolled, atau Graduate).
- Membuat dashboard interaktif yang dapat digunakan manajemen untuk memantau performa siswa secara visual dan informatif.

## 4. Persiapan

### Sumber Data:

Data yang digunakan merupakan data internal dari Jaya Jaya Institut yang berisi informasi siswa
Link CSV: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv

### Langkah Persiapan Data:

- Label Encoding untuk kolom target Status.
- One-hot encoding untuk variabel kategorikal lainnya.
- Normalisasi fitur numerik menggunakan MinMaxScaler.
- Split data menjadi training dan testing set dengan proporsi 80:20.

## 5. Modeling
Model yang digunakan adalah Random Forest Classifier, karena:
- Mampu menangani fitur kategorikal dan numerik secara bersamaan.
- Robust terhadap overfitting dan memberikan feature importance.

### Hasil Evaluasi:
- Akurasi: 76.61%
- Performa berdasarkan precision, recall, dan F1-score untuk tiap kelas (Dropout, Enrolled, Graduate).
- Confusion Matrix menunjukkan distribusi prediksi dan kesalahan.

### Model Deployment
https://menyelesaikan-permasalahan-institusi-pendidikan-qesnurj28m8d7u.streamlit.app/

## 6. Dashboard

Dashboard dibuat menggunakan **Tableau Public** untuk menampilkan data statistik dan performa siswa secara visual.

📊 **Link dashboard Tableau**:
👉 [Dashboard Tableau - Monitoring Siswa]((https://public.tableau.com/app/profile/muhammad.fauzan.alkhairi/viz/Menyelesaikan-Permasalahan-Institusi-Pendidikan/Dashboard1))

## 8. Conclusion
Model machine learning berhasil dibangun dengan akurasi yang cukup baik untuk memprediksi status mahasiswa. Sistem ini dapat menjadi alat bantu dalam proses pengambilan keputusan manajerial, terutama dalam mencegah siswa yang berpotensi dropout.

### Rekomendasi Tindak Lanjut:
a. Tindak lanjut terhadap siswa "Enrolled":
- Lakukan analisis lebih lanjut untuk mengklasifikasikan apakah mereka berisiko dropout atau tidak.
- Pertimbangkan teknik balancing dataset seperti SMOTE untuk memperbaiki distribusi kelas.

b. Intervensi Dini untuk Siswa Berisiko Tinggi:
- Fokus pada siswa yang berusia lebih tua dan memiliki beban finansial tinggi.
- Sediakan program dukungan finansial dan mentoring akademik untuk mengurangi risiko dropout.
