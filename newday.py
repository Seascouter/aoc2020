#!/usr/bin/env python3

import sys
import os

class termtext:
    ERR = '\033[91m'
    END = '\033[0m'
    BOLD = '\u001b[1m'
    UNDERLINE = '\u001b[4m'
    GREEN = '\u001b[32m'
    
sys.argv = sys.argv[1:]
if len(sys.argv) < 1:
    print(f"{termtext.ERR}ERROR: not enough arguments supplied (expected 1){termtext.END}")
    print("Usage: ./newday.py {number}")
    sys.exit(1)

folder = f"day{sys.argv[0]}"

os.system(f"cp -r dayexample {folder}")

print(f"{termtext.GREEN}Successfully created directory 'day{sys.argv[0]}'{termtext.END}")
