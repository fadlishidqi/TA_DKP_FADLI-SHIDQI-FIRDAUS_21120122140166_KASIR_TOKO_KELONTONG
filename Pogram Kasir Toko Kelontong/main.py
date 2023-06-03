import re
from tkinter import *
import random
from tkinter import messagebox
import locale
import time
from tkinter import ttk

class LoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x300")
        self.root.title("Ini Namanya Loading Screen...")

        self.progress_var = DoubleVar()

        frame = Frame(self.root, bd=0, padx=10, pady=10)
        frame.place(x=50, y=100, width=400, height=200)

        loading_label = Label(frame, text="Loading...", font=("Times New Roman", 20, "bold"))
        loading_label.pack()

        progressbar = ttk.Progressbar(frame, variable=self.progress_var, orient=HORIZONTAL, length=360, mode='determinate', style='Custom.Horizontal.TProgressbar')
        progressbar.pack(pady=20)

        self.root.update_idletasks()
        self.start_loading(progressbar)

    def start_loading(self, progressbar):
        self.progress_var.set(0)
        self.root.update_idletasks()

        for i in range(101):
            time.sleep(0.03)
            self.progress_var.set(i)
            self.root.update()

        self.root.destroy()

# Membuat window Tkinter
root = Tk()
root.title("Ini Namanya Loading Screen...")

# Mendapatkan ukuran layar
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Menghitung koordinat tengah
x = (screen_width - 500) // 2
y = (screen_height - 300) // 2

# Mengatur posisi window root di tengah layar
root.geometry(f"500x300+{x}+{y}")

style = ttk.Style()
style.theme_use('xpnative')
style.configure("Custom.Horizontal.TProgressbar", thickness=0)
loading_screen = LoadingScreen(root)
root.mainloop()

