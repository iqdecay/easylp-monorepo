import numpy as np

from src.model.utils import get_tick_from_price


def get_transition_probabilities(prices, percentage_differences, tau, alpha):
    ticks = np.array([get_tick_from_price(x) for x in prices])
    transitions = np.zeros(shape=(2 * tau + 1, 2 * tau + 1))
    transition = np.zeros(shape=2 * tau + 1)
    for j in range(0, len(prices), 3):
        initial_tick = ticks[j]
        states = ticks - initial_tick
        starting_state = states[j]
        current_price = prices[j]

        for k in range(j + 1, len(prices)):
            ending_state = states[k]
            if ending_state > tau or ending_state < -tau:
                reset_state()
                break
            transition[starting_state + tau] += 1
            if ending_state == 0:
                starting_state = ending_state
                continue
            transitions[tau + starting_state, tau + ending_state] += 1
            starting_state = ending_state
    for i in range(len(transitions)):
        if transition[i] > 0:
            transitions[i] = transitions[i] / transition[i]
    # transitions = transitions / transition
    for i in range(len(transitions)):
        transitions[i, tau] = 1 - transitions[i, :].sum()
    return transitions
