

def get_requirements():
    print("Python Lists")
    print("\nProgram Requirements:\n"
          + "1. Lists (Python data structure): mutable, ordered sequence of elements.\n"
          + "2. Lists are mutable/changeable--that is, can insert, update, delete.\n"
          + '3. Cretae list - using square brackets [list]: my_list = ["Cherries", "apples", "bananas", "oranges"].\n'
          + "4. Create a program that mirros the following IPO (input/process/output) format.\n"
          + "Note: user enters number off requested  list elements, dynamically rendered below (that is, number of elements can change each run).\n")
    
    
def user_input():
    # initialize variables and list
    num = 0
    
    # Input: get user dta
    print("Input: ")
    num = int(input("Enter number of list elements: "))
    return num

print ()

def using_lists(num):
    my_list = []
    
    for i in range(num):
        my_element = input('Please enter list element' + str(i + 1) + ":")
        my_list.append(my_element)
        
    print("\nOutput:")
    print("Print my_list:")
    print(my_list)
    
    elem = input("\nPlease enter list element: ")
    pos = int(
        input("Please enter list *index* position (note: must convert to int):"))
    
    print("\nInsert element into specific position in my_list")
    my_list.insert(pos, elem)
    print(my_list)
    
    print("\nCount number of elements in list: ")
    
    print(len(my_list))
    
    print("\nSort elements in list alphabetically: ")
    my_list.sort()
    print(my_list)
    
    print("\nReverse list: ")
    my_list.reverse()
    print(my_list)
    
    print("\nRemove last list element: ")
    my_list.pop()
    print(my_list)
    
    print("\nDelete second element from list by *index* (note: 1=2nd element):")
    
    del my_list[1]
    print(my_list)
    
    print("\nDelete element from list by *value* (cherries): ")
    my_list.remove('cherries')
    print(my_list)
    
    print("\nDelete all elements from list: ")
    my_list.clear()
    print(my_list)
          