# Relay Removal Script for Quantum-AQ
#### by William Li | [https://github.com/williamli9300/quantum-removerelays](https://github.com/williamli9300/quantum-removerelays) | v1.0 release
For use with SwissTiming Quantum-AQ and start list files (`quantum.slx`) created by HyTek Meet Manager 8.0. Creates `*.slx` files with Relay events removed, to overcome Team Name bug on some video boards.


## Table of Contents
1. [Use Case](#usecase)
2. [Installation Instructions](#installation)
3. [Usage Instructions](#usage)
4. [Note on Re-Pushing Start Lists](#repush)

Disclaimer: As per the included License, the author of this script offers no warranty and disclaims all responsibility and/or liability for incidents relating to the use of this script. This script has been tested with real Quantum start lists before being published; however, you use this software at your own risk. Please ensure that qualified, technologically literate Quantum operators are present to supervise the process. 

Feedback is welcome! Please feel free to report any bugs, issues, and/or communicate feature requests or other forms of feedback to the author of the script.

## Use Case <a name="usecase"></a>
On some video boards (e.g. UBC Aquatic Centre, TPASC), a bug in the way that the Quantum-AQ Software reads start lists can causes the Team Name/Nationality field to show up incorrectly during individual events, i.e. as a Relay Name (e.g. `RELAY-A`, `TEAM-A`, etc.)

This tool bypasses this bug by eliminating Relay Team Names from the startlist, preventing the software from confusing Team Names and Relay Team Names.  

This tool does the equivalent of unseeding relays on the Start List level, allowing the Clerk of Course to seed relays in HyTek without affecting team name displays.  

After running the script, Relay Team Name format will work normally and will not affect Team Names/Nationality. Recommended Relay Team Name format (can be changed under `Run > Interfaces > Scoreboard > Customize` in Hy-Tek SwMM8) is `Abbr-A`.
## Installation Instructions <a name="installation"></a>
- Download and unzip the release package.
- Place **the folder containing** `removerelays.exe` into the Quantum Data Set directory (i.e. into the folder containing `quantum.slx`)
  - The script is designed to work on the parent directory. For example, if your QAQF Data Set is in `C:\Quantum DB\Race1\`, the application should be found at `C:\Quantum DB\Race1\RemoveRelaysScript\removerelays.exe`. 
  - The executable application requires the other files in the folder to work, so make sure to move the entire folder! 
- At the beginning of the session, double-click `removerelays.exe` to run the script. You may need to give the app permission to "Run Anyway".
## Usage Instructions <a name="usage"></a>
**NOTE: Instructions are provided when you run the script.**
 Follow the on-screen prompt to select the format of your session by entering a number from 1 to 5, then hit "Enter".

- **Use Case 1: Relays then Events**
  - Before the first event: Rename the file `quantum_1HasRelays.slx` into `quantum.slx`. Refresh the start list.
  - During the last few heats of relays, delete the file now named `quantum.slx` (previously `quantum_1HasRelays.slx`), then rename the file `quantum_2NoRelays.slx` into `quantum.slx`.
  - Refresh the start list again after all relays have finished, right before the start of individual events.

- **Use Case 2: Events then Relays**
  - Before the first event: Rename the file `quantum_1NoRelays.slx` into `quantum.slx`. Refresh the start list.
  - During the last few heats of relays, delete the file now named `quantum.slx` (previously `quantum_1NoRelays.slx`), then rename the file `quantum_2HasRelays.slx` into `quantum.slx`.
  - Refresh the start list again after all relays have finished, right before the start of individual events.

- **Use Case 3: Relays, Events, Relays**
  - Before the first event: Rename the file `quantum_1HasRelays.slx` into `quantum.slx`. Refresh the start list.
  - During the last few heats of the first block of relays, delete the file now named `quantum.slx` (previously `quantum_1HasRelays.slx`), then rename the file `quantum_2NoRelays.slx` into `quantum.slx`.
  - Refresh the start list again after the first block of relays, right before the start of individual events.
  - During the last few heats of individual events, delete the file now named `quantum.slx` (previously `quantum_2NoRelays.slx`), then rename the file `quantum_3HasRelays.slx` into `quantum.slx`.
  - Refresh the start list again after all the individual events have finished, right before the start of the last block of relay events.
- **Use Case 4: Events, Relays, Events**
  - Before the first event: Rename the file `quantum_1NoRelays.slx` into `quantum.slx`. Refresh the start list.
  - During the last few heats of individual events before relays, delete the file now named `quantum.slx` (previously `quantum_1NoRelays.slx`), then rename the file `quantum_2HasRelays.slx` into `quantum.slx`.
  - Refresh the start list again after the first block of individual events have finished, right before the start of relay events.
  - During the last few heats of relay events, delete the file now named `quantum.slx` (previously `quantum_2HasRelays.slx`), then rename the file `quantum_3NoRelays.slx` into `quantum.slx`.
  - Refresh the start list again after all the relay events have finished, right before the start of the last block of individual events.

- **Use Case 5: Other Format/Manual Usage**
  - In the folder containing `quantum.slx`, there are now two new files:  one called `quantum_NoRelays.slx` and one called `quantum_HasRelays.slx`. 
  - If your session starts with relays: 
    - Rename the file `quantum_HasRelays.slx` into `quantum.slx`. Refresh the start list.
  - If your session starts with individual events: 
    - Rename the file `quantum_NoRelays.slx` into `quantum.slx`. Refresh the start list.
  - A few heats before you change from relays to individual events or vice versa:
    - Rename `quantum.slx` back into its original name, either `quantum_HasRelays.slx` or `quantum_NoRelays.slx`.
    - Rename the other file (the one you have not yet renamed) into `quantum.slx`.
    -  Refresh the start list right before you need the new list.
    - Repeat these steps each time there is a switch between individual events and relays.

## Note on Re-Pushing Start Lists <a name="repush"></a>
**NOTE:** Pushing a new Start List from Quantum overwrites the current `quantum.slx` file in the Quantum directory. This does not affect anything on the Quantum's end until the Start List is refreshed. 

**NOTE:** If you need a fresh start list, please DELETE ALL FILES WITH THE `*.slx` EXTENSION FIRST, THEN RE-PULL FROM HY-TEK. 

**If you need to re-push a start-list, it is recommended that you re-run the script, unless you are confident in your ability to quickly re-organize the files manually.**

It is recommended to make a copy of the new start list in the Quantum directory and name it `quantum_NEW.slx`.
