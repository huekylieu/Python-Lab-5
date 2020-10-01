## Lab 5: Required Questions - Dictionaries Questions ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    "*** YOUR CODE HERE ***"
    new = {}
    new = dict(dict1)
    new.update(dict2) 

    for x, a in dict1.items():
        for y, b in dict2.items():
            if x == y:
                new[x]=(a+b)
    return new


# RQ2
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"


# RQ3
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"

# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys value pairs. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
   True
   """
   "*** YOUR CODE HERE ***"

#RQ5
def middle_tweet(word, table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string that is of length right in middle of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """"
    "*** YOUR CODE HERE ***"


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
