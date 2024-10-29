import data
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
'''This function takes 2 Times and adds them together, being careful to not create a Time with 
a minute or second value over 59. It inputs 2 Times and outputs 1 Time. 
'''
def time_add(time1:data.Time, time2:data.Time) -> data.Time:
    newTime = data.Time(0,0,0)
    newTime.hour = time1.hour + time2.hour
    newTime.minute = time1.minute + time2.minute
    newTime.second = time1.second + time2.second
    if newTime.second > 59:
        newTime.minute += 1
        newTime.second -= 60
    if newTime.minute > 59:
        newTime.hour += 1
        newTime.minute -= 60
    return newTime

# Part 4
'''This function takes a list of floats and tests if it sorted in descending order. If it is, 
it returns the bool True. If not, it returns nothing. 
'''
def is_descending(values:list[float]) -> bool:
    check = 0
    for i in range(len(values) - 1):
        if values[i] < values[i + 1]:
            check += 1
    if check == 0:
        return True

# Part 5
'''This function inputs a list and two integers and outputs either None or an int. This function
takes the input list and treating the integers and indexes, finds the largest value in the list
between the two indexes and returns it. However, if the first index is larger than the second, 
the function returns None. 
'''
def largest_between(vals:list[int], lower:int, upper:int) -> None or int:
    if lower > upper:
        return None
    biggest = lower
    for i in range(lower, upper + 1):
        if vals[i] > biggest:
            biggest = vals[i]
    return biggest

# Part 6
'''This function inputs a list of Points and outputs an integer. The function takes the input list
and finds the distance from each Point to the origin. It then returns the index of the Point in
the list furthest from the origin.
'''
def furthest_from_origin(pts:list[data.Point])->None or data.Point:
    furthest_distance = 0
    furthest_index = 0
    if pts == []:
        return None
    for i in range(len(pts)):
        i_distance = math.sqrt((pts[i].x)**2 + (pts[i].y)**2)
        if i_distance > furthest_distance:
            furthest_distance = i_distance
            furthest_index = i

    return furthest_index

