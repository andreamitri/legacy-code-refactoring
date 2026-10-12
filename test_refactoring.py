
import unittest

from converter import FahrenheitToCelsiusConverter
from discount import calculate_discounted_total
from process_order import calculate_total, apply_discount


class TestRefactoring(unittest.TestCase):

    def test_converter(self):
        converter = FahrenheitToCelsiusConverter()
        self.assertEqual(converter.convert(212), 100)
        self.assertEqual(converter.convert(32), 0)

    def test_discount(self):
        self.assertEqual(calculate_discounted_total(6000), 5400)

    def test_no_discount(self):
        self.assertEqual(calculate_discounted_total(5000), 5000)

    def test_vip_discount(self):
        self.assertEqual(apply_discount(100, "VIP"), 80)

    def test_no_vip_discount(self):
        self.assertEqual(apply_discount(100, ""), 100)

    def test_calculate_total(self):
        class Item:
            def __init__(self, price, qty):
                self.price = price
                self.qty = qty

        items = [Item(100, 2), Item(50, 1)]
        self.assertEqual(calculate_total(items), 250)


if __name__ == "__main__":
    unittest.main()
