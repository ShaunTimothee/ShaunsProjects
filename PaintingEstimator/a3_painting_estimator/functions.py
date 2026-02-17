def get_requirements():
    
    print("\nDveloper: Shaun Timothee")
    print("Painting Estimator")
    print("\nProgram Requiremnts"
          + "\n1. Calculate how interior paint cost (w/o primer)"
          + "\n2. Must use  float data types. \n"
          + "3. Must use SQFT_PER_GALLON constant (350). \n"
          + "4. Must use iteration structure (aka loop).\n"
          + "5. Format, right-allign numbers, and round to two decimal places."
          + "\n6. Create at least five functions that are called by the program:\n"
          + "         a. main(): calls two other functions: get_requirments() and estimate_painting_cost()"
          + "\n       b. get_requirement(): displays the program requirments."
          + "\n       c. estimate_painting_cost(): calculates interior home painting, and calss print function."
          + "\n       d. print_painting_estimate(): displays painting costs."
          + "\n       e. print_painting_percentage(): displays painting cost percentages.")
    
    
def estimate_painting_costs():
    
    #intialize variables
    interior_sqft = 0.0
    price_per_gallon = 0.0
    hourly_rate = 0.0
    
    #get input
    print("\nInput:")
    interior_sqft = float(input("Enter total interior sq ft: "))
    price_per_gallon = float(input(" Ente price per gallon paint: "))
    hourly_rate = float(input("Enter hourly painting rate per sq ft: "))
    
    #calculate
    SQFT_PER_GALLON = 350.0
    num_of_gallons = interior_sqft / SQFT_PER_GALLON
    
    paint_cost = price_per_gallon * num_of_gallons
    labor_cost = hourly_rate * interior_sqft
    total = paint_cost + labor_cost
    
    paint_percent = paint_cost / total
    labor_percent = labor_cost / total
    
    #call print statements 
    print_painting_estimate(interior_sqft, SQFT_PER_GALLON, num_of_gallons, price_per_gallon, hourly_rate)
    print_painting_percentage(paint_cost, labor_cost, total, paint_percent, labor_percent)
    
def print_painting_estimate(total_sqft, sqft_per_gal, num_gallons, ppg, rate):
    
    print("\nOutput:")
    print("{0:8}{1:>25}".format("Item", "Amount"))
    print("{0:8}{1:20,.2f}".format("Total Sq Ft:", total_sqft))
    print("{0:8}{1:15,.2f}".format("Sq Ft per Gallon:", sqft_per_gal))
    print("{0:8}{1:14,.2f}".format("Number of Gallons:", num_gallons))
    print("{0:8}{1:11,.2f}".format("Paint per Gallon:  $", ppg))
    print("{0:8}{1:11,.2f}".format("Labor per Sq Ft:   $", rate))
    
def print_painting_percentage(paint_price, labor_price, total_price, paint_percentage, labor_percentage):
    
    print()
    print("{0:8}{1:>11}{2:>14}".format("Cost", "Amount", "Percentage"))
    
    print("{0:8}${1:10,.2f}{2:13.2%}".format("Paint:", paint_price, paint_percentage))
    
    print("{0:8}${1:10,.2f}{2:13.2%}".format("Labor:", labor_price, labor_percentage))
    
    print("{0:8}${1:10,.2f}{2:13.2%}".format("Total:", total_price, 1))