import numpy as np
import math





"""
Given a parameter k we consider the sets of tick intervals centered around the current price b_s. b_s is fixed until
we reset liquidity provision. At that point we set b_s as the tick containing the current price.
The other ticks are indices based on b_s
"""
k = 600

b_s = 30000
"""
Find good k to 
"""
class Position:
    def __init__(self, b_s, lower_tick, upper_tick, liquidity_token_a, liquidity_token_b):
        self.b_s = b_s
        self.lower_tick = lower_tick
        self.upper_tick = upper_tick
        self.liquidity_token_a = liquidity_token_a
        self.liquidity_token_b = liquidity_token_b

contract = None
def get_current_position():
    lower_tick, upper_tick, liquidity_token_a, liquidity_token_b = None, None, None, None
    position = Position(lower_tick, upper_tick, liquidity_token_a, liquidity_token_b)
    return position


def withdraw_liquidity(position: Position):
    if position.liquidity_token_a > 0 or position.liquidity_token_b > 0:
        contract.widthdraw_liquidity(position)


def provide_liquidity(lower_tick, upper_tick, amount_token_a, amount_token_b):
    pass


def get_new_liquidity_range():
    pass

def reset_state():
    pass


prices = []
def get_percentage_change(prices):
    first_diff = np.diff(prices)
    return 100 * (first_diff / prices[:-1])

starting_price = 29000
prices = []
for j in range(10000):
    starting_price = starting_price + np.random.normal(0, 8)
    prices.append(starting_price)

#prices = [29000 + np.random.normal(0, 3) for x in range(10000)]

#prices = np.random.randint(29800, 31000, 1000)
#prices = [30002, 30000, 30002, 30001, 30005, 30007, 30002, 29998, 29999, 29999, 30000, 30001, 30002, 30001,  29998, 29999, 29999, 30000, 30005, 30008, 30007]

#train_model(prices[1:], np.diff(prices), 30, 1)



def reset_liquidity():
    """This function should reset some internals and call the reset strategy function.
    This function should allocate liquidity based on some transition probability given by the model."""
    position = get_current_position()
    withdraw_liquidity(position)
    get_new_liquidity_range()
    provide_liquidity(None, None, None, None)
    reset_state()

"""
Distributions over the space of bins are needed.
The simplest one is
"""
def uniform_lp(relative_ticks, liquidity):
    return [liquidity / len(relative_ticks) for x in range(len(relative_ticks))]


def to_reset():
    """Function containing the logic that determines the reset condition. This function does not need to know about
    the model, but it is "found" using the model"""
    pass

if to_reset():
    reset_liquidity()










