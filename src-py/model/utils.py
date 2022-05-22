import math

def get_tick_from_price(price):
    return int(math.log(price, 1.0001))

