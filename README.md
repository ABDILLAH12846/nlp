# Cara untuk Menjalankan Aplikasi Klasifikasi Sentimen Teks dengan Flask

**File ini menjelaskan cara menjalankan aplikasi klasifikasi sentimen teks yang dibangun dengan Flask.**

## Instalasi

Pastikan Anda memiliki Python 3 dan pip terinstal. Jalankan perintah berikut untuk menginstal dependensi yang dibutuhkan:

```cmd 
pip install -r req.txt
```

## Penggunaan

1. **Simpan file `app.py` di direktori yang sama dengan file `model.pkl` dan `vect.pkl`.**
[Image of file app.py]
2. **Untuk menjalankan aplikasi di port default (3000):**
   `python app.py`
3. **Untuk mengakses titik akhir prediksi:
  Kirim permintaan POST dengan format JSON ke `http://localhost:3000/`. Isi body JSON dengan kunci "text" dan isikan teks yang ingin Anda klasifikasikan sentimennya.**

    ```json
    {
    "text": "Ini adalah film yang bagus sekali!"
    }
    ```
4. **Aplikasi akan mengembalikan respon JSON dengan kunci "prediction":**

    ```json
    {
        "prediction": "Positive"
    }
    ```
  
   **Contoh penggunaan curl**
   ```curl
   curl -X POST -H "Content-Type: application/json" -d '{"text": "Ini adalah film yang sangat membosankan."}' http://localhost:3000/
   ```
   ```json
   {
    "prediction": "Negative"
   }
   ```

## Catatan tambahan

* File `model.pkl` dan `vect.pkl` berisi model klasifikasi sentimen yang telah dilatih.
* Aplikasi ini hanya memprediksi sentimen positif atau negatif. Anda dapat memodifikasi kode untuk menambahkan lebih banyak kategori sentimen.
* Pastikan model dan vectorizer yang Anda gunakan kompatibel dengan versi joblib dan scikit-learn yang terinstal.

## Umpan balik dan kontribusi

Silakan bagikan umpan balik dan kontribusi Anda untuk meningkatkan aplikasi ini.

## Perubahan yang dilakukan

* Judul dan deskripsi diperbarui agar lebih spesifik.
* Instruksi instalasi ditambahkan.
* Penjelasan penggunaan titik akhir prediksi diperinci.
* Contoh penggunaan dengan curl ditambahkan.
* Catatan tambahan diperbarui.

**Semoga readme.md ini membantu Anda menjalankan dan menggunakan aplikasi klasifikasi sentimen dengan mudah!**


Kode ini mencakup semua perubahan yang dijelaskan sebelumnya. Judul dan deskripsi diperbarui agar lebih spesifik. Instruksi instalasi ditambahkan. Penjelasan penggunaan titik akhir prediksi diperinci. Contoh penggunaan dengan curl ditambahkan. Catatan tambahan diperbarui.

Berikut adalah penjelasan singkat tentang setiap bagian kode:

* **Judul dan deskripsi:** Judul dan deskripsi diperbarui agar lebih spesifik dan informatif. Judul sekarang adalah "Readme.md untuk Menjalankan Aplikasi Klasifikasi Sentimen Teks dengan Flask" dan deskripsinya sekarang adalah "File ini menjelaskan cara menjalankan aplikasi klasifikasi sentimen teks yang dibangun dengan Flask."
* **Instalasi:** Instruksi instalasi ditambahkan untuk memudahkan pengguna dalam menginstal dependensi yang dibutuhkan.
* **Penggunaan:** Penjelasan penggunaan titik akhir prediksi diperinci untuk memudahkan pengguna dalam memahami cara menggunakan aplikasi.
* **Contoh penggunaan dengan curl:** Contoh penggunaan dengan curl ditambahkan untuk memudahkan pengguna dalam menggunakan aplikasi dari baris perintah.
* **Catatan tambahan:** Catatan tambahan diperbarui untuk menyertakan informasi tambahan yang mungkin berguna bagi pengguna.

Saya harap kode ini bermanfaat!



