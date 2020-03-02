import random
import pdb

# Floyd Triangle
"""Floyd Triangle is like this
1
23
456
78910
1112131415
161718192021
22232425262728

Write a custom program to display the Floyd Triangle
based on the number of rows provided by the user.
"""
# solution
"""
the first row starts with an element; 1 and then we 
continue with the next row by adding one more element. 
"""
def floyd_triangle(rows):
    triangle = [[1,]]
    current_row = [1,]
    new_row = []
    el = current_row[-1]
    row_cycles = rows - 1
    for cycle in range(row_cycles):
       cycles = len(current_row) + 1
       for cycle in range(cycles):
           el = el + 1
           new_row.append(el)
       current_row = new_row
       triangle.append(current_row)
       el = current_row[-1]
       new_row = []            
    return triangle


def display_triangle(triangle):
    for row in triangle:
        row = [str(i) for i in row]
        res  = int("".join(row))
        print(res)

"""
Print prime numbers in python
"""
# solution
"""
A prime number is a number which can be divided only
with one and with itself.
1, 3, 5, 7, 11, 13...
"""
def gen_primes(prime_range):
    primes = []
    for num in range(prime_range+1)[1:]:
        prime = True
        for x in range(num):
            if x not in (0,1):
                if num % x == 0:
                    prime = False
                    break
        # pdb.set_trace()
        if prime:
            primes.append(num)
    #pdb.set_trace()
    return primes

"""
Write a program to find out if a number is palindrone
or not.
"""
# solution
"""
A palindrone number is a number that remains the same
when the digits are reversed. 111->111, 101->101, 121->121 etc
"""
def is_palindrome(number):
    pass

"""
A one-year old queen forms a new colony with a single male. Each year they
have a new litter of pups.The number of pups for this queen just happen to
follow a special pattern: 2 pups in the first year, then 3 the next, then
5 the next, 8 the next and so on.This queen dies before any of her pups or
the original male.
Write an efficent program to work out the size of her colony after each year
if the pattern is followed until she dies.
"""
# solution
"""
The pattern for the colony is a fibonacci progression.Each year of reproduction
matches an element in the fibonacci sequence. So the size of the colony is just
the sum of the fibonacci sequences for as long as the queen lives.
1. The first thing we should do is to generate the fibonacci sequence.
2. Then write an algo to find the sum of elements in the sequence. 
"""
def colony_size(year):
    current_index = 0
    queen_lives = True
    years = 1
    fibonnaci_pups = [2,]
    while years < year:
        years +=1
        if years == 2:
            fibonnaci_pups.append(3)
        if years > 2:
            next_index = current_index + 1
            next_pups = fibonnaci_pups[current_index] + fibonnaci_pups[next_index]
            fibonnaci_pups.append(next_pups)
            current_index = current_index + 1

    return fibonnaci_pups
        
"""
Add two numbers without using the addition operator.
"""
# first method
def add_nums(a, b):
    return a-(-b)

# second method
def add_nums_no_plus(a, b):
   
    while (a > 0):
        a -= 1
        b += 1
   
    while a < 0:
        b -=1
        a += 1
    return b
"""
Write a function to check if a number is even or odd.
Then write it again without the conditionals.
"""
# solution
def even(num):
    is_even = False
    if num % 2 == 0 or num == 0:
        is_even = True

    return is_even

def is_even(num):
    if num == 0:
        return True

    x = num / 2
    return 2 * x == num

def is_it_even(num):
    pass

"""
Find the minimum of an array without using builtin,
then find the maximum.
"""
def find_min(array=[]):
    minimo = array[0]
    for el in array[1:]:
        if minimo > el:
            minimo = el

    return minimo

def find_max(array):
    pass

"""
Sort an array without using the builtin.
"""
def sort_array(array):
    # [13, 14, 11, 2, 1] --> [1, 2, 11, 13, 14]
    sorted_list = []
    while len(array) > 0:
        minimal = find_min(array)
        sorted_list.append(minimal)
        array.remove(minimal)
    return sorted_list

"""
Implement power function without using the multiplication
or division operators.
"""
def power(a, b):
    # a * a... -->b times
    result = 0
    initial_temp = a
    for cycle in range(b-1):
        for cycle in range(a):
            result += initial_temp
        initial_temp = result
        result = 0
    return initial_temp

