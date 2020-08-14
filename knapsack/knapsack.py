#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    print(capacity)
    items.sort(key=lambda x: x.value, reverse=True)
    print(items[0], items)
    # would be better if we sorted by value/weight ratio...
    sack = []
    cur_weight = 0

    for i in range(len(items)):
        if cur_weight + items[i].size <= capacity:
            sack.append(items[i])
    return sack

# BRUTE FORCE METHOD
from itertools import combinations

def kapsack_brute_force(items, weight_limit):
    all_combos = []
    for i in range(1, len(items)+1):
        list_of_combos = list(combinations(items, i))
        for combo in list_of_combos:
            all_combos.append(combo)

    max_value = -1
    for combo in all_combos:
        value = 0
        weight = 0
        for item in combo:
            value += item.value
            weight += item.size
        if weight <= weight_limit:
            if value > max_value:
                max_value = value
                best_combo = combo

    return best_combo

# Greedy solution:
# Quick and dirty, but fairly good result. PROBABLY won't give the BEST result
def knapsack_greedy(items, limit):
    for i in items:
        print(i)
        # creating a key in item called efficiency
        setattr(i, 'efficiency', i.value / i.size)

    items.sort(keys=lambda x: x.efficiency, reverse=True)

    sack = []
    size = 0
    for i in items:
        size += i.size
        if size > limit:
            return sack
        else:
            sack.append(i)

    return sack

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
          data = line.rstrip().split()
          items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')


