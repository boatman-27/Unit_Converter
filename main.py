import pandas as pd

Area_Units = {
            "1": "Square kilometer",
            "2": "Square meter",
            "3": "Square mile",
            "4": "Square yard",
            "5": "Square foot",
            "6": "Square inch",
            "7": "Hectare",
            "8": "Acre"
        }

Data_Transfer_Rate_Units = {
            "1": "Bit per second",
            "2": "Kilobit per second",
            "3": "Kilobyte per second",
            "4": "Kibibit per second",
            "5": "Megabit per second",
            "6": "Megabyte per second",
            "7": "Mebibit per second",
            "8": "Gigabit per second",
            "9": "Gigabyte per second",
            "10": "Gibibit per second",
            "11": "Terabit per second",
            "12": "Terabyte per second",
            "13": "Tebibit per second",           
        }

Energy_Units = {
            "1": "Joule",
            "2": "Kilojoule",
            "3": "Gram calorie",
            "4": "Kilocalorie",
            "5": "Watt hour",
            "6": "Kilowatt hour",
            "7": "Electronvolt",
            "8": "British thermal unit",
            "9": "US therm",
            "10": "Foot-pound",
}

Frequency_Units = {
            "1": "Hertz",
            "2": "Kilohertz",
            "3": "Megahertz",
            "4": "Gigahertz",
}

Fuel_Ecconomy_Units = {
            "1": "Miles per gallon",
            "2": "Miles per gallon (Imperial)",
            "3": "Kilometer per liter",
            "4": "Liter per 100 kilometers",
}

Length_Units = {
            "1": "Kilometre",
            "2": "Meter",
            "3": "Centimeter",
            "4": "Millimetre",
            "5": "Micrometres",
            "6": "Nanometre",
            "7": "Mile",
            "8": "Yard",
            "9": "Foot",
            "10": "Inch",
            "11": "Nautical mile",
}

Mass_Units = {
            "1": "Tonne",
            "2": "Kilogram",
            "3": "Gram",
            "4": "Milligram",
            "5": "Microgram",
            "6": "Imperial ton",
            "7": "US ton",
            "8": "Stone",
            "9": "Pound",
            "10": "Ounce",
}

Plane_Angle_Units = {
            "1": "Arcsecond",
            "2": "Degree",
            "3": "Gradian",
            "4": "Milliradian",
            "5": "Minute of arc",
            "6": "Radian",
}

Pressure_Units = {
            "1": "Bar",
            "2": "Pascal",
            "3": "Pound per square inch",
            "4": "Standard atmosphere",
            "5": "Torr",
}

Speed_Units = {
            "1": "Mile per hour",
            "2": "Foot per second",
            "3": "Meter per second",
            "4": "Kilometer per hour",
            "5": "Knot",
}

Temperature_Units = {
            "1": "Degree Celsius",
            "2": "Fahrenheit",
            "3": "Kelvin",
}

Time_Units = {
            "1": "Nanosecond",
            "2": "Microsecond",
            "3": "Millisecond",
            "4": "Second",
            "5": "Minute",
            "6": "Hour",
            "7": "Day",
            "8": "Week",
            "9": "Month",
            "10": "Calendar year",
            "11": "Decade",
            "12": "Century",
}

Volume_Units = {
            "1": "US liquid gallon",
            "2": "US liquid quart",
            "3": "US liquid pint",
            "4": "US legal cup",
            "5": "Fluid ounce",
            "6": "US tablespoon",
            "7": "US teaspoon",
            "8": "Cubic meter",
            "9": "Liter",
            "10": "Milliliter",
            "11": "Imperial gallon",
            "12": "Imperial quart",
            "13": "Imperial pint",
            "14": "Imperial cup",
            "15": "Imp. fluid ounce",
            "16": "Imperial tablespoon",
            "17": "Imperial teaspoon",
            "18": "Cubic foot",
            "19": "Cubic inch",
}