"""
Ross brings 5 * 6 = 30 slices.
Rachel brings 3 * 6 = 18 slices.
Joey gets 2 slices from Rachel and 14 from Ross.
Since Joey has $8 in total; each slice would cost
$8/16 = $0.5.

Rachel should be paid 2 * $0.5 = $1.
Ross should be paid 14 * $0.5 = $7.

Let's write the program to automatically calculate it.
"""

"""
Multiples.
Given n and m print the m multiples of n
Input: n = 2, m = 3
Output: 2, 4, 6
"""
def find_multiples(n, m):
    possible_multiple = n
    multiples = [n,]
    while len(multiples) < m:
        possible_multiple += 1
        if possible_multiple % n == 0:
            multiples.append(possible_multiple)
    return multiples

# implement the above solution without any kind of loop.
def find_multiples_no_loop(n, m):
    return range(n, (n*m)+1, n)

"""
Write a program which will find all the numbers which are divisible
by 7 but are not a multiple of 5, between 2000 and 3200. The nums
should be printed in a comma-separated sequence on a single line.
"""
# solution
def divisible7():
    nums = []
    for el in range(2000, 3200):
        if el % 7 == 0 and el % 5 != 0:
            nums.append(el)
        line = ','.join(str(num) for num in nums)

    print(line)


"""
Write a program to compute the factorial of a given number.
"""
# solution
def factorial(number):
    result = 1
    factors = range(number+1)[1:]
    for factor in factors:
        result *= factor

    return result

# the following is a more elegant solution
def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

"""
Write a program which accepts a sequence of comma
separated values from the console and generates a
list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34, 67, 55, 33, 12, 98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question,
it should be assumed to be a console input.
"""
# solution
def sequence_convert():
    sequence = raw_input()
    l = sequence.split(',')
    t = tuple(l)
    print(l)
    print(t)

"""
Write a program which accepts a sentence and calculates
the number of uppercase letters and lowercase letters.
Suppose the following input is provided to the program:
Hello world!
Then the output should be:
UPPER CASE 1
LOWER CASE 9
"""
# solution
def uppercase_lowercase():
    d = {'UPPER_CASE':[], 'LOWER_CASE':[]}
    sequence = raw_input("Type here:")
    for c in sequence:
        if c.isupper():
            d['UPPER_CASE'].append(c)
        elif c.islower:
            d['LOWER_CASE'].append(c)
    
    print('UPPER CASE %d' % len(d['UPPER_CASE']))
    print('LOWER CASE %s' % len(d['LOWER_CASE']))

"""
Write a program that computes a value of a+aa+aaa+aaaa with
a given digit as the value of a. Suppose the following input
is supplied to the program:
9
Then, the output should be:
11106
"""
# solution
def compute_expression():
    a = raw_input("Enter digit:")
    num1 = int("%s" % a)
    num2 = int("%s%s" % (a, a))
    num3 = int("%s%s%s" % (a, a, a))
    num4 = int("%s%s%s%s" % (a, a, a, a))
    s = num1 + num2 + num3 + num4
    return s

"""
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
"""
# solution
def filter_oddnums():
    sequence = raw_input("Type sequence of numbers:")
    sequence = [x for x in sequence.split(',') if int(x)%2!=0]
    sequence = ','.join(sequence)
    print(sequence)

"""
Write a program that computes the net amount of a bank account
based on a transaction log from console input. The transaction
log format is shown as following:
D 100
W 200
D means deposit while W means withdrawl.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
# solution
def bank_amount():
    net_amount = 0 # initial amount equals 0 
    while True:
        sq = raw_input("Enter operation and amount:")
        if not sq:
            break

        values = sq.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation == "D":
            net_amount += amount
        elif operation == "W":
            net_amount -= amount
        else:
            pass
    print(net_amount)

"""
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords 
and will check them according to the above criteria. Passwords that match
 the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed 
