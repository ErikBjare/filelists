filelists
=========

Generate a list of all the files on your computer for faster search, backup purposes and more.

 - Simply grep the output file or search it with less to find the location of a file you're looking for.
 - If an entire disk is lost, the knowledge of which files once existed may still be of value.
 - Worried you might have put a sensitive file in a unsafe place? Look it up quickly!

There are probably faster ways to index and query the list, but this is keeping it very simple.
Also, this was fast enough for me, surprisingly. (apart from building the original filelist)

### Things you can do

*Where are the most files located?*

    # Creates a file filelist_root.txt (may be larger than 1GB if you, like me, have a lot of files)
    # May take a long time, it took 33 minutes on my ~6 million files spread across
    # multiple drives, some of them slow and encrypted (taking significant time to traverse)
    # It is also likely to spew a bunch of "Permission denied", they are harmless.
    ./generate_filelist_root.sh

    # Create a list of the directories up to the default depth 4
    # Each directory is prepended with the total number of files it contains
    ./common_paths.py > filelist_common_dirs.txt

    # Sort the list of directories in order of number of files contained by them
    sort -nr < filelist_common_dirs.txt | less
    
*Where is my Bitcoin wallet?*

    grep "wallet.dat" filelist_root.txt

### Performance

`common_paths.py`

 - Can only utilize a single processor core
 - Took about 58s to process a list with 6773057 files on a Intel Core i7-6700K (4.00GHz)
    - Sourcefile was 1.1GB and read from a SSD

