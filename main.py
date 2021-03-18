import re
import os
from BigNumber import BigNumber
from calculator import ToomCookCalculator

def main():
    if os.path.exists("logs.log"):
        os.remove("logs.log")
    first_number = input("Enter first number ")
    while is_input_incorrect(first_number):
        first_number = input("Enter first number again ")
    second_number = input("Enter second number ")
    while is_input_incorrect(second_number):
        second_number = input("Enter second number again ")
    first_big_num = BigNumber(first_number)
    second_big_num = BigNumber(second_number)
    toom_calculator = ToomCookCalculator(first_big_num, second_big_num)
    print("Answer is: " + toom_calculator.calculate().number)


def is_input_incorrect(text):
    return not re.match("^[-]?[0-9]*$", text) or len(text) <= 0


if __name__ == "__main__":
    main()
