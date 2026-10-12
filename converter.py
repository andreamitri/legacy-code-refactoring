class FahrenheitToCelsiusConverter:
    """Convert temperatures from Fahrenheit to Celsius."""

    def convert(self, fahrenheit):
        """Return the temperature in Celsius."""
        return (fahrenheit - 32) * 5 / 9


converter = FahrenheitToCelsiusConverter()
print(converter.convert(212))