# Progress

Progress is a lightweight command line tool for measuring large data transfers. Although rsync has a built in progress bar, it only measures the progress of individual file transfers. Users who need to use rsync to transfer entire uncompressed directories, at terabyte and petabyte scales, will not find rysnc's per-file progress output to be particularly informative.

Progress works by measuring the size of the target directory on the destination host and comparing it against a user provided value that represents the total size of the data transfer, in gigabytes.

## Example Usage:

$ cd /target/directory
$ python progress.py 4500

...where 4500 equals the total size of the data transfer, in gigabytes.
