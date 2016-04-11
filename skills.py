"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """

    all_odd_nums = [] # create an empty list
    for each_number in number_list: # iterate through each number in the list
        if each_number % 2 == 1: # if number is divided by 2 and has a remainder it is an odd number
            all_odd_nums.append(each_number) # append odd number to the all_odd_nums list
    return all_odd_nums # return the list of odd numbers

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    all_even_nums = [] # create an empty list
    for each_number in number_list: # iterate through each number in the list
        if each_number % 2 == 0: # if number is divided by 2 and has no remainder it is even
            all_even_nums.append(each_number) # append even numbers to he all_even_nums list
    return all_even_nums # return the list of even numbers

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    for each_car in range(len(my_list)): # Iterate through each item in the list
        print "{} {}".format(each_car, my_list[each_car]) #print the index and value

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    long_words = [] # create an empty list
    for each_word in word_list: # iterate through each word in the list
        if len(each_word) > 4: # compare length of each word 
            long_words.append(each_word) # append each word to the long_words list
    return long_words # return the list with long words 

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    # the below will only grab the first number
    # smallest_int = 999999999
    # for each_integer in number_list: # iterate through each integer in the list
    #     if each_integer < smallest_int:
    #         smallest_int = each_integer
    #     return smallest_int

    # smallest_int = number_list.sort(number_list)
    # return smallest_int[0]

    # sorted_list = sorted(number_list)
    # smallest_int = sorted_list[0]
    # return smallest_int

    return sorted(number_list)[0]

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    # largest_int = 0
    # for each_num in number_list:
    #     if each_num > largest_int:
    #         largest_int = each_number
    if number_list == None:
        return
    else:
        return sorted(number_list)[-1]

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    # using comprehension to divide each number in the number_list by 2 and returning the number
    half_of_number = [each_num / 2.0 for each_num in number_list]
    return half_of_number


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    word_length = [] # create an empty list
    for each_word in word_list: # iterate throught each word in the list
        word_length.append(len(each_word)) # append the list with the lenght of each word
    return word_length # return the list

def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    sum_of_each_number = 0 # create a variable
    for each_number in number_list: # iterate through each number in the list
        sum_of_each_number += each_number # add each number and reassign the sum_of_each_number
    return sum_of_each_number # return the total number


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    product_of_number = 1 # create a variable
    for each_number in number_list: # iterate through each number in the list
        if each_number == 0:
            return product_of_number * 0
        elif each_number > 1:
            product_of_each_number = product_of_each_number * each_number
            return product_of_each_number  # return the product of all the numbers if 0 is not in the list
        else:
            return 1

def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    joined_word = []
    for each_word in word_list:
        joined_word = reduce(lambda x,y:x+y,word_list)  # i don't understand this but i found this on stack overflow 
        if word_list == []:
            return ''
    return joined_word


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    return sum(number_list) / float(len(number_list))


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    return ", ".join(list_of_words)


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
