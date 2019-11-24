# AirBnB_clone
### Overview
This project is a collection of all that we have learnt in Python. Using all our knowledge of what we know, we are tasked to build a clone of AirBnB. Broken down into smaller chunks, this first portion is building the console and setting up classes that will be used in the console. Updates will be posted as new sections are released.
### Installation
Clone the repository to your terminal in your desired working directory. To clone the repository, run the following command to your command line:
`git clone <url of repo>`
### Getting started
Once the repo has been cloned, ensure that all files are executable if they are not already executable. To give execution rights, use the following command in each individual directory:
`chmod u+x *` for all files or `chmod u+x <file>` for individual files.
### Usage
For usage, run the following command to your command line for interactive mode:
`./console.py`

The prompt should be "(hbnb) "

For non-interactive mode, please use the following format:
`echo "<cmd>" | ./console.py`

The results will print out to the stdout along with your shell's prompt following after, indicating the program has exited after executing command.
### Commands
Command | Description
--------|-------------
help    | Displays all available commands in console
EOF     | Exits console, equivalent of ctrl D
quit    | Exits console, equivalent of ctrl C
create  | Creates a new instance
show    | Prints string representation of an instance
all     | Prints all string representation or of a specified class
update  | Updates attributes of an instance and saves
destroy | Deletes specified instance
### Examples
* Interactive console
```
$ ./console
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
* Non-interactive console
```
$ echo "help" | ./console
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) $
```
### Release History
* 0.1.0 - First release - 14 Nov 2019
## Authors
* [Marco Chan](https://github.com/inspiredtolive)
* [Alia Vang](https://github.com/aliavang)
## Acknowledgments
All the wonderful people who helped us build the AirBnB_clone!
