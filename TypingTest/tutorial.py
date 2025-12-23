import curses
from curses import wrapper
import time
import random

def starter_screen(stdscr): #First function and its the starter screen
    stdscr.clear()
    stdscr.addstr(0,0, "Welcome to the Speed Typing Test! This was my favorite thing to do afterschool")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
  
    
def display_text(stdscr, target, current, wpm=0): #This function will how our text will type on top of each other while the color is chnaging
    stdscr.addstr(target) # Adding the target text under this function
    stdscr.addstr(1, 0, f"WPM: {wpm}") #f strign allows us to embedd python expressions inside the string without addind them
    
    for i, char in enumerate(current): # Looping through all the characters that the user types
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char: #If the character that was typed doesn't match the display 
            color = curses.color_pair(2) #Then it will equal red
            
        stdscr.addstr(0, i, char, color)  # Adding the character then displaying it with color on the screeen


def load_text(): #This function is opening our text file
   with open("text.txt", "r") as f:
       lines = f.readlines()
       return random.choice(lines).strip()
    
def wpm_test(stdscr):
    target_text = load_text() 
    current_text = []# The list for what the user is typing
    wpm = 0
    start_time = time.time()#Tells the time when the user starts
    stdscr.nodelay(True)
    
    while True: #Using the while loop for the users answers 
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) #Characters per minute
        
        stdscr.clear() #This will help clear the previous text so the user may start anew
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:#Here we are making the list into the string
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()# This line is waiting for the user to type something 
        except:
            continue
        
        if ord(key) == 27: # The ord is the value of each key on your keyboard. 27 being the escape key
            break # Brekaing out of the loop and continuing
        
        if key in ("KEY_BACKSPACE",  '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop() #Will remove the last elemnt of the list
        elif len(current_text) < len(target_text): #This is to ensure that the currrent text doesn't exceed the target count and cause an error
            current_text.append(key)#List of all the keys the user has pressed
                



def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)#Deals with the color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)#Deals with the color
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)#Deals with the color

    starter_screen(stdscr) #The start screen that the users will se when first encountering the test
    while True: #while loop that will allow for the users to actually play again
        wpm_test(stdscr)#calling the function after the start screen
        stdscr.addstr(2, 0, "Congrats! You've completed the test. Press any key to continue...")
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
    
wrapper(main)

