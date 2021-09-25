# Lipi Programming Language

## Description
**Lipi** is a small programming language created by Naman Agarwal. It supports various fundamental programming concepts such as variable-declaration, function calling, conditional statements, loops, proper order of operations, and recursion. Along with the language there is a **Python** based interpreter to run the code written in Lipi. <br>
* The execution of a program in Lipi starts with the main function which does not return anything. 
* Lipi does not use *semi-colons* to terminate statements, instead it relies on the fact that each new line is the start of a new statement and end of the previous. 
* In Lipi the words need to carefully spaced out. 
* Lipi supports recursion.
* A variable is only available from inside the function it is created.

## Language Grammar
<details><summary><b> Click Here To See <i><ins>Language Grammar </ins></i></b></summary>
  
### 1. Variable Declaration:
* There is no need to specify the data type.
* All variables start with a `$` symbol. 
* A variable can hold a ```int```, ```double``` or a ```string```.
* There are no boolean values in Lipi, so ```True``` and ```False``` are represented as ```1``` and ```0``` respectively.
  #### Wrong Declaration:
  ```python
      int $number1 = 20
      number2 = 20
      $name = Naman
      $boolValue = True
      $number3 = $name*($number1+30)
  ```
  #### Right Declaration:
  ```python
      $number2 = 20
      $name = "Naman"
      $name = 30.52
      $boolValue = 1
      $number3 = $name * ( $number1 + 30 )
  ```
### 2. Input / Output Statements:
* We use `IN` keyword to input data and `OUT` keyword to display the data.
   #### 1. Input - `IN`:
     * The input statement can take in multiple inputs at a time seperated by a *space-bar*.
     * The input statement can also display a statement before inputting the data.
   #### 2. Output - `OUT`:
     * The output statement can display multiple statements and variables at a time seperated by a space bar.
   #### Incorrect Code:
   ```python
       IN Enter the $a variable $a

       OUT The value of $a is: $a
   ```
   #### Correct Code:
   ```python
       IN "Enter the $a variable" $a
       IN "Enter the value of $a: " $a ", the value of $b:" $b "and the value of $c:" $c

       OUT "The value of $a is:" $a
       OUT "The value of $a is:" $a ", $b is:" $b "and $c is" $c
   ```
### 3. Conditional Statements: 
* The conditional statement uses keyword `IS`
* The `IS` statement block has an option to be followed by `NONE` statement block acting as an `else` statement. 
* `IS` statement expects a 0 or 1 input in the form of a condition within the brackets. 
  #### Incorrect Code:
  ```python
      $a = 20
      $b = 30
      
      IS ( $a > $b )
          OUT $a "greater that" $b
      NONE IS ($a<>$b)
      {
          OUT $a "equal to" $b
      }
      NONE 
      {
          OUT $a "less than" $b
      }
      
      IS ( ( $a < 30 + 20 ) ++ ( 20 < $b .. $b < 50 ) )
      {
          OUT "True"
      }
  ```
  #### Correct Code:
  ```python
      $a = 20
      $b = 30
      
      IS ( $a > $b )
      {
          OUT $a "greater that" $b
      }
      NONE 
      {
          IS ( $a <> $b )
          {
            OUT $a "equal to" $b
          }
          NONE 
          {
            OUT $a "less than" $b
          }
      }
      
      IS ( ( $a < ( 30 + 20 ) ) ++ ( 20 < $b < 50 ) )
      {
          OUT "True"
      }
  ```
### 4. Loop Statements: 
* The loop stattement uses the keyword `LOOP`
* The Loop in Lipi is like `while` loop in other programming language.
* You can use an `EXIT` statement to break out of the loop if a certain condition is fulfilled.
* You can easily create nested loops to do your work.
  #### Incorrect Code:
  ```python
      LOOP ( $i > 30 )
      {
          OUT "In Loop"
      }
      
      $i = 0
      $j = 2
      LOOP ( $i < 30 )
      {
          $j = $j * $j
          $i = $i + 1
          IS ( $j > 200 )
          {
              EXIT
          }
       }
  ```
  #### Correct Code:
  ```python
      $i = 0
      LOOP ( $i > 30 )
      {
          OUT "In Loop"
          $i = $i + 1
      }
      
      $i = 0
      $j = 2
      LOOP ( $i < 30 )
      {
          $j = $j * $j
          $i = $i + 1
          EXIT ( $j > 200 )
      }
  ```
  #### Nested Loop:
  ```python 
      $d = 0
      $f = 0
      LOOP ( $d < 3 )
      {
          $e = 0
          LOOP ( $e < 3 )
          {
              $e = $e + 1
              $f = $f + 1
              EXIT ( $f > 5 )
          }
          $d = $d + 1
      }
      OUT "Exitted $d:" $d "and $e:" $e "and $f:" $f 
  ```
