## *1. bilanganterbesar.py*

Program pertama yang akan dibuat adalah Program untuk menampilkan bilangan terbesar dari 3 Bilangan yang di Inputkan

Berikut flowchartnya

![image](https://github.com/user-attachments/assets/459f1329-8d1f-45c0-9d71-48a6cdf086bc)


*Program akan meminta kita untuk memasukkan 3 angka untuk dibandingkan :*

![image](https://github.com/user-attachments/assets/fc0ea680-5f0c-42c1-9988-ab9995c0e2df)


*Penjelasan Code*

*1.*


def mencari_bilangan_terbesar(a, b, c):
    if a > b:
        if a > c:
            return a, "A adalah terbesar"
        else:
            return c, "C adalah terbesar"
    else:
        if b > c:
            return b, "B adalah terbesar"
        else:
            return c, "C adalah terbesar"

# Input bilangan A, B, C
print("Masukkan tiga bilangan:")
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

# Menentukan bilangan terbesar
largest, message = mencari_bilangan_terbesar(a, b, c)

# Menampilkan hasil
print(f"\n{message}")
print(f"Bilangan terbesar adalah: {largest}")


1. Kita mendefinisikan function mencari_bilangan_terbesar yang mengambil tiga parameter (a,b,c).
2. function tersebut menggunakan nested if-else statement untuk membandingkan angka yang di inputkan
3. Kemudian akan menampilkan Mana bilangan terbesar
4. Lalu di Program utamanya kita masukkan angka yang harus dimasukkan oleh user
5. Lalu kita panggil kembali function mencari_biilangan_terbesar
6. Lalu Output bilangan terbesar dari ketiga bilangan yang di input akan muncul

## *2. bilanganN.py*

Program Kedua adalah untuk membandingkan bilangan yang di Input, input akan terus berjalan kecuali user memasukkan nilai 0

*Flowchartnya*

![image](https://github.com/user-attachments/assets/a6965ca4-9331-4e41-85e2-5a4ad5f6bdfc)



*Program akan meminta kita untuk memasukkan angka untuk dibandingkan, `input akan terus diminta sebelum user memasukkan angka 0 :*

![image](https://github.com/user-attachments/assets/f537bbdc-4392-4bb5-9e8e-08a563ae2303)


*Penjelasan Code*

# Input number of elements
N = int(input("Masukkan jumlah bilangan: "))

# Initialize maximum value to 0
max_val = 0

# Loop through N times to get the numbers
for i in range(1, N + 1):
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    # Check if the current number is greater than max_val
    if bilangan > max_val:
        max_val = bilangan

# Display the maximum number
print(f"Bilangan terbesar adalah: {max_val}")

Penjelasan: Di sini, kita membuat variabel max_val dan menginisialisasinya dengan nilai 0. Variabel ini akan digunakan untuk menyimpan nilai terbesar dari semua angka yang akan dibandingkan nanti. Kita mulai dengan nilai 0 karena kita belum membandingkan dengan angka apa pun.
Penjelasan: Bagian ini adalah sebuah loop (perulangan). Loop akan berjalan sebanyak N kali (sesuai dengan nilai yang dimasukkan pengguna sebelumnya).
for i in range(1, N + 1):: Baris ini memulai sebuah loop dengan variabel i yang akan mengambil nilai dari 1 hingga N. Setiap iterasi loop, nilai i akan bertambah 1.
bilangan = int(input(f"Masukkan bilangan ke-{i}: ")): Pada setiap iterasi, program akan meminta pengguna untuk memasukkan sebuah bilangan bulat. Bilangan yang dimasukkan akan disimpan dalam variabel bilangan. Format f"Masukkan bilangan ke-{i}: " digunakan untuk menampilkan pesan yang dinamis, di mana nilai i akan diganti dengan nomor urutan bilangan yang sedang diminta.
Setelah loop selesai berjalan, program akan mencetak hasil akhir, yaitu nilai terbesar yang ditemukan. Format f"Bilangan terbesar adalah: {max_val}" digunakan untuk menampilkan pesan yang disertai dengan nilai max_val.
