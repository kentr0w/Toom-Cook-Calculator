import math
from copy import deepcopy


class BigNumber(object):
    def __init__(self, num):
        if num[0] == '-':
            self.number = num[1:len(num)]
            self.sign = False
        else:
            self.number = num
            self.sign = True
   
    def addition(self, another_num):
        f = deepcopy(self)
        s = deepcopy(another_num)
        if f.sign != s.sign:
            if f.sign:
                s.sign = True
                return f.subtraction(s)
            else:      
                f.sign = True
                return s.subtraction(f)
        str1 = preparing(f.number)
        str2 = preparing(s.number)
        if len(str1) > len(str2): 
            temp = str1 
            str1 = str2 
            str2 = temp
        str3 = "" 
        n1 = len(str1) 
        n2 = len(str2) 
        diff = n2 - n1 
        carry = 0
        for i in range(n1-1, -1, -1): 
            _sum = Ord(str1[i]) + Ord(str2[i+diff]) + carry
            str3 = str3+str(_sum % 10)
            carry = _sum//10
        for i in range(n2-n1-1, -1, -1): 
            _sum = Ord(str2[i]) + carry
            str3 = str3+str(_sum % 10)
            carry = _sum//10
        if carry:
            str3 += chr(carry + 48)
        str3 = str3[::-1] 
        result = BigNumber(preparing(str3))
        result.sign = f.sign
        return result

    def subtraction(self, another_num):
        s = deepcopy(another_num)
        if self.sign != s.sign:
            if self.sign:
                s.sign = True
            else:
                s.sign = False
            return self.addition(s)
        if not self.sign:
            s.sign = True
            f = deepcopy(self)
            f.sign = True
            return s.subtraction(f)
        str1 = preparing(self.number)
        str2 = preparing(s.number)
        sign = True
        if is_smaller(str1, str2):
            temp = str1
            str1 = str2
            str2 = temp
            sign = False
        str3 = ""
        n1 = len(str1)
        n2 = len(str2)
        str1 = str1[::-1]
        str2 = str2[::-1]
        carry = 0
        for i in range(n2):
            sub = Ord(str1[i])-Ord(str2[i])-carry
            if sub < 0:
                sub = sub + 10
                carry = 1
            else:
                carry = 0
            str3 = str3+str(sub)
        for i in range(n2, n1):
            sub = Ord(str1[i]) - carry
            if sub < 0:
                sub = sub + 10
                carry = 1
            else:
                carry = 0
            str3 = str3+str(sub)
        str3 = str3[::-1]
        result = BigNumber(preparing(str3))
        result.sign = sign
        return result

    def multiplication(self, another_num):
        str1 = self.number
        str2 = another_num.number
        len1 = len(str1)
        len2 = len(str2)
        result = [0] * (len1 + len2)
        i_n1 = 0
        for i in range(len1 - 1, -1, -1):
            carry = 0
            n1 = Ord(str1[i])
            i_n2 = 0
            for j in range(len2 - 1, -1, -1):
                n2 = Ord(str2[j])
                _sum = n1 * n2 + result[i_n1 + i_n2] + carry
                carry = _sum // 10
                result[i_n1 + i_n2] = _sum % 10
                i_n2 += 1
            if carry > 0:
                result[i_n1 + i_n2] += carry
            i_n1 += 1
        i = len(result) - 1
        while i >= 0 and result[i] == 0:
            i -= 1
        if i == -1:
            return BigNumber("0")
        result_str = ""
        while i >= 0:
            result_str += chr(result[i] + 48)
            i -= 1
        answer = BigNumber(result_str)
        answer.sign = not(self.sign ^ another_num.sign)
        return answer

    def division(self, divisor):
        num = self.number
        ans = ""
        idx = 0
        temp = Ord(num[idx])
        while temp < divisor and idx < len(num) - 1:
            temp = (temp * 10) + Ord(num[idx+1]) 
            idx += 1 
        idx += 1
        while (len(num)) > idx:
            ans += chr(math.floor(temp // divisor) + ord('0')) 
            temp = (temp % divisor) * 10 + Ord(num[idx]) 
            idx += 1 
        ans += chr(math.floor(temp // divisor) + ord('0'))
        if len(ans) == 0:
            return BigNumber("0")
        result = BigNumber(preparing(ans))
        result.sign = self.sign
        return result


def preparing(str_num):
    idx = 0
    while str_num[idx] == '0' and idx < len(str_num)-1:
        idx += 1
    return str_num[idx:]


def Ord(symbol):
    return ord(symbol) - ord('0')


# function for find difference of larger numbers
def is_smaller(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    max_len = max(n1, n2)
    str3 = "0"*(max_len-n1) + str1
    str4 = "0"*(max_len - n2) + str2
    for i in range(n1):
        if str3[i] < str4[i]:
            return True
        elif str3[i] > str4[i]:
            return False
    return False
