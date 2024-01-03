# Mulai

Anda perlu menginstal Docker dan menjalankannya di komputer Anda.

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
   ```

### Menjalankan Unit Test

```shell
npm run test:php -- --filter Tests_User_CountUserPosts
npm run test:php -- --filter Tests_User_GetActiveBlogForUser
npm run test:php -- --filter Tests_Admin_IncludesComment
npm run test:php -- --filter Tests_Admin_IncludesUser
npm run test:php -- --filter Tests_Formatting_Redirect
npm run test:php -- --filter Tests_Admin_wpThemeInstallListTable
```

### Menjalankan E2E Test
Pastikan wordpress-develop sudah berjalan di port 8889
Jalankan Sript e2eTest.py dengan perintah
```shell
pytest e2eTest.py
```
