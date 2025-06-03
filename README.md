# Setup Raspberry Pi Pico W dengan MicroPython

Panduan ini menjelaskan cara mengatur Raspberry Pi Pico W menggunakan MicroPython dan Thonny IDE.

---
Pinout Raspberry pi pico W
![PinOut](/aset/pico-pinout.png)

---
pin ir dan ultrasonik 
![pins](/aset/pin.png)

---
Skematik
![Skematik](/skematik/skematik_bb.png)

---
Output
![Output](/aset/output.png)

---

## 1. Install Python

Unduh dan instal Python dari situs resminya:

👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## 2. Unduh Thonny IDE

👉 [https://thonny.org/](https://thonny.org/)

---

## 3. Unduh Firmware MicroPython untuk Pico W

👉 [https://micropython.org/download/RPI_PICO_W/](https://micropython.org/download/RPI_PICO_W/)

---

## 4. Masuk ke Mode Bootsel

1. Tahan tombol **BOOTSEL** pada Raspberry Pi Pico W.
2. Sambil menahan tombol, sambungkan ke komputer via USB.
3. Komputer akan mendeteksi drive baru bernama `RPI-RP2`.

---

## 5. Unggah Firmware

Salin file firmware `.uf2` yang sudah diunduh ke dalam drive `RPI-RP2`.

---

## 6. Setting dengan Thonny

1. Buka aplikasi Thonny.
2. Klik pojok kanan bawah, pilih “Install MicroPython”.
3. Sesuaikan varian board Raspberry Pi Pico W.
4. Klik install.
5. Setelah selesai, klik kembali pojok kanan bawah dan pilih **MicroPython (Raspberry Pi Pico)**.
6. Pilih port COM yang sesuai.

---

## 7. Membuat dan Menyimpan Program

- Buat program Python di Thonny.
- Klik **File > Save As**, pilih penyimpanan `Raspberry Pi Pico`.
- Simpan dengan nama **main.py**.

---

## 8. Menjalankan Program Otomatis

Setelah disimpan, cukup sambungkan Pico W ke sumber daya, dan program akan langsung berjalan.

---

## Ilustrasi Langkah-Langkah

---

### Langkah 1
**Upload file firmware (drag and drop)**  
![Langkah 1](/aset/1.png)

---

### Langkah 2
**Setting dengan Thonny**

1. Buka Thonny dan lakukan pengaturan awal.  
   ![Langkah 2 - Setting Awal](/aset/2.png)

2. Pilih interpreter Raspberry Pi Pico W, Install firmware jika belum terinstall.  
   ![Langkah 2 - Pilih Interpreter](/aset/3.png)

3. pilih variant yang sesuai.  
   ![Langkah 2 - Install Firmware](/aset/4.png)

4. Setelah di-install, klik Interpreter untuk terhubung ke Raspberry Pi Pico W.  
   ![Langkah 2 - Hubungkan ke Pico W](/aset/5.png)

---

### Langkah 3
**Simpan program ke Raspberry Pi Pico**

- Pilih menu "Save As" lalu pilih "Raspberry Pi Pico" agar program disimpan ke mikrokontroler.  
  ![Langkah 3 - Simpan Program](/aset/6.png)

----
