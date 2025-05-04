# Import thuật toán McEliece với tham số cụ thể mceliece348864 từ thư viện pypqc
from pqc.kem import mceliece348864 as kemalg

# === BƯỚC 1: SINH CẶP KHÓA ===
# Hàm keypair() sinh ra một cặp khóa gồm:
# - pk (public key): dùng để mã hóa (encapsulation)
# - sk (secret key): dùng để giải mã (decapsulation)
pk, sk = kemalg.keypair()

print("Khoa cong khai (Public Key):", pk)
print("Khoa bi mat (Secret Key):", sk)

# === BƯỚC 2: MÃ HÓA (ENCAPSULATION) ===
# Hàm encap(pk) thực hiện mã hóa với khóa công khai, tạo ra:
# - ss: khóa chia sẻ (shared secret) sẽ được dùng làm khóa phiên
# - kem_ct: bản mã (ciphertext) dùng để gửi cho người nhận
ss, kem_ct = kemalg.encap(pk)

print("Ban ma (Ciphertext):", kem_ct)
print("Khoa chia se (Shared Secret) đa ma hoa:", ss)

# === BƯỚC 3: GIẢI MÃ (DECAPSULATION) ===
# Hàm decap(ciphertext, secret key) dùng để giải mã bản mã,
# tái tạo lại khóa chia sẻ ss_result từ ciphertext và secret key
ss_result = kemalg.decap(kem_ct, sk)

print("Khoa chia se giai ma duoc (Decapsulated Shared Secret):", ss_result)

# === BƯỚC 4: KIỂM TRA TÍNH ĐÚNG ĐẮN ===
# So sánh khóa chia sẻ ban đầu và sau khi giải mã
# Nếu hai khóa trùng nhau thì quá trình mã hóa và giải mã thành công
if ss_result != ss:
    print("Khong trung khop")  # Có lỗi trong quá trình mã hóa/giải mã
else:
    print("Trung khop")        # Thành công, hai bên có cùng khóa phiên
