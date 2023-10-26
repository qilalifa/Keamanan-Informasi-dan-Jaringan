def encrypt(text, key):
    # Buat matriks dengan key kolom
    matrix = [['' for _ in range(key)] for _ in range(len(text) // key + 1)]

    # Isi matriks dengan huruf dari teks
    row, col = 0, 0 # melacak baris dan kolom saat mengisi matriks
    for char in text: 
        # memeriksa apakah karakter bukan spasi, jika bukan maka akan dimasukkan ke dalam matriks
        if char != ' ': 
            matrix[row][col] = char 
            col += 1 # setelah mengisi karakter, variabel 'col' akan diinkremen dan dipindah ke kolom kanan
            
            # memeriksa apakah kolom sudah mencapai batas sesuai 'key'
            if col == key: 
                col = 0 # varibel 'col' akan diatur kembali, 'row' diinkremen beralih ke baris berikutnya
                row += 1

    # Baca matriks dalam bentuk baris
    result = ''
    for col in range(key):
        for row in range(len(matrix)):
            # memeriksa apakah ada string yang kosong
            if matrix[row][col] != '': 
                result += matrix[row][col]
            else: # jika ada akan ditambahkan karakter x
                result += 'x'

    return result


def decrypt(ciphertext, key):
    # Hitung jumlah baris berdasarkan panjang ciphertext dan key
    num_rows = len(ciphertext) // key

    # Buat matriks dengan key kolom
    matrix = [['' for _ in range(key)] for _ in range(num_rows)]

    # Isi matriks dengan huruf dari ciphertext
    index = 0
    for col in range(key):
        for row in range(num_rows):
            # mengisi kolom dengan karakter dan mengisi baris sesuai dengan panjang cipherteks
            matrix[row][col] = ciphertext[index] 
            index += 1

    # Baca matriks dalam bentuk baris
    result = ''
    for row in range(num_rows):
        for col in range(key):
            # memeriksa apakah ada karakter x dan mengabaikan karakter x jika ada
            if matrix[row][col] != 'x':
                result += matrix[row][col]

    return result

while True:
    option = input("Pilih opsi (e untuk enkripsi, d untuk dekripsi, q untuk keluar): ")
    if option == 'q':
        break
    elif option == 'e':
        plaintext = input("Masukkan teks yang akan dienkripsi: ")
        key = int(input("Masukkan key: "))
        encrypted_text = encrypt(plaintext, key)
        print("Hasil cipher teks: " + encrypted_text)
    elif option == 'd':
        ciphertext = input("Masukkan teks yang akan didekripsi: ")
        key = int(input("Masukkan key: "))
        decrypted_text = decrypt(ciphertext, key)
        print("Hasil plain teks: " + decrypted_text)
    else:
        print("Opsi tidak valid. Silakan coba lagi.")
