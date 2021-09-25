# Lipi Programming Language

## Description
**Lipi** is a small programming language created by Naman Agarwal. It supports various fundamental programming concepts such as variable-declaration, function calling, conditional statements, loops, proper order of operations, and recursion. Along with the language there is a **Python** based interpreter to run the code written in Lipi. 
 The execution of a program in Lipi starts with the main function which does not return anything. 
 Lipi does not use semi-colons to terminate statements, instead it relies on the fact that each new line is the start of a new statement and end of the previous. 
 In Lipi the words need to carefully spaced out.

## Language Grammar
### 1. Variable Declaration:
* There is no need to specify the data type.
* All variables start with a ```$``` symbol. 
* A variable can hold a ```int```, ```double``` or a ```string```.
* There are no boolean values in Lipi, so ```True``` and ```False``` are represented as ```1``` and ```0``` respectively.
  #### Grammer
  ```enbf
    variable-declaration  ::=  variable-name  assignment-operator  variable-body
    variable-name  ::=  identifier
    assignment-operator  ::=  "="
    variable-body  ::=  constant  |  expression  |  comparison
  ```
  #### Wrong Declaration
  ```java
      int $number1 = 20
      number2 = 20
      $name = Naman
      $boolValue = True
      $number3 = $name*($number1+30)
  ```
  #### Right Declaration
  ```java
      $number2 = 20
      $name = "Naman"
      $name = 30.52
      $boolValue = 1
      $number3 = $name * ( $number1 + 30 )
  ```
  
