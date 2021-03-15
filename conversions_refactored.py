class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):

    if fromUnit == "C" and toUnit == "K":

        Kelvin = value + 273.15

        return round(Kelvin, 2)

    elif fromUnit == "C" and toUnit == "F":

        Fahrenheit = value * 9 / 5 + 32

        return round(Fahrenheit, 2)

    elif fromUnit == "K" and toUnit == "F":

        Fahrenheit = value * 9 / 5 - 459.67

        return round(Fahrenheit, 2)

    elif fromUnit == "K" and toUnit == "C":

        Celsius = value - 273.15

        return round(Celsius, 2)

    elif fromUnit == "F" and toUnit == "C":

        Celsius = (value - 32) * 5 / 9

        return round(Celsius, 2)

    elif fromUnit == "F" and toUnit == "K":

        Kelvin = value + 459.67 * 5 / 9

        return round(Kelvin, 2)

    elif fromUnit == "Mi" and toUnit == "YD":

        YD = value * 1760.0

        return round(YD, 2)
    elif fromUnit == "Mi" and toUnit == "M":

        M = value / 0.00062137

        return round(M, 2)
    elif fromUnit == "YD" and toUnit == "Mi":
        Mi = value * 0.00056818

        return round(Mi, 2)

    elif fromUnit == "YD" and toUnit == "M":

        M = value / 1.0936

        return round(M, 2)

    elif fromUnit == "M" and toUnit == "YD":

        YD = value * 1.0936

        return round(YD, 2)

    elif fromUnit == "M" and toUnit == "Mi":

        Mi = value * 0.00062137

        return round(Mi, 2)

    elif fromUnit == "C" or "F" or "K" or "" and toUnit == "M" or "Mi" or "YD" or "":
        raise ConversionNotPossible
    elif fromUnit == "M" or "Mi" or "YD" or "" and toUnit == "C" or "F" or "K" or "":
        raise ConversionNotPossible
