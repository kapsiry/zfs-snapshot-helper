#!/usr/bin/env python
import sys
import os
import os.path
import re
from datetime import datetime
from glob import glob

# Snapshot patterns to ignore
IGNORE = ["^sync-snap", "^zfs-auto-snap"]

def find_zfs_root(path):
    if not path:
        return None
    cwd = os.path.abspath(path)
    while not cwd == "/":
        zfsdir = os.path.join(cwd, ".zfs")
        if os.path.exists(zfsdir):
            return cwd
        cwd = os.path.abspath(os.path.join(cwd, ".."))
    return None

def list_snapshots(path):
    if not path:
        return None
    globpat = os.path.join(path, ".zfs", "snapshot", "*")
    snapdirs = glob(globpat)
    snapshots = []
    for d in snapdirs:
        d = os.path.basename(d)
        # Ignore if any of the ignores match
        ignored = any([re.match(pattern, d) for pattern in IGNORE])
        if not ignored:
            snapshots.append(d)
    return snapshots

def sort_key(x):
    if '-' in x:
        return x.split("-", 1)[1]
    else:
        return " " + x

cwd = os.getcwd()
fs_root = find_zfs_root(cwd)
if not fs_root:
    sys.exit(1)
reldir = cwd.lstrip(fs_root)

snapshots = list_snapshots(fs_root)
if not snapshots:
    sys.exit(1)
snapshots.sort(key=sort_key)

for snapshot in snapshots:
    path = os.path.join(fs_root, ".zfs", "snapshot", snapshot, reldir)
    if not os.path.exists(path):
        continue
    displayname = snapshot
    match = re.match(".*-(\d{4}-\d{2}-\d{2}_\d{4})", snapshot)
    if match:
        date = datetime.strptime(match.group(1), "%Y-%m-%d_%H%M")
        displayname = date.strftime("%a %d.%m.%Y %H:%M")
    sys.stdout.write(displayname + "\t" + path + "\0")
