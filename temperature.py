TEMPERATURE_SCALES = ("fahrenheit","kelvin","celsius")

def convert_to_celsius(degrees,source="fahrenheit"):
    '''convert celsius to fahrenheit or kelvin'''
    if source.lower() == "fahrenheit":
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"Don't know how to convert form {source}"