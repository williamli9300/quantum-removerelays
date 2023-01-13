import os
import sys

'''-----------------------------------
--------- TEXT HANDLING CODE ---------
-----------------------------------'''

def removeRelays(l): # inputs: takes list "l" as lines of text file; outputs: list "noRelays" as lines with relays removed
    noRelays=[]
    counter = 0
    #enum_list = list(enumerate(l))
    isRelay = False
    while counter < len(l):
        '''
        if enum_list[counter][1][0].isnumeric():
            if not "relay" in (enum_list[counter][1]).lower():
                noRelays.append(enum_list[counter][1])
                isRelay = False
            else:
                isRelay = True
        else:
            if isRelay == False:
                noRelays.append(enum_list[counter][1])
        counter +=1
        '''
        if l[counter][0].isnumeric():
            if not "relay" in (l[counter]).lower():
                noRelays.append(l[counter])
                isRelay = False
            else:
                isRelay = True
        else:
            if isRelay == False:
                noRelays.append(l[counter])
        counter+=1
    return noRelays
        
'''-----------------------------------
------ SESSION FORMAT SELECTION ------
-----------------------------------'''
def checkOneToFive(n): # inputs: string "n" as input value; outputs: int(n) if n is integer, else outputs "False".
    if n.isnumeric():
        if int(n) in [i for i in range(1, 6)]:
            #print("n in (1, 6)")
            return int(n)
        else:
            print("Please enter a number between 1 and 5.")
            return False
    else:
        print("Please enter a number between 1 and 5.")
        return False
def getOptions(): # inputs: asks for console input; outputs: result from checkOneToFive(n).
    print("What is the layout of your session? \"Events\" signifies non-relay events.\n \
          1. Relays - Events \n \
          2. Events - Relays \n \
          3. Relays - Events - Relays \n \
          4. Events - Relays - Events \n \
          5. Other/Manual \n")
    option = input("Please enter a number:\n")
    opt = checkOneToFive(option)
    return opt

'''-----------------------------------
------------ FILE HANDLING -----------
-----------------------------------'''
def getFile(): # inputs: pulls './quantum.slx'; outputs: list "lines" of file split by line into list.
    if os.path.isfile('./quantum.slx') == False:
        input("File \"quantum.slx\" does not exist! Please push Start List \
from Hy-Tek SwMM into the correct directory, and ensure that this executable \
is in the same folder as the start list file.\nPlease press \"Enter\" to close this window.")
        sys.exit()
    fileObj = open('./quantum.slx', 'r')
    lines = fileObj.read().splitlines()
    fileObj.close()

    print("renaming old quantum.slx...")
    os.rename("./quantum.slx", "./quantum_OLD.slx")
    print("done.")
    return lines
def writeFile(l, p): # inputs: list "l" of file lines, "p" path; outputs: writes text to file; prints "done."
    with open(p, 'w') as f:
        f.writelines("\n".join(l))
        f.write("\n")

