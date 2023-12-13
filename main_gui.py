import tkinter as tk
from tkinter import font
import pandas as pd

def on_dropdown_change(event):
    selected_category = category_var.get()
    update_unit_dropdowns(selected_category)

def update_unit_dropdowns(selected_category):
    # Update the options of the unit dropdown menus based on the selected category
    unit_dropdown1['menu'].delete(0, 'end')
    unit_dropdown2['menu'].delete(0, 'end')

    units_for_category = units.get(selected_category, [])
    for unit in units_for_category:
        unit_dropdown1['menu'].add_command(label=unit, command=tk._setit(unit_var1, unit))
        unit_dropdown2['menu'].add_command(label=unit, command=tk._setit(unit_var2, unit))

def convert_units():
    input= entry.get()
    category = category_var.get()
    unit1 = unit_var1.get()
    unit2 = unit_var2.get()
    conversions(category, unit1, unit2, input)

def conversions(category, unit1, unit2, input):
    if unit1 == unit2:
        conversion_label.configure(text='Both units are the same, please change one of them. :)')
    else:
        match category:
            case 'Area':
                file_path = 'area_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Data Transfer Rate':
                file_path = 'data_transfer_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Digital Energy':
                file_path = 'energy_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Frequency':
                file_path = 'frequency_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Fuel Economy':
                file_path = 'fuel_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Length':
                file_path = 'length_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Mass':
                file_path = 'mass_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Plane Angle':
                file_path = 'angle_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Pressure':
                file_path = 'pressure_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Speed':
                file_path = 'speed_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Time':
                file_path = 'time_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Volume':
                file_path = 'volume_conversion_factors.csv'
                converting_process(category, unit1, unit2, file_path, input)
            case 'Temperature':
                Temperature_Conversion(category, unit1, unit2, input)
            case _:
                conversion_label.configure(text='Invalid choice. Please enter a valid number.')
                    
def converting_process(category, unit_1, unit_2, csv_path, input):
    conversions = pd.read_csv(csv_path)
    converted_input = (conversions.loc[(conversions['unit_from'] == unit_1) & (conversions['unit_to'] == unit_2), 'factor'].values[0]) * float(input)
    conversion_label.configure(text=f'{input} converted from {unit_1} to {unit_2} in Category {category} is {converted_input}')

def Temperature_Conversion(category, unit_1, unit_2, input):   
    conversion_functions = {
        ("Degree Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Degree Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Fahrenheit", "Degree Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Degree Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
    }
    conversion_function = conversion_functions.get((unit_1, unit_2))
    converted_input = conversion_function(float(input))
    print(converted_input)
    conversion_label.configure(text=f'{input} converted from {unit_1} to {unit_2} in Category {category} is {converted_input}')

window = tk.Tk(className='Unit Converter')
window.geometry('1200x600')

label_font = font.Font(weight="bold", size=36)

label = tk.Label(text="Unit Converter", font=label_font, fg="#a89b22", bg="#030945")
label.pack()

window.configure(bg='#030945')

categories = [
    "Area", "Data Transfer Rate", "Digital Energy", "Frequency",
    "Fuel Economy", "Length", "Mass", "Plane Angle",
    "Pressure", "Speed", "Temperature", "Time", "Volume"
]

units = {
    "Area": ["Square kilometer", "Square meter", "Square mile", "Square yard", "Square foot", "Square inch", "Hectare", "Acre"],
    "Data Transfer Rate": ["Bit per second", "Kilobit per second", "Kilobyte per second", "Kibibit per second",
                           "Megabit per second", "Megabyte per second", "Mebibit per second", "Gigabit per second",
                           "Gigabyte per second", "Gibibit per second", "Terabit per second", "Terabyte per second",
                           "Tebibit per second"],
    "Digital Energy": ["Joule", "Kilojoule", "Gram calorie", "Kilocalorie", "Watt hour", "Kilowatt hour", "Electronvolt",
                       "British thermal unit", "US therm", "Foot-pound"],
    "Frequency": ["Hertz", "Kilohertz", "Megahertz", "Gigahertz"],
    "Fuel Economy": ["Miles per gallon", "Miles per gallon (Imperial)", "Kilometer per liter", "Liter per 100 kilometers"],
    "Length": ["Kilometre", "Meter", "Centimeter", "Millimetre", "Micrometres", "Nanometre", "Mile", "Yard", "Foot",
               "Inch", "Nautical mile"],
    "Mass": ["Tonne", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial ton", "US ton", "Stone", "Pound", "Ounce"],
    "Plane Angle": ["Arcsecond", "Degree", "Gradian", "Milliradian", "Minute of arc", "Radian"],
    "Pressure": ["Bar", "Pascal", "Pound per square inch", "Standard atmosphere", "Torr"],
    "Speed": ["Mile per hour", "Foot per second", "Meter per second", "Kilometer per hour", "Knot"],
    "Temperature": ["Degree Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Nanosecond", "Microsecond", "Millisecond", "Second", "Minute", "Hour", "Day", "Week", "Month",
             "Calendar year", "Decade", "Century"],
    "Volume": ["US liquid gallon", "US liquid quart", "US liquid pint", "US legal cup", "Fluid ounce", "US tablespoon",
               "US teaspoon", "Cubic meter", "Liter", "Milliliter", "Imperial gallon", "Imperial quart", "Imperial pint",
               "Imperial cup", "Imp. fluid ounce", "Imperial tablespoon", "Imperial teaspoon", "Cubic foot", "Cubic inch"],
}

category_var = tk.StringVar()
unit_var1 = tk.StringVar()
unit_var2 = tk.StringVar()
input_var = tk.Variable()

dropdown_label = tk.Label(window, text="Select Category:", font=("Helvetica", 14), fg="white", bg="#030945")
dropdown_label.pack(pady=10)

category_dropdown = tk.OptionMenu(window, category_var, *categories, command=on_dropdown_change)
category_dropdown.pack(pady=10)
category_dropdown.config(font=("Helvetica", 14), bg="#030945", fg="white")
category_dropdown["menu"].config(bg="#030945", fg="white")

# First dropdown menu for units:
dropdown_label = tk.Label(window, text="Select Unit:", font=("Helvetica", 12), fg="white", bg="#030945")
dropdown_label.pack(pady=10)

unit_dropdown1 = tk.OptionMenu(window, unit_var1, "")
unit_dropdown1.pack(side=tk.LEFT, anchor='center')
unit_dropdown1.config(font=("Helvetica", 14), bg="#030945", fg="white")
unit_dropdown1["menu"].config(bg="#030945", fg="white")

# Second dropdown menu for units:
unit_dropdown2 = tk.OptionMenu(window, unit_var2, "")
unit_dropdown2.pack(side=tk.RIGHT, anchor='center')
unit_dropdown2.config(font=("Helvetica", 14), bg="#030945", fg="white")
unit_dropdown2["menu"].config(bg="#030945", fg="white")

# Button to trigger unit conversion
convert_button = tk.Button(window, text="Convert Units", command=convert_units, font=("Helvetica", 14), bg="#a89b22", fg="white")
convert_button.pack(pady=20)

# User Input
entry= tk.Entry(window, width= 40)
entry.focus_set()
entry.pack()

# Label to show Conversion
conversion_label = tk.Label(window, text="", font=("Helvetica", 14), fg="white", bg="#030945")
conversion_label.pack(pady=10)

# Initial update of the unit dropdowns
update_unit_dropdowns(categories[0])

window.mainloop()
