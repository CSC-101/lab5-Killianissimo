import data
import lab5
import unittest




# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 3
    def test_time_add_1(self):
        time1 = data.Time(1,2,3)
        time2 = data.Time(1,2,3)
        testResult = lab5.time_add(time1, time2)
        self.assertEqual(testResult, data.Time(2,4,6))
    def test_time_add_2(self):
        time1 = data.Time(1,50,50)
        time2 = data.Time(1,40,30)
        testResult = lab5.time_add(time1, time2)
        self.assertEqual(testResult, data.Time(3,31,20))

    # Part 4
    def test_is_descending_1(self):
        input = [5,3,2]
        expected = True
        testResult = lab5.is_descending(input)
        self.assertEqual(expected, testResult)
    def test_is_descending_2(self):
        input = [5,3,6]
        expected = None
        testResult = lab5.is_descending(input)
        self.assertEqual(expected, testResult)

    # Part 5
    def test_largest_between_1(self):
        input1 = [1,2,3,4,5,6]
        input2 = 2
        input3 = 5
        expected = 6
        testResult = lab5.largest_between(input1, input2, input3)
        self.assertEqual(expected, testResult)
    def test_largest_between_2(self):
        input1 = [3,6,1,16,1,23]
        input2 = 2
        input3 = 5
        expected = 16
        testResult = lab5.largest_between(input1, input2, input3)
        self.assertNotEqual(expected, testResult)

    # Part 6
    def test_furthest_from_origin_1(self):
        input = [data.Point(1,2),data.Point(3,-4)]
        expected = 1
        testResult = lab5.furthest_from_origin(input)
        self.assertEqual(expected, testResult)
    def test_furthest_from_origin_2(self):
        input = []
        expected = None
        testResult = lab5.furthest_from_origin(input)
        self.assertEqual(expected, testResult)





if __name__ == '__main__':
    unittest.main()
