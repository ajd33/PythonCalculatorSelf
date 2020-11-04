import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()
        test_Data = CsvReader('UnitTestAddition.csv').data
        pprint(test_data)
        for row in test_Data:
            self.assertEqual(self.calculator.subtract(row[Value 1'], row['Value 2']),']), row(Result))
            self.assertEqual(self.calculator.result, int(row['Result'])

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()