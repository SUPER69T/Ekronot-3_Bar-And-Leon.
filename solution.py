#names: Leon Subbotsky,   Bar Cohen.
#IDs:   323862524,        324268309.
# ------------------------------------------------
#       Q1(ADT Date - dispatch)
# ------------------------------------------------
import math
import sys
from itertools import accumulate
from os.path import split

from contourpy.util import data
from numpy import integer
from typing_extensions import override

#going to be useful for overloading "print" in exercise 6...:
import builtins

def make_time(h, m, s):
    hours = h
    minutes = m
    seconds = s
    def inner_clock(clock_hand):
        if clock_hand == 0: return hours
        if clock_hand == 1: return minutes
        if clock_hand == 2: return seconds
    return inner_clock

# ------------------------------------------------
def getitem_pair(p, i):
    return p(i)
# ------------------------------------------------
def hour(time):
    return time(0)
# ------------------------------------------------
def minute(time):
    return time(1)
# ------------------------------------------------
def second(time):
    return time(2)
# ------------------------------------------------
def time_difference(time1, time2):
    # -------
    h_diff = hour(time1) - hour(time2)
    m_diff = minute(time1) - minute(time2)
    s_diff = second(time1) - second(time2)
    # -------
    return h_diff * 3600+ m_diff * 60 + s_diff
# ------------------------------------------------
def str_time(time, tformat = 'hh:mm:ss'):
    h_temp = str(hour(time))
    m_temp = str(minute(time))
    s_temp = str(second(time))
    if 0 <= hour(time) <= 9: h_temp = "0" + h_temp
    if 0 <= minute(time) <= 9: m_temp = "0" + m_temp
    if 0 <= second(time) <= 9: s_temp = "0" + s_temp
    if tformat == 'hh:mm:ss':
        return f"{h_temp}:{m_temp}:{s_temp}"
    elif tformat == 'hh:mm':
        return f"{h_temp}:{m_temp}"
    else:
        if hour(time) < 12:
            halve = "A.M"
            if hour(time) == 0:
                h_temp = 12
        else:
            halve = "P.M"
            if hour(time) != 12: #if hour(time) = 12, the state is P.M and the count is not subtracted: 12.
                h_temp = hour(time) - 12
        if tformat == 'HH:MM':
            #print(f"h: {h_temp} m: {m_temp} s: {s_temp}, {halve}")
            return f"{h_temp}:{m_temp} {halve}"
        elif tformat == 'HH:MM:SS':
            #print(f"h: {h_temp} m: {m_temp} s: {s_temp}, {halve}")
            return f"{h_temp}:{m_temp}:{s_temp} {halve}"
        else:
            return "Incompatible time format."
