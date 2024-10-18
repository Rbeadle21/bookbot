import tkinter as tk
from tkinter import filedialog, messagebox
import os

def main():
    root = tk.Tk()
    root.title("Book Report Generator")
    root.geometry("600x400")
    
    # Create a label
    label = tk.Label(root, text="Select a book to generate the report", font=("Arial", 14))
    label.pack(pady=20)
    
    # Create a button for file selection
    select_button = tk.Button(root, text="Select Book", command=lambda: select_book(root))
    select_button.pack(pady=10)

    # Text area to display the report
    report_text = tk.Text(root, height=15, width=70)
    report_text.pack(pady=10)

    root.mainloop()

def select_book(root):
    # Open file dialog to select a book
    file_path = filedialog.askopenfilename(
        initialdir="books",
        title="Select a book file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    if file_path:
        # If a file is selected, generate the report and display it
        text = get_book_text(file_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        report = generate_report(file_path, num_words, chars_dict)

        # Display the report in a new window or text area
        display_report(report)

def display_report(report):
    # Create a new window for the report
    report_window = tk.Toplevel()
    report_window.title("Book Report")
    report_window.geometry("600x500")

    # Add a scrollable text widget to display the report
    text_widget = tk.Text(report_window, wrap="word")
    text_widget.insert("1.0", report)
    text_widget.config(state="disabled")
    text_widget.pack(expand=True, fill="both")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

def generate_report(book_path, num_words, chars_dict):
    report = f"--- Begin report of {book_path} ---\n"
    report += f"{num_words} words found in the document\n\n"
    
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_chars:
        report += f"The '{char}' character was found {count} times\n"
    
    report += "--- End report ---\n"
    return report

main()
