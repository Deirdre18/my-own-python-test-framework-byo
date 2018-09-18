## Build Your Own Test Framework
 
- What is it?

Build your own reusable testing framework.


- What does it do?

Gives us a series of tests that we can use with our own functions.


- How do you use it?

Import the byotest module, which we will create in this lesson.

In this unit we're going to bring everything that we've learned together
and we're going to build our own testing framework. So far the tests that we've
written have just been simple assertions. If they fail we see an error message
associated with that assertion, but we don't see the actual value that our
function returned. All we got is an error message to tell
us it was the wrong value. We can improve on this by wrapping our assertion in a
function. Have a look at this, for example. We're going to define a function called
"test are equal" and that takes two arguments. The actual value and the
expected value. Then we use assert to see if the expected and the actual are equal. If
they're not we return an error message. But this time what we're going to do, as
we did before, is put values into our error message to make it more
understandable; and you remember we do that using the format function. So let's
see this in practice. Above it we'll define a very simple function we'll call
it "number of evens" like we did before. It expects to take "numbers" as an argument,
but this time we're just going to put return 0. Now we can call our testing
function by typing test_are_equal, so what are we expecting to come back?
Well, let's pass in a value to our number_of_evens. We'll pass in an array of 1 2 3 4 5
So we're expecting, then, to get back the number two because there are two
even numbers in there. Of course we know this isn't going to work because we're
returning 0, but let's save it and see what happens.
As you can see our tests worked. We have an assertion error at the end there, but
this time it's much more verbose. It's telling us that we're we expected
to get the value of 2, but we actually got 0. We can see that
by what we passed in to the test_are_equal function we sent in the
actual and we also sent in what we would expect. The function then performed the
test for us and gave us the error message.
Now, when you understand how this works, then you can write other tests as
well. For instance, we could write another one and call it test_not_equal. This time,
for ease, we'll just use a and b. So again we can assert now that a, our expected,
does not equal b - our actual. We have to change our error message as well.
It doesn't end there! There is almost any number of tests that we can write.
For example, we could write one to see if an item is in a collection. Let's just
move the window down a little bit to get a bit more space and then we're going to
write a function called "test_is_in". That will pass in a collection and an
item, and then we're going to assert that the item is in the collection. If it's
not then the error message tells us that our collection name does not contain the
item that we sent in. Again our format method takes the collection and item. So take a
few minutes to look over these tests and understand how they work. Then try
the challenges that are at the bottom of this page. Firstly, try writing some tests
that fail the tests_not_equal and the test_is_in methods to make sure you
understand how to use them properly. Then, try writing some new test methods. Create
one called "test_not_in" which checks that an item is not in a collection. Then
create "test_between" which tests that a value is between a lower and upper limit
inclusive. Finally, just as we've done here,
save your test methods in a Python file called byotest.py. BYO stands for "build
your own". Then, when you want to perform testing on your own projects, you can
import byotest.py. We're going to use this test framework in the upcoming mini
project. Remember, before you create your byotest.py file, to initialize a git
repository and then to add and commit your files to it as we go along. In our
next unit, we'll have a look at our mini project for this section
End of transcript. Skip to the start.
View Source Code
 Challenge 1
 Challenge Hint
Write some tests that fail the test_not_equal, and test_is_in test methods. Verify that the message is correct for the values given.

 Challenge 2
 Challenge Hint
Write test methods for test_not_in which tests than an item is not in a collection, and test_between which tests that a value is between a lower and upper limit, inclusive.

 Challenge 3
 Challenge Hint
Put your test methods in a python file called byotest.py (byo stands for 'build your own'). You should now be able to import byotest when you want to write tests. We will use your new test framework in the upcoming Mini Project.

  