import random
from matplotlib import pyplot as plt
import copy
import time


class car:

    def __init__(self, position):
        self.turned_times = 0
        self.stop_time = 0
        self.runing_time = 0
        self.position = [[0, 0], [0, 0]]
        self.waiting_time = 0
        self.stop_stage = 0
        self.restart_stage = 0
        self.position[0][0] = position[0][0]
        self.position[0][1] = position[0][1]
        self.position[1][0] = position[1][0]
        self.position[1][1] = position[1][1]

    def get_pose(self):
        if self.position[0][0] - self.position[1][0] == -1:
            return 'up'
        elif self.position[0][0] - self.position[1][0] == 1:
            return 'down'
        elif self.position[0][1] - self.position[1][1] == -1:
            return 'left'
        else:
            return 'right'

    def move_to_left_lane(self):
        if self.get_pose() == 'up':
            self.position[0][0] -= 1  # x0
            self.position[1][0] -= 1  # x1
            self.position[0][1] -= 1  # y0
            self.position[1][1] -= 1  # y1
            return
        if self.get_pose() == 'down':
            self.position[0][0] += 1  # x0
            self.position[1][0] += 1  # x1
            self.position[0][1] += 1  # y0
            self.position[1][1] += 1  # y1
            return
        if self.get_pose() == 'left':
            self.position[0][0] += 1  # x0
            self.position[1][0] += 1  # x1
            self.position[0][1] -= 1  # y0
            self.position[1][1] -= 1  # y1
            return
        if self.get_pose() == 'right':
            self.position[0][0] -= 1  # x0
            self.position[1][0] -= 1  # x1
            self.position[0][1] += 1  # y0
            self.position[1][1] += 1  # y1
            return

    def move_to_right_lane(self):
        if self.get_pose() == 'up':
            self.position[0][0] -= 1  # x0
            self.position[1][0] -= 1  # x1
            self.position[0][1] += 1  # y0
            self.position[1][1] += 1  # y1
            return
        if self.get_pose() == 'down':
            self.position[0][0] += 1  # x0
            self.position[1][0] += 1  # x1
            self.position[0][1] -= 1  # y0
            self.position[1][1] -= 1  # y1
            return
        if self.get_pose() == 'left':
            self.position[0][0] -= 1  # x0
            self.position[1][0] -= 1  # x1
            self.position[0][1] -= 1  # y0
            self.position[1][1] -= 1  # y1
            return
        if self.get_pose() == 'right':
            self.position[0][0] += 1  # x0
            self.position[1][0] += 1  # x1
            self.position[0][1] += 1  # y0
            self.position[1][1] += 1  # y1
            return

    def turn(self, direction):
        self.turned_times += 1
        if direction == 'left':
            if self.get_pose() == 'up':
                self.position[0][0]
                self.position[0][1] -= 1
                self.position[1][0] -= 1
                self.position[1][1]
                return
            if self.get_pose() == 'down':
                self.position[0][0]
                self.position[0][1] += 1
                self.position[1][0] += 1
                self.position[1][1]
                return
            if self.get_pose() == 'left':
                self.position[0][0] += 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] -= 1
                return
            if self.get_pose() == 'right':
                self.position[0][0] -= 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] += 1
                return
        else:
            if self.get_pose() == 'up':
                self.position[0][0]
                self.position[0][1] += 1
                self.position[1][0] -= 1
                self.position[1][1]
                return
            if self.get_pose() == 'down':
                self.position[0][0]
                self.position[0][1] -= 1
                self.position[1][0] += 1
                self.position[1][1]
                return
            if self.get_pose() == 'left':
                self.position[0][0] -= 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] -= 1
                return
            if self.get_pose() == 'right':
                self.position[0][0] += 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] += 1
                return

    def move_forward(self):
        if self.get_pose() == 'up':
            self.position[0][0] -= 1
            self.position[0][1]
            self.position[1][0] -= 1
            self.position[1][1]
            return
        if self.get_pose() == 'down':
            self.position[0][0] += 1
            self.position[0][1]
            self.position[1][0] += 1
            self.position[1][1]
            return
        if self.get_pose() == 'left':
            self.position[0][0]
            self.position[0][1] -= 1
            self.position[1][0]
            self.position[1][1] -= 1
            return
        if self.get_pose() == 'right':
            self.position[0][0]
            self.position[0][1] += 1
            self.position[1][0]
            self.position[1][1] += 1
            return

    def move_backward(self):
        if self.get_pose() == 'up':
            self.position[0][0] += 1
            self.position[0][1]
            self.position[1][0] += 1
            self.position[1][1]
            return
        if self.get_pose() == 'down':
            self.position[0][0] -= 1
            self.position[0][1]
            self.position[1][0] -= 1
            self.position[1][1]
            return
        if self.get_pose() == 'left':
            self.position[0][0]
            self.position[0][1] += 1
            self.position[1][0]
            self.position[1][1] += 1
            return
        if self.get_pose() == 'right':
            self.position[0][0]
            self.position[0][1] -= 1
            self.position[1][0]
            self.position[1][1] -= 1
            return

    def turn_backward(self, direction):
        if direction == 'left':
            if self.get_pose() == 'up':
                self.position[0][0] += 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] -= 1
                return
            if self.get_pose() == 'down':
                self.position[0][0] -= 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] += 1
                return
            if self.get_pose() == 'left':
                self.position[0][0]
                self.position[0][1] += 1
                self.position[1][0] += 1
                self.position[1][1]
                return
            if self.get_pose() == 'right':
                self.position[0][0]
                self.position[0][1] -= 1
                self.position[1][0] -= 1
                self.position[1][1]
                return
        elif direction == 'right':
            if self.get_pose() == 'up':
                self.position[0][0] += 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] += 1
                return
            if self.get_pose() == 'down':
                self.position[0][0] -= 1
                self.position[0][1]
                self.position[1][0]
                self.position[1][1] -= 1
                return
            if self.get_pose() == 'left':
                self.position[0][0]
                self.position[0][1] += 1
                self.position[1][0] -= 1
                self.position[1][1]
                return
            if self.get_pose() == 'right':
                self.position[0][0]
                self.position[0][1] -= 1
                self.position[1][0] += 1
                self.position[1][1]
                return


