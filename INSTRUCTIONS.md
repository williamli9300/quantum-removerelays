# **INSTRUCTIONS: Video Board Relay Name Bug Workaround**

### **Background:**

You may have seen the bug where some swimmers’ Team Names show up as their Relay Name (e.g. VPSC-A, UBCT-B, RAPID-A, etc.) instead of the proper Team Name (VPSC, UBCT, RAPID, etc.) This is because of a bug where, when Quantum reads a start list file, it interprets the Relay Name (VPSC-A etc.) as the Team Name when it generates an athlete list. Here, we describe a workaround using a script that automatically removes relays from the start list.

### **Relay Blocks**

Before you begin, you should determine what your Relay Blocks are going to be.

Here, a “relay block” is defined to mean a block of consecutive relays with no individual events between them, where each relay swimmer will only swim once (i.e. is only on one relay team within the block). 

For example: In a session with Events 1-10, if E1-4 are all relays, and 5-10 are all individual events, then Events 1-4 is considered a “block of consecutive relays”.

Ideally, a relay block should only contain 2 events if each event is a gender-separated relay, or 1 event if it’s a mixed relay. If you have four events in two different age groups (e.g. F12&U, M12&U, F13&O, M13&O) for the same type of relay, it is acceptable to group these four events into a single relay block, although younger swimmers swimming in both age groups may display incorrectly if they are on, for example, Relay A for one, and Relay B for another.

Determine how many relay blocks you will have, and when they will occur.

### **Quantum Logic**

The Quantum software reads the file called `quantum.slx` in the path specified in your DH I/O. 

### **Setup in HyTek**

In Interfaces > Scoreboard > Customize, You should select “Abbr.-A” as the Relay Name format.

### **Downloading the Script**

1. Visit <https://github.com/williamli9300/quantum-removerelays/releases/tag/release> and download `RemoveRelaysScript.zip`.
1. Right Click the zip file and extract to `\Downloads\RemoveRelaysScript\`.
1. In HyTek SwMM8.0, push the Start List (quantum.slx) to the Quantum folder.
1. Drag the folder `\RemoveRelaysScript\` into the folder containing `quantum.slx`.
1. Make a copy of the existing quantum.slx and rename it to `quantum_copy.slx`.
1. Open the folder `\RemoveRelaysScript\` that’s in the Quantum folder and run `removerelays.exe`. This will remove all relays the file named quantum.slx. We will call this the “relayless” `quantum.slx`.
**


### **Sessions with One Block of Consecutive Relays**

In sessions with one block of relays (e.g. in a session with events 1-10, Events 1-4 are all relays, and 5-10 are all individual), this is how to work around the issue:

1. If the Relay Block is at the end of the session:
   1. Ensure that your relayless `quantum.slx` is named `quantum.slx`.
   1. Right click on `quantum_copy.slx`, and open with Notepad. Delete all events before and after your Relay Block. Lines that start with a number are Events/Heats, while lines starting with semicolons denote lanes/swimmers. For example, if your relay is Event 21-22, find the line that starts with “21;1” or otherwise implies the E21H1 (the first line starting with “21”, and delete everything before that. Then find the line that starts with “23;1” or otherwise implies E23H1 (the first line starting with “23”) and delete that line and everything after it. Press `Ctrl + S` to save.
   1. Refresh the Start List in Quantum software, then proceed with individual events. 
   1. Right before relays start, delete the relayless `quantum.slx`, and rename `quantum_copy.slx` back to quantum.slx. 
1. If the Relay Block is at the beginning of the session:
   1. Rename the relayless quantum.slx to `quantum_norelays.slx`.
   1. Right click on `quantum_copy.slx` and open with Notepad. Delete all events before and after your Relay Block. Lines that start with a number are Events/Heats, while lines starting with semicolons denote lanes/swimmers. For example, if your relay is Event 21-22, find the line that starts with “21;1” or otherwise implies the E21H1 (the first line starting with “21”, and delete everything before that. Then find the line that starts with “23;1” or otherwise implies E23H1 (the first line starting with “23”) and delete that line and everything after it. Press `Ctrl + S` to save, then rename `quantum_copy.slx` to quantum.slx.
   1. Refresh the start list.
   1. After relays are done, delete quantum.slx (the one with only relays and nothing else). Then, rename `quantum_norelays.slx` back to quantum.slx. Refresh the start list again.

### **Sessions with More than One Block of Consecutive Relays**

Follow the same steps as the previous section. However, instead of 2 copies of the start list, you will need (N+1) copies, where N is the number of Relay Blocks you will have. You will need 1 “relayless” copy. This can be done by executing removerelays.exe while you still have a clean, untouched `quantum.slx` in your Quantum folder. Then, you will need a copy of `quantum.slx` for each relay block, containing only the heats of each relay block, as per 7B and 8B. 

### **Notes**

You may delete/switch over which `quantum.slx` file you would like Quantum to read from next, a few heats before you need it, as long as you DO NOT refresh the start list until immediately before you need it.