to be a console input.
"""
def validate_password():
    pass


"""
Write a program to sort the (name, age, height) tuples
by ascending order where name is string, age and height
are numbers. The tuples are input by console.The criteria
is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score,
The priority is that name > age > score.
If the following tuples are given as input
to the program:
Tom, 19, 80
John, 20, 90
Jony 17, 91
Jony, 17, 93
Json, 21, 85
Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'),
('Tom', '19', '80')]
"""

"""
A robot moves in a plane starting from the original point (0, 0). Write
a program to compute the distance from the original point after a sequence
of movements. 
If the following tuples are given as input:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then the output of the program should be 2.
"""
# solution
def calc_distance():
    import math
    distance = 0
    initial_position = (0, 0)
    # new_position = None
    while True:
        move = raw_input("Enter the move:").split(" ")
        if move[0] == "UP":
            initial_position = (initial_position[0], initial_position[1]+int(move[1]))
        elif move[0] == "DOWN":
            initial_position = (initial_position[0], initial_position[1]-int(move[1]))
        elif move[0] == "RIGHT":
            initial_position = (initial_position[0]+int(move[1]), initial_position[1])
        elif move[0] == "LEFT":
            initial_position = (initial_position[0]-int(move[1]), initial_position[1])
        else:
            break
    x = initial_position[0]
    y = initial_position[1]
    distance = math.sqrt(x*x + y*y) 
    return distance

"""
Write a program that will print the following pattern.
1******
12*****
123****
1234***
12345**
123456*
1234567
"""
# solution
def display_pattern():
    index = 0
    full_sq = ""
    num_sq = ""
    nums = [1, 2, 3, 4, 5, 6, 7]
    stars = ["*", "*", "*", "*", "*", "*"]
    for cycle in range(7):
        num_sq += str(nums[index])
        full_sq = num_sq + "".join(stars)
        print(full_sq)
        if len(stars):
            stars.pop()
        index += 1

# solution, another way
def print_pattern():
    nums_list = []
    full_list = []
    index = 0
    nums = [1, 2, 3, 4 ,5, 6, 7]
    stars = ["*", "*", "*", "*", "*", "*"]
    while len(stars) >= 0:
        nums_list.append(nums[index])
        full_list.extend(nums_list)
        full_list.extend(stars)
        sq = "{0}{1}{2}{3}{4}{5}{6}".format(*full_list)
        print(sq)
        index +=1
        if len(stars):
            stars.pop()
        full_list = []

# find a more elegant way to print the pattern
def gen_pattern():
    pass

"""
Define a function that can accept two strings as input
and print the string with maximum length on the console.
If two strings have the same length, then the function
should print all strings line by line.
"""
# solution
def longer_string(s1, s2):
    first_length = len(s1)
    second_length = len(s2)
    if first_length - second_length > 0:
        print(s1)
    elif first_length - second_length == 0:
        print(s1)
        print(s2)
    else:
        print(s2)

# is there a more elegant solution for the above?
"""
Define a function that can accept an integer number as input
and print the "It is an even number" if the number is even, otherwise
print "It is an odd number".
"""
# solution
def check_num(num):
    if num % 2 == 0:
        print("It's an even number.")
    else:
        print("It's an odd number.")

"""
Define a function which can print a dictionary where the keys are numbers
between 1 and 3 (both included) and the values are the square of the keys.
"""
# solution
def gen_dict():
    d = {}
    keys = [1, 2, 3]
    for el in keys:
        d[el] = el * el
    return d

"""
Write a program to generate and print another tuple whose values are even
numbers in the given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10).
"""
def gen_tup():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    num_list = []
    for el in tup:
        if el % 2 == 0:
            num_list.append(el)
    num_list = tuple(num_list)
    return num_list

"""
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""
def check_string():
    check_list = ["yes", "Yes", "YES"]
    sq = raw_input("Enter the sequence:")
    if sq in check_list:
        print("Yes")
    else:
        print("No")

# the following is another solution
def check_string_now():
    sq = raw_input("Enter the sequence:") 
    if sq == "yes" or sq == "Yes" or sq == "YES":
        print("Yes")
    else:
        print("No")

"""
Write a program to filter even numbers in a list using the
filter function.The list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
"""
def filter_list():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_nums = filter(lambda x:x%2==0, l) 
    print(even_nums)

"""
Define a class named American which has a static method
called printNationality. Hints: Use @staticmethod decorator
to define the class's static method.
"""
# solution
class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()