def set_parkinglot_status(position, status, parkinglot):
    if position[0] >= 0 and position[0] < len(parkinglot) and position[1] >= 0 and position[1] < len(parkinglot[0]):
        parkinglot[position[0]][position[1]] = status


def set_multi_parkinglot_status(positions, status, parkinglot):
    for i in positions:
        set_parkinglot_status(i, status, parkinglot)


def recovery(position, parkinglot, designed_parkinglot):
    set_parkinglot_status(position, get_parkinglot_status(
        position, designed_parkinglot), parkinglot)


def recoveries(positions, parkinglot, designed_parkinglot):
    for i in positions:
        recovery(i, parkinglot, designed_parkinglot)


def car_occupy(car, parkinglot):
    for i in car.position:
        set_parkinglot_status(i, 5, parkinglot)


def get_parkinglot_status(position, parkinglot):
    if position[0] >= 0 and position[0] < len(parkinglot) and position[1] >= 0 and position[1] < len(parkinglot[0]):
        return parkinglot[position[0]][position[1]]
    else:
        return 4


def get_multi_parkinglot_status(positions, parkinglot):
    status = []
    for i in positions:
        status.append(get_parkinglot_status(i, parkinglot))
    return status


def get_front_position(car):
    head = car.position[0]
    v = {
        'up': [head[0] - 1, head[1]],
        'down': [head[0] + 1, head[1]],
        'left': [head[0], head[1] - 1],
        'right': [head[0], head[1] + 1]
    }
    return v[car.get_pose()]


def get_front_left_position(car):
    head = car.position[0]
    v = {
        'up': [head[0] - 1, head[1] - 1],
        'down': [head[0] + 1, head[1] + 1],
        'left': [head[0] + 1, head[1] - 1],
        'right': [head[0] - 1, head[1] + 1]
    }
    return v[car.get_pose()]


def get_front_right_position(car):
    head = car.position[0]
    v = {
        'up': [head[0] - 1, head[1] + 1],
        'down': [head[0] + 1, head[1] - 1],
        'left': [head[0] - 1, head[1] - 1],
        'right': [head[0] + 1, head[1] + 1]
    }
    return v[car.get_pose()]


def get_back_position(car):
    tail = car.position[1]
    v = {
        'up': [tail[0] + 1, tail[1]],
        'down': [tail[0] - 1, tail[1]],
        'left': [tail[0], tail[1] + 1],
        'right': [tail[0], tail[1] - 1]
    }
    return v[car.get_pose()]


def get_front_status(car, parkinglot):
    return get_parkinglot_status(get_front_position(car), parkinglot)


