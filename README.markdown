ZFS snapshots are stored in the root of the filesystem under
a hidden .zfs/snapshot directory. This is difficult for users
to find when there is no filesystem per user but a shared large
filesystem.

## Installation ##
    $ cd /usr/local
    $ git clone git://github.com/kapsiry/zfs-snapshot-helper.git
    (for each user, maybe from global bashrc?)
    $ source /usr/local/snapshot.sh

## Requirements ##

* zfs; the whole point depends on having snapshots in the first place
* Recent python
* bash4 (for associative arrays)

## Usage ##

The helper script works like this:

    # List snapshots for current directory and cd into #13
    joneskoo@lakka:~/siilo$ zfs-snapshots
    1) Sun 11.12.2011 00:00    9) Mon 19.12.2011 00:00
    2) Mon 12.12.2011 00:00   10) Tue 20.12.2011 00:00
    3) Tue 13.12.2011 00:00   11) Wed 21.12.2011 00:00
    4) Wed 14.12.2011 00:00   12) Thu 22.12.2011 00:00
    5) Thu 15.12.2011 00:00   13) Fri 23.12.2011 00:00
    6) Fri 16.12.2011 00:00   14) Sat 24.12.2011 00:00
    7) Sat 17.12.2011 00:00   15) Sun 25.12.2011 00:00
    8) Sun 18.12.2011 00:00
    #? 13
    /siilo/.zfs/snapshot/daily-2011-12-23_0000/users/joneskoo ~/siilo ~
    joneskoo@lakka:/siilo/.zfs/snapshot/daily-2011-12-23_0000/users/joneskoo$ ls
    -rw-------+    1 joneskoo users       5316 Apr  4  2009 readme.txt
    drwx------+    2 joneskoo users         64 Jan 28  2011 safe
    # Return to original directory
    joneskoo@lakka:/siilo/.zfs/snapshot/daily-2011-12-23_0000/users/joneskoo$ popd
    ~/siilo ~
    joneskoo@lakka:~/siilo$ 
