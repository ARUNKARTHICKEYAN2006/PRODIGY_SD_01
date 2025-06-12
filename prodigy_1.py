def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature():
    print("Temperature Converter")
    print("Enter the temperature unit you have:")
    print("C - Celsius")
    print("F - Fahrenheit")
    print("K - Kelvin")

    unit = input("Enter the unit (C/F/K): ").upper()

    if unit == 'C':
        temp = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        print("Fahrenheit: {:.2f} °F".format(f))
        print("Kelvin: {:.2f} K".format(k))
        
    elif unit == 'F':
        temp = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(temp)
        print("Celsius: {:.2f} °C".format(c))
        print("Kelvin: {:.2f} K".format(k))

    elif unit == 'K':
        temp = float(input("Enter temperature in Kelvin: "))
        c = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(temp)
        print("Celsius: {:.2f} °C".format(c))
        print("Fahrenheit: {:.2f} °F".format(f))
        
    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "__main__":
    convert_temperature()
