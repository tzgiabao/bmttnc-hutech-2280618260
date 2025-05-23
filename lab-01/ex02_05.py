so_gio_lam = float(input("Nhap so gio lam: "))
Luong_gio = float(input("nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * Luong_gio + gio_vuot_chuan * Luong_gio * 1.5
print(f"so tien thuc linh cua nhan vien:{thuc_linh}")