'''## Exercise 10: Is it even? - 35 Marks

Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.'''

def odd_even_checker(number):                      ## Creating Function
    if number % 2 == 0:                            ## If there is a remainder the number will be even if no remaind the number will be odd 
        return "The number is even."
    else:
        return "The number is odd."

def main():
    number = int(input("Enter number: "))    ## Asks player for input of number
    result = odd_even_checker(number)          ## Sending number to function 
    print(result)                              ## Prints the result

if __name__ == "__main__":
    main()
