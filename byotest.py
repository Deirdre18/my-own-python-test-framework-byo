
def number_of_evens(numbers):
    
    return 0

#def test_are_equal(actual, expected):
 #  assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
   
    
#(Challenge 1 - test 1 failed )- AssertionError: Expected 0, but got 0.
def test_not_equal(a, b):
     assert a != b, "Did not expect {0}, but got {1}".format(a, b)

 
#(Challenge 2 - test 2 failed) - AssertionError: (6, 2) does contain 5.           
#def test_is_in(collection, item):
 #       assert item in collection, "{0} does contain {1}".format(collection, item)        


 
#--NEW TESTS--

#(Challenge 3 - test 3 passed) AssertionError: [1, 2] does not contain 9
#def test_not_in(collection, item): 
 #   assert item in collection, "{0} does not contain {1}".format(collection, item)        


#def test_between(collection, item): 
 #    assert item in collection, "{0} does contain {1}".format(collection, item)        

     
#test_are_equal(number_of_evens([1,2,3,4,5]), 2)

test_not_equal(number_of_evens([0]), 0)
 
#test_not_in([1,2,], 9)
  
#test_between([1:5] ,2)  
    
          
 #new test - test between (example of testing in a range):-
 
 #https://www.w3resource.com/python-exercises/python-functions-exercise-6.php
 
#def test_range(n):
 #   if n in range(3,9):
  #      print( " %s is in the range"%str(n))
   # else :
    #    print("The number is outside the given range.")
#test_range(5)


#Other python tests are on this website:

#https://www.w3resource.com/python-exercises/python-functions-exercises

     
    #--CHALLENGES--
    #Then try the challenges that are at the bottom of this page. Firstly, try writing some tests that fail the tests_not_equal and the test_is_in methods to make sure you understand how to use them properly. 
    
    #Then, try writing some new test methods. Create one called "test_not_in" which checks that an item is not in a collection. 
    
    #Then create "test_between" which tests that a value is between a lower and upper limit inclusive. 
    
    #Finally, just as we've done here, save your test methods in a Python file called byotest.py. BYO stands for "build your own". Then, when you want to perform testing on your own projects, you can import byotest.py. We're going to use this test framework in the upcoming mini project. Remember, before you create your byotest.py file, to initialize a git repository and then to add and commit your files to it as we go along. In our next unit, we'll have a look at our mini project for this section End of transcript. Skip to the start.



#--CHALLENGES


#Challenge 1
 
#Write some tests that fail the test_not_equal, and test_is_in test methods. Verify that the message is correct for the values given.

 #Challenge 2
 
#Write test methods for test_not_in which tests than an item is not in a collection, and test_between which tests that a value is between a lower and upper limit, inclusive.

 #Challenge 3
 
#Put your test methods in a python file called byotest.py (byo stands for 'build your own'). You should now be able to import byotest when you want to write tests. We will use your new test framework in the upcoming Mini Project.

 