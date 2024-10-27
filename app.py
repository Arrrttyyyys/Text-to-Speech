import os
import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS

output_path = "static/output.mp3"
text_input = ""

# Initialize main application window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("500x350")

def convert_text_to_speech():
    global text_input

    # Get text from text box if nothing is uploaded
    text_input = text_entry.get("1.0", tk.END).strip()

    if not text_input:
        messagebox.showerror("Error", "Please enter some text or upload a file.")
        return

    try:
        # Show converting message
        convert_button.config(text="Converting...", state=tk.DISABLED)
        root.update_idletasks()

        # Perform the text-to-speech conversion
        tts = gTTS(text=text_input, lang='en')
        tts.save(output_path)

        # Conversion successful, show download button
        messagebox.showinfo("Success", f"MP3 file saved at {output_path}")
        download_button.pack(pady=10)  # Show download button

    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to speech: {e}")

    finally:
        # Reset convert button
        convert_button.config(text="Convert to MP3", state=tk.NORMAL)

def select_file():
    global text_input
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'r') as file:
            text_input = file.read()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, text_input)
        file_label.config(text=f"Selected file: {os.path.basename(file_path)}")

# UI Elements
frame = tk.Frame(root)
frame.pack(pady=20)

# Upload button
upload_button = tk.Button(frame, text="Upload Text File", command=select_file)
upload_button.grid(row=0, column=0, padx=10)

# Text entry box
text_entry = tk.Text(frame, width=40, height=5)
text_entry.grid(row=1, column=0, columnspan=2, pady=10)
text_entry.insert(tk.END, "Enter text here or upload a file.")
text_entry.bind("<FocusIn>", lambda event: text_entry.delete("1.0", tk.END))  # Clear placeholder on focus

# Convert button
convert_button = tk.Button(frame, text="Convert to MP3", command=convert_text_to_speech)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to show selected file name
file_label = tk.Label(root, text="No file selected")
file_label.pack()

# Download MP3 button
def download_file():
    if os.path.exists(output_path):
        save_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                 filetypes=[("MP3 files", "*.mp3")],
                                                 initialfile="output.mp3")
        if save_path:
            os.rename(output_path, save_path)
            messagebox.showinfo("Download Complete", f"File saved as {save_path}")
    else:
        messagebox.showerror("Error", "No MP3 file to download. Please convert text first.")

download_button = tk.Button(root, text="Download MP3", command=download_file)

root.mainloop()
#test