### 5.Functions:
* Lipi supports fucntions and by extention recursion.
  #### Fucntion Declaration: 
  * A function declaration starts with the `FN` keyword.
  * A fucntion does not have to start with a `$` symbol.
  * A function can have as many parameters as you want.
  * All the parameters can be written after the fucntion name seperated by a *space-bar*.
  * A function can return by using `RET` keyword.
  * `RET` can be used with a condition or without a condition.
    ##### Incorrect Code:
    ```python
        FN Add ( $n )
        {
            $n = $n + $n
            OUT $n
        }
        
        FN AddTwo $n $m
        {
            $a = $n + $m
            RET
        }
        
        FN isEven $a
        {
            IS ( $a % 2 <> 0 )
            {
                RET "Even"
            }
            RET "ODD"
        }
    ```
    ##### Correct Code:
    ```python
        FN Add $n
        {
            $n = $n + $n
            OUT $n
        }
        
        FN AddTwo $n $m
        {
            $a = $n + $m
            RET $a
        }
        
        FN isEven $a
        {
            $even = "Even"
            $odd = "Odd"
            RET ( $a % 2 <> 0 ) $even
            RET $odd
        }
    ```
  #### Fucntion Calling: 
    * A function can be called using `CALL` keyword.
    * The number of arguments given should be the same as the parameters required.
    * If the fucntion returns something then it is mandatory to give a variable to store the returned value.
    * You can still give a returning variable even if the fucntion doesn't return anything. In this case the returning variable would store 1 if the fucntion was run successfully.
      ##### Incorrect Code:
      ```python
          # Assume that fucntions 'Add' , 'AddTwo' and 'isEven' have the above mentioned declaration
          $a = 15
          $b = 20

          CALL Add ( $a )

          CALL Add 20

          $c = CALL Add $a

          CALL AddTwo $a $b

          OUT CALL isEven $a 
      ```
      ##### Correct Code:
      ```python
          # Assume that fucntions 'Add' , 'AddTwo' and 'isEven' have the above mentioned declaration
          $a = 15
          $b = 20

          CALL Add $a 

          $a = 20
          CALL Add $a

          CALL Add $a -> $c

          CALL Add $a $b -> $c

          CALL isEven $a -> $c
          OUT $c
      ```
</details>
  
## Operators Available on `int` and `double` values
<details><summary><b> Click Here To See <i><ins>Operators Available</ins></i></b></summary>  
  
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
  
</details>
  
## Operators Available on `string` values
<details><summary><b> Click Here To See <i><ins>Operators Available</ins></i></b></summary>  
  
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
  </details>
  
## Comparitors Available
<details><summary><b> Click Here To See <i><ins>Comparators Available</ins></i></b></summary>  
  
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
      
      $m = ( $a [] "Naman" ) .. ( $c > $d )
      # $m = 0 (As the second condition is wrong and '0 and 1' = 0)
      
      $n = ( $a [] "Naman" ) ++ ( $c > $d )
      # $n = 1 (Even though the second condition is wrong but '0 or 1' = 1)
  ```
</details>

## Keywords Available
<details><summary><b> Click Here To See <i><ins>Keywords Available</ins></i></b></summary>  

* `IN` -> Keyword used to write an input variables from the users.
* `OUT` -> Keyword usef to output data to the users.
* `IS` -> Keyword used to write a conditional block.
* `NONE` -> Keyword used in conjuction with an `IS` statement to specify what to do if the condition fails.
* `LOOP` -> Keyword used to start a loop.
* `EXIT` -> Keyword used to break out of a loop.
* `FN` -> Keyword used to declare and define a fucntion.
* `RET` -> Keyword used to return a value from the function.
* `CALL` -> Keyword used to call a function.
  
</details>

## Examples of code written in Lipi
  
### Even-Odd
This is a program to find if a number is even or odd for as many numbers you want. The program will let you enter the numbers one after another till you type 'yes'. This is a good introductory program to understand the basics of **variable declaration**, **input**, **output**, **conditions** and **loops** in Lipi.
  
 #### Code:
  ```python
      # This is a program to find if a number is even or odd for as many numbers you want
      FN main
      {
          IN "Type 'YES' to enter more numbers" $yes
          # The condition -> [] ensures that the eqality check is not case sensitive
          LOOP ( $yes [] "YES" )
          { 
              IN "Enter a number" $num
              IS ( $num % 2 <> 0 )
              {
                  OUT $num "is Even"
              }
              NONE
              {
                  OUT $num "is ODD"
              }
              IN "Type 'YES' to enter more numbers" $yes
          }
      }
  ```
 #### Output: 
  ![Even-Odd](https://user-images.githubusercontent.com/53811147/134787433-10fe881d-8218-4dd6-a9a0-7d651d35fda6.PNG)

 
## Instruction To Run The Code:
* Download the [Lipi Programming Language Interpreter.py](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Lipi%20Programming%20Language%20Interpreter.py) file and save it in a folder.
* Create a **Lipi Program** in a textfile and save it in the same folder with **.txt** extention.
* Run the **"Lipi Programming Language Interpreter.py"** file and input the name of **Lipi Program** file **.txt** extention and hhit enter.
##### Note: Make sure you have the latest **Python** in your system.