"""
Define a class American and its subclass NewYorker.
Hint: Use class SubClass(ParentClass) to define a subclass.
"""
# solution
class NewYorker(American):
    pass

"""
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.
"""
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius**2*3.14

"""
Define a class named Rectangle which can be constructed by length
and width. The Rectangle class has a method which can compute the 
area.
"""
# solution
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

"""
Write a function to compute 5/0 and use try/except to catch the 
exceptions. Hints: Use try/except to catch exceptions.
"""
def doesnt_throw():
    try:
        5/0
    except ZeroDivisionError:
        print("Division by zero.")
    except Exception, err:
        print("Caught an exception.")
    finally:
        print("Final block for cleanup.")

"""
Define a custom exception class which takes a string
message as attribute.Hints:To define a custome exception
define a class which inherits from builtin Exception.
"""
# solution
class MyCustomError(Exception):
    def __init__(self, msg):
        self.msg = msg

"""
Make use of the assert statement to verify that every number in
the list [2, 4, 6, 8] is even.
"""
def check_even():
    l = [2, 4, 6, 8]
    for el in l:
        assert(el%2 == 0)

"""
Write a program which takes basic arithmetic expression from
console and print the evaluation result.Example:
35 + 3
Then, the output of the program should be:
38
Hints: Use eval() to evaluate the expression.
"""
# solution
def eval_examp():
    exp_sq = raw_input("Enter the expression:")
    result = eval(exp_sq)
    print(result)

"""
Write a program to generate all the sentences where subject is
in ["I", "You"], verb is in ["Play", "Love"] and the object is
in ["Hockey", "Football"].
"""
def all_sentences():
    sentence = ""
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = " ".join([subject, verb, obj])
                print(sentence)
                sentence = ""

"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
prime factor of the number 600851475143"""
# solution


"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there 
is no upper bound on the number of cigars. Return True if the party
with the given values is successful, or False otherwise.
"""
# solution
# cigar_party(30, False)->False
# cigar_party(50, False)->True
# cigar_party(70, True)->True
# cigar_party(70, False)->False
def cigar_party(cigars, is_weekend):
    if cigars >= 40:
        if is_weekend:
            return True
        else:
            return cigars <= 60

    return False
  
"""
You and your date are trying to get a table at a restaurant.
The parameter "you" is the stylishness of your clothes, in
the range 0..10, and "date" is the stylishness of your date's
clothes.The result getting the table is encoded as int value
with 0=no, 1=maybe, 2=yes. If either of you is very stylish,
8 or more, then the result is 2 (yes). With the exception that
either of you has style of 2 or less, then the result is 0(no).
Otherwise the result is 1 (maybe).
"""
# date_fashion(5, 10)->2
# date_fashion(5, 2)->0
# date_fashion(5, 5)->1
# solution
def date_fashion(you, date):
    if you <=2 or date <=2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    else:
        return 1

"""
The squirrels in Palo Alto spend most of the day playing.In
particular, they playif the temperature is between 60 and 90.
Unless it is summer, then the upper limit is
100 instead of 90.Given an int temperature and a boolean 
is_summer, return True if the squirrels play and False
otherwise.
"""
# squirrel_play(70, False)->True
# squirrel_play(95, False)->False
# squirrel_play(95, True)->True
def squirrel_play(temp, is_summer):
    if temp>=60:
        if is_summer:
            return temp<=100
        else:
            return temp<=90
    return False

"""
You are driving a little too fast, and a police officer
stops you.Write code to compute the result, encoded as
an int value: 0=no ticket, 1=small ticket, 2=big ticket.
If speed is 60 or less, the result is 0.If speed is between
61 and 80 inclusive, the result is 1.If speed is 81 or more
the result is 2.Unless it is your birthday--on that day, your
speed can be 5 higher in all cases.
"""
# 0--> no ticket, 1--> small ticket, 2-->big ticket.
# caught_speeding(60, False)->0
# caught_speeding(65, False)->1
# caught_speeding(65, True)->0
def caught_speed(speed, is_birthday):
    pass

"""
Given 2 ints, a and b, return their sum. However, sums 
in the range 10..19 inclusive, are forbideen, so in that
case just return 20.
"""
# solution
def sorta_sum(a, b):
    total = a + b
    if total in range(10, 20):
        return 20
    return total

