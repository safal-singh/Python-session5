import pytest
import random
import string
import session5
import os
import inspect
import re
import math
import time

README_CONTENT_CHECK_FOR = [
    'time_it',
	'fn',
	'repetitions',
    '*args',
    '**kwargs',
    'squared_power_list',
	'start',
	'end',
	'sides',
	'base_temp',
	'temp_given_in',
	'kmph',
	'dist',
	'time',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding='utf-8')    
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding='utf-8')    
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_invalid_number_squared_power_list():
    with pytest.raises(ValueError):
        session5.squared_power_list('a', start=0, end=5)

def test_invalid_number_relevent_error():
    with pytest.raises(ValueError, match=r".* numeric .*"):
        session5.squared_power_list('a', start=0, end=5)

def test_invalid_start_end_squared_power_list():
    with pytest.raises(ValueError):
        session5.squared_power_list(2, start=0.3, end=5)
    with pytest.raises(ValueError):
        session5.squared_power_list(2, start=0, end=5.2)

def test_invalid_start_end_relevent_message():
    with pytest.raises(ValueError, match=r".* integer .*"):
        session5.squared_power_list(2, start=2.3, end=5)
    with pytest.raises(ValueError, match=r".* integer .*"):
        session5.squared_power_list(2, start=2, end=5.3)		

def test_invalid_s_length_polygon_area():
    with pytest.raises(ValueError):
        session5.polygon_area(-2, sides=3)

def test_invalid_s_length_relevent_error():
    with pytest.raises(ValueError, match=r".* non-positive"):
        session5.polygon_area(-2, sides=5)

def test_invalid_sides_relevent_error():
    with pytest.raises(ValueError, match=r".* lesser than or equal to 2, or greater than 6"):
        session5.polygon_area(2, sides=2)
    with pytest.raises(ValueError, match=r".* lesser than or equal to 2, or greater than 6"):
        session5.polygon_area(2, sides=7)

def test_invalid_sides_polygon_area():
    with pytest.raises(ValueError):
        session5.polygon_area(2, sides=2)
    with pytest.raises(ValueError):
        session5.polygon_area(2, sides=7)

def test_equal_start_end():
    assert session5.squared_power_list(4, start=3, end=3) == list(), f"Empty list should be returned for equal start and end values!"	

def test_print_time():
    start_time = time.time()
    print(1, 2, 3, sep='d', end='bla\n')
    time_for_print = time.time() - start_time
    time_it = session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitions=5)
    assert math.isclose(time_it, time_for_print,  rel_tol = 1e-02, abs_tol=1e-2) == True, f"Time not matching for print!!!"

def test_squared_power_list_time():
    start_time = time.time()
    power_list = session5.squared_power_list(2, start=0, end=5)
    time_for_call = time.time() - start_time
    assert math.isclose(session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitions=5), time_for_call,  rel_tol = 1e-12, abs_tol=1e-02) == True, f"Time not matching for squared_power_list!!!"

def test_polygon_area_time():
    start_time = time.time()
    power_list = session5.polygon_area(15, sides=3)
    time_for_call = time.time() - start_time
    time_it = session5.time_it(session5.polygon_area, 15, sides = 3, repetitions=10)
    print('polygon time: ', time_for_call, time_it)	
    assert math.isclose(time_it, time_for_call,  rel_tol = 1e-02, abs_tol=1e-2) == True, f"Time not matching for polygon_area!!!"

def test_invalid_temp_given_in():
    with pytest.raises(ValueError):
        session5.temp_converter(-2, temp_given_in='g')

def test_invalid_kmph():
    with pytest.raises(ValueError):
        session5.speed_converter(-2, dist='km', time='hr')

def test_invalid_kmph_relevent_error():
    with pytest.raises(ValueError, match=r".* lesser than 0"):
        session5.speed_converter(-4, dist='yrd', time='min')
		
def test_invalid_temp_given_in_relevent_error():
    with pytest.raises(ValueError, match=r"Invalid value .*"):
        session5.temp_converter(-4, temp_given_in='g')

def test_invalid_dist():
    with pytest.raises(ValueError):
        session5.speed_converter(12, dist='bla', time='min')

def test_invalid_time():
    with pytest.raises(ValueError):
        session5.speed_converter(12, dist='km', time='mm')

def test_invalid_dist_relevent_error():
    with pytest.raises(ValueError, match=r".* km/m/ft/yrd"):
        session5.speed_converter(4, dist='bla', time='min')

def test_invalid_time_relevent_error():
    with pytest.raises(ValueError, match=r".* ms/s/min/hr/day"):
        session5.speed_converter(4, dist='km', time='mm')

def test_temp_converter_time():
    start_time = time.time()
    power_list = session5.temp_converter(100, temp_given_in = 'f')
    time_for_call = time.time() - start_time
    time_it = session5.time_it(session5.temp_converter, 100, temp_given_in = 'f', repetitions=100)
    print('temp_converter time: ', time_for_call, time_it)	
    assert math.isclose(time_it, time_for_call,  rel_tol = 1e-02, abs_tol=1e-2) == True, f"Time not matching for temp_converter!!!"

def test_speed_converter_time():
    start_time = time.time()
    power_list = session5.speed_converter(100, dist='km', time='min')
    time_for_call = time.time() - start_time
    time_it = session5.time_it(session5.speed_converter, 100, dist='km', time='min', repetitions=100)
    print('speed_converter time: ', time_for_call, time_it)	
    assert math.isclose(time_it, time_for_call,  rel_tol = 1e-02, abs_tol=1e-2) == True, f"Time not matching for speed_converter!!!"	