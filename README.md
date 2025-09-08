# Bulk File Rename Replacer

A simple Python GUI tool to batch rename files in a directory by replacing a specified word or phrase in filenames with new text.

## Features

- Select a directory containing files to rename
- Specify the word or phrase to replace in filenames
- Specify the new word or phrase to use instead
- Renames all matching files in the selected directory
- User-friendly interface built with Tkinter
- Error handling and completion messages

## Input Fields

The application consists of three input fields:

1. **Directory**: The path to the folder containing the files you want to rename in bulk.
2. **Text to Change**: The word or phrase in the filenames that you want to replace.
3. **Replacement Text**: The new word or phrase that will replace the old text in the filenames.

## Usage

1. **Run the application:**
   - You can run the script directly with Python:
     ```sh
     python main.py
     ```
   - Or build a standalone executable with PyInstaller:
     ```sh
     pyinstaller --onefile main.py
     ```
2. **In the GUI:**
   - Enter the path to the directory containing the files you want to rename.
   - Enter the word or phrase you want to replace in the filenames.
   - Enter the new word or phrase to use instead.
   - Click the **Replace** button.
   - The app will show a message with the results.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Notes

- Only files (not subdirectories) in the specified directory are renamed.
- The replacement is case-sensitive and replaces all occurrences in each filename.
- Use responsibly—renaming cannot be undone automatically.

## License

This project is provided as-is for personal or educational use.