"""
Given a day of the week encoded as 0=Sun, 1=Mon,
2=Tue,...6=Sat, and a boolean indicating if we are
on a vacation, return a string of the form "7:00"
indicating when the alarm clock should ring.Weekdays,
the arlam should be "7:00" and on the weekend it should
be "10:00".Unless we are on vacation--then on weekdays it
should be "10:00" and weekends it should be "off".
"""
# alarm_clock(1, False)->'7:00'
# alarm_clock(5, False)->'7:00'
# alarm_clock(0, False)->'10:00'
def alarm_clock(day, vacation):
    first_alarm = "7:00"
    second_alarm = "10:00"
    if day in range(1, 6):
        if not vacation:
            return first_alarm
        else:
            return second_alarm
    if day == 0 or day == 6:
        if not vacation:
            return second_alarm
        else:
            return "off"

"""
The number 6 is truly a great number.Given two int
values, a and b, return True if either one is 6. Or
if their sum or difference is 6.Note: the function abs(num)
computes the absolute value of a number.
"""
# love6(6, 4)-->True
# love6(4, 5)-->False
# love(1, 5)-->True
def love6(a, b):
    if a == 6 or b == 6:
        return True
    if abs(a-b) == 6 or (a+b) == 6:
       return True
    return False

"""
Given a number n, return True if n is in the range
1..10, inclusive.Unless outside_mode is True, in which
case return True if the number is less or equal to 1,
or greater or equal to 10.
"""
# solution
def int1to10(n, outside_mode):
    if outside_mode:
        if n <=1 or n >= 10:
            return True
    else:
        return n in range(1, 11)
    return False

"""
Given a non-negative number "num", return True if
num is within 2 of a multiple of 10.Note: (a%b) is
the remainder of dividing a by b, so (7%5) is 2.
"""
# near_ten(12)-->True
# near_ten(17)-->False
# near_ten(19)-->True
def near_ten(num):
    return abs(num % 10) <=2 or abs(num % 10) >=8

"""
We want to make a row of bricks that is goal inches long.
We have a number of small bricks(1 inch each) and big bricks
(5 inches each).Return True if it is possible to make the goal
by choosing from the given bricks.
"""
# make_bricks(3, 1, 8)-->True
# make_bricks(3, 1, 9)-->False
# make_bricks(3, 2, 10)--True
# solution
def make_bricks(small, big, goal):
    if goal < 5:
        return goal <= small
    
    if goal/5 >= big:
        return ((goal/5 - big)*5 + (goal % 5)) <= small

    if goal/5 <= big:
        return (goal % 5) <= small

# the above works correctly

"""
Given 3 int values, a  b c, return their sum.However,
if one of the values is the same as another of the values,
it does not count towards the sum.
"""
# lone_sum(1, 2, 3)->6
# lone_sum(3, 2, 3)->2
# lone_sum(3, 3, 3)->0
#  solution
def lone_sum(a, b, c):
    if a==b and a==c:
        return 0
    elif a==b and a!=c:
        return c
    elif a==c and a!=b:
        return b
    elif c==b and c!=a:
        return a
    else:
        return a + b + c

# try to simplify the above solution

"""
Given 3 int values, a b c, return their sum.However, if one
of the values is 13, then it does not count towards the sum
and values to its right do not count.So for example, if b is
13 then both b and c do not count.
"""
# lucky_sum(1, 2, 3)-->6
# lucky_sum(1, 2, 13)-->3
# lucky_sum(1, 13, 3)-->1

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a+b
    else:
        return a + b + c

"""
Given 3 int values, a b c, return their sum.However,if any
of the values is a teen -- in the range 13..19 inclusive--
then that value counts as 0,except 15 and 16 do not count as 
teens.Write a separate helper "def fix_teen(n):" that takes
n as an int value and returns that value fixed for the teen
rule.In this way, you avoid repeating the teen code 3 times
(i.e. "decomposition").Define the helper below and at the same
indent level as the main no_teen_sum().
"""
# no_teen_sum(1, 2, 3)-->6
# no_teen_sum(2, 13, 1)-->3
# no_teen_sum(2, 1, 14-->3

