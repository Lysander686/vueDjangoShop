from random import choice

from django.test import TestCase


# Create your tests here.


def generate_code():
    """
    生成四位数字的验证码
    """
    seeds = "1234567890"
    random_str = []
    for i in range(4):
        random_str.append(choice(seeds))

    return "".join(random_str)


print(generate_code())
