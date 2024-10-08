FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = input("Enter the temperature to convert: ")
result = temp.isnumeric()
if result == False:
    print("Invalid temperature. Please enter a numeric value.")
    exit()
temperature = int(temp)

temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

def convert_to_celsius(fahrenheit = 0):
    if temperature_type == "F":
        fahrenheit = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print("{0}°F is {1}°C".format(temperature, fahrenheit))
        return fahrenheit
        pass

def convert_to_fahrenheit(celsius = 0):
    if temperature_type == "C":
        celsius = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print("{0}°C is {1}°F".format(temperature, celsius))
        return celsius
        pass


convert_to_celsius()
convert_to_fahrenheit()
