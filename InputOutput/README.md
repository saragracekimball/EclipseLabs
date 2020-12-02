# Input/Output Assignment

## Part 1 - Output

Make sure the file <code>output.py</code> is selected in the text editor to the right.

The function <Code>print()</Code> will output to the terminal (also called the console).

Whatever is inside the parenthesis will be printed to the screen.

* **Remember to use quotation marks**

Example:

    print("Hello and welcome to Eclipse")

### To run the file output.py, go to the terminal and use the following command: 
> $ python output.py

{% next %}

## Part 2 - Variables

Variables store data. To assign a value to a variable use the format

    name = "Ryan"

The variable will then be stored in the computer for the rest of the program.

We can print out the value of a variable using <code>print()</code>

    print(name)

The print function can also print out multiple items if they are separated by commas.

    print("My name is", name)

### To try it out:
1. add the lines of code to the file output.py
2. use the same command as above:
> $ python output.py

{% next %}

## Part 3 - Input

Make sure the <code>input.py</code> file is open in the text editor on the right.

What if we want to get our data from the current user? We can use a function called <code>input()</code>. The input function prompts the user, then waits for the user to type something in the terminal window, followed by the <code>[Enter]</code> key. Then the input function "returns" whatever the user typed so that it can be stored in a variable.

For example:

    username = input()

Edit the file input.py in the text editor so that the program will
1. allow the user to input their name (use the input function)
2. print precisely <code>hello, [name] </code> where name is the name the user inputted.

### To run the file
> $ python input.py

{% spoiler "Hint" %}

To get the desired output, use the last line of the output.py file

{% endspoiler %} {% spoiler "Solution" %}

    print("Hello,", name)

{% endspoiler %}

## Part 4 - Your first program

Write a program called **dorm.py** which meets the following criteria:
1. ask the user a question like "What dorm do you live in?"
2. print the name of the dorm to the console along with a message which welcomes them back to campus.

To restart the lab, you can use the reset button in the top right corner (you will lose all progress)