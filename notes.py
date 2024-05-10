import tkinter as tk

def save_note():
    note = text.get("1.0", tk.END)
    filename = filename_entry.get()
    
    if not filename:
        filename = "untitled_note"
    
    filename = filename.strip().replace(" ", "_") + ".txt"
    
    with open(filename, "w") as file:
        file.write(note)
    text.delete("1.0", tk.END)
    status_label.config(text=f"Заметка сохранена в файле: {filename}")

root = tk.Tk()
root.title("Notes")

text = tk.Text(root, height=10, width=50, font=("Arial", 12))
text.pack()

filename_label = tk.Label(root, text="File Name:", font=("Arial", 12))
filename_label.pack()

filename_entry = tk.Entry(root, font=("Arial", 12))
filename_entry.pack()

save_button = tk.Button(root, text="Save Note", bg="#4CAF50", fg="white", font=("Arial", 12, 'bold'), command=save_note)
save_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
status_label.pack()

root.mainloop()
