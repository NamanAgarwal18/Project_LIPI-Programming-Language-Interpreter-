# Lipi Programming Language

## Description
**Lipi** is a small programming language created by Naman Agarwal. It supports various fundamental programming concepts such as variable-declaration, function calling, conditional statements, loops, proper order of operations, and recursion. Along with the language there is a **Python** based interpreter to run the code written in Lipi. <br>
The execution of a program in Lipi starts with the main function which does not return anything. <br>
Lipi does not use semi-colons to terminate statements, instead it relies on the fact that each new line is the start of a new statement and end of the previous. <br>
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
 ### 2. Conditional Statements: 
 * The conditional statement uses keyword `IS`
 * 


## Operators Available on `int` and `double` values
* `+`  -> for addition
* `-`  -> for substraction
* `*`  -> for multiplication
* `/`  -> for normal division
* `//` -> for floor division (returns integer)
* `%`  -> for modulus 
* `**` -> for raise to the power

  ```python
      $a = 20 + 30
      # $a = 50
      
      $b = 20 - 30
      # $a = -10
      
      $c = $a * $b
      # $c = -500
      
      $d = 101 / $a
      # $d = 2.02
      
      $e = 101 // $a
      # $e = 2
      
      $f = 101 % $a
      # $f = 1
      
      $g = 2 ** 3
      # $g = 8
  ```

## Operators Available on `string` values
* `+`  -> for concatenating strings
* `*`  -> for concatenating same string multiple times

  ```python
      $a = "naman"
      $b = "agarwal"
      
      $c = $a + $b
      # $c = "namanagarwal"
      
      $d = $a + 5
      # $d = "naman5"
      
      $e = $a * 3
      # $e = "namannamannaman" 
  ```

## Comparitors Available
#### Comparitors returns 1 for True and 0 for False
* `>`  -> to check greater than 
* `<`  -> to check less than 
* `>=` -> to check greater than equal to 
* `<=` -> to check less than equal to 
* `<>` -> to check equal to
* `><` -> to check not equal to 
* `[]` -> to check if absolute values are equal 
* `[]` -> to check if absolute values are not equal 
* `..` -> the logical AND
* `++` -> the logical OR

  ```python
      $a = "naman"
      $b = "agarwal"
      $c = 20
      $d = 35
      
      $e = $a > $b
      # $e = 1 ("naman" comes after "agarwal" alphabetically)
      
      $f  = $c >= $d
      # $f = 0 (35 > 20)
      
      $g = $c >< 21
      # $g = 1 (20 != 21)
      
      $h = $d <> -35
      # $h = 0 (35 != -35)
      
      $i = $a <> "naman"
      # $i = 1 ("naman" == "naman")
      
      $j = $b <> "Agarwal"
      # $j = 0 ("agarwal" != "Agarwal")
      
      $k = $d [] -35
      # $k = 1 ( abs(35) == abs(-35) )
      
      $l = $b [] "AgArwAl"
      # $l = 1 ( [] checks equality case insensitivity ) 
  ```
