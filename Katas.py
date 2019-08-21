# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.
#
# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
# Input
#
# Input will consist of a list of lists containing two items each. Each list contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.
#
# Note for F#: The input will be of (int list list) which is a List<List>
# Example Input
#
# [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
#
# Output
#
# Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.
# Example Output
#
# ["Open", "Open", "Senior", "Open", "Open", "Senior"]

#BDD:
#The input willbe integer of giving the data as years and the value of handicarp
# The output should be a string of either two values in a list, the open or senior
# SUDO CODE:
# Our sudo code will be in python language:
# we will pass the data into a function openSnior
#return an argument with a branching if, and, and  a loop 'for .. in'
# SOLUTION ONE


def openOrSenior(data):
    return ["Senior" if m[0] > 54 and m[1] > 7 else "Open" for m in data]


# REFFERED SOLUTION

def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


# CHALLENGE TWO
"""
Well met with Fibonacci bigger brother, AKA Tribonacci.
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1,1,1] as a starting input (AKA signature), we have this sequence:
```
[1,1,1,3,5,9,17,31,...]
```
But what if we started with [0,0,1] as a signature? As starting with [0,1] instead of [1,1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
```
[0,0,1,1,2,4,7,13,24,...]
```
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if `n==0`, then return an empty array and be ready for anything else which is not clearly specified ;)
If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata
"""
# BDD:
#Define a function tribonacci and pass signature and number n of the elements;
# Input the signature and number n
# <Output the tribonacci resulting
#SUDO code:
#define a function tribonacy
#define an empty listing of the inputed tribonacci
# branch using a 'for .. in ' loop
# paaend the new signature element n, and the tribonacci as the final element appended
# return tribonacci


def tribonacci(signature, n):
    #your code here
    tribonacci = []
    for i in range(n):
        new_element = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_element)
        element = signature.pop(0)
        tribonacci.append(element)
    return tribonacci

# possible sollutions REFFERED


def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3):
      res.append(sum(res[-3:]))
  return res
    
 # second


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]

# third


def tribonacci(s, n):
    for i in range(3, n):
        s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]

# fourth


def tribonacci(signature, n):
    return signature[:n] if n <= len(signature) else tribonacci(signature + [sum(signature[-3:])], n)

# fifth


def tribonacci(sig, n):
    return [sig[i] for i in range(n) if not sig.append(sum(sig[-3:]))]


# # third CHALLENGE
#
# // Your task is to write a function maskify, which changes all but the last four characters into '#'.
#
# // Examples
# // maskify("4556364607935616") == "############5616"
# // maskify(     "64607935616") ==      "#######5616"
# // maskify(               "1") ==                "1"
# // maskify(                "") ==                 ""
#
# // "What was the name of your first pet?"
# // maskify("Skippy")                                   == "##ippy"
# // maskify("Nananananananananananananananana Batman!") == "####################################man!"


# // return masked string
# BDD :
    # Input : a string of the secret word
    # Output : a string with the last four letters #

#SUDO CODE:
    #define a function maskify and pass an argument cc for secret key in this function
    # return the secret key replaced using the replace method with a hash on the last four ;etters.

function maskify(cc) {
    return cc.replace(/.(?=.{4, }$)/g, '#')
}


# Fourth CHALLENGE Given an input n, write a function always that returns a function n. Rubby shuld return a lambda or a p[roc]

# function always(n){
# return function(){return n};
# }

# 21/8/19
# Wilson primes satisfy the following condition. Let P represent a prime number.
#
# Then ((P-1)! + 1) / (P * P) should give a whole number.
#
# Your task is to create a function that returns true if the given number is a Wilson prime.

# BDD

# Define a function that takes a numerical variable, tests whther it is a wilson's prime, and rturns a true or false respectively

# | Input               |    Output             |
# |_____________________|_______________________|
# | 88                  | False                 |
# | 563                 | True                  |
# | 5                   | True                  |
# | 13                  | True                  |
#  Note: there three clearly known Wilson's Pirme numbers .
# A Wilson prime, named after English mathematician John Wilson, is a prime number p such that p² divides! + 1, where "!" denotes the factorial function; compare this with Wilson's theorem, which states that every prime p divides! + 1.

# Sudo code:

#  define a function(pass in the variable n):
# branch using a conditional statement if (math's formula, the factorial method (of n-1)+1) modulo (n*n) is equal to zero remainder):
# return True if this is a Wilson's prime
# else:
# return False

def am_i_wilson(n):
    if ((math.factorial(n-1)+1) % (n*n) == 0):
        return True
    else:
        return False


# Fifth sweetener


# Challenge 5. Does my number look big in this?
# A Narcissistic Number is a number which is the sum of its own digits,
# each raised to the power of the number of digits.
# Return true or false depending upon whether the given number is a Narcissistic number.

# BDD
# Define a function narcissistic that takes a value integer and returns true or false if the number is nacissistic

# input: a nuber;
# output : a boolean

# sudo code
# define a function and pass a value into the value
    # return the sum of the index if integers that forms the number iterate through the string of indices forming the value using a for .... in loop, output a boolean if the value is nassistic

def narcissistic(value):
    return bool(sum(int(i)**len(str(value)) for i in str(value)) == value)

# solution two sure by mercyjohn
def narcissistic( value ):
    sum_of_power = 0
    for i in range(0,len(str(value))):
        sum_of_power += int(str(value)[i])**int(len(str(value)))
    return sum_of_power == value
# Solution three/ reffered
def narcissistic(value):
    return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))

# Test Six

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

#BDD:
    #   The program takes in a list of numbers and loops through them to check if it is either an even or an odd number, if else, it returns the outlier, that is, the odd-one-out
    # |Input             | Output                            |
    # |__________________|___________________________________|
    # |2, 4, 6, 8, 10, 3]| 3                                 |

    #In the above example 3 is the odd-one-out since when divided by two, there is one as a remainder, thus not even

    # |Input                    | Output                            |
    # |_________________________|___________________________________|
    # |160, 3, 1719, 19,11|     |  11                               |


# SUDO CODE:
    # define a function and pass integer into the function:
        #  declare variables evens & odds and assign an empty array where we will be appending our data
        #  iterate through the provided array of integers using a for .. in loop to find out whether they are even or odd:
            #  Using if statements, branch the programe when the integer is even and append it to the evens array
            #  Using if statements, branch the programe when the integer is odd and append it to the odds array
        # using if statements, branch the programme to find out the outlier by defining whether the array is of even as a majority, in such case, a number that is not is the outlier:
            # return the outlier as  odd, else if not odd, return as even #??????


def find_outlier(integers):
    evens = []
    odds = []
    for i in integers:
        if i % 2 > 0:
            odds.append(i)
        if i % 2 == 0:
            evens.append(i)
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]
# second solution, voted best on codewars
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]