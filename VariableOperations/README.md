# Variable Operations Assignment

## Part 1 - Entering different types

Begin by running the file to the right.

When run, the program should ask the user for a value, then multiply it by 2 and print it out.

Section 1 should look familiar as we get input--

```python
number = input("Enter an integer value:")
```

Section 2 looks a little bit different.
Note the different syntax from what we have been using before.

```python
import cs50
value = cs50.get_int("Enter another integer value:")
```

**Notice that these lines are asking the user to enter a value, but only accepts an integer. Because of that, the variable value can be treated like a number.**

{% next %}

## Part 2 - Writing a simple program

Create a program called <code>circles.py</code> which does the following. *Model your code after Section 2.*

 - Store the value of pi (3.14) in a variable
 - Ask the user to enter a value of the radius of a circle (as an integer)
 - Print out the circumference of that circle.
 - Print out the area of that circle.

{% next %}

## Part 3 - Changing a variable

Create another program called <code>barter.py</code> which does the following.

 - Ask the user how much money they would want in exchange for their shoes.
 - Multiply that price by 0.9, because it doesn't want to pay full price
 - Print out a message saying "I will buy them for -value-"

For example: 
```
How much do you want for your shoes? 100
That's too much, I will buy them for $90!
```