import time
from math import tan, pi
from numbers import Number


def squared_power_list(number, start, end):
    if not isinstance(number, Number):
        raise ValueError(f'{number} is not numeric type')
    if not isinstance(start, int):
        raise ValueError(f'{start} is not integer type')
    if not isinstance(end, int):
        raise ValueError(f'{end} is not integer type')

    return [number**power for power in range(start, end)]

def polygon_area(s_length, sides):
    if s_length <= 0:
        raise ValueError('Polygon side length cannot be non-positive!')
    if not 2 < sides <= 6:
        raise ValueError('Number of sides in polygon cannot be lesser than or equal to 2, or greater than 6')
    p_area = sides * (s_length ** 2) / (4 * tan(pi / sides))
    return p_area

def temp_converter(base_temp, temp_given_in):
    temp_given_in = temp_given_in.lower()

    if temp_given_in == 'f':
        return (base_temp - 32) * 5/9
    elif temp_given_in == 'c':
        return (base_temp * 9/5) + 32
    else:
        raise ValueError(f'Invalid value for temp_given_in: {temp_given_in}. Valid values are c or f (uppercase or lowercase)')

def speed_converter(kmph, dist, time):
    dist = dist.lower()
    time = time.lower()

    if kmph<0:
        raise ValueError(f'speed ({kmph}) cannot be lesser than 0')

    dist_conv = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yrd': 1093.61}
    time_conv = {'ms': 3600*1000, 's': 3600, 'min': 60, 'hr': 1, 'day': 1/24}

    if dist not in dist_conv:
        raise ValueError(f"Invalid value for parameter 'dist': {dist}. Valid values: km/m/ft/yrd")
    if time not in time_conv:
        raise ValueError(f"Invalid value for parameter 'time': {time}. Valid values: ms/s/min/hr/day")
    return kmph * dist_conv.get(dist) / time_conv.get(time)

def time_it(fn, *args, repetitions=1, **kwargs):
    time_list = list()
    while repetitions>0:
        start_time = time.time()
        fn(*args, **kwargs)
        time_list.append(time.time() - start_time)
        repetitions -= 1
    return sum(time_list) / len(time_list)

if __name__=='__main__':
    print(f"print time_it:", time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=5))
    print(f"squared_power_list time_it: ", time_it(squared_power_list, 2, start=2, end=2, repetitions=5))
    print(f"polygon_area time_it: ", time_it(polygon_area, 15, sides = 2, repetitions=10))
    print(f"temp_converter time_it: ", time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100))
    print(f"speed_converter time_it: ", time_it(speed_converter, 100, dist='km', time='min', repetitions=200))