# ------------------------------------------------
def time_correction(time, corr = 0):
    #if corr == 0: time_correction will treat the make_time() instance as a regular time -
    #and will reformat and construct a new, corrected version of make_time().
    # -------
    ###
    temp_s = (second(time) + corr) % 60
    ###(Seconds) after modulo - 60.
    ###
    temp_m = (minute(time) + ((second(time) + corr) // 60)) % 60
    ###(Minutes + (Seconds after division by - 60)) after modulo - 60.
    ###
    temp_h = (hour(time) + ((minute(time) + ((second(time) + corr) // 60)) // 60)) % 24
    ###(Hours + (Minutes + (Seconds after division by - 60)) after division by - 60) after modulo - 24.
    # -------
    new_time = make_time(temp_h, temp_m, temp_s)
    return new_time
# ------------------------------------------------
'''
>>> t1 = make_time(11,5,47)
>>> t1
<function make_time.<locals>.dispatch at 0x000001EC41BDC180>
>>> hour(t1)
11
>>> minute(t1)
5
>>> str_time(t1)
'11:05:47'
>>> t2 = make_time(0,12,23)
>>> str_time(t2,'HH:MM')
'12:12 A.M.'
>>> str_time(time_difference(t1,t2))
'10:53:24'
>>> str_time(time_correction(t1,4623),'HH:MM:SS')
'12:22:50 P.M.'
>>> t2 = time_correction(t2,-920)
>>> str_time(t2)
'23:57:03'
>>> str_time(t2,'HH:MM')
'11:57 P.M.'
'''

# ------------------------------------------------
#       Q2(ADT Tree - dispatch?)
# ------------------------------------------------
def make_tree(val,left,right):
    v = val
    l = left
    r = right
    def inner_make_tree(tree):
        if tree == 0: return v
        if tree == -1: return l
        if tree == 1: return r

    return inner_make_tree
# ------------------------------------------------
def getitem_pair(p,i):
    return p(i)
# ------------------------------------------------
def value(tree):
    return tree(0)
# ------------------------------------------------
def left(tree):
    return tree(-1)
# ------------------------------------------------
def right(tree):
    return tree(1)
# ------------------------------------------------
def print_tree(node):
    if node is not None:
        if left(node) is not None:
            print_tree(left(node))
        if value(node) is not None:
            print(value(node), end= " ")
        if right(node) is not None:
            print_tree(right(node))
# ------------------------------------------------
def min_value(node):
    if node is None: return float('inf') #covers all three cases: (valueL,valueR), (valueL,None), (None,valueR).
    else:
        return min(value(node), min_value(left(node)), min_value(right(node)))
# ------------------------------------------------
def mirror_tree(node):
    if node is None: return
    else:
        return make_tree(value(node), mirror_tree(right(node)), mirror_tree(left(node))) #switching.
# ------------------------------------------------
'''
>>> tree = make_tree(12,make_tree(6,make_tree(8,None,None),None),
make_tree(7,make_tree(2,None,None),make_tree(15,None,None)))
>>> tree
<function make_tree.<locals>.dispatch at 0x000001FA9A92C4A0>
>>> value(tree)
12
>>> value(left(tree))
6
>>> left(right(tree))
<function make_tree.<locals>.dispatch at 0x000001FA9A92C2C0>
>>> value(left(right(tree)))
2
>>> print_tree(tree)
8 6 12 2 7 15 
>>> min_value(tree)
2
>>> tree1 = mirror_tree(tree)
>>> print_tree(tree1)
15 7 2 12 6 8 
'''

# ------------------------------------------------
# Q3(Conventional Interfaces, Generator expressions)
# ------------------------------------------------
Q3 = lambda func,data: tuple((d for d in data if sum(f(d) for f in func) == 1))
# ------------------------------------------------
'''
>>> Q3((lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100),(20,-45,133,8,400,7,-300,68))
(-45, 133, 7, -300)
'''

# ------------------------------------------------
# Q4(Pipeline)
# ------------------------------------------------
from functools import reduce
temp =[('London',18,16),('Paris',18,20),('Madrid',30,35),('Berlin',20,20),('Roma',32,27)]
Q4a = lambda data: list(map(lambda measure: (measure[0], max(measure[1], measure[2])),data))
Q4b = lambda data: list(map(lambda m: m[0],filter(lambda m: m[1] < m[2], data)))
Q4c = lambda data: reduce(lambda a, b: a and b[1] != b[2], data, True)
#Q4d = lambda data: dict(list(map(lambda m: (abs(m[1] - m[2]), m[0]), data)))# - this was our original code that doesn't work because the python dictionary doesn't save states.
#chat-GPT helped with solving the state saving problem by comparing each new value's key to each new key creation, thus building lists of mutual-key values.
#
#          outer_iteration's_key        (inner_iteration's_tuple)                                   (outer_iteration's_tuple)
#                       v                          v                                                            v
Q4d = lambda data: {abs(t1 - t2): [city for city, t1_, t2_ in data if abs(t1_ - t2_) == abs(t1 - t2)] for city, t1, t2 in data}
#                                   ^                                      ^                   ^            ^
#                             inner_iteration                   inner_difference         outer_difference   outer_iteration
# ---------------------- a -----------------------
'''
Q4a(temp)
[('London', 18), ('Paris', 20), ('Madrid', 35), ('Berlin', 20), ('Roma', 32)]
'''
# ---------------------- b -----------------------
'''
Q4b(temp)
['Paris', 'Madrid']
'''
# ---------------------- c -----------------------
'''
Q4c(temp)
False
Q4c(temp[:3]+temp[-1:])
True
'''
# ---------------------- d -----------------------
'''
Q4d(temp)
{0: ['Berlin'], 2: ['London', 'Paris'], 5: ['Madrid', 'Roma']}
'''
# ------------------------------------------------

# ------------------------------------------------
#       Q5(Dispatch, Message Passing - Sets)
# https://en.wikipedia.org/wiki/Set_(mathematics)#Basic_operations
# ------------------------------------------------
def sets(d):
    #don't want boilerplate code...:
    #-------
    def bound_to_range(d):
        return tuple(n for n in d if n in range(21))
    def remove_duplicates(d):
        return tuple(dict.fromkeys(d))
    #-------
    t = bound_to_range(remove_duplicates(d))

    def dispatch(message, value= None):
        nonlocal t

        if message == 'set':
            t = bound_to_range(value)

        elif message == 'view':
            return set(t) #', '.join(chr(n) for n in t)

        elif message == 'in':
            return value in t

        elif message == 'not in':
            return not value in t

        elif message == 'not': #COMPLEMENT.
            return sets(tuple(n for n in range(21) if dispatch('not in', n)))
            #        ^
#|creating a new sets object |iterating over the numbers of 0-20 and returning only  |
                            #|the ones that don't appear in t by using dispatch again|

        elif message == '+': #UNION.
            return sets(remove_duplicates(t + tuple(value('view')))) #the ('view') is necessary here because 'value' isn't a collection.
            #                                               ^
            #                    |gets all elements from the value (=sets object) itself|

        elif message == '*': #INTERSECTION.
            return sets(tuple(n for n in value('view') if dispatch('in', n)))

        elif message == '//': #(t / value).
            #removing the union of t and value(t*value) from t:
            return  sets(tuple(n for n in t if n not in dispatch('*', value)('view')))

        elif message == 'xor':
            return sets(tuple(n for n in dispatch('+', value)('view') if n not in dispatch('*', value)('view')))

        """this is another way of doing the xor:
        return sets(tuple(dispatch('//', value) + tuple(n for n in value if n not in t)))
        #       |          (t / value)          |             (value / t)             |
        """
    return dispatch

# ------------------------------------------------
'''
>>> s1 = sets((1,2,3,4,5,100))
>>> s1
<function sets.<locals>.dispatch at 0x00000288FF7DC860>
>>> s1('view')
'{1, 2, 3, 4, 5}'
>>> s1('in',3)
True
>>> s1('not in',31)
True
>>> s1('not in',3)
False
>>> s2 = s1('not')
>>> s2
<function sets.<locals>.dispatch at 0x00000288FF7DD120>
>>> s2('view')
'{6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}'     #this should also contain - 0. this checking-file is dogshit.
>>> s1('set',(1,2,3,4,5,7,9,12,17))
>>> s2('set',(2,4,5,10,14,16,20)) 
>>> s1('+',s2)('not')('view')
'{6, 8, 11, 13, 15, 18, 19}'                                   #also here, there should be a - 0. this checking-file is still dogshit.


>>> s1('*',s2)('xor',s1('//',sets((2,3,5,12))))('view')
#   |UNION___|------|(t / value)----------------------|
#   |2, 4, 5_|------|__________1, 4, 7, 9, 17___________|
        v                            v
        |---|XOR__________________|--|
            v                     v
#           |1, 2, 5, 7, 9, 17|   --> this should be the correct output. (V) - it is.

'{1, 2, 5, 7, 9, 17}'
'''

# ------------------------------------------------
# Q6(Dispatch Dictionary, Message Passing-Matrix)
# ------------------------------------------------
def matrix(mtr,n,m):
    #n = len(rows)   } =
    #m = len(columns)} = assuming both inputs are valid and correct.
    #mtr_data = [list(row) for row in mtr]
    mtr_data =[]
    index = 0
    for row in range(n):
        mtr_data.append(list(mtr[index, index + m]))
        index += m


    def add_line(n_row):
        nonlocal mtr_data
        nonlocal n
        mtr_data.append(list(n_row)) #adding an entire tuple_to_list converted row.
        n = n + 1

    def add_column(r_col):
        nonlocal mtr_data
        nonlocal m
        for r in range(n): mtr_data[r].append(r_col[r]) #adding each final element in a row, for each - r_col - matching row.
        m = m + 1

    def print():
        for row in mtr_data:
            for elem in row:
                builtins.print(elem, end= "")
            builtins.print()

    def line():
        return n

    def column():
        return m

    def shift_up():
        nonlocal mtr_data
        new_mtr = [mtr[i + 1] if i > 0 else mtr[0] for i in
                   range(len(mtr))]  # includes the first and last rows switching.
        # mtr_data = mtr_data[1:] + [mtr_data[-1]] this is also possible.
        mtr_data = new_mtr

    def shift_down():
        nonlocal mtr_data
        new_mtr = [mtr[i - 1] if i > 0 else mtr[0] for i in
                   range(len(mtr))] #includes the first and last rows switching.
        #new_mtr = [mtr_data[0]] + mtr_data[:-1] is also possible.
        mtr_data = new_mtr

    def shift_left():
        nonlocal mtr_data
        for r in n:
            mtr_data[r] = [r[1:]] + r[-1]

    def shift_right():
        nonlocal mtr_data
        for r in n:
            mtr_data[r] = [r[0]] + r[:-1]

    def transpose():
        nonlocal mtr_data
        for i in range(n):
            for j in range(i, m): #runs from the diagonal to the last column of the mtr_data matrix.
                mtr_data[i][j] = mtr_data[j][i]

    dispatch = {'add_line' : add_line, 'add_column' : add_column, 'print' : print,
                'line' : line, 'column' : column, 'shift_up' : shift_up,
                'shift_down' : shift_down, 'shift_left' : shift_left,
                'shift_right' : shift_right, 'transpose' : transpose}

    return dispatch


# ------------------------------------------------
'''
>>> m1 = matrix((1,2,3,4,5,6,7,8),2,4)
>>> m1['add_line']((1,3,5,7))
[1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5, 7]
>>> m1['add_column']((2,4,6))
[1, 2, 3, 4, 2, 5, 6, 7, 8, 4, 1, 3, 5, 7, 6]
>>> mat1 = m1['print']()
>>> for _ in range(m1['line']()):
	line = mat1['print']()
	for _ in range(m1['column']()):
		print(line['print'](), end=' ')
	print()
1 2 3 4 2 
5 6 7 8 4 
1 3 5 7 6 
>>> m1['shift_up']()
[5, 6, 7, 8, 4, 1, 3, 5, 7, 6, 1, 2, 3, 4, 2]
>>> m1['shift_right']()
[4, 5, 6, 7, 8, 6, 1, 3, 5, 7, 2, 1, 2, 3, 4]
>>> m1['transpose']()
[4, 6, 2, 5, 1, 1, 6, 3, 2, 7, 5, 3, 8, 7, 4]
>>> mat1 = m1['print']()
>>> for _ in range(m1['line']()):
	line = mat1['print']()
	for _ in range(m1['column']()):
		print(line['print'](), end=' ')
	print()
4 6 2 
5 1 1 
6 3 2 
7 5 3 
8 7 4 
>>>
'''
# ------------------------------------------------
#   driver
# ------------------------------------------------
def driver():
    """
    print('<<< Q1 >>>')
    t1 = make_time(11,5,47)
    print(t1)
    print(hour(t1))
    print(minute(t1))
    print(str_time(t1))
    t2 = make_time(0,12,23)
    print(str_time(t2,'HH:MM'))
    #print(str_time(time_difference(t1,t2))) WRONG.
    td = time_difference(t1, t2)
    print(f"time difference: {str_time(time_correction(make_time(0, 0, time_difference(t1, t2)), 0))}")
    print(str_time(time_correction(t1,4623),'HH:MM:SS'))
    t2 = time_correction(t2,-920)
    print(str_time(t2))
    print(str_time(t2,'HH:MM'))
    """
    """
    print('<<< Q2 >>>')
    tree = make_tree(12,make_tree(6,make_tree(8,None,None),None),
    make_tree(7,make_tree(2,None,None),make_tree(15,None,None)))
    print(tree)
    print(value(tree))
    print(value(left(tree)))
    print(left(right(tree)))
    print(value(left(right(tree))))
    print_tree(tree)
    print()
    print(min_value(tree))
    tree1 = mirror_tree(tree)
    print_tree(tree1)
    print()
    """
    """
    print('<<< Q3 >>>')
    print(Q3((lambda x: x > 0, lambda x: x % 2 == 0, lambda x: 9 < abs(x) < 100),
               (20, -45, 133, 8, 400, 7, -300, 68)))
    """
    """
    print('<<< Q4 >>>')
    print(Q4a(temp))
    print(Q4b(temp))
    print(Q4c(temp))
    print(Q4c(temp[:3]+temp[-1:]))
    print(Q4d(temp))
    """
    """
    print('<<< Q5 >>>')
    s1 = sets((1,2,3,4,5,100))
    print(s1)
    print(s1('view'))
    print(s1('in',3))
    print(s1('not in',31))
    print(s1('not in',3))
    s2 = s1('not')
    print(s2)
    print(s2('view'))
    s1('set',(1,2,3,4,5,7,9,12,17))
    s2('set', (2,4,5,10,14,16,20))
    print("s1: " , s1('view'))
    print("s2: ", s2('view'))
    print(s1('+',s2)('not')('view'))
    print(s1('*',s2)('xor',s1('//',sets((2,3,5,12))))('view'))
    """
    #"""
    print('<<< Q6 >>>')
    m1 = matrix((1,2,3,4,5,6,7,8),2,4)
    print(m1['add_line']((1,3,5,7)))
    print(m1['add_column']((2,4,6)))
    mat1 = m1['print']()
    for _ in range(m1['line']()):
        line = mat1['print']()
        for _ in range(m1['column']()):
            print(line['print'](), end=' ')
        print()
    print(m1['shift_up']())
    print(m1['shift_right']())
    print(m1['transpose']())
    mat1 = m1['print']()
    for _ in range(m1['line']()):
        line = mat1['print']()
        for _ in range(m1['column']()):
            print(line['print'](), end=' ')
        print()
    #"""

# ------------------------------------------------
'''
<<< Q1 >>>
<function make_time.<locals>.dispatch at 0x000001D35DF3FA60>
11
5
11:05:47
12:12 A.M.
10:53:24
12:22:50 P.M.
23:57:03
11:57 P.M.
<<< Q2 >>>
<function make_tree.<locals>.dispatch at 0x000001D35DF3FEC0>
12
6
<function make_tree.<locals>.dispatch at 0x000001D35DF3FCE0>
2
8 6 12 2 7 15 
2
15 7 2 12 6 8 
<<< Q3 >>>
(-45, 133, 7, -300)
<<< Q4 >>>
[('London', 18), ('Paris', 20), ('Madrid', 35), ('Berlin', 20), ('Roma', 32)]
['Paris', 'Madrid']
False
True
{0: ['Berlin'], 2: ['London', 'Paris'], 5: ['Madrid', 'Roma']}
<<< Q5 >>>
<function sets.<locals>.dispatch at 0x000001D35DF4C9A0>
{1, 2, 3, 4, 5}
True
True
False
<function sets.<locals>.dispatch at 0x000001D35DF4D120>
{6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
{6, 8, 11, 13, 15, 18, 19}
{1, 2, 5, 7, 9, 17}
<<< Q6 >>>
[1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5, 7]
[1, 2, 3, 4, 2, 5, 6, 7, 8, 4, 1, 3, 5, 7, 6]
1 2 3 4 2 
5 6 7 8 4 
1 3 5 7 6 
[5, 6, 7, 8, 4, 1, 3, 5, 7, 6, 1, 2, 3, 4, 2]
[4, 5, 6, 7, 8, 6, 1, 3, 5, 7, 2, 1, 2, 3, 4]
[4, 6, 2, 5, 1, 1, 6, 3, 2, 7, 5, 3, 8, 7, 4]
4 6 2 
5 1 1 
6 3 2 
7 5 3 
8 7 4 
'''
driver()