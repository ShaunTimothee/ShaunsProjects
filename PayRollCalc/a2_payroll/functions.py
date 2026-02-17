def get_requirements():
    print("Payroll Calculator")
    print("\nProgram Requirments: \n"
          + "1. Must use float data type for user input .\n"
          + "2. Overtime rate: 1.5 times hourly rate (hours over 40). \n"
          + "3. Holiday rate: 2.0 times hourly rate (all holiday hours) .\n"
          + "4. Must format currency with dollar sign, and round to two decimal places.\n"
          + "5. Create  at least three functions that are called by the program:\n"
          + "\ta. main(): calls at least two other functions.\n"
          + "\tb. get_requirements(): displays the program requirments .\n"
          + "\tc. calculate_payroll(): calculates an individual one-week paychek.\n")
def calculate_payroll():
    # constats to represent base hours, ovetime and holiday rates
    # Note: oython doesn'tprovide true constants
    BASE_HOURS = 40
    OT_RATE = 1.5
    HOLIDAY_RATE = 2.0
    
    #IPO: Input > Process > Output
    # get user data
    print("Input:")
    # get hours worked and hourly pay rate
    hours = float(input( 'Enter hours worked: '))
    holiday_hours = float(input('Enter holiday hours: '))
    pay_rate = float(input('Enter hourly pay rate: '))
    
    #Process:
    #calculations
    base_pay = BASE_HOURS * pay_rate
    OVERTIME_HOURS = hours - BASE_HOURS
    
    # calculate andsiplay gross pay
    if hours > BASE_HOURS:
        # calculate gross pay with overtime
        
        #calculate overtime pay
        overtime_pay = OVERTIME_HOURS * pay_rate * OT_RATE
        
        # calculate holiday pay
        holiday_pay = holiday_hours * pay_rate * HOLIDAY_RATE
        
        # calculate gross pay
        gross_pay = BASE_HOURS * pay_rate + overtime_pay + holiday_pay
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)
    else:
        # calculate gross pay without overtime, but include holiday pay
        overtime_pay = 0
        holiday_pay = holiday_hours * pay_rate + HOLIDAY_RATE 
        gross_pay = hours * pay_rate + holiday_pay
        
        #display pay
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)
        # https://docs.python.org/3.0/tutorial/inputoutput.html
        
        '''
https://docs.python.org/3/library/string.html#format-specification-mini-language
https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
alignment specifiers:
'<' Forces field to be left-aligned within available space (default for most objects).

'>' Forces field to be right-aligned within available space (default for numbers).

'=' Forces padding to be placed after sign (if any) but before digits.
Used for printing fields: '+060000120'. Alignment option only valid for numeric types.

'^'Forces field to be centered within available space.
'''

# two Steps:
# 1) right-align with spaces
# 2) currency symbol, with thousand separator, and decimal places
# print(*\nBase: {:>15)".format('$(:,.2f) '.format (base_pay)))

# Passing integer ofter ' causes field to be minimum number of characters wide

# for x in range(1, 11):
# print(' [0:2d] [1:3d] [2:4d]'，formot（x, x * x， x * × * x))
print() # create blank Line. DON'T use \n on first print will misalign first column!
# #fiLL character（*）
# print("{0:*<10} ${1:,.2f}".format('Base:', base_pay))

# Output:
#https://docs.python.org/3/Library/string.htmleformat-specification-mini-Language
#https://docs.python.org/3/library/string.htmlestring-formatting
# https://www.python-course.eu/python3_formatted_output.php
#https://ww.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3

def print_pay(base_pay, overtime_pay, holiday_pay, gross_pay):
    print("\nOutput:")
    print("{0:<10} ${1:,.2f}".format('Base:', base_pay))
    print("{0:<10} ${1:,.2f}".format('Overtime:', overtime_pay))
    print("{0:<10} ${1:,.2f}".format('Holiday:', holiday_pay))
    print("{0:<10} ${1:,.2f}".format('Gross:', base_pay))

    