'''-----------------------------------
----------- HANDLING CODE -----------
-----------------------------------'''
def execute(n):
    rawList = getFile()
    noRelays = removeRelays(rawList)
    print("writing new files...")
    if n == 1:
        writeFile(rawList, './quantum_1HasRelays.slx')
        writeFile(noRelays, './quantum_2NoRelays.slx')
        print("done. \n======================")
        print("==== INSTRUCTIONS ==== \n \
    - Before the first event: Rename the file  \"quantum_1HasRelays.slx\" into \"quantum.slx\". Refresh the start list. \n \
    - During the last few heats of relays, delete the file now named \"quantum.slx\" (previously \"quantum_1HasRelays.slx\"), then rename the file \"quantum_2NoRelays.slx\" into \"quantum.slx\". \n \
    - Refresh the start list again after all relays have finished, right before the start of individual events. \n \
    NOTE: If you need a fresh start list, please DELETE ALL FILES WITH THE *.slx EXTENSION FIRST, THEN RE-PULL FROM HY-TEK. \
    ")
    elif n == 2:
        writeFile(noRelays, './quantum_1NoRelays.slx')
        writeFile(rawList, './quantum_2HasRelays.slx')
        print("done. \n======================")
        print("==== INSTRUCTIONS ==== \n \
    - Before the first event: Rename the file \"quantum_1NoRelays.slx\" into \"quantum.slx\". Refresh the start list. \n \
    - During the last few heats of individual events, delete the file now named \"quantum.slx\" (previously \"quantum_1NoRelays.slx\"), then rename the file \"quantum_2HasRelays.slx\" into \"quantum.slx\". \n \
    - Refresh the start list again after all individual events have finished, right before the start of relay events. \n \
    NOTE: If you need a fresh start list, please DELETE ALL FILES WITH THE *.slx EXTENSION FIRST, THEN RE-PULL FROM HY-TEK. \
    ")
    elif n == 3:
        writeFile(rawList, './quantum_1HasRelays.slx')
        writeFile(noRelays, './quantum_2NoRelays.slx')
        writeFile(rawList, './quantum_3HasRelays.slx')
        print("done. \n======================")
        print("==== INSTRUCTIONS ==== \n \
    - Before the first event: Rename the file \"quantum_1HasRelays.slx\" into \"quantum.slx\". Refresh the start list. \n \
    - During the last few heats of the first block of relays, delete the file now named \"quantum.slx\" (previously \"quantum_1HasRelays.slx\"), then rename the file \"quantum_2NoRelays.slx\" into \"quantum.slx\". \n \
    - Refresh the start list again after the first block of relays, right before the start of individual events. \n \
    - During the last few heats of individual events, delete the file now named \"quantum.slx\" (previously \"quantum_2NoRelays.slx\"), then rename the file \"quantum_3HasRelays.slx\" into \"quantum.slx\". \n \
    - Refresh the start list again after all the individual events have finished, right before the start of the last block of relay events. \n \
    NOTE: If you need a fresh start list, please DELETE ALL FILES WITH THE *.slx EXTENSION FIRST, THEN RE-PULL FROM HY-TEK. \
            ")
    elif n == 4:
        writeFile(noRelays, './quantum_1NoRelays.slx')
        writeFile(rawList, './quantum_2HasRelays.slx')
        writeFile(noRelays, './quantum_3NoRelays.slx')
        print("done. \n======================")
        print("==== INSTRUCTIONS ==== \n \
    - Before the first event: Rename the file \"quantum_1NoRelays.slx\" into \"quantum.slx\". Refresh the start list. \n \
    - During the last few heats of individual events before relays, delete the file now named \"quantum.slx\" (previously \"quantum_1NoRelays.slx\"), then rename the file \"quantum_2HasRelays.slx\" into \"quantum.slx\". \n \
    - Refresh the start list again after the first block of individual events have finished, right before the start of relay events. \n \
    - During the last few heats of relay events, delete the file now named \"quantum.slx\" (previously \"quantum_2HasRelays.slx\"), \n then rename the file \"quantum_3NoRelays.slx\" into \"quantum.slx\". \n \
    - Refresh the start list again after all the relay events have finished, right before the start of the last block of individual events. \n \
    NOTE: If you need a fresh start list, please DELETE ALL FILES WITH THE *.slx EXTENSION FIRST, THEN RE-PULL FROM HY-TEK. \
            ")
    elif n == 5:
        writeFile(noRelays, './quantum_NoRelays.slx')
        writeFile(rawList, './quantum_HasRelays.slx')
        print("done. \n======================")
        print("==== INSTRUCTIONS ==== \n \
    - In the folder containing \"quantum.slx\", there are now two new files: one called \"quantum_NoRelays.slx\" and one called \"quantum_HasRelays.slx\". \
    - If your session starts with relays: Rename the file \"quantum_HasRelays.slx\" into \"quantum.slx\". Refresh the start list. \n \
    - If your session starts with individual events: Rename the file \"quantum_NoRelays.slx\" into \"quantum.slx\". Refresh the start list. \n \
    - A few heats before you change from relays to individual events or vice versa: \n \
        - Rename \"quantum.slx\" back into its original name, either \"quantum_HasRelays.slx\" or \"quantum_NoRelays.slx\". \n \
        - Rename the other file (the one you have not yet renamed) into \"quantum.slx\". Refresh the start list right before you need the new list. \n \
    - Repeat these steps each time there is a switch between individual events and relays. \n \
    NOTE: If you need a fresh start list, please DELETE ALL FILES WITH THE *.slx EXTENSION FIRST, THEN RE-PULL FROM HY-TEK. \
            ")
    input("====================== \nPress \"Enter\" to close this window.\n")
    
def go():
    number = getOptions() # gets input from user
    if number == False: # checks if input is valid choice
        go()
    else:
        print("You have chosen option", number, ".")
        execute(int(number))

'''--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------'''

go()

'''
LICENSE: MODIFIED MIT License

Copyright (c) 2022 William Li

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Please contact the copyright holder before, and please credit the copyright
holder when using, copying, modifying, merging, publishing, distributing, 
sublicensing, and/or selling copies of the Software for commercial use.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
