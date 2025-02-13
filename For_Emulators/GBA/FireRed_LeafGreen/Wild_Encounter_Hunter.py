import cv2 as cv
import pyautogui
import time


'''Goals
    try to use opencv to get the dimensions of the encounter box (calibration) so any screen size works
    change some of the transitions to be color based rather than timing based
'''


encounters = 0 #initial count for incrementing encounters, not specific to a target pokemon

def key_input(key,sleep_time):
    pyautogui.keyDown(key)
    time.sleep(sleep_time)
    pyautogui.keyUp(key)

encounter_color = (41,82,107) # Text box during an encounter (where "WILD" appears)
#wild_location = pyautogui.locateCenterOnScreen('Wild.png')
#print(wild_location)
#move up and down until the encounter box pixel detected
def wait_for_encounter():
    while (pyautogui.pixel(1032,736) != encounter_color): #wait until encounter box is found
        #move up and down 
        key_input('a',0.25)
        time.sleep(0.25)
        key_input('d',0.25)

def wait_for_wild():
    while(True):
        try:
            location = pyautogui.locateOnScreen("Wild.png")
            break
        except:
            pass

def run_from_battle():
    while True:
        try:
            battle_prompt = pyautogui.locateOnScreen("Battle_Prompt.png")
            
            key_input('d',0.5)
            key_input('s',0.5) #navigate from battle to run


            key_input('l',0.5)
            key_input('l',0.5)

            break
        except:
            pass

pyautogui.moveTo(1043,736)
pyautogui.click(1043,736) # get into the game

while True:
    wait_for_encounter()
    encounters += 1
    print(f"Encounters: {encounters}")
    #print("color found")
    start_time = time.time() #get the starting time of the encounter

    wait_for_wild()
    #print("wild found")
    time.sleep(0.25)
    key_input('l',0.5)
    wild_time = time.time()
    print(f"The encounter time was {wild_time-start_time}")
    if (wild_time-start_time) > 4:
        print("SHINY")
        break
    else:
        time.sleep(0.5)
        key_input('l',0.5)
        run_from_battle()
        time.sleep(1)
        key_input('l',0.5)
        print("battle fled")
    #wild_text = pyautogui.locateOnScreen("Wild.png")
