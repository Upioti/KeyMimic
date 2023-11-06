import time
import random
import pyautogui
import os
import keyboard
from prompt_toolkit import prompt

os.system("title " + "KeyMimic v1.0 - @Upioti")
print("-----------------------------------------")
print("Welcome to KeyMimic v1.0 - By Upioti")
print("Simple human typing simulator (ifykyk)")
print("Loading.....")
print("-----------------------------------------")
time.sleep(3)
os.system("cls")

#Check if file exist
file_path = 'mimic.txt'
    

if not os.path.isfile(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('')  #Create file
    print("-----------------------------------------")
    print(f"Error: The file '{file_path}' was not found!")
    print("")
    print("File has been created.")
    print("Please fill the file with text and press enter to proceed.")
    input("-----------------------------------------")
    time.sleep(0.1)
    os.system("cls")




print("-----------------------------------------")
print("Lets begin the program configuration!")
print("-----------------------------------------")
print("[TIPS]:")
print("On probability values:")
print("0.001 = 0.1%")
print("1.000 = 100%")
print("")
print("Format:")
print("Option Description (Values):")
print("-----------------------------------------")
print("Speed Configuration (Typing speed):")
SPEED = float(prompt("Seconds per Character (0.001-Inf): ", default="0.050"))
SPEED_VARIATION = float(prompt("Seconds Variation (0.001-Inf): ", default="0.020"))
print("-----------------------------------------")
print("Pause Configuration (Stop for some seconds out of nowhere): ")
PAUSE_CHANCE = float(prompt("Pause Probability (0.001-1.000): ", default="0.010"))  
PAUSE_DURATION_MIN = float(prompt("Minimum Pause Duration in Seconds (0.001-Inf): ", default="1.000")) 
PAUSE_DURATION_MAX = float(prompt("Max Duration in Seconds (0.001-Inf): ", default="3.000"))
print("-----------------------------------------")
print("Break Configuration (After finishing a paragraph take a break): ")
BREAK_CHANCE = float(prompt("Break Probabilty (0.001-1.000): ", default="0.250"))   
BREAK_DURATION_MIN = float(prompt("Minimum Break Seconds (0.001-Inf): ", default="10.000"))
BREAK_DURATION_MAX = float(prompt("Max Break Seconds (0.001-Inf): ", default="120.000"))
print("-----------------------------------------")
print("Mistake Configuration (Make typos):")
MISTAKE_FREQUENCY = float(prompt("Mistake Probability (0.001-1.000): ", default="0.050"))
print("-----------------------------------------")
time.sleep(0.5)
os.system("cls")


#accent support
def type_accented_vowel(vowel):
    keyboard.press_and_release('´')  
    time.sleep(0.1)  
    keyboard.press_and_release(vowel)  

#vowel index
accented_chars = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U'
}


def type_text(text):
    for char in text:
        
        #Mistakes:
        if random.random() < MISTAKE_FREQUENCY:
            pyautogui.write(random.choice('abcdefghijklmnopqrstuvwxyz'))
            
            seconds = random.uniform(SPEED - SPEED_VARIATION, SPEED + SPEED_VARIATION)
            if seconds < 0:
                seconds = 0.001
               
            time.sleep(seconds)
            #Correcting mistake
            pyautogui.hotkey('backspace')
            seconds = random.uniform(SPEED - SPEED_VARIATION, SPEED + SPEED_VARIATION)
            if seconds < 0:
                seconds = 0.001
               
            time.sleep(seconds)



        # Type the char:
        if char in accented_chars:
            # Support for accented chars
            type_accented_vowel(accented_chars[char])
        else:
            # type char
            keyboard.write(char)
        seconds = random.uniform(SPEED - SPEED_VARIATION, SPEED + SPEED_VARIATION)
        if seconds < 0:
            seconds = 0.001
           
        time.sleep(seconds)
        
        # randomized break when line jump:
        if char == '\n':
            if random.random() < BREAK_CHANCE:
                time.sleep(random.uniform(BREAK_DURATION_MIN, BREAK_DURATION_MAX) + 0.001)

        #small pause while typing
        elif random.random() < PAUSE_CHANCE:
            time.sleep(random.uniform(PAUSE_DURATION_MIN, PAUSE_DURATION_MAX) + 0.001)



def main():
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    #confirm start and tell users to click field
    print("-----------------------------------------")
    print("Everything is ready to go!")
    print("Press enter to start!")
    input("-----------------------------------------")
    os.system("cls")
    print("-----------------------------------------")
    print("Starting in 3 seconds, please click the target text field.")
    print("-----------------------------------------")
    time.sleep(3)
    os.system("cls")
    print("-----------------------------------------")
    print("Started typing!")
    print("-----------------------------------------")
    type_text(text)

if __name__ == "__main__":
    main()