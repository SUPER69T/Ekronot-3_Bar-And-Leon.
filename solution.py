#names: Leon Subootsky,   Bar Cohen.
#IDs:   323862524,        324268309.
# ------------------------------------------------
#       Q1(ADT Date - dispatch)
# ------------------------------------------------
def make_time(h, m, s):
    """"
    @param: h-hours, m-minutes, s-seconds.
    """
    hours = h, minutes = m, seconds = s
    def inner_clock(clock_hand):
        if clock_hand == 0: return hours
        if clock_hand == 1: return minutes
        if clock_hand == 2: return seconds
    return inner_clock

# ------------------------------------------------
def getitem_pair(p, i):
    pass
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
    h_diff = time1(0) - time2(0)
    m_diff = time1(1) - time2(1)
    s_diff = time1(2) - time2(2)
    # -------
    return h_diff * 3600+ m_diff * 60 + s_diff
# ------------------------------------------------
def str_time(time, tformat = 'hh:mm:ss'):
    if tformat == 'hh:mm:ss':
        return f"{0}:{1}:{2}".format(time[0], time[1], time[2])
    elif tformat == 'hh:mm':
        return f"{0}:{1}".format(time[0], time[1])
    elif tformat == 'HH:MM':
        return f"{0}:{1}, {2}".format(time[0], time[1], "AM" if time[0] < 12 else "PM")
    elif tformat == 'HH:MM:SS':
        return f"{0}:{1}:{2}".format(time[0], time[1], time[2])
    else:
        return "Incompatible time format"
# ------------------------------------------------
def time_correction(time, corr = 0):
    #if corr == 0: time_correction will treat the make_time() instance as a regular time -
    #and will reformat and construct a new, corrected version of make_time().
    # -------
    ###checking for the sign of corr and modifying the sign of the time conversion operations:
    i = 1
    if corr < 0:
        i = -1
    ###
    # -------
    ###
    temp_s = (time(2) + corr) % 60
    ###(Seconds) after modulo - 60.
    ###
    temp_m = (time(1) + ((time(2) + corr) // 60 * i)) % 60
    ###(Minutes + (Seconds after division by - (60 * i))) after modulo - 60.
    ###
    temp_h = (time(0) + ((time(1) + ((time(2) + corr) // 60)) // 60 * i)) % 24
    ###(Hours + (Minutes + (Seconds after division by - 60)) after division by (60 * i)) after modulo - 24.
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
    pass
# ------------------------------------------------
def getitem_pair(p,i):
    pass
# ------------------------------------------------
def value(tree):
    pass
# ------------------------------------------------
def left(tree):
    pass
# ------------------------------------------------
def right(tree):
    pass
# ------------------------------------------------
def print_tree(tree):
    pass
# ------------------------------------------------
def min_value(tree):
    pass
# ------------------------------------------------
def mirror_tree(tree):
    pass
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
Q3 = lambda func,data: None
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
Q4a = lambda data: None
Q4b = lambda data: None
Q4c = lambda data: reduce(None)
Q4d = lambda data: None
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
    pass
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
'{6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}'
>>> s1('set',(1,2,3,4,5,7,9,12,17))
>>> s2('set',(2,4,5,10,14,16,20)) 
>>> s1('+',s2)('not')('view')
'{6, 8, 11, 13, 15, 18, 19}'
>>> s1('*',s2)('xor',s1('\\',sets((2,3,5,12))))('view')
'{1, 2, 5, 7, 9, 17}'
'''

# ------------------------------------------------
# Q6(Dispatch Dictionary, Message Passing-Matrix)
# ------------------------------------------------
def matrix(mtr,n,m):
    pass
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
    #"""
    print('<<< Q1 >>>')
    t1 = make_time(11,5,47)
    print(t1)
    print(hour(t1))
    print(minute(t1))
    print(str_time(t1))
    t2 = make_time(0,12,23)
    print(str_time(t2,'HH:MM'))
    print(str_time(time_difference(t1,t2)))
    print(str_time(time_correction(t1,4623),'HH:MM:SS'))
    t2 = time_correction(t2,-920)
    print(str_time(t2))
    print(str_time(t2,'HH:MM'))
    #"""
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
    print(Q3((lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100),
               (20,-45,133,8,400,7,-300,68)))
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
    s2('set',(2,4,5,10,14,16,20))
    print(s1('+',s2)('not')('view'))
    print(s1('*',s2)('xor',s1('\\',sets((2,3,5,12))))('view'))
    """
    """
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
    """

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