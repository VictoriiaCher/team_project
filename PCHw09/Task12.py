from functools import reduce


def amount_payment(payment):
    return reduce(lambda x, y: x + y , [i for i in filter(lambda x : x >= 0, payment)])