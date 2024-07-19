import os
import subprocess
import sys 

def run_scripts(name):
    paths = {
        "AZ" : 'some path',
        "SY" : 'another path'
    }
    print(f'Using {paths[name]}')
    for script in ['scriptA.py', 'scriptB.py', 'scriptC.py']:
        subprocess.call(["python3", script])

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '--name':
        print("Usage: python test.py --name <name>")
        sys.exit(1);
    name = sys.argv[2]
    run_scripts(name)