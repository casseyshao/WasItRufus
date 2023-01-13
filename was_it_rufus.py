import sys # For command line arguments.
import os # For running commands in script.
from datetime import datetime, timedelta

# Initialize dictionary to hold output.
out = {
    "active branch:": "",
    "local changes:": False,
    "recent commit:": False,
    "blame Rufus:": False
}

# Process the input.
# Check that the command format is correct.
# Case when there are spaces in the directory name.
dir = sys.argv[2]

# Get active branch.
try:
    os.chdir(dir)
    branch = os.popen("git rev-parse --abbrev-ref HEAD").read()
    out["active branch:"] = branch.rstrip()
except:
    print("The directory does not exist or it is not a git repository")

# Check if repository files have been modified.
changes = os.popen("git diff --exit-code").read()
out["local changes:"] = (changes != "")

# Check if the current head commit was authored in the last week (boolean).
curr = datetime.today()
latest = os.popen("git log -1 --format=%cd").read()
latest = datetime.strptime(' '.join(latest.split(' ')[:-1]), '%a %b %d %H:%M:%S %Y')
out["recent commit:"] = (latest >= (curr-timedelta(days=7)))

# Check if the current head commit was authored by Rufus (boolean).
author = os.popen("git log -1 --format=%an").read()
out["blame Rufus:"] = (author == "Rufus")

# Print output.
for key in out:
    print(key, out[key])
