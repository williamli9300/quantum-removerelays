# Remove Relays Script for Quantum-AQ
For use with SwissTiming Quantum-AQ and start list files (`quantum.slx`) created by HyTek Meet Manager 8.0.

## Use Case
During sessions with relays, Team Names for some athletes may show up as a Relay Team Name (e.g. `Relay-A`, `TEAM-A`, `ShortName`, depending on the format selected under `Run > Interfaces > Scoreboard > Customize`). This is because of a bug in the way that Quantum-AQ software indexes athlete names and Team Names from the start list for a particular session. <br>
This tool bypasses this bug by eliminating Relay Team Names from the startlist, preventing the software from confusing Team Names and Relay Team Names. <br>
This tool does the equivalent of unseeding relays on the Start List level, allowing the Clerk of Course to seed relays in HyTek without affecting team name displays.<br>
After running the script, Relay Team Name format will work normally and will not affect Team Names. Recommended Relay Team Name format is `Abbr-A`. 

## Instructions
- Download and unzip the release package.
- Place **the folder containing** `removerelays.exe` into the Quantum Data Set directory (i.e. the directory containing `quantum.slx`)
  - The script works on the parent directory. For example, if your QAQF Data Set is in `C:\Quantum DB\Race1\`, the application should be found at `C:\Quantum DB\Race1\RemoveRelaysScript\removerelays.exe`. No paths need to be defined if this format is followed correctly.
- At the beginning of a session of individual events, open the folder containing `removerelays.exe`. Double click the application to run the script. Then, import your meet schedule and refresh your start list as normal.
  - The script will need to be re-run each time the start list is re-pushed for individual events.
- Re-push relay-seeded Start List from HyTek Meet Manager 8.0 before relay events. Refresh the start list without running the relay removal script immediately prior to relays.
  - Relay start list can be pushed from Meet Manager 8.0 as soon as the relay-less start list has been imported into Quantum-AQ. However, if you need to refresh your start list, re-run the script.

## System Requirements
This application has been produced for use with SwissTiming Quantum-AQ and HyTek Swim Meet Manager 8.0 softwares, on Windows x86-64 operating systems. It has been tested to work on Windows 10 and Windows 11 operating systems with x64 CPUs. <br>
The package comes as a Windows (`*.exe`) application, which can be run without Python. However, Python3 is required to run the Python (`*.py`) application. The `setup.py` file has been included for compiling using [py2exe](https://pypi.org/project/py2exe/).
