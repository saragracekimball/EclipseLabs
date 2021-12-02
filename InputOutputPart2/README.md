# Input/Output Assignment Section 2

## Part 1 - Variables

Variables store data. To assign a value to a variable use the format

    name = "Ryan"

The variable will then be stored in the computer for the duration of the program.

We can print out the value of a variable using <code>print()</code>

```print(name)```

The print function can also print out multiple items if they are separated by commas.

```print("My name is", name)```

### To try it out:
1. add the lines of code to a file above
2. use the command:
> $ python output.py

{% next %}

## Part 2 - Input

What if we want to get our data from the current user? We can use a function called <code>input()</code>. The input function prompts the user, then waits for the user to type something in the terminal window, followed by the <code>[Enter]</code> key. Then the input function "returns" whatever the user typed so that it can be stored in a variable.

In order to ask the user a question with the <code>input()</code> function, add a **prompt** message in the parenthesis. Remember that a string (a sequence of characters) must be in quotes.

For example:

```username = input("What is your username?")```

After this line of code, *username* will contain whatever the user enters.

Edit the file input.py in the text editor so that the program will
1. allow the user to input their name (use the input function)
2. print precisely <code>hello, [name]! </code> where [name] is the name the user inputted.

Example Run:
```
What is your name? McGee
Hello, McGee!
```

### To run the file
> $ python input.py

{% next %}

## Part 3 - Input/Output Program

Write a program called **dorm.py** which meets the following criteria:
1. ask the user a question: "What dorm do you live in?"
2. print the name of the dorm to the console along with a message which welcomes them back to campus.


Example Run:
```
What is your name? McGee
What dorm do you live in? Turner
Hi McGee, have a great year living on Turner
```

To restart the lab, you can use the reset button in the top right corner (you will lose all progress)