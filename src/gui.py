import tkinter as tk
from tkinter import font
import text_analyzer_algo as taa

# Modul untuk diproses
def process_text(text):
    # Lakukan pemrosesan atau operasi lain pada teks
    processed_text = taa.full_analysis(text)
    if processed_text > 0:
        return "Positif"
    elif processed_text < 0:
        return "Negatif"
    else:
        return "Netral"

# Fungsi untuk memproses tombol
def process_button_click():
    input_text = input_textbox.get("1.0", tk.END).strip()  # Ambil teks dari kotak teks input
    output_text = process_text(input_text)  # Panggil fungsi dari modul
    output_textbox.configure(state=tk.NORMAL)  # Aktifkan mode penulisan pada kotak teks output
    output_textbox.delete("1.0", tk.END)  # Hapus teks yang ada di kotak teks output
    output_textbox.insert(tk.END, output_text)  # Tampilkan keluaran fungsi di kotak teks output
    output_textbox.configure(state=tk.DISABLED)  # Nonaktifkan mode penulisan pada kotak teks output

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("DeenVirtuoso")
root.geometry("600x600")
root.resizable(False, False)

# Mengatur warna latar belakang
root.configure(bg="#F4ECE1")

# Membuat judul besar
title_font = font.Font(family="Helvetica", size=24, weight="bold")
title_label = tk.Label(root, text="DeenVirtuoso", font=title_font, bg="#F4ECE1")
title_label.pack(pady=(50, 10))

# Membuat subjudul
subtitle_font = font.Font(family="Helvetica", size=14)
subtitle_label = tk.Label(root, text="Simple Dakwah-Text Sentiment Evaluator App", font=subtitle_font, bg="#F4ECE1")
subtitle_label.pack()

# Kotak teks input
input_label = tk.Label(root, text="Masukkan Teks:", bg="#F4ECE1")
input_label.pack()
input_textbox = tk.Text(root, height=10, width=60)
input_textbox.pack(pady=10)

# Tombol proses
process_button = tk.Button(root, text="Proses", command=process_button_click, bg="#CCDBEF")
process_button.pack(pady=10)

# Kotak teks output
output_label = tk.Label(root, text="Hasil:", bg="#F4ECE1")
output_label.pack()
output_textbox = tk.Text(root, height=10, width=60)
output_textbox.configure(state=tk.DISABLED)  # Mengatur kotak teks output menjadi tidak dapat diubah
output_textbox.pack()

root.mainloop()
