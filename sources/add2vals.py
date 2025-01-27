'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

LIGHT_GREEN = "\033[1;32m"
LIGHT_RED = "\033[1;31m"
YELLOW = "\033[1;33m"
END = "\033[0m"

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    result = str(calc.add2(str(sys.argv[1]), str(sys.argv[2])))
    print("")
    print("The result is " + f"{LIGHT_GREEN}{result}{END}")
    print("")
    sys.exit(0)

if argnumbers != 2 :
    strarg = str(argnumbers)
    print("")
    print("You entered " + f"{LIGHT_RED}{strarg}{END}" + " value/s.")
    print("")
    print(f"{YELLOW}Usage: 'add2vals X Y' where X and Y are individual values.")
    print(f"       If add2vals is not in your path, usage is './add2vals X Y'.")
    print(f"       If unbundled, usage is 'python add2vals.py X Y'.{END}")
    print("")
    sys.exit(1)
