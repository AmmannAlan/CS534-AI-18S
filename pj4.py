import xlrd
import numpy as np
import random
import matplotlib.pyplot as plt

def open_file():
    data = xlrd.open_workbook('CS 534 map for assignment 4 .xlsx')
    table = data.sheet_by_name('Sheet1')
    nrows = table.nrows
    colnames = table.row_values(0)
    list =[]
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        if row:
            app = []
            for i in range(len(colnames)):
                if row[i] != 'X':
                    app.append(row[i])
            if app:
                list.append(app)
            else:
                break
    return list

def set_start(start_map, value_goal, value_fall, value_giveup, max_x, max_y):
    all_value = {}
    for i in range(len(start_map)):
        for j in range(len(start_map[0])):
            if start_map[i][j] == '':
                all_value[10 * i + j] = [0, 0, 0, 0, value_giveup]
            elif start_map[i][j] == 'P':
                all_value[10 * i + j] = value_fall
            else:
                all_value[10 * i + j] = value_goal
    return all_value

def start_point(all_value):
    n=[]
    for k, v in all_value.items():
        if type(v) == list:
            n.append(k)
    key = random.choice(n)
    return key

def SARSA(all_value, key, epsilon, alpha, move_cost, gamma):
    out = 0
    new_key = 0
    value = 0
    step = 1
    x = int(key / 10)
    y = key % 10
    p = random.random()
    if p < epsilon:
        next_action = random.randint(0, len(all_value[key]) -1)
    else:
        next_action = all_value[key].index(max(all_value[key]))
    old_value = all_value[key][next_action]
    if next_action == 0:
        if x <= 0:
            new_key = key
        else:
            new_key = key - 10
    elif next_action == 1:
        if x >= max_x - 1:
            new_key = key
        else:
            new_key = key + 10
    elif next_action == 2:
        if y <= 0:
            new_key = key
        else:
            new_key = key - 1
    elif next_action == 3:
        if y >= max_y - 1:
            new_key = key
        else:
            new_key = key + 1
    else:
        out = 1
        step = 0
        value = all_value[key][next_action]
    if out == 0:
        p = random.random()
        if p < epsilon:
            if type(all_value[new_key]) == list:
                ntnt_action = random.randint(0, len(all_value[new_key]) -1)
            else:
                value = all_value[new_key]
                all_value[key][next_action] = old_value + alpha * (move_cost + gamma * value - old_value)
                out = 1
                step = 1
        else:
            if type(all_value[new_key]) == list:
                ntnt_action = all_value[new_key].index(max(all_value[new_key]))
            else:
                value = all_value[new_key]
                all_value[key][next_action] = old_value + alpha * (move_cost + gamma * value - old_value)
                out = 1
                step = 1
        if out == 0:
            new_value = all_value[new_key][ntnt_action]
            all_value[key][next_action] = old_value + alpha * (move_cost + gamma * new_value - old_value)
            p2 = random.random()
            if p2 > 0.3:
                key = new_key
            elif p2 < 0.1:
                if next_action == 0 or 1:  #left
                    if y <= 0:
                        key = key
                    else:
                        key = key - 1
                elif next_action == 2 or 3:  #up
                    if x <= 0:
                        key = key
                    else:
                        key = key - 10
            elif 0.1 <= p2 <= 0.2:
                if next_action == 0 or 1:  #right
                    if y >= max_y -1:
                        key = key
                    else:
                        key = key + 1
                elif next_action == 2 or 3:  #down
                    if x >= max_x -1:
                        key = key
                    else:
                        key = key + 10

            elif 0.2 < p2 <= 0.3:
                if next_action == 0:
                    if x <= 0:
                        key = key
                    elif x - 1 == 0 or type(all_value[key - 10]) == int:
                        key = new_key
                    else:
                        key = key - 20
                elif next_action == 1:
                    if x >= max_x -1:
                        key = key
                    elif x + 1 == max_x -1 or type(all_value[key + 10]) == int:
                        key = new_key
                    else:
                        key = key + 20
                elif next_action == 2:
                    if y <= 0:
                        key = key
                    elif y - 1 == 0 or type(all_value[key - 1]) == int:
                        key = new_key
                    else:
                        key = key - 2
                elif next_action == 3:
                    if y >= max_y -1:
                        key = key
                    elif y + 1 == max_y -1 or type(all_value[key + 1]) == int:
                        key = new_key
                    else:
                        key = key + 2

            if type(all_value[key]) == int:
                out = 1
                value = all_value[key]
                step = 1
    return all_value, key, value, out, step, next_action

def iteration(all_value, epsilon, alpha, move_cost, gamma, iteration_time):
    all_values = []
    for i in range(iteration_time):
        key = start_point(all_value)
        steps = 0
        while True:
            all_value, key, value, out, step, next_action = SARSA(all_value, key, epsilon, alpha, move_cost, gamma)
            steps += step
            if out == 1:
                values = value + steps * move_cost
                break
        all_values.append(values)
    return all_values, all_value


def load_input():
    str = input('Please input:').split()
    value_goal=int(str[1])
    value_fall=int(str[2])
    move_cost=float(str[3])
    value_giveup=int(str[4])
    iteration_time = int(str[5])
    epsilon = float(str[6])
    return value_goal, value_fall, move_cost, value_giveup, iteration_time, epsilon


action = ['^', 'v', '<', '>', 'T']
iteration_time = 10000
value_goal = 5
value_fall = -2
value_giveup = -3
epsilon = 0
alpha = 0.5
move_cost = -1
gamma = 1
value_goal, value_fall, move_cost, value_giveup, iteration_time, epsilon = load_input()
start_map = np.array(open_file())
max_x = len(start_map)
max_y = len(start_map[0])

all_value = set_start(start_map, value_goal, value_fall, value_giveup,max_x, max_y)

all_values, all_value = iteration(all_value, epsilon, alpha, move_cost, gamma, iteration_time)

for i in range(len(start_map)):
    for j in range(len(start_map[0])):
        if start_map[i][j] == '':
            start_map[i][j] = action[all_value[10 * i + j].index(max(all_value[10 * i + j]))]



all_values = np.array(all_values)
print(start_map)
mean50 = []
for i in range(500):
    temp = np.array(all_values[i * 20: i * 20 + 20])
    mean50.append(np.median(temp))
plt.figure()
plt.plot(mean50)
plt.show()

