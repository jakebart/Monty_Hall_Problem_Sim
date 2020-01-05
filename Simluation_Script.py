"""
A simulation of the Monty Hall problem
with the computer implementing a "stay" and "switch" strategy
0 for loss, 1 for winning door
"""

import random


def _set_up_list():  # initialize list to represent "doors"
    doors = [0, 0, 0]
    doors[random.randint(0, len(doors) - 1)] = 1
    return doors


def _switch_strat(curr_doors, choice, num_win):  # func for "switching" choice
    if curr_doors[choice] == 0:
        print("win")
        num_win[0] += 1
    else:
        print("loss")


def _stay_strat(curr_doors, choice, num_win):  # func for "stay" choice
    if curr_doors[choice] == 1:
        print("win")
        num_win[0] += 1
    else:
        print("loss")


def _reveal_single_door(door_list, choice):  # Used for output of one losing door
    for i in range(len(door_list)):
        if door_list[i] != 1 and i != choice:
            return i
    return None


num_sim: int = 10000  # num times to play game
num_win_switch = [0]
num_win_stay = [0]

for _ in range(num_sim):
    game_options = _set_up_list()
    cpu_choice = random.randint(0, len(game_options)-1)

    print("cpu choice:", str(cpu_choice))

    revealed_num = _reveal_single_door(game_options, cpu_choice)

    print("Door revealed: ", revealed_num)

    print("switch:")
    _switch_strat(game_options, cpu_choice, num_win_switch)
    print("stay:")
    _stay_strat(game_options, cpu_choice, num_win_stay)
    print("\n")


print("Wins with staying: % d or % 3f chance of winning\nWins with switching: % d or % 3f chance of winning"
      % (num_win_stay[0], num_win_stay[0]/num_sim, num_win_switch[0], num_win_switch[0]/num_sim))
