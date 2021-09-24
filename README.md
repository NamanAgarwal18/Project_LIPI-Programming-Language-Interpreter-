# Lipi Programming Language

## Description
**Lipi** is a small programming language created by Naman Agarwal. It supports various fundamental programming concepts such as variable-declaration, function calling, conditional statements, loops, proper order of operations, and recursion. Along with the language there is a **Python** based interpreter to run the code written in Lipi. The execution of a program in Lipi starts with the main function which does not return anything.

## Language Grammar
### 1. Variable Declaration:
* There is no need to specify the data type.
* All variables start with a ```$``` symbol. 
* A variable can hold a ```int```, ```double``` or a ```string```.
* There are no boolean values in Lipi, so ```True``` and ```False``` are represented as ```1``` and ```0``` respectively.
  ```java
  # Wrong Declaration
    int $number1 = 20
    number2 = 20
    $name = Naman
    $boolValue = True
  
  # Right Declaration
    $number2 = 20
    $name = "Naman"
    $name = 30.52
    $boolValue = 1
  ```
