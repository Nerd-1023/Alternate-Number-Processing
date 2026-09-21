# Functions

## `getSquare(x)`
#### Returns x² for any input of x
* Whole numbers only (no decimals)
* Can be positive or negative
#### How it works:
1. Remove negative sign if it exists, to add back later
2. Adds together all the first x odd numbers (the first 4 odd numbers are 1, 3, 5, and 7)
3. Returns the value, always positive because it's squared

## `getSquareRoot(x)`
#### Returns √x for any input of x
* Perfect squares only (no decimals, √x must be a whole number, possible inputs include 4, 16, and 25)
* No negative numbers will be processed
* √x must be less than 1,000,000. This means the maximum input is √1,000,000,000,000 (`getSquareRoot(1000000000000)`)
#### How it works:
1. Loop over every odd number from 1 to 1000000
2. If the number squared (using the method used by `getSquare()`) is equal to x, then return the number
