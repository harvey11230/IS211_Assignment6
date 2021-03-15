import unittest
import conversions
import conversions_refactored


class ConversionFunctions(unittest.TestCase):

    celsius = [300, 400, -500, 600, 700.20]
    fahrenheit = [500, 600, -700, 800, 900.90]
    kelvin = [700, 800, -900, 1000, 1100.10]

    def test_convertCelsiusToKelvin(self):
        #C +273.15 = K

        expected = [573.15, 673.15, -226.85, 873.15, 973.35]
        actual = []
        for i in ConversionFunctions.celsius:
            actual.append(conversions.convertCelsiusToKelvin(i))

        self.assertEqual(expected, actual, msg="Celsius to Kelvin conversion failed")

    def test_convertCelsiusToFahrenheit(self):
        #C*9/5 + 32 = F

        expected = [572.00, 752.00, -868, 1112, 1292.36]
        actual = []
        for i in ConversionFunctions.celsius:
            actual.append(conversions.convertCelsiusToFahrenheit(i))

        self.assertEqual(expected, actual, msg="Celsius to Fahrenheit conversion failed")


    def test_FahrenheitToCelsius(self):
        #F-32*5/9 = C

        expected = [260.0, 315.56, -406.67, 426.67, 482.72]
        actual = []
        for i in ConversionFunctions.fahrenheit:
            actual.append(conversions.convertFahrenheitToCelsius(i))

        self.assertEqual(expected, actual, msg=" Fahrenheit to Celsius conversion failed")

    def test_FahrenheitToKelvin(self):
        # F + 459.67 * 5 / 9 = K

        expected = [755.37, 855.37, -444.63, 1055.37, 1156.27]
        actual = []

        for i in ConversionFunctions.fahrenheit:
            actual.append(conversions.convertFahrenheitToKelvin(i))

        self.assertEqual(expected, actual, msg=" Fahrenheit to Kelvin conversion failed")

    def test_KelvinToCelsius(self):
        # K -273.15 = C
        expected = [426.85, 526.85, -1173.15, 726.85, 826.95]
        actual = []

        for i in ConversionFunctions.kelvin:
            actual.append(conversions.convertKelvinToCelsius(i))

        self.assertEqual(expected, actual, msg=" Kelvin to Celsius conversion failed")

    def test_KelvinToFahrenheit(self):
        # kelvin * 9 / 5 - 459.67 = F
        expected = [800.33, 980.33, -2079.67, 1340.33, 1520.51]
        actual = []

        for i in ConversionFunctions.kelvin:
            actual.append(conversions.convertKelvinToFahrenheit(i))

        self.assertEqual(expected, actual, msg=" Kelvin to Fahrenheit conversion failed")


    def test_convert(self):

        test_case = [('C', 'K', 100), ('C', 'F', 200), ('K', 'C', 300), ('K', 'F', 400), ('F', 'C', 500), ('F', 'K', 600), ('Mi', 'YD', 700), ('Mi', 'M', 800), ('YD', 'Mi', 900), ('YD', 'M', 1000), ('M', 'Mi', 1100), ('M', 'YD', 1200)]
        expected = [373.15, 392.00, 26.85, 260.33, 260.00, 855.37, 1232000.00, 1287477.67, 0.51, 914.41, 0.68, 1312.32]
        result =[]
        for items in test_case:
            result.append(conversions_refactored.convert(items[0], items[1], items[2]))
        self.assertEqual(expected, result, msg="Conversation failed")


if __name__ == '__main__':
    unittest.main()