def fix_teen(n):
    if n in range(11, 20):
        if n not in (15, 16):
            return n
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

"""
For this problem, we'll round an int value up to the next
multiple of 10 if its rightmost digit is 5 or more, so 15
rounds up to 20.Alternately, round down to the previous multiple
of 10 if its rightmost digit is less than 5, so 12 rounds down to
10.Given 3 ints, a b c, return the sum of their rounded values.To
avoid code repetition,write a separate helper "def round10(num):"
and call it 3 times.Write the helper entirely below and at the same
indent level as the round_sum().
"""
# round_sum(16, 17, 18)--> 60
# round_sum(12, 13, 14)--> 30
# round_sum(6, 4, 4)--> 10

def round10(num):
    if num < 5:
        return 0
    if num % 10 == 0:
        return num
    if num % 10 >= 5:
        return num + (10 - (num % 10))
    if num % 10 < 5:
        return num - (num % 5)


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

"""
Given three ints, a b c return True if one of b or c
is "close" (differing from a by at most 1), while the other
is "far", differing from both values by 2 or more.Note: abs(num)
computes the absolute value of a number.
"""
# close_far(1, 2, 10)-->True
# close_far(1, 2, 3)-->False
# close_far(4, 1, 3)-->True

def close_far(a, b, c):
    if abs(b-a) <= 1:
         return (abs(c-a) >=2 and abs(c-b)>=2)
    if abs(c-a) <= 1:
         return (abs(b-a)>=2 and abs(b-c)>=2)
    return False

"""
We want to make a package of goal kilos of chocolate.We have 
small bars (1 kilo each) and big bars (5 kilos each).Return 
the number of small bars to use, assuming we always use big
bars before small bars.Return -1 if it can't be done.
"""
# make_chocolate(4, 1, 9)-->4
# make_chocolate(4, 1, 10)-->-1
# make_chocolate(4, 1, 7)--> 2
# make_chocolate(6, 1, 10)-->5

def make_chocolate(small, big, goal):
    # we use the big bars first
    if goal/5 <= big:
        if goal % 5 <= small:
            return goal % 5
        else:
            return -1
    if goal/5 >= big:
        if (goal/5 - big) * 5 + (goal%5) <= small:
            return (goal/5 -big)*5 + goal % 5
        else:
            return -1

"""
Cows and Bulls.
Create a program that will play the "cows and bulls" game with
the user.The game works like this:Randomly generate a 4-digit
number.Ask the user to guess a 4-digit number.For every digit
that the user guessed correctly in the correct place, they have
a "cow". For every digit the user guessed correctly in the wrong
place is a "bull."Every time the user makes a guess, tell them
how many "cows" and "bulls" they have.Once the user guesses the
correct number the game is over.Keep track of the number of gu-
esses the user makes through the game and tell the user at the
end.
"""
# procedural decomposition
def digit_split(num):
    digits = []
    while num > 10:
        digit = num % 10
        num = num / 10
        digits.append(digit)
    
    if num == 10:
        digits.append(0)
        digits.append(1)
    else:
        last_digit = num % 10
        digits.append(last_digit)
   
    return list(reversed(digits))
         

def cow_or_bull(rand_num, user_num):
    cowbull = [0, 0] # cows, then bulls
    rand_digits = digit_split(rand_num)
    user_digits = digit_split(user_num)
    temp = [el for el in rand_digits]
    # [1, 2, 3, 4] & [1, 2, 5, 7]
    for idx in range(4):
        if user_digits[idx] in temp:
            if user_digits[idx] == rand_digits[idx]:
                cowbull[0] += 1
            else:
                cowbull[1] += 1
            temp.remove(user_digits[idx])

    return cowbull


def cb_game():
    while True:
        # ask_the_user_to_guess_a_digitnmm
        random_num = random.randint(1000, 9999)
        print("Random number is {}".format(random_num))
        user_num = int(raw_input("Enter 4 digit number:"))
        print("Guessed number is {}".format(user_num))
        cows_plus_bulls = cow_or_bull(random_num, user_num)
        if cows_plus_bulls[0] == 4:
            print("You Won.")    
            break
        print("{} cows, {} bulls".format(cows_plus_bulls[0], cows_plus_bulls[1])) 
       
