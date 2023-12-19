import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if from_unit == "Celcius":
            if to_unit == "Fahrenheit":
                result = (temperature * 9/5) + 32
            elif to_unit == "Reamur":
                result = temperature * 4/5
            elif to_unit == "Kelvin":
                result = temperature + 273.15
            else:
                result = temperature  # Same unit, no conversion needed
        elif from_unit == "Fahrenheit":
            if to_unit == "Celcius":
                result = (temperature - 32) * 5/9
            elif to_unit == "Reamur":
                result = (temperature - 32) * 4/9
            elif to_unit == "Kelvin":
                result = (temperature - 32) * 5/9 + 273.15
            else:
                result = temperature  # Same unit, no conversion needed
        elif from_unit == "Reamur":
            if to_unit == "Celcius":
                result = temperature * 5/4
            elif to_unit == "Fahrenheit":
                result = temperature * 9/4 + 32
            elif to_unit == "Kelvin":
                result = temperature * 5/4 + 273.15
            else:
                result = temperature  # Same unit, no conversion needed
        elif from_unit == "Kelvin":
            if to_unit == "Celcius":
                result = temperature - 273.15
            elif to_unit == "Fahrenheit":
                result = (temperature - 273.15) * 9/5 + 32
            elif to_unit == "Reamur":
                result = (temperature - 273.15) * 4/5
            else:
                result = temperature  # Same unit, no conversion needed

        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Create widgets
label_temperature = ttk.Label(root, text="Enter Temperature:")
entry_temperature = ttk.Entry(root, width=10)
label_from = ttk.Label(root, text="From:")
combo_from = ttk.Combobox(root, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
label_to = ttk.Label(root, text="To:")
combo_to = ttk.Combobox(root, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
result_label = ttk.Label(root, text="Result: ")

# Place widgets in the grid
label_temperature.grid(row=0, column=0, padx=5, pady=5)
entry_temperature.grid(row=0, column=1, padx=5, pady=5)
label_from.grid(row=1, column=0, padx=5, pady=5)
combo_from.grid(row=1, column=1, padx=5, pady=5)
label_to.grid(row=2, column=0, padx=5, pady=5)
combo_to.grid(row=2, column=1, padx=5, pady=5)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