def Unit_Categories():
    while True:
        print("Please enter the number corresponding to the unit category:")
        print("1. Area")
        print("2. Data Transfer Rate")
        print("3. Digital Energy")
        print("4. Frequency")
        print("5. Fuel Economy")
        print("6. Length")
        print("7. Mass")
        print("8. Plane Angle")
        print("9. Pressure")
        print("10. Speed")
        print("11. Temperature")
        print("12. Time")
        print("13. Volume")

        choice = input("Your choice: ")
        
        match choice:
            case "1":
                print("You have chosen the category of units that are used for Area conversion.")
                file_path = 'area_conversion_factors.csv'
                Conversions(Area_Units, file_path)
                break
            case "2":
                print("You have chosen the category of units that are used for Data Transfer Rate conversion.")
                file_path = 'data_transfer_conversion_factors.csv'
                Conversions(Data_Transfer_Rate_Units, file_path)
                break
            case "3":
                print("You have chosen the category of units that are used for Digital Energy conversion.")
                file_path = 'energy_conversion_factors.csv'
                Conversions(Energy_Units, file_path)
                break
            case "4":
                print("You have chosen the category of units that are used for Frequency conversion.")
                file_path = 'frequency_conversion_factors.csv'
                Conversions(Frequency_Units, file_path)
                break
            case "5":
                print("You have chosen the category of units that are used for Fuel Economy conversion.")
                file_path = 'fuel_conversion_factors.csv'
                Conversions(Fuel_Ecconomy_Units, file_path)
                break
            case "6":
                print("You have chosen the category of units that are used for Length conversion.")
                file_path = 'length_conversion_factors.csv'
                Conversions(Length_Units, file_path)
                break
            case "7":
                print("You have chosen the category of units that are used for Mass conversion.")
                file_path = 'mass_conversion_factors.csv'
                Conversions(Mass_Units, file_path)
                break
            case "8":
                print("You have chosen the category of units that are used for Plane Angle conversion.")
                file_path = 'angle_conversion_factors.csv'
                Conversions(Plane_Angle_Units, file_path)
                break
            case "9":
                print("You have chosen the category of units that are used for Pressure conversion.")
                file_path = 'pressure_conversion_factors.csv'
                Conversions(Pressure_Units, file_path)
                break
            case "10":
                print("You have chosen the category of units that are used for Speed conversion.")
                file_path = 'speed_conversion_factors.csv'
                Conversions(Speed_Units, file_path)
                break
            case "11":
                print("You have chosen the category of units that are used for Temperature conversion.")
                file_path = ''
                Conversions(Temperature_Units, file_path)
                break
            case "12":
                print("You have chosen the category of units that are used for Time conversion.")
                file_path = 'time_conversion_factors.csv'
                Conversions(Time_Units, file_path)
                break
            case "13":
                print("You have chosen the category of units that are used for Volume conversion.")
                file_path = 'volume_conversion_factors.csv'
                Conversions(Volume_Units, file_path)
                break
            case _:
                print("Invalid choice. Please enter a valid number.")

def Conversions(Convserion_Units, csv_path):
    while True:
        print("Available Area Units:")
        for key, value in Convserion_Units.items():
            print(f"{key}. {value}")

        choice_1 = input("Please select an option from the ones stated above: ")
        choice_2 = input("Please select another option from the ones stated above (different from the one you picked before): ")

        if choice_1 == choice_2 or choice_1 not in Convserion_Units or choice_2 not in Convserion_Units:
            print("Invalid selection. Please choose different and valid options.")
            continue
        
        unit_1 = Convserion_Units[choice_1]
        unit_2 = Convserion_Units[choice_2]
    
        converting_process(unit_1, unit_2, csv_path)
        
        choice = input("Would you like to do another conversion or try another category (y/n/o): ").lower()
        if choice == 'y':
            continue
        elif choice == 'o':
            Unit_Categories()
            break
        else:
            break     

def converting_process(unit_1, unit_2, csv_path):
    conversions = pd.read_csv(csv_path)
        
    input_value = float(input(f"Enter the value you want to convert from {unit_1} to {unit_2}: "))
    converted_input = (conversions.loc[(conversions['unit_from'] == unit_1) & (conversions['unit_to'] == unit_2), 'factor'].values[0]) * input_value
        
    print(f"{input_value} {unit_1} is equal to {converted_input} {unit_2}")
    
def main():
    print("Welcome to the Unit Conversion Program!")
    Unit_Categories()
    print("Thank you for using!")
    
main()