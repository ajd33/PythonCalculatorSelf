import unittest
from CsvReader.CsvReader import CsvReader, class_factory


class MyTestCase(unittest.TestCase):

    def test_return_data_as_objects(self):
        value1 = self.csv_reader.return_data_as_class('Value 1')
        value2 = self.csv_reader.return_data_as_class('Value 2')
        result = self.csv_reader.return_data_as_class('Result')

        self.assertIsInstance(value1, list)
        self.assertIsInstance(value2, list)
        self.assertIsInstance(result, list)

        test_class_column1 = class_factory('Value 1', self.csv_reader.data[0])
        test_class_column2 = class_factory('Value 2', self.csv_reader.data[0])
        test_class_column3 = class_factory('result', self.csv_reader.data[0])

        for value in value1:
            self.assertEqual(value.__name__, test_class_column1.__name__)

        for value in value2:
            self.assertEqual(value.__name__, test_class_column2.__name__)

        for value in result:
            self.assertEqual(value.__name__, test_class_column3.__name__)


if __name__ == '__main__':
    unittest.main()