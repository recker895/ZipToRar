import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def select_file():
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)

def select_output():
    output_path = filedialog.asksaveasfilename(defaultextension=".rar",
                                               filetypes=[("RAR files", "*.rar")])
    entry_output.delete(0, tk.END)
    entry_output.insert(0, output_path)

def convert_to_rar():
    input_file = entry_file.get()
    output_file = entry_output.get()

    if not input_file or not output_file:
        messagebox.showerror("Error", "Please select input and output files.")
        return

    try:
        # Command to create RAR archive
        command = f'rar a "{output_file}" "{input_file}"'
        subprocess.run(command, shell=True, check=True)

        messagebox.showinfo("Success", "RAR file created successfully!")

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to create RAR.\nMake sure WinRAR is installed and 'rar' is in PATH.")

# UI Setup
root = tk.Tk()
root.title("File to RAR Converter")
root.geometry("400x200")

# Input File
tk.Label(root, text="Select File:").pack()
entry_file = tk.Entry(root, width=50)
entry_file.pack()
tk.Button(root, text="Browse", command=select_file).pack()

# Output File
tk.Label(root, text="Save As (.rar):").pack()
entry_output = tk.Entry(root, width=50)
entry_output.pack()
tk.Button(root, text="Choose Location", command=select_output).pack()

# Convert Button
tk.Button(root, text="Convert to RAR", bg="green", fg="white", command=convert_to_rar).pack(pady=10)

root.mainloop()