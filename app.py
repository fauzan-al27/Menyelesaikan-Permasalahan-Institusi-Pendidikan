import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Judul aplikasi
st.title("Prediksi Dropout Mahasiswa")
st.write("Aplikasi ini memprediksi apakah seorang mahasiswa akan dropout atau lulus berdasarkan data yang tersedia.")

# Memuat data
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv'
    return pd.read_csv(url, sep=';')

data = load_data()
st.subheader("Data Awal")
st.dataframe(data.head())

# Preprocessing
label_encoder = LabelEncoder()
data['Status'] = label_encoder.fit_transform(data['Status'])
data = pd.get_dummies(data, columns=['Gender', 'Daytime_evening_attendance', 'International'], drop_first=True)

# Normalisasi fitur numerik
scaler = MinMaxScaler()
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns.drop('Status')
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Split fitur dan label
X = data.drop(columns=['Status'])
y = data['Status']

# Split data train dan test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Model dan tuning
params = {
    'n_estimators': [100],
    'max_depth': [None],
    'min_samples_split': [2],
    'min_samples_leaf': [1],
    'criterion': ['gini']
}
grid = GridSearchCV(RandomForestClassifier(random_state=42), params, cv=5)
grid.fit(X_train, y_train)
best_model = grid.best_estimator_

# Evaluasi model
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.subheader("Evaluasi Model")
st.write(f"Akurasi: {accuracy * 100:.2f}%")
st.text("Classification Report:")
st.text(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Visualisasi Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
            xticklabels=label_encoder.classes_,
            yticklabels=label_encoder.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
st.pyplot(fig)

# Visualisasi Fitur Penting
importances = best_model.feature_importances_
feat_importance = pd.DataFrame({'Fitur': X.columns, 'Importance': importances})
feat_importance = feat_importance.sort_values(by='Importance', ascending=False)

st.subheader("Fitur Terpenting")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=feat_importance.head(10), y='Fitur', x='Importance')
st.pyplot(fig2)

# Prediksi seluruh data dan simpan untuk dashboard
y_pred_full = best_model.predict(X)
df_final = X.copy()
df_final['Actual_Status'] = label_encoder.inverse_transform(y)
df_final['Predicted_Status'] = label_encoder.inverse_transform(y_pred_full)

# Tampilkan hasil prediksi
st.subheader("Hasil Prediksi Seluruh Data")
st.dataframe(df_final[['Actual_Status', 'Predicted_Status']].value_counts().rename("Jumlah").reset_index())

# Unduh hasil prediksi
csv = df_final.to_csv(index=False).encode('utf-8')
st.download_button("Download Hasil Prediksi sebagai CSV", data=csv, file_name="data_with_predictions.csv", mime='text/csv')
