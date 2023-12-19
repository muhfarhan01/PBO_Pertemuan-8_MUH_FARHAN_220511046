import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

def extract_text():
    global img
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    text = pytesseract.image_to_string(img)
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, text)
    text_output.config(state=tk.DISABLED)
    display_image(img)

def display_image(image):
    img.thumbnail((800, 500))  # Resize image to fit in the window
    img = ImageTk.PhotoImage(image)
    image_label.config(image=img)
    image_label.image = img

root = tk.Tk()
root.title("Image Text Extractor")

btn_extract = tk.Button(root, text="Select Image", command=extract_text)
btn_extract.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

text_output = tk.Text(root, height=10, width=50)
text_output.pack(padx=10, pady=10)
text_output.config(state=tk.DISABLED)  # Disable editing of text output

root.mainloop()
