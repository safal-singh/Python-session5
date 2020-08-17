##Function time_it(fn, *args, repetitions= 1, **kwargs)
Function to calculate the average time per call. 
#Parameters:
fn : Function for which the average time for calling is to be calculated.
\*args: takes variable number of positional arguments. Used to provide positional arguments of "fn" function call.
repeatitions: total calls to "fn" for calculating average time per call
\*\*kwargs: takes variable number of keyword arguments. Used here to provide keyword arguments of "fn" function call.

##squared_power_list(number, start, end)
Function to return list of powers of the "number" from "start" to "end", both inclusive.
#Parameters:
number: integer 
start: first power of the "number"
end: last power of the "number" 

##polygon_area(s_length, sides)
Function to calculate polygon area. 
#Parameters
s_length: side length of the polygon. Cannot be non-positive.
sides: number of sides of the polygon. Cannot be lesser than 3 or greater than 6.

##temp_converter(base_temp, temp_given_in)
Function to convert temperature from celsius to farenheit and vice-versa.
#Parameters:
base_temp: temperature to be converted to celsius/farenheit.
temp_given_in: unit of the base_temp. Can be 'c' for Celsius or 'f' for Farenheit (uppercase inclusive).

##speed_converter(kmph, dist, time)
Function to convert unit of speed from kmph to km/m/ft/yrd (distance), ms/s/min/hr/day (time).
#Parameters:
kmph: input speed in kmph.
dist: unit of distance for input to be converted. Valid values - km/m/ft/yrd
time: unit of time for input to be converted. Valid values - ms/s/min/hr/day