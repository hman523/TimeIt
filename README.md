# TimeIt
A program for timing the run time of other programs

This program uses the MIT licence. Please respect it.

# How to use it and what it is for
This program is for timing programs.  It can be used to compare the actual runtimes of algorithms or for
testing how a program holds up.  It also can iterate through multiple times to gain more accurate results.

## Parameters
The command structure is
```
python TimeIt.py -c 'Your command' [Optional commands]
```
The optional command is -i.  It represents the ieterations for averaging.  It takes an integer and that is the number of iterations.


### Examples
```
python TimeIt.py -c 'touch hello' -i 10
```
This command would run ``` touch hello ``` ten times.

If you would like to run a command such as ```echo 'hello' ``` and time it, you must include propper Python 2 escape sequences.
The correct notation would be
```
python TimeIt.py -c 'echo \'hello\''
```

