# Make
Project Initialization Automation

## Overview
Problem: The proccess for creating projects is tedious and can be automated.\
The process:
- User enters command to execute Make
- Make takes in the parameters with exception and edge-case handling
- Make creates the nessesary files and folders
- Make opens ```README.md``` and writes the default text
- Make initializes git and opens Visual Studio Code
- Make prints a summary of everything it did for the user
## Setup
- On your computer, go to the terminal and type: ```git clone https://github.com/et-sollertis-animi/Make.git```
- In ```make.py```, change the value of the variable ```PROJECTDIRECTORY``` to the directory you keep your projects (keep the ```r``` in front of the double-quotes).
- **Linux-based Operating Systems**
	- In the terminal, type ```nano ~/.bashrc``` and use the arrow keys on the keyboard to scroll all the way down. 
	- Type ```alias make="python /path/to/make.py"```. Be sure to replace ```/path/to/make.py``` with the path to the ```make.py``` file that you cloned.
	- Press ```Ctrl+x``` and ```y``` to save and exit nano. Type ```source ~/.bashrc``` in the terminal. After this, you are done. To start using Make, type ```make``` and follow what the program returns.
- **Windows Operating System**
	- In the Powershell terminal, type ```$profile``` and copy the path returned.
	- Type ```notepad C:/path/given```, replace ```C:/path/given``` with the path that you copied.
	- In the notepad window, type ```function makePath {python C:/path/to/make.py}```, replacing ```C:/path/to/make.py``` with the path to the ```make.py``` file that you cloned.
	- Press enter and type ```set-alias -name make -value makePath```
	- Press ```Ctrl+s``` to save and close the window.
	- In the terminal, type ```powershell```. After this, you are done. To start using Make, type ```make``` and follow what the program returns.
