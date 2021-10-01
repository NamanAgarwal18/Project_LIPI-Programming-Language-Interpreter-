# Lipi Programming Language


<a href="https://www.youtube.com/watch?v=MEdDwKtX_3g" target="_blank"><img src="http://img.youtube.com/vi/MEdDwKtX_3g/hqdefault.jpg" alt="IMAGE ALT TEXT HERE" width="500" height="375" border="20" />

[<h3>Click Here To Watch The Video Demonstration</h3>](https://www.youtube.com/watch?v=MEdDwKtX_3g)

## Description
**Lipi** is a small programming language created by Naman Agarwal. It supports various fundamental programming concepts such as variable-declaration, function calling, conditional statements, loops, proper order of operations, and recursion. Along with the language there is a **Python** based interpreter to run the code written in Lipi. <br>
* The execution of a program in Lipi starts with the main function which does not return anything. 
* Lipi does not use *semi-colons* to terminate statements, instead it relies on the fact that each new line is the start of a new statement and end of the previous. 
* In Lipi the words need to carefully spaced out. 
* Lipi supports recursion.
* A variable is only available from inside the function it is created.
* Lipi can take use of arrays and in Lipi you also have the option to resize array dynamically.
* In Lipi arrays are passed by reference to the fucntions.

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

### 5. Arrays:
* An array variable also starts like any other variable (i.e. with a `$` symbol)
* To declare an array of a fixed size we use the keyword `ARR`
* Any element in the array can be acessed in the same way you access in other laguages like C++.
* Each array creates another variable (for array named `$arr` the variable formed => `$arr-len`) that is used in various ways like:
  * To get the length of the array
  * To pass the array into the fucntion
  * To resize the array

  #### Incorrect Code:
  ```python
      ARR $array[20]
  
      $a = 5
      $array[0] = $array[a] + 1
  
      OUT "Length of array" $array.len
  ```
  #### Correct Code:
  ```python
      ARR $array 20
      # OR
      $a = 20
      ARR $array $a
  
      $a = 5
      $array[0] = $array[$a] + 1
  
      OUT "Length of array" $array-len
  
      # To resize the array
      $array-len = $array-len + 5
      $array-len = 5
  ```
  
  
### 6. Functions:
* Lipi supports fucntions and by extention recursion.
  #### Fucntion Declaration: 
  * A function declaration starts with the `FN` keyword.
  * A fucntion does not have to start with a `$` symbol.
  * A function can have as many parameters as you want.
  * All the parameters can be written after the fucntion name seperated by a *space-bar*.
  * A function can take an array as a parameter.
  * The array is passed by reference and all the other variables are passed by value.
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
  
        FN takeArray $array[] $size
        {
            OUT "Size is:" $size
            OUT "length of array is:" $array-len
            OUT "First element is:" $array[0]
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
  
        FN takeArray $array-len $size
        {
            OUT "Size is" $size
            OUT "length of array is" $array-len
            OUT "First element is:" $array[0]
        }
    ```
  #### Fucntion Calling: 
    * A function can be called using `CALL` keyword.
    * The number of arguments given should be the same as the parameters required.
    * If the fucntion returns something then it is mandatory to give a variable to store the returned value.
    * You can still give a returning variable even if the fucntion doesn't return anything. In this case the returning variable would store 1 if the fucntion was run successfully.
    * While send the *'len'* variable of the array into a fucntion then:
      * If the recieving variable also has an *'len'* then the array reference is passed.
      * If the recieving variable doesn't have an *'len'* then the size of the array is passed.
  
      ##### Incorrect Code:
      ```python
          # Assume that fucntions 'Add' , 'AddTwo' , 'isEven' and 'takeArray' have the above mentioned declaration
          $a = 15
          $b = 20

          CALL Add ( $a )

          CALL Add 20

          $c = CALL Add $a

          CALL AddTwo $a $b

          OUT CALL isEven $a 
  
          CALL takeArray $array $array-len
      ```
      ##### Correct Code:
      ```python
          # Assume that fucntions 'Add' , 'AddTwo' , 'isEven' and 'takeArray' have the above mentioned declaration
          $a = 15
          $b = 20

          CALL Add $a 

          $a = 20
          CALL Add $a

          CALL Add $a -> $c

          CALL Add $a $b -> $c

          CALL isEven $a -> $c
          OUT $c
  
          ARR $array 5
          CALL takeArray $array-len $array-len
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
* `-`  -> for getting a few elements from the front or the ack of the string
* `*`  -> for concatenating same string multiple times
* `/`  -> for removing a few elements from the front or the ack of the string

  ```python
      $a = "naman"
      $b = "agarwal"
      
      $c = $a + $b
      # $c = "namanagarwal"
      
      $d = $a + 5
      # $d = "naman5"
      
      $e = $a * 3
      # $e = "namannamannaman" 
  
      $f = 2 - $a
      # $f = "na"
  
      $g = $a - 2
      # $g = "an"
  
      $h = 2 / $a
      # $h = "man"
  
      $i = $a / 2
      # $i = "nam"
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
* `ARR` -> Keyword used to declare an array of a given size.
  
</details>

## Examples of Code Written in Lipi
  
<details><summary><b> Click Here To See all the <i><ins>Sample Lipi Codes</ins></i></b></summary> 
  
### Even-Odd:
This is a program to find if a number is even or odd for as many numbers you want. The program will let you enter the numbers one after another till you type 'yes'. This is a good introductory program to understand the basics of **variable declaration**, **input**, **output**, **conditions** and **loops** in Lipi.
  
  <details><summary><b> Click Here To See The Code</b></summary>
    
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
   #### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Even-Odd.txt) to see the code. 
   #### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Even-Odd.PNG) to see the output.
    
  </details>

### FizzBuzz:
This is the popular FizzBuzz program coded in Lipi. This program will let you type in the maximum limit and then it will print accordingly. This is a good program to show a little complex **conditional statements**. Apart from intensive use of conditional statements I have also created multiple **fucntions** to implement this program.
    
   <details><summary><b> Click Here To See The Code</b></summary>
   
   ```python
        # This is a fizzbuzz program
        FN Condition $n
        {
            IS ( $n % 3 <> 0 .. $n % 5 <> 0 )
            {
                OUT "FizzBuzz"
            }
            NONE
            {
                IS ( $n % 3 <> 0 )
                {
                    OUT "Fizz"
                }
                NONE
                {
                    IS ( $n % 5 <> 0 )
                    {
                        OUT "Buzz"
                    }
                    NONE
                    {
                        OUT $n
                    }
                }
            }
        }

        FN FizzBuzz $n
        {
            # This frunction is just for the loop
            $i = 1
            LOOP ( $i <= $n )
            {
                CALL Condition $i
                $i = $i + 1
            }
        }

        FN main
        {
            IN "Enter the maximum number:" $a
            CALL FizzBuzz $a
        }
   ```
   #### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/FizzBuzz.txt) to see the code. 
   #### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/FizzBuzz.PNG) to see the output.
   
   </details>
    
### Printing Pattern:
Printing various patters using stars or numbers in the form of triangles or rectangles is a good way too test **nested loop** logic building. Here i have implemented a code that will input a single digit even number and then print a complex pattern using nested loops.


   <details><summary><b> Click Here To See The Code</b></summary>
     
  ``` python

      # For an input of '6'
      # The output would be - 
      #
      #  6 5 4 3 2 1 2 3 4 5 6  
      #  5 4 3 2 1   1 2 3 4 5  
      #  4 3 2 1       1 2 3 4  
      #  3 2 1           1 2 3  
      #  2 1               1 2  
      #  1                   1  
      #  2 1               1 2  
      #  3 2 1           1 2 3  
      #  4 3 2 1       1 2 3 4  
      #  5 4 3 2 1   1 2 3 4 5  
      #  6 5 4 3 2 1 2 3 4 5 6 

      FN upperPattern $n
      {
          $i = $n
          # Loop for the Number of rows -> n rows
          LOOP ( $i > 0 )
          {
              $text = " "
              $j = $i
              $k = 0

              # Loop for the first left-top square
              LOOP ( $k < $n )
              {
                  IS ( $j < 1 )
                  {
                      $text = $text + " "
                  }
                  NONE
                  {
                      $text = $text + $j
                  }
                  # To give an extra space
                  $text = $text + " "
                  $j = $j - 1
                  $k = $k + 1 
              }

              $k = $n - $i - 1
              LOOP ( $k > 0 )
              {
                  $text = $text + " "
                  $text = $text + " "
                  $k = $k - 1
              }

              $k = 1
              LOOP ( $k <= $i )
              {
                  IS ( ( $i >< $n ) ++ ( $k >< 1 ) )
                  {
                      $text = $text + $k
                      $text = $text + " "
                  }
                  $k = $k + 1
              }
              $i = $i - 1
              OUT $text
            }
        }

        FN lowerPattern $n
        {
            $i = 2
            # Loop for the Number of rows -> n-1 rows
            LOOP ( $i <= $n )
            {
                $text = " "
                $j = $i
                $k = 0
                LOOP ( $k < $n )
                {
                    IS ( $j > 0 )
                    {
                        $text = $text + $j
                    }
                    NONE
                    {
                        $text = $text + " "
                    }
                    $j = $j - 1
                    $k = $k + 1
                    $text = $text + " "
                }
                $k = $n - $i - 1
                LOOP ( $k > 0 )
                {
                    $text = $text + " "
                    $text = $text + " "
                    $k = $k - 1
                }
                $k = 1
                LOOP ( $k <= $i )
                {
                    IS ( ( $i >< $n ) ++ ( $k >< 1 ) )
                    {
                        $text = $text + $k
                        $text = $text + " "
                    }
                    $k = $k + 1
                }
                $i = $i + 1
                OUT $text
          }
      }

      FN pattern $n
      {
          # To Print the upper half of the pattern
          CALL upperPattern $n

          # To Print the lower half of the pattern
          CALL lowerPattern $n
      }

      FN main
      {
          $n = 1
          LOOP ( $n % 2 >< 0 ++ $n > 9 )
          {
              IN "Enter an Even Single Digit Number:" $n
          }
          CALL pattern $n
      }
  ```
   
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Pattern.txt) to see the code. 
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Pattern.PNG) to see the output.
   </details>
  
### Fibonacci Recursive:
Writing the fibonacci series till a given index is a very popular basic coding program. Eventhough the recursive way of writing a fibonacci program creates a slow program overall as it needs to calculate same thing over and over again, it still is a good way too practice the concept of basic recursion and check a language's capabilities of handling multiple recursive calls.
 
   <details><summary><b> Click Here To See The Code</b></summary>
     
   ```python
        # This is a fibonacci program via recursive approach
        FN fib $n
        {
            RET ( $n < 2 ) $n
            $a = $n - 1
            $b = $n - 2
            CALL fib $a -> $a
            CALL fib $b -> $b
            $a = $b + $a
            RET $a
        }

        FN main
        {
            IN "Enter the index" $a
            $i = 1
            OUT "The Fibonacci series is:"
            LOOP ( $i <= $a )
            {
                CALL fib $i -> $b
                OUT $i "->" $b
                $i = $i + 1
            }
        }
   ```
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Fibonacci%20Recursive.txt) to see the code. 
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Fibonacci%20Recursive.PNG) to see the output.
     
   </details>
 
### Palindrome: 
Checking if a string is palindrome or not is a good program to check basic string manipulation. It also uses the features provided by the Lipi language very well in accessing the charecters in sting and in removing the characters from the string. 
 
   <details><summary><b> Click Here To See The Code</b></summary>
     
   ```python
        # Check if a string is Palindrome or not
        FN Palindrome $name
        {
            $ans = "Yes"
            LOOP ( $name >< 0 )
            {
                $left = 1 - $name
                $right = $name - 1
                $name = 1 / $name
                $name = $name / 1
                IS ( $left ][ $right )
                {
                    $ans = "No"
                }
                EXIT ( $left ][ $right )
            }
            RET $ans
        }

        FN main
        {
            IN "Enter a String:" $name
            CALL Palindrome $name -> $ans
            OUT $ans
        }
   ```
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Palindrome.txt) to see the code. 
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Palindrome.PNG) to see the output.
     
   </details>
  
### Search An Element: *(**Normal Search**, **Sorting** and **Binary Search** using **Recursion**)*
Searching an element in an array is a good example to understand how arrays work. I have implimented a normal search that checks all the elements of the array and then i have implimented a **Sorting Algorithm** and then applied **Binary Search** using **Recusrion** to find the same element. This program shows how arrays can be created, passed through a function and how the array handles recursion.
     
     
   <details><summary><b> Click Here To See The Code</b></summary>
     
   ```python
        # Normal Search Algorithm
        FN normalSearch $array-len $ele
        {
            OUT "Normal Search for element"
            $i = 0
            LOOP ( $i < $array-len )
            {
                EXIT ( $array[$i] <> $ele )
                $i = $i + 1
            }
            IS ( $i <> $array-len )
            {
                OUT $ele "not found"
            }
            NONE
            {
                OUT $ele "found at the" $i "th position"
            }
        }

        # Normal Sorting algorithm
        FN sort $array-len
        {
            $i = 0
            LOOP ( $i < $array-len )
            {
                $pos = $i
                $j = $i + 1
                LOOP ( $j < $array-len )
                {
                    IS ( $array[$j] < $array[$pos] )
                    {
                        $pos = $j
                    }
                    $j = $j + 1
                }
                IS ( $pos >< $i )
                {
                    $temp = $array[$i]
                    $array[$i] = $array[$pos]
                    $array[$pos] = $temp
                }
                $i = $i + 1
            }
        }

        # Printing the array
        FN printArray $array-len
        {
            $i = 0
            $text = "Array"
            $text = $text + " "
            LOOP ( $i < $array-len )
            {
                $text = $text + $array[$i] + ","
                $i = $i + 1
            }
            OUT $text
        }

        # Binary search algorithm 
        FN binarySearch $array-len $start $end $ele
        {
            IS ( $start >= $array-len )
            {
                OUT $ele "not found"
            }
            NONE
            {
                IS ( $start >= $end )
                  {
                      IS ( $array[$start] <> $ele )
                      {
                          OUT $ele "found at" $start "position"
                      }
                      NONE
                      {
                          OUT $ele "not found"
                      }
                }
                NONE
                {
                    $mid = ( $start + $end ) // 2
                    IS ( $array[$mid] <> $ele )
                    {
                        OUT $ele "found at" $mid "position"
                    }
                    NONE
                    {
                        IS ( $array[$mid] > $ele )
                        {
                            $mid = $mid - 1
                            CALL binarySearch $array-len $start $mid $ele
                        }
                        NONE
                        {
                            $mid = $mid + 1
                            CALL binarySearch $array-len $mid $end $ele
                        }
                    }
                }
            }
        }

        FN main
        {
            IN "Enter the number of elements:" $n
            ARR $array $n
            $i = 0
            LOOP ( $i < $n )
            {
                $a = $i + 1
                OUT "Enter the" $a "th element"
                IN $array[$i]
                $i = $i + 1
            }
            CALL printArray $array-len
            IN "Enter the element to be searched:" $ele
            CALL normalSearch $array-len $ele
            CALL sort $array-len
            CALL printArray $array-len
            CALL binarySearch $array-len 0 $array-len $ele
        }
   ```
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Search%20An%20Element.txt) to see the code. 
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Search%20An%20Element.PNG) to see the output.
     
   </details>
 
### Sorting an Array:
Here I have implimented various sorting techniques that helped me debug my interpreter and refine my language even further. It also helped me learn different sorting algorithms and helped me be proficient in **Lipi Programing Language**. The Sorting algorithms implimented are:
     * Selection Sort
     * Bubble Sort
     * Murge Sort (**Recursively**)
     * Insertion Sort
     * Quick Sort (**Recursively**)
     * Radix Sort
     * Heap Sort (**Recursively**)
          
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Sorting%20Algorithms.txt) to see the code. 
#### [Click Here](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Test%20Codes/Sorting%20Algorithms.PNG) to see the output.
     
       
</details>
     
## Instruction To Run The Code:
* Download the [Lipi Programming Language Interpreter.py](https://github.com/NamanAgarwal18/Project_Lipi-Programming-Language/blob/main/Lipi%20Programming%20Language%20Interpreter.py) file and save it in a folder.
* Create a **Lipi Program** in a textfile and save it in the same folder with **.txt** extention.
* Run the **"Lipi Programming Language Interpreter.py"** file and input the name of **Lipi Program** file **.txt** extention and hhit enter.
##### Note: Make sure you have the latest **Python** in your system.
