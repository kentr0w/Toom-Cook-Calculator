import logging
import time
from BigNumber import BigNumber
from BigNumber import preparing


class ToomCookCalculator(object):
    def __init__(self, first_num, second_num):
        self.init_logging()
        logging.info("First number = {}".format(first_num.number))
        logging.info("Second number = {}".format(second_num.number))
        self.radix_length = max(len(first_num.number), len(second_num.number))//3 + 1
        self.result_sign = not (first_num.sign ^ second_num.sign)
        self.first_num = self.prepare(first_num)
        self.first_num.sign = True
        self.second_num = self.prepare(second_num)
        self.second_num.sign = True
        logging.info("Radix lenght = {}".format(self.radix_length))

    def init_logging(self):
        logging.basicConfig(filename='logs.log', level=logging.DEBUG)

    def prepare(self, num):
        max_len = max(self.radix_length * 3, 5)
        if len(num.number) < max_len:
            num.number = "0"*(max_len-len(num.number)) + num.number
        return num

    def write_logs(self, text, list_to_write):
        logging.info(text + '   '.join(list(map(lambda x: preparing(x), list_to_write))))

    def calculate(self):
        start = time.time()
        logging.info("Starting calculate: ")
        split_first_num = self.init_polynomial(self.first_num)
        self.write_logs("First  number after spliting step: ", list(map(lambda num: num.number, split_first_num)))
        split_second_num = self.init_polynomial(self.second_num)
        self.write_logs("Second snumber after spliting step: ", list(map(lambda num: num.number, split_second_num)))
        first_polynom = self.evaluation(split_first_num)
        self.write_logs("First number after evaluation ster: ", list(map(lambda num: num.number, first_polynom)))
        second_polynom = self.evaluation(split_second_num)
        self.write_logs("First number after evaluation ster: ", list(map(lambda num: num.number, second_polynom)))
        mult_pol = self.mult_polynom(first_polynom, second_polynom)
        self.write_logs("Polynom after pointwise multiplication: ", list(map(lambda num: num.number, mult_pol)))
        product_pol = self.interpolation(mult_pol)
        self.write_logs("Coefficients after interpolation: ", list(map(lambda num: num.number, product_pol)))
        answer = self.recomposition(product_pol)
        end = time.time()
        logging.info("Answer is: " + answer.number)
        logging.info("Spent time: " + str(end - start))
        return answer

    def init_polynomial(self, number):
        str = number.number
        if len(str) < 3:
            str = "0"*(3-len(str))+str
        chunks = len(str)
        chunk_size = self.radix_length
        split_num = []
        for i in range(3):
            delta_split = chunks - chunk_size*i
            if delta_split < chunk_size:
                delta_number = str[0:delta_split]
            else:
                delta_number = str[delta_split-chunk_size: delta_split]
            num = BigNumber(delta_number)
            num.sign = True
            split_num.append(num)
        return split_num

    def evaluation(self, split_num):
        p = split_num[0].addition(split_num[2])
        p0 = split_num[0]
        p1 = p.addition(split_num[1])
        pm1 = p.subtraction(split_num[1])
        pm2 = pm1.addition(split_num[2]).multiplication(BigNumber("2")).subtraction(split_num[0])
        pi = split_num[2]
        return [p0, p1, pm1, pm2, pi]

    def mult_polynom(self, first_polynom, second_polynom):
        return list(map(lambda x, y: x.multiplication(y), first_polynom, second_polynom))

    def interpolation(self, mult_pol):
        r0 = mult_pol[0]
        r4 = mult_pol[4]
        r3 = mult_pol[3].subtraction(mult_pol[1]).division(3)
        r1 = mult_pol[1].subtraction(mult_pol[2]).division(2)
        r2 = mult_pol[2].subtraction(mult_pol[0])
        r3 = r2.subtraction(r3).division(2).addition(mult_pol[4]).addition(mult_pol[4])
        r2 = r2.addition(r1).subtraction(r4)
        r1 = r1.subtraction(r3)
        return [r0, r1, r2, r3, r4]

    def recomposition(self, product_pol):
        result = BigNumber("0")
        for i in range(0, len(product_pol)):
            product_pol[i].number += "0"*self.radix_length*i
            result = result.addition(product_pol[i])
        result = result
        if not self.result_sign and result.number != "0":
            result.number = "-" + result.number
        return result

