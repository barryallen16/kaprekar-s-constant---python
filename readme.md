***Kaprekar constant***
---
**Kaprekar constant** is a number that occurs when we take a 4 digit number, create both highest and lowest number with those digits and perform subtraction iteratively upto 7 times to get the number **6174**
The steps involved in finding kaprekar constant
1. Take a 4 digit number
2. create a lowest number and highest number from those digits
3. perform subtraction on highest and lowest number
4. step 2 and 3 from the result until 6174 arrives as result

if there are only 3 digits after performing any subtraction , add a zero to the digit and performs step 2 and 3.
numbers which have all 4 digits as the same does not obey kaprekar constant.

let's take an example.
4 digit number - 1000
***Steps***
1. low number - 1  high number - 1000  result - 999
2. low number - 999 high number - 9990 result - 8991
3. low number - 1899 high number - 9981 result - 8082
4. low number - 8820 high number - 288  result - 8532
5. low number - 2358 high number - 8532  result - **6174**
see there you go
The python code demonstrates this.
