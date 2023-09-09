import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
import subprocess

def execute_ipconfig():
    output_text.delete(1.0, tk.END)
    try:
        with open("ipconfig_output.txt", "wb") as output_file:
            result = subprocess.run(["ipconfig", "/all"], stdout=output_file, stderr=subprocess.PIPE)
        with open("ipconfig_output.txt", "rb") as output_file:
            output_data = output_file.read()
            output_text.insert(tk.END, output_data.decode(errors='ignore'))
    except Exception as e:
        output_text.insert(tk.END, f"Fehler beim Ausführen von 'ipconfig /all': {str(e)}")

root = tk.Tk()
root.title("WIFI-DATA-VIEWER")

root.configure(bg="black")

style = ttk.Style(root)
style.configure('TButton', foreground='lime green', background='black')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

output_text = tk.Text(root, wrap=tk.WORD, width=80, height=20, bg="black", fg="lime green")
output_text.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(root, command=output_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
output_text.config(yscrollcommand=scrollbar.set)

execute_button = tk.Button(root, text="EXPLORE WIFI DATA", command=execute_ipconfig, bg="black", fg="lime green")
execute_button.grid(row=1, column=0, columnspan=2, sticky="nsew")

window_width = 800
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.iconbitmap("wifi.ico")

root.mainloop()