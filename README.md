## Nama: Hendriana Mayrino Mahdiyyah
## NIM: 1203220040

Program file transfer protocol menggunakan socket programming, berikut adalah penjelasan singkat tentang cara menggunakan progam ini:

## Cara Penggunaan

### Server
1. Pastikan Python telah terinstal di komputer Anda.
2. Buka terminal atau command prompt.
3. Jalankan script server dengan menjalankan perintah berikut:

Server akan mulai menunggu koneksi dari klien.

### Klien
1. Pastikan Python telah terinstal di komputer Anda.
2. Buka terminal atau command prompt.
3. Jalankan script klien dengan menjalankan perintah berikut:

Klien akan mencoba terhubung ke server.

### Perintah yang Tersedia

Setelah klien terhubung ke server, Anda dapat menggunakan perintah-perintah berikut:

1. **ls** - List files: Menampilkan daftar file dan folder dalam direktori saat ini pada server.

2. **rm** - Remove file: Menghapus file dari server.
Contoh: `rm file.txt`

3. **upload** - Upload file: Mengunggah file dari klien ke server.
Contoh: `upload file.txt`

4. **download** - Download file: Mengunduh file dari server ke klien.
Contoh: `download file.txt`

5. **size** - File size: Menampilkan ukuran file dalam megabyte (MB).
Contoh: `size file.txt`

6. **byebye** - Exit: Mengakhiri koneksi dengan server.

Ikuti petunjuk di atas untuk berbagi file antara klien dan server menggunakan aplikasi ini. Selamat menggunakan!

## Soal Tambahan
## Penanganan Nama File Duplikat

Apa yang terjadi jika pengirim mengirimkan file dengan nama yang sama dengan file yang telah dikirim sebelumnya? Dapat menyebabkan masalah kah ? Lalu bagaimana solusinya? Implementasikan ke dalam program, solusi yang Anda berikan.

Ketika pengirim mengirimkan file dengan nama yang sama dengan file yang telah dikirim sebelumnya, akan terjadi konflik yang dapat menyebabkan kehilangan data dari file yang sudah ada sebelumnya. Untuk menghindari masalah ini, kami telah menerapkan solusi yang memungkinkan server untuk memberikan nama unik kepada file yang baru dikirim.

Solusi ini diterapkan dengan menambahkan angka unik ke nama file baru sebelum ekstensi file. Jika file dengan nama yang sama sudah ada di dalam folder, maka angka unik akan ditambahkan ke nama file baru sebelum file tersebut disimpan.

Implementasi solusi ini dapat ditemukan dalam kode server di bagian fungsi receive_file. Kami telah menambahkan logika untuk memeriksa apakah file dengan nama yang sama sudah ada. Jika ya, maka angka unik akan ditambahkan ke nama file sebelum file tersebut disimpan.

Untuk detail lebih lanjut, silakan lihat kode di server.py.

