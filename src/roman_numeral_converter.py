class RomanNumeralConverter(object):

    # Test for Arabic Number 1
    # Step 1 : Run the test for number 1
    # Result: Step 1 Passed
    # Step 2: When running the same test for arabic number 2, it failed:

    def convert1(self, number):
        if (number == 1):
            return('I')

# Test for Arabic Number 2
# Result: Now the test passes for arabic number 2, since we added If block to handle arabic number 2 as shown below

    def convert2(self, number):
        if(number == 2):
            return('II')
        else:
            return('I')

# Adding another test for arabic number 3
# Result : Failed
# We need to add if/else statments, then It will pass the test case for arabic number 3
# By adding if and else all the way to 3000 which is not sustainable, so now It's time to...
# refactoring to make It work .
# Add while loop to convert arabic number to roman numerals,  which will handle arabic numbers to remove..
# unnecessary  if/else block.

# Result, passed for arabic number 3 after change in function as shown below (changed If/else to while)

    def convert3(self, number):
        roman_number = ""
        while (number > 0):
            roman_number += "I"
            number -= 1
            print(roman_number)
        return roman_number


# Test for arabic number 10
# Result: Failed, because It will give result as 'IIIIIIIIII' which is not equal to 'X', when used above function code..
# function requires changes to handle  arabic number 10

# Result, passed for arabic number 10 after change in function as shown below


    def convert10(self, number):
        if (number == 10):
            return ('X')
        roman_number = ""
        while (number > 0):
            roman_number += "I"
            number -= 1
            print(roman_number)
        return roman_number


# Test for arabic number 20
# Result : Failed, because It return "IIIIIIIIIIIIIIIIIIII" which is not equal to 'XX' when used above function code..
# Action: function requires changes to handle arabic number 20, changes added below
# Result passed,even though code works, but It requires refactor, It has two while loops to handle arabic numbers

    def convert20(self, number):
        roman_number = ''
        while (number >= 10):
            roman_number += "X"
            number -= 10

        while (number > 0):
            roman_number += "I"
            number -= 1
            print(roman_number)
        print(roman_number)
        return roman_number

    # Final: Now our code need to be refactored to handle roman numerals, we can't use duplicates..
    #        while loop and also duplicate if/else blocks - which is bad practice of coding

    # Create key value pair for roman numeral and arabic number for 1, 5, 10, 50, 100, 500, 1000..
    # If input number matches to key from array It will return value as sysmbol
    # 2nd If block is to

    def convert(self,  number):
        numerals = {"I": 1, "IV": 4, "V": 5, "VI": 6, "IX": 9, "X": 10, "XL": 40,
                    "L": 50, "C": 100, "D": 500, "M": 1000, "MM": 2000, "MMM": 3000}
        rngFlag = ""
        for symbol, integer in numerals.items():
            if (integer == number):
                return symbol
            if (number > integer):
                rngFlag = symbol

        left = number - numerals[rngFlag]
        leftNumber = self.convert(left)
        return rngFlag + leftNumber
