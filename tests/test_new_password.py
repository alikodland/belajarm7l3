import string
from password.new_password import generate_password

def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters

"""
Tambahkan satu atau lebih tes dari pilihan berikut. Atau buat tes kamu sendiri.
Akan lebih bagus jika kamu bisa membuat lebih banyak tes!

Tes untuk memastikan panjang password sesuai dengan yang diminta
Tes untuk memastikan dua password yang dibuat berurutan tidak sama
"""
def test_password_length():
    """Menguji apakah panjang kata sandi sesuai dengan panjang yang ditentukan"""
    for length in range(1, 21): 
        assert len(generate_password(length)) == length

def test_password_randomness():
    """Menguji bahwa dua kata sandi yang dihasilkan secara berurutan berbeda"""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2, "Dua kata sandi yang dibuat secara berurutan tidak boleh sama."
