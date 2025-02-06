# -*- coding: utf-8 -*-
import os
import json
from heapq import heappush, heappop
from collections import deque

def load_memory():
    if os.path.exists('memory.json'):
        with open('memory.json', 'r') as f:
            memory = json.load(f)
    return {}

def save_memory(data):
    with open('memory.json', 'w') as f:
        json.dump(data, f)

def isValid(x, y, cur_map):
    if 0 <= x < len(cur_map) and 0 <= y < len(cur_map[0]):
        return cur_map[x][y] in ['goal', 'road']
    
def isRoad(x, y, cur_map):
    if 0 <= x < len(cur_map) and 0 <= y < len(cur_map[0]):
        return cur_map[x][y] == 'road'
    
def manhattan(x, y, goal):
    return abs(x - goal[0]) + abs(y - goal[1])

def close_coins(start, cur_coins, penalty_k):
    coins = set()
    for c in cur_coins:
        if manhattan(start[0], start[1], c) <= 10//penalty_k:
            coins.add(c)
    return coins

def bfs(cur_map, start, cur_coins, hazard_cells):
    visited = set()
    visited.add(start)

    moves = {
        'W': (0, -1), # Up
        'S': (0, 1), # Down
        'A': (-1, 0), # Left
        'D': (1, 0), # Right
    }

    queue = deque()
    queue.append((start, []))

    while queue:
        curr, path =  queue.popleft()

        for key, value in moves.items():
            new_x = curr[0] + value[0]
            new_y = curr[1] + value[1]

            if isRoad(new_x, new_y, cur_map) and (new_x, new_y) not in hazard_cells:
                if (new_x, new_y) in visited:
                    continue
                if (new_x, new_y) in cur_coins:
                    return path + [key]
                else:
                    queue.append(((new_x, new_y), path + [key]))
                    visited.add((new_x, new_y))

    return None

def aStarSearch(map, start, goal, hazard_cells, penalty_k, cur_coins):
    if start == goal: 
        return []
    
    open_set = []
    heappush(open_set,(0, 0, start, []))
    
    visited = set()
    visited.add(start)
    
    moves = {
        'W': (0, -1), # Up
        'S': (0, 1), # Down
        'A': (-1, 0), # Left
        'D': (1, 0), # Right
    }
    
    while open_set:
        _, g, (x,y), path = heappop(open_set)

        for key, value in moves.items():
            new_x = x + value[0]
            new_y = y + value[1]

            if isValid(new_x, new_y, map) and (new_x, new_y) not in hazard_cells:
                if (new_x, new_y) == goal:
                    return path + [key]
                else:
                    if (new_x, new_y) in visited:
                        continue

                    step_cost = penalty_k
                    if (new_x, new_y) in cur_coins:
                        step_cost -= 10
                    
                    new_g = g + step_cost
                    f = new_g + manhattan(new_x, new_y, goal) * penalty_k
                    heappush(open_set, (f, new_g, (new_x, new_y), path + [key]))
                    visited.add((new_x, new_y))
    return None

                
def logic_A(cur_map, cur_position, cur_coins, cur_car_positions, penalty_k):
    memory = load_memory()
    # Retrive goal position ( x, y ) from memory
    goal = memory.get('goal_pos', None)
    state = memory.get('state', 'coin')

    # If goal position is not in memory, find it and save it in memory
    if goal is None:
        for x in range(len(cur_map)):
            for y in range(len(cur_map[x])):
                if cur_map[x][y] == 'goal':
                    goal = (x, y)
                    memory['goal_pos'] = goal
                    save_memory(memory)
                    break
    
    moves = {
        'W': (0, -1), # Up
        'S': (0, 1), # Downhttps://ucsb.instructure.com/calendar
        'A': (-1, 0), # Left
        'D': (1, 0), # Right
    }

    # Check for possible future car positions
    hazard_cells = set()
    for car in cur_car_positions:
        for move in moves.values():
            new_x = car[0] + move[0]
            new_y = car[1] + move[1]
            if isValid(new_x, new_y, cur_map):
                hazard_cells.add((new_x, new_y))
    
    closest_coins = close_coins(cur_position, cur_coins, penalty_k)
    if closest_coins is None or len(closest_coins) == 0:
        state = 'goal'
        memory['state'] = 'goal'
        save_memory(memory)
    else:
        state = 'coin'
        memory['state'] = 'coin'
        save_memory(memory)

    if state == 'coin':
        path = bfs(cur_map, cur_position, closest_coins, hazard_cells)

    if state == 'goal':
        path = aStarSearch(cur_map, cur_position, goal, hazard_cells, penalty_k, cur_coins)

    if path is None or len(path) == 0:
        return 'I'
    else:
        return path[0]x