# ===============main=====================
class AplikasiBilling:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700")
        self.root.title("Program Kasir Toko By Fadli")
        bg_color = "#1fb4ff"
        title = Label(self.root, text="Program Kasir Toko", font=('monaco', 30, 'bold'), pady=2, bd=22, bg="#1fb4ff", fg="Black", relief=GROOVE)
        title.pack(fill=X)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - 1200) // 2
        y = (screen_height - 700) // 2

        self.root.geometry(f"1200x700+{x}+{y}")
        
        # ============barang_kelontong==============================
        self.beras = IntVar()
        self.minyak_goreng = IntVar()
        self.gandum = IntVar()
        self.bumbu_dapur = IntVar()
        self.terigu = IntVar()
        self.mie_instan = IntVar()

        # ==============minuman_dingin=============================
        self.sprite = IntVar()
        self.air_mineral = IntVar()
        self.jus = IntVar()
        self.coca_cola = IntVar()
        self.cendol = IntVar()
        self.fanta = IntVar()

        # ==============Total harga produk================
        self.harga_barang_kelontong = StringVar()
        self.harga_minuman_dingin = StringVar()
        self.masukan_uang = StringVar()

        # ==============Pelanggan==========================
        self.nama_pelanggan = StringVar()
        self.no_telepon = StringVar()
        self.nomor_nota = StringVar()
        x = random.randint(1000, 9999)
        self.nomor_nota.set(str(x))

        # =============detail_retail_pelanggan======================
        F1 = LabelFrame(self.root, text="Detail Pelanggan", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#1fb4ff")
        F1.place(x=0, y=94, relwidth=1)

        self.validate_nama_pelanggan = root.register(self.validate_nama_pelanggan)

        lbl_nama_pelanggan = Label(F1, text="Nama Pelanggan:", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_nama_pelanggan.grid(row=0, column=0, padx=20, pady=5)
        txt_nama_pelanggan = Entry(F1, width=15, textvariable=self.nama_pelanggan, font='arial 15', bd=7, relief=GROOVE, validate="key", validatecommand=(self.validate_nama_pelanggan, '%P'))
        txt_nama_pelanggan.grid(row=0, column=1, pady=5, padx=10)

        self.validate_number = root.register(self.validate_number)

        lbl_no_telepon = Label(F1, text="Nomor Telepon:", bg="#1fb4ff", font=('times new roman', 15, 'bold'))
        lbl_no_telepon.grid(row=0, column=2, padx=20, pady=5)
        txt_no_telepon = Entry(F1, width=15, textvariable=self.no_telepon, font='arial 15', bd=7, relief=GROOVE, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_no_telepon.grid(row=0, column=3, pady=5, padx=10)

        lbl_nomor_nota = Label(F1, text="Nomor Nota:", bg="#1fb4ff", font=('times new roman', 15, 'bold'))
        lbl_nomor_nota.grid(row=0, column=4, padx=20, pady=5)
        txt_nomor_nota = Entry(F1, width=15, textvariable=self.nomor_nota, font='arial 15', bd=7, relief=GROOVE)
        txt_nomor_nota.grid(row=0, column=5, pady=5, padx=10)

        # ============barang_kelontong==============================
        F2 = LabelFrame(self.root, text="Barang Kelontong", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#1fb4ff")
        F2.place(x=5, y=180, width=325, height=380)

        lbl_beras = Label(F2, text="Beras", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_beras.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        txt_beras = Spinbox(F2, width=8, from_=0, to=100, textvariable=self.beras, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_beras.grid(row=0, column=1, padx=10, pady=10)

        lbl_minyak_goreng = Label(F2, text="Minyak Goreng", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_minyak_goreng.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        txt_minyak_goreng = Spinbox(F2, width=8, from_=0, to=100, textvariable=self.minyak_goreng, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_minyak_goreng.grid(row=1, column=1, padx=10, pady=10)

        lbl_gandum = Label(F2, text="Gandum", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_gandum.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        txt_gandum = Spinbox(F2, width=8, from_=0, to=100, textvariable=self.gandum, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_gandum.grid(row=2, column=1, padx=10, pady=10)

        lbl_bumbu_dapur = Label(F2, text="Bumbu Dapur", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_bumbu_dapur.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        txt_bumbu_dapur = Spinbox(F2, width=8, from_=0, to=100, textvariable=self.bumbu_dapur, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_bumbu_dapur.grid(row=3, column=1, padx=10, pady=10)

        lbl_terigu = Label(F2, text="Terigu", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_terigu.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        txt_terigu = Spinbox(F2, width=8, from_=0, to=100, textvariable=self.terigu, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_terigu.grid(row=4, column=1, padx=10, pady=10)

        lbl_mie_instan = Label(F2, text="Mie Instan", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_mie_instan.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        txt_mie_instan = Spinbox(F2, width=8, from_=0, to=100, textvariable=self.mie_instan, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_mie_instan.grid(row=5, column=1, padx=10, pady=10)

        # ==============minuman_dingin=============================
        F3 = LabelFrame(self.root, text="Minuman Dingin", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#1fb4ff")
        F3.place(x=340, y=180, width=325, height=380)

        lbl_sprite = Label(F3, text="Sprite", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_sprite.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        txt_sprite = Spinbox(F3, width=8, from_=0, to=100, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_sprite.grid(row=0, column=1, padx=10, pady=10)

        lbl_air_mineral = Label(F3, text="Air Mineral", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_air_mineral.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        txt_air_mineral = Spinbox(F3, width=8, from_=0, to=100, textvariable=self.air_mineral, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_air_mineral.grid(row=1, column=1, padx=10, pady=10)

        lbl_jus = Label(F3, text="Jus", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_jus.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        txt_jus = Spinbox(F3, width=8, from_=0, to=100, textvariable=self.jus, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_jus.grid(row=2, column=1, padx=10, pady=10)

        lbl_coca_cola = Label(F3, text="Coca Cola", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_coca_cola.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        txt_coca_cola = Spinbox(F3, width=8, from_=0, to=100, textvariable=self.coca_cola, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_coca_cola.grid(row=3, column=1, padx=10, pady=10)

        lbl_cendol = Label(F3, text="Cendol", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_cendol.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        txt_cendol = Spinbox(F3, width=8, from_=0, to=100, textvariable=self.cendol, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_cendol.grid(row=4, column=1, padx=10, pady=10)

        lbl_fanta = Label(F3, text="Fanta", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_fanta.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        txt_fanta = Spinbox(F3, width=8, from_=0, to=100, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_fanta.grid(row=5, column=1, padx=10, pady=10)

        # ==============Area Nota==================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=670, y=180, width=520, height=380)

        judul_nota = Label(F5, text="Output", font=('arial', 15, 'bold'), bd=7, relief=GROOVE)
        judul_nota.pack(fill=X)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set, state='disabled')
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)

        self.txtarea.pack(fill=BOTH, expand=1)


        # =============Button Frame===============
        F6 = LabelFrame(self.root, text="Menu Nota", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#1fb4ff")
        F6.place(x=0, y=560, relwidth=1, height=140)
        lbl_total_harga_barang_kelontong = Label(F6, text="Total Harga Barang Kelontong", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_total_harga_barang_kelontong.grid(row=0, column=0, padx=20, pady=1, sticky="w")
        txt_total_harga_barang_kelontong = Entry(F6, width=25, textvariable=self.harga_barang_kelontong, font='arial 10 bold', bd=7, relief=SUNKEN)
        txt_total_harga_barang_kelontong.grid(row=0, column=1, pady=1, padx=10)

        lbl_total_harga_minuman_dingin = Label(F6, text="Total Harga Minuman Dingin", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_total_harga_minuman_dingin.grid(row=1, column=0, padx=20, pady=1, sticky="w")
        txt_total_harga_minuman_dingin = Entry(F6, width=25, textvariable=self.harga_minuman_dingin, font='arial 10 bold', bd=7, relief=SUNKEN)
        txt_total_harga_minuman_dingin.grid(row=1, column=1, pady=1, padx=10)

        lbl_masukan_uang = Label(F6, text="Masukan Jumlah Uang", bg=bg_color, font=('times new roman', 15, 'bold'))
        lbl_masukan_uang.grid(row=2, column=0, padx=20, pady=1, sticky="w")
        txt_masukan_uang = Entry(F6, width=25, textvariable=self.masukan_uang, font='arial 10 bold', bd=7, relief=SUNKEN, validate="key", validatecommand=(self.validate_number, '%P'))
        txt_masukan_uang.grid(row=2, column=1, pady=1, padx=10)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=570, width=586, height=100)

        btn_total = Button(btn_F, command=self.total, text="Total", bg="#1a2dd6", fg="white", pady=15, bd=3, width=10, font='arial 15 bold')
        btn_total.grid(row=0, column=0, padx=5, pady=5)

        btn_generate_nota = Button(btn_F, command=self.area_nota, text="Buat Nota", bg="#1a2dd6", fg="white", pady=15, bd=3, width=10, font='arial 15 bold')
        btn_generate_nota.grid(row=0, column=1, padx=5, pady=5)

        btn_clear = Button(btn_F, command=self.clear, text="Clear", bg="#1a2dd6", fg="white", pady=15, bd=3, width=10, font='arial 15 bold')
        btn_clear.grid(row=0, column=2, padx=5, pady=5)

        btn_exit = Button(btn_F, command=self.exit_app, text="Exit", bg="#1a2dd6", fg="white", pady=15, bd=3, width=10, font='arial 15 bold')
        btn_exit.grid(row=0, column=3, padx=5, pady=5)

    def hitung_kembalian(self):
        total_nota = self.total_harga_barang_kelontong + self.total_harga_minuman_dingin
        masukan_uang = int(self.masukan_uang.get())
        kembalian = masukan_uang - total_nota
        self.txtarea.config(state="normal")
        self.txtarea.insert(END, f"\n\nJumlah Uang: {masukan_uang}")
        self.txtarea.insert(END, f"\nKembalian: {kembalian}")
        self.txtarea.config(state="disabled")


    def validate_nama_pelanggan(self, value):
        # Fungsi validasi untuk memeriksa apakah nilai input hanya huruf
        if value and not value.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Input hanya boleh berisi huruf.")
            return False
        return True

    def validate_number(self, value):
        # Fungsi validasi untuk memeriksa apakah nilai input hanya angka
        if value and not re.match(r"^[0-9]+$", value):
            messagebox.showerror("Error", "Input hanya boleh berisi angka.")
            return False
        return True 
    
    def total(self):
        self.txtarea.config(state="normal")
        self.txtarea.delete('1.0', END)
        # Set Lokasi 
        locale.setlocale(locale.LC_ALL, 'id_ID')

        # =========barang_kelontong=========
        if all(isinstance(value.get(), int) for value in [self.beras, self.minyak_goreng, self.gandum, self.bumbu_dapur, self.terigu, self.mie_instan]):
            self.total_harga_barang_kelontong = (
                (self.beras.get() * 50000) +
                (self.minyak_goreng.get() * 120000) +
                (self.gandum.get() * 20000) +
                (self.bumbu_dapur.get() * 30000) +
                (self.terigu.get() * 15000) +
                (self.mie_instan.get() * 12000)
        )
            self.harga_barang_kelontong.set(locale.currency(self.total_harga_barang_kelontong, grouping=True))
        
        # =========minuman_dingin=========
        if all(isinstance(value.get(), int) for value in [self.sprite, self.air_mineral, self.jus, self.coca_cola, self.cendol, self.fanta]):
            self.total_harga_minuman_dingin = (
                (self.sprite.get() * 40000) +
                (self.air_mineral.get() * 20000) +
                (self.jus.get() * 45000) +
                (self.coca_cola.get() * 30000) +
                (self.cendol.get() * 35000) +
                (self.fanta.get() * 50000)
            )
            self.harga_minuman_dingin.set(locale.currency(self.total_harga_minuman_dingin, grouping=True))

        # total harga tidak 0
        if self.total_harga_barang_kelontong == 0 and self.total_harga_minuman_dingin == 0:
            messagebox.showerror("Error", "Tidak ada barang yang dibeli")
        else:
            self.txtarea.config(state="disabled")

    def welcome_nota(self):
        self.txtarea.config(state="normal")
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tSelamat Datang Di Toko Fadli\n")
        self.txtarea.insert(END, f"\n Nomor Nota : {self.nomor_nota.get()}")
        self.txtarea.insert(END, f"\n Nama Pelanggan : {self.nama_pelanggan.get()}")
        self.txtarea.insert(END, f"\n Nomor Telepon : {self.no_telepon.get()}")
        self.txtarea.insert(END, f"\n===============================================")
        self.txtarea.insert(END, f"\n Barang \t\tQty\t\tHarga")
        self.txtarea.insert(END, f"\n===============================================")
        self.txtarea.config(state="disabled")

    def area_nota(self):
        def format_rupiah(amount):
            locale.setlocale(locale.LC_ALL, 'id_ID')  # Set locale ke Indonesia
            return locale.currency(amount, grouping=True)

        if self.nama_pelanggan.get() == "" or self.no_telepon.get() == "":
            messagebox.showerror("Error", "Detail pelanggan harus diisi")
        elif self.harga_barang_kelontong.get() == "":
            messagebox.showerror("Error", "Tidak ada barang yang dibeli")
        elif self.masukan_uang.get() == "":
            messagebox.showerror("Error", "Masukkan jumlah uang yang valid")
        else:
            masukan_uang = int(self.masukan_uang.get())
            total_nota = self.total_harga_barang_kelontong + self.total_harga_minuman_dingin
            kembalian = masukan_uang - total_nota

            if masukan_uang < total_nota:
                messagebox.showerror("Error", "Jumlah uang yang dimasukkan kurang!")
            else:
                self.welcome_nota()
                self.txtarea.config(state="normal")

            # =========barang_kelontong=========
            if self.beras.get() != 0:
                self.txtarea.insert(END, f"\n Beras\t\t{self.beras.get()}\t\t{format_rupiah(self.beras.get() * 50000)}")
            if self.minyak_goreng.get() != 0:
                self.txtarea.insert(END, f"\n Minyak Goreng\t\t{self.minyak_goreng.get()}\t\t{format_rupiah(self.minyak_goreng.get() * 120000)}")
            if self.gandum.get() != 0:
                self.txtarea.insert(END, f"\n Gandum\t\t{self.gandum.get()}\t\t{format_rupiah(self.gandum.get() * 20000)}")
            if self.bumbu_dapur.get() != 0:
                self.txtarea.insert(END, f"\n Bumbu Dapur\t\t{self.bumbu_dapur.get()}\t\t{format_rupiah(self.bumbu_dapur.get() * 30000)}")
            if self.terigu.get() != 0:
                self.txtarea.insert(END, f"\n Terigu\t\t{self.terigu.get()}\t\t{format_rupiah(self.terigu.get() * 15000)}")
            if self.mie_instan.get() != 0:
                self.txtarea.insert(END, f"\n Mie Instan\t\t{self.mie_instan.get()}\t\t{format_rupiah(self.mie_instan.get() * 12000)}")

            # =========minuman_dingin=========
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{format_rupiah(self.sprite.get() * 40000)}")
            if self.air_mineral.get() != 0:
                self.txtarea.insert(END, f"\n Air Mineral\t\t{self.air_mineral.get()}\t\t{format_rupiah(self.air_mineral.get() * 20000)}")
            if self.jus.get() != 0:
                self.txtarea.insert(END, f"\n Jus\t\t{self.jus.get()}\t\t{format_rupiah(self.jus.get() * 45000)}")
            if self.coca_cola.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.coca_cola.get()}\t\t{format_rupiah(self.coca_cola.get() * 30000)}")
            if self.cendol.get() != 0:
                self.txtarea.insert(END, f"\n Cendol\t\t{self.cendol.get()}\t\t{format_rupiah(self.cendol.get() * 35000)}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{format_rupiah(self.fanta.get() * 50000)}")

            self.txtarea.insert(END, f"\n-----------------------------------------------")
            self.txtarea.insert(END, f"\n Total Harga Barang Kelontong\t\t\t{format_rupiah(self.total_harga_barang_kelontong)}")
            self.txtarea.insert(END, f"\n Total Harga Minuman Dingin\t\t\t\t{format_rupiah(self.total_harga_minuman_dingin)}")
            self.txtarea.insert(END, f"\n-----------------------------------------------")
            total_nota = self.total_harga_barang_kelontong + self.total_harga_minuman_dingin
            self.txtarea.insert(END, f"\n Total Nota : \t\t\t\t{format_rupiah(total_nota)}")
            self.txtarea.insert(END, f"\n Jumlah Uang: \t\t\t\t{format_rupiah(masukan_uang)}")
            self.txtarea.insert(END, f"\n Kembalian: \t\t\t\t{format_rupiah(kembalian)}")
            self.txtarea.config(state="disabled")


    def clear(self):
        self.txtarea.config(state="normal")
        self.nama_pelanggan.set("")
        self.no_telepon.set("")
        self.beras.set(0)
        self.minyak_goreng.set(0)
        self.gandum.set(0)
        self.bumbu_dapur.set(0)
        self.terigu.set(0)
        self.mie_instan.set(0)
        self.sprite.set(0)
        self.air_mineral.set(0)
        self.jus.set(0)
        self.coca_cola.set(0)
        self.cendol.set(0)
        self.fanta.set(0)
        self.harga_barang_kelontong.set("")
        self.harga_minuman_dingin.set("")
        self.masukan_uang.set("")
        self.nomor_nota.set(str(random.randint(1000, 9999)))
        self.txtarea.delete("1.0", END)
        self.txtarea.config(state="disabled")

    def exit_app(self):
        response = messagebox.askyesno("Exit Application", "Apakah Anda yakin ingin keluar dari aplikasi?")
        if response == 1:
            self.root.destroy()

root = Tk()
app = AplikasiBilling(root)
root.mainloop()