def get_head_status(car, parkinglot):
    return get_parkinglot_status(car.position[0], parkinglot)


def get_front2_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0] - 2, head[1]], parkinglot),
        'down': get_parkinglot_status([head[0] + 2, head[1]], parkinglot),
        'left': get_parkinglot_status([head[0], head[1] - 2], parkinglot),
        'right': get_parkinglot_status([head[0], head[1] + 2], parkinglot)
    }
    return v[car.get_pose()]


def get_head_left_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0], head[1] - 1], parkinglot),
        'down': get_parkinglot_status([head[0], head[1] + 1], parkinglot),
        'left': get_parkinglot_status([head[0] + 1, head[1]], parkinglot),
        'right': get_parkinglot_status([head[0] - 1, head[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_head_left2_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0], head[1] - 2], parkinglot),
        'down': get_parkinglot_status([head[0], head[1] + 2], parkinglot),
        'left': get_parkinglot_status([head[0] + 2, head[1]], parkinglot),
        'right': get_parkinglot_status([head[0] - 2, head[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_tail_left_status(car, parkinglot):
    tail = car.position[1]
    v = {
        'up': get_parkinglot_status([tail[0], tail[1] - 1], parkinglot),
        'down': get_parkinglot_status([tail[0], tail[1] + 1], parkinglot),
        'left': get_parkinglot_status([tail[0] + 1, tail[1]], parkinglot),
        'right': get_parkinglot_status([tail[0] - 1, tail[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_back_status(car, parkinglot):
    tail = car.position[1]
    v = {
        'up': get_parkinglot_status([tail[0] + 1, tail[1]], parkinglot),
        'down': get_parkinglot_status([tail[0] - 1, tail[1]], parkinglot),
        'left': get_parkinglot_status([tail[0], tail[1] + 1], parkinglot),
        'right': get_parkinglot_status([tail[0], tail[1] - 1], parkinglot)
    }
    return v[car.get_pose()]


def get_tail_right_status(car, parkinglot):
    tail = car.position[1]
    v = {
        'up': get_parkinglot_status([tail[0], tail[1] + 1], parkinglot),
        'down': get_parkinglot_status([tail[0], tail[1] - 1], parkinglot),
        'left': get_parkinglot_status([tail[0] - 1, tail[1]], parkinglot),
        'right': get_parkinglot_status([tail[0] + 1, tail[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_tail_left2_status(car, parkinglot):
    tail = car.position[1]
    v = {
        'up': get_parkinglot_status([tail[0], tail[1] - 2], parkinglot),
        'down': get_parkinglot_status([tail[0], tail[1] + 2], parkinglot),
        'left': get_parkinglot_status([tail[0] + 2, tail[1]], parkinglot),
        'right': get_parkinglot_status([tail[0] - 2, tail[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_head_right_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0], head[1] + 1], parkinglot),
        'down': get_parkinglot_status([head[0], head[1] - 1], parkinglot),
        'left': get_parkinglot_status([head[0] - 1, head[1]], parkinglot),
        'right': get_parkinglot_status([head[0] + 1, head[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_head_right2_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0], head[1] + 2], parkinglot),
        'down': get_parkinglot_status([head[0], head[1] - 2], parkinglot),
        'left': get_parkinglot_status([head[0] - 2, head[1]], parkinglot),
        'right': get_parkinglot_status([head[0] + 2, head[1]], parkinglot)
    }
    return v[car.get_pose()]


def get_head_front_left_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0] - 1, head[1] - 1], parkinglot),
        'down': get_parkinglot_status([head[0] + 1, head[1] + 1], parkinglot),
        'left': get_parkinglot_status([head[0] + 1, head[1] - 1], parkinglot),
        'right': get_parkinglot_status([head[0] - 1, head[1] + 1], parkinglot)
    }
    return v[car.get_pose()]


def get_head_front_right_status(car, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0] - 1, head[1] + 1], parkinglot),
        'down': get_parkinglot_status([head[0] + 1, head[1] - 1], parkinglot),
        'left': get_parkinglot_status([head[0] - 1, head[1] - 1], parkinglot),
        'right': get_parkinglot_status([head[0] + 1, head[1] + 1], parkinglot)
    }
    return v[car.get_pose()]


def get_head_frontx_rightx_status(car, delta_front, delta_right, parkinglot):
    head = car.position[0]
    v = {
        'up': get_parkinglot_status([head[0] - delta_front, head[1] + delta_right], parkinglot),
        'down': get_parkinglot_status([head[0] + delta_front, head[1] - delta_right], parkinglot),
        'left': get_parkinglot_status([head[0] - delta_right, head[1] - delta_front], parkinglot),
        'right': get_parkinglot_status([head[0] + delta_right, head[1] + delta_front], parkinglot)
    }
    return v[car.get_pose()]


def is_has_left_cross(car, parkinglot, designed_parkinglot):
    if get_head_left2_status(car, parkinglot) == 1 and get_head_left_status(car, parkinglot) == 1 and get_tail_left2_status(car, designed_parkinglot) == 1:
        return True
    else:
        return False


def is_has_right_cross(car, parkinglot, designed_parkinglot):
    if get_head_right2_status(car, parkinglot) == 1 and get_head_right_status(car, parkinglot) == 1 and get_head_front_right_status(car, designed_parkinglot) == 1:
        return True
    else:
        return False


def car_turn(car, direction, parkinglot, designed_parkinglot):
    recoveries(car.position, parkinglot, designed_parkinglot)
    j.turn(direction)
    # set_parkinglot_status(j.position[0], 5, parkinglot)
    car_occupy(car, parkinglot)


def print_parkinglot(parkinglot):
    print('#' * (len(parkinglot[0]) * 3 + 2))
    for i in parkinglot:
        print('#', end='')
        print(i, end='#\n')
    print('#' * (len(parkinglot[0]) * 3 + 2))
    print('')


def is_berth_at_front(car, parkinglot):
    if get_front_status(car, parkinglot) == 2:
        car.stop_stage = 1
        return True
    return False


def is_berth_nearby(car, parkinglot):
    return is_berth_at_front(car, parkinglot)


if __name__ == '__main__':
    # 1: line
    # 2: berth
    # 3: berth(unaccessable)
    # 4: unaccessable
    # 5: Occupied
    parkinglot = []
    guidemap = []
    with open('map.csv', 'r') as f:
        content = f.readlines()
        for i in content:
            line = [int(j) for j in i.split(',')]
            guideline = []
            parkinglotline = []
            for j in line:
                if j >= 6:
                    guideline.append(j)
                    parkinglotline.append(1)
                else:
                    guideline.append(0)
                    parkinglotline.append(j)
            parkinglot.append(copy.copy(parkinglotline))
            guidemap.append(copy.copy(guideline))

    designed_parkinglot = [copy.copy(i) for i in parkinglot]
    entry = [[6, 1], [6, 0]]
    wayout = [[6, 15], [6, 16]]
    carlist = []
    stoped_car_list = []
    restarted_car_list = []
    out_car = []
    simulation_time = 120

    carlist.append(car(entry))
    set_multi_parkinglot_status(entry, 5, parkinglot)

    for i in range(simulation_time):
        if get_multi_parkinglot_status(entry, parkinglot) == [1, 1] and random.randint(0, 12) < 4:
            #     Put a car at entry.
            newcar = car(entry)
            carlist.append(copy.copy(newcar))
            # set_multi_parkinglot_status(entry, 5, parkinglot)
            car_occupy(newcar, parkinglot)
        for j in stoped_car_list:
            j.stop_time += 1
            if random.randint(0, 12) < 2:
                restarted_car_list.append(copy.copy(j))
                del stoped_car_list[stoped_car_list.index(j)]
        for j in restarted_car_list:
            if j.position[0] == wayout[1]:
                recoveries(j.position, parkinglot, designed_parkinglot)
                out_car.append(copy.copy(j))
                del restarted_car_list[restarted_car_list.index(j)]
            if j.restart_stage == 0:
                # if get_head_frontx_rightx_status(j, -2, 0, parkinglot) == 1:
                if get_back_status(j, parkinglot) == 1:
                    j.restart_stage = 1
                    recoveries(j.position, parkinglot, designed_parkinglot)
                    j.move_backward()
                    set_multi_parkinglot_status(j.position, 5, parkinglot)
            elif j.restart_stage == 2:
                if get_head_status(j, guidemap) == 6:
                    if j.get_pose() == 'up':
                        if get_front_status(j, parkinglot) == 1:
                            if get_head_front_right_status(j, parkinglot) == 1 and get_head_right_status(j, parkinglot) == 1 and not is_has_right_cross(j, parkinglot, designed_parkinglot):
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_to_right_lane()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                            else:
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_forward()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'down':
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        elif get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'left':
                        if get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                elif get_head_status(j, guidemap) == 7:
                    if j.get_pose() == 'up':
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        elif get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'down':
                        if get_front_status(j, parkinglot) == 1:
                            if get_head_front_right_status(j, parkinglot) == 1 and get_head_right_status(j, parkinglot) == 1 and not is_has_right_cross(j, parkinglot, designed_parkinglot):
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_to_right_lane()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                            else:
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_forward()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'left':
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                elif get_head_status(j, guidemap) == 8:
                    if j.get_pose() == 'up':
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'down':
                        if get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'left':
                        if get_front_status(j, parkinglot) == 1:
                            if get_head_front_right_status(j, parkinglot) == 1 and get_head_right_status(j, parkinglot) == 1 and not is_has_right_cross(j, parkinglot, designed_parkinglot):
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_to_right_lane()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                            else:
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_forward()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        elif get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                else:
                    if j.get_pose() == 'up':
                        if get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'down':
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    elif j.get_pose() == 'left':
                        if get_head_left_status(j, parkinglot) == 1:
                            car_turn(j, 'left', parkinglot,
                                     designed_parkinglot)
                        elif get_head_right_status(j, parkinglot) == 1:
                            car_turn(j, 'right', parkinglot,
                                     designed_parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_front_status(j, parkinglot) == 1:
                            if get_head_front_right_status(j, parkinglot) == 1 and get_head_right_status(j, parkinglot) == 1 and not is_has_right_cross(j, parkinglot, designed_parkinglot):
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_to_right_lane()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                            else:
                                recoveries(j.position, parkinglot,
                                           designed_parkinglot)
                                j.move_forward()
                                set_multi_parkinglot_status(
                                    j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1

            elif j.restart_stage == 1:
                if get_parkinglot_status(j.position[1], guidemap) == 6:
                    if j.get_pose() == 'left':
                        if get_tail_left_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('left')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_tail_right_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('right')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                if get_parkinglot_status(j.position[1], guidemap) == 7:
                    if j.get_pose() == 'left':
                        if get_tail_right_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('right')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_tail_left_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('left')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                if get_parkinglot_status(j.position[1], guidemap) == 8:
                    if j.get_pose() == 'up':
                        if get_tail_right_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('right')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_tail_left_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('left')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                if get_parkinglot_status(j.position[1], guidemap) == 9:
                    if j.get_pose() == 'up':
                        if get_tail_left_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('left')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
                    else:
                        if get_tail_right_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.turn_backward('right')
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        elif get_back_status(j, parkinglot) == 1:
                            j.restart_stage = 2
                            recoveries(j.position, parkinglot,
                                       designed_parkinglot)
                            j.move_backward()
                            set_multi_parkinglot_status(
                                j.position, 5, parkinglot)
                        else:
                            j.waiting_time += 1
        for j in carlist:
            j.runing_time += 1
            if j.stop_stage == 9:
                stoped_car_list.append(copy.copy(j))
                del carlist[carlist.index(j)]
                print(stoped_car_list)
                continue
            elif j.stop_stage in [1, 2, 4, 5, 7, 8]:
                j.stop_stage += 1
                continue
            elif j.stop_stage in [3, 6]:
                j.stop_stage += 1
                recoveries(j.position, parkinglot, designed_parkinglot)
                j.move_forward()
                set_multi_parkinglot_status(j.position, 5, parkinglot)
            # elif j.stop_stage == 6:
            #     j.stop_stage += 1
            #     recoveries(j.position, parkinglot, designed_parkinglot)
            #     j.move_forward()
            #     set_multi_parkinglot_status(j.position, 5, parkinglot)
            # berth at front
            elif get_front_status(j, parkinglot) == 2 and get_front2_status(j, parkinglot) == 3:
                j.stop_stage = 4
                recoveries(j.position, parkinglot, designed_parkinglot)
                j.move_forward()
                set_multi_parkinglot_status(j.position, 5, parkinglot)
            # berth at front left
            elif get_head_front_left_status(j, parkinglot) == 2 and get_head_frontx_rightx_status(j, 2, -1, parkinglot) == 3 and get_head_left_status(j, parkinglot) == 1 and get_tail_left_status(j, parkinglot) == 1:
                j.stop_stage = 4
                recoveries(j.position, parkinglot, designed_parkinglot)
                j.move_to_left_lane()
                set_multi_parkinglot_status(j.position, 5, parkinglot)
            # berth at front right
            elif get_head_front_left_status(j, parkinglot) == 2 and get_head_frontx_rightx_status(j, 2, 1, parkinglot) == 3 and get_head_right_status(j, parkinglot) == 1 and get_tail_right_status(j, parkinglot) == 1:
                # get_head_front_right_status
                j.stop_stage = 4
                recoveries(j.position, parkinglot, designed_parkinglot)
                j.move_to_right_lane()
                set_multi_parkinglot_status(j.position, 5, parkinglot)
            elif get_head_right_status(j, parkinglot) == 2 and get_head_right2_status(j, parkinglot) == 3:
                j.stop_stage = 4
                car_turn(j, 'right', parkinglot, designed_parkinglot)
            elif get_head_left_status(j, parkinglot) == 2 and get_head_left2_status(j, parkinglot) == 3:
                j.stop_stage = 4
                car_turn(j, 'left', parkinglot, designed_parkinglot)
            elif j.stop_stage == 0 and get_head_frontx_rightx_status(j, 0, -2, parkinglot) == 2 and get_head_frontx_rightx_status(j, 0, -3, parkinglot) == 3 and get_head_left_status(j, parkinglot) == 1:
                j.stop_stage = 1
                car_turn(j, 'left', parkinglot, designed_parkinglot)
            # elif get_head_frontx_rightx_status(j, 1, 2, parkinglot) == 2 and get_head_frontx_rightx_status(j, 1, 3, parkinglot) == 3 and get_head_front_right_status(j, parkinglot) == 1:
            #     j.stop_stage += 1
            #     j.turn('right')
            else:
                # cross, turn left
                if j.turned_times == 0 and is_has_left_cross(j, parkinglot, designed_parkinglot) and random.randint(0, 12) < 6:
                    car_turn(j, 'left', parkinglot, designed_parkinglot)
                # cross, turn right
                elif j.turned_times == 0 and is_has_right_cross(j, parkinglot, designed_parkinglot) and random.randint(0, 12) < 6:
                    car_turn(j, 'right', parkinglot, designed_parkinglot)
                # change lane to right
                elif get_head_front_right_status(j, parkinglot) == 1 and get_head_right_status(j, parkinglot) == 1 and not is_has_right_cross(j, parkinglot, designed_parkinglot):
                    j.turned_times = 0
                    recovery(j.position[0], parkinglot, designed_parkinglot)
                    recovery(j.position[1], parkinglot, designed_parkinglot)
                    j.move_to_right_lane()
                    set_multi_parkinglot_status(j.position, 5, parkinglot)
                elif get_front_status(j, parkinglot) == 1:  # move front
                    j.turned_times = 0
                    j.move_forward()
                    set_multi_parkinglot_status(j.position, 5, parkinglot)
                    set_parkinglot_status(get_back_position(j), get_parkinglot_status(
                        get_back_position(j), designed_parkinglot), parkinglot)
                    # overtake from left
                elif get_head_front_left_status(j, parkinglot) == 1 and get_head_left_status(j, parkinglot) == 1:
                    recoveries(j.position, parkinglot, designed_parkinglot)
                    j.move_to_left_lane()
                    set_multi_parkinglot_status(j.position, 5, parkinglot)
                # elif get_head_left_status(j, parkinglot) == 1 and (get_head_left2_status(j, parkinglot) == 1 or get_head_left2_status(j, parkinglot) == 5):  # turn left
                elif get_front_status(j, parkinglot) != 5 and get_front_status(j, designed_parkinglot) != 1 and get_head_left_status(j, designed_parkinglot) == 1 and get_head_left2_status(j, designed_parkinglot) == 1:
                    car_turn(j, 'left', parkinglot, designed_parkinglot)
                # elif get_head_right_status(j, parkinglot) == 1:
                elif get_front_status(j, parkinglot) != 5 and get_front_status(j, designed_parkinglot) != 1 and get_head_right_status(j, designed_parkinglot) == 1 and get_head_right2_status(j, designed_parkinglot) == 1:
                    car_turn(j, 'right', parkinglot, designed_parkinglot)
                elif j.position[0] == wayout[1]:
                    del carlist[carlist.index(j)]
                else:
                    j.waiting_time += 1
        plt.imshow(parkinglot)
        plt.title('simulation_time = %d' % i)
        plt.pause(0.005)
    for i in carlist:
        print(i.stop_time)
