def convertCelsiusToKelvin(celsius):


    Kelvin = celsius +273.15

    return round(Kelvin, 2)

def convertCelsiusToFahrenheit(celsius):


    Fahrenheit = celsius * 9 / 5 + 32

    return round(Fahrenheit, 2)

def convertFahrenheitToCelsius(fahrenheit):


    Clsius = (fahrenheit-32) * 5 / 9

    return round(Clsius, 2)

def convertFahrenheitToKelvin(fahrenheit):


    Kelvin = fahrenheit + 459.67 * 5 / 9

    return round(Kelvin, 2)

def convertKelvinToCelsius(kelvin):

    Clsius = kelvin - 273.15

    return round(Clsius, 2)

def convertKelvinToFahrenheit(kelvin):

    Fahrenheit = kelvin * 9 / 5 - 459.67

    return round(Fahrenheit, 2)
