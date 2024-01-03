# WordPress

Selamat datang di repositori pengembangan WordPress! Silakan lihat [panduan kontributor](CONTRIBUTING.md) untuk informasi tentang cara membuka laporan bug, berkontribusi dalam pembuatan patch, menguji perubahan, menulis dokumentasi, atau terlibat dalam berbagai cara lainnya.

## Memulai
### Kredensial
#### Memulai

WordPress adalah proyek berbasis PHP, MySQL, dan JavaScript, serta menggunakan Node untuk dependensi JavaScript-nya. Lingkungan pengembangan lokal tersedia untuk memulai dengan cepat.

Anda akan memerlukan pemahaman dasar tentang cara menggunakan baris perintah (command line) di komputer Anda. Hal ini akan memungkinkan Anda untuk mengatur lingkungan pengembangan lokal, menjalankannya, menghentikannya jika diperlukan, dan menjalankan pengujian.

Anda akan memerlukan Node dan npm terinstal di komputer Anda. Node adalah runtime JavaScript yang digunakan untuk alat pengembangan, dan npm adalah manajer paket yang disertakan dengan Node. Jika Anda memiliki manajer paket yang terinstal di sistem operasi Anda, pengaturan bisa secepat ini:

- macOS: `brew install node`
- Windows: `choco install nodejs`
- Ubuntu: `apt install nodejs npm`

Jika Anda tidak menggunakan manajer paket, lihat halaman [unduhan Node.js](https://nodejs.org/en/download/) untuk pemasang dan biner.

Anda juga perlu menginstal Docker dan menjalankannya di komputer Anda. Docker adalah perangkat lunak virtualisasi yang menggerakkan lingkungan pengembangan lokal. Docker dapat diinstal seperti aplikasi biasa.

#### Perintah Lingkungan Pengembangan
Pastikan Docker berjalan sebelum menggunakan perintah-perintah ini.

**Untuk memulai lingkungan pengembangan untuk pertama kalinya:**
- Klone repositori saat ini dengan perintah `git clone https://github.com/WordPress/wordpress-develop.git`.
- Kemudian, di terminal Anda, pindah ke folder repositori dengan perintah `cd wordpress-develop` dan jalankan perintah-perintah berikut:

  ```shell
  npm install
  npm run build:dev
  npm run env:start
  npm run env:install
