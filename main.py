import os
import tkinter as tk
from tkinter import messagebox


# directory, old_word, new_word
def replace_text_in_filenames():
    directory = dir.get()
    old_word = oldText.get()
    new_word = newText.get()

    renamed_files = []

    try:
        # Check if the directory exists
        if not os.path.isdir(directory):
            messagebox.showerror(
                title="error", message=f"Directory {directory} not found"
            )
            return

        # Iterate through files in the specified directory
        for filename in os.listdir(directory):
            # Full path to the file
            full_path = os.path.join(directory, filename)

            # Skip directories
            if os.path.isdir(full_path):
                continue

            # Replace only whole words using word boundaries
            if old_word in filename:
                new_filename = filename.replace(old_word, new_word)

                # New full path for the renamed file
                new_full_path = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(full_path, new_full_path)
                # print(f'Renamed: "{filename}" to "{new_filename}"')
                renamed_files.append(f'"{filename}" to "{new_filename}"')

        if renamed_files:
            message = "Renaming completed:\n" + "\n".join(renamed_files)
            messagebox.showinfo(title="Renaming Completed", message=message)
        else:
            messagebox.showinfo(title="No Changes", message="No files were renamed.")
    except Exception as e:
        print(f"Error: {e}")


root = tk.Tk()

root.geometry("800x500")
root.title("Laced")

label = tk.Label(root, text="Enter Directory!", font=("Arial", 19))
label.pack(
    padx=10,
    pady=10,
)

dir = tk.Entry(root, width=40)
dir.pack(padx=10, ipad=10)

label = tk.Label(root, text="Enter word you want to remove", font=("Arial", 19))
label.pack(
    padx=10,
    pady=10,
)

oldText = tk.Entry(root, width=40)
oldText.pack(padx=10, ipad=10)

label = tk.Label(root, text="Enter text you want instead", font=("Arial", 19))
label.pack(
    padx=10,
    pady=10,
)

newText = tk.Entry(root, width=40)
newText.pack(padx=10, ipad=10)

button = tk.Button(
    root, text="Replace", font=("arial", 19), command=replace_text_in_filenames
)
button.pack(
    pady=10,
)

root.mainloop()

# pyinstaller --onefile main.py
