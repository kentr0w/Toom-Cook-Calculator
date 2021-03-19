import unittest
from calculator import ToomCookCalculator
from BigNumber import BigNumber
import random


class ToomCalculatorTest(unittest.TestCase):

    def test_from_wiki(self):
        first = BigNumber("1234567890123456789012")
        second = BigNumber("987654321987654321098")
        calculator = ToomCookCalculator(first, second)
        result = calculator.calculate()
        self.assertEqual(result.number, "1219326312467611632493760095208585886175176")

    def test_random_value(self):
        for i in range(100):
            f = random.randint(1, 1000)
            s = random.randint(1, 1000)
            first = BigNumber(str(f))
            second = BigNumber(str(s))
            calculator = ToomCookCalculator(first, second)
            result = calculator.calculate()
            print("1 = " + str(f))
            print("2 = " + str(s))
            self.assertEqual(result.number, str(f*s))

    def test_extreme(self):
        extreme = ["-1", "0", "00", "1", "01"]
        for i in range(len(extreme)):
            for j in range(len(extreme)):
                first = BigNumber(extreme[i])
                second = BigNumber(extreme[j])
                calculator = ToomCookCalculator(first, second)
                result = calculator.calculate()
                print("1 = " + extreme[i])
                print("2 = " + extreme[j])
                self.assertEqual(result.number, str(int(extreme[i]) * int(extreme[j])))


if __name__ == "__main__":
    unittest.main()
