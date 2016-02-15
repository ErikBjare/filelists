#!/bin/bash


# TODO: Add list of words which should be filtered away by default
# TODO: Don't generate for root, generate for individual partitions since filenames may contain sensitive information

echo "Generating filelist of /"
find / > filelist_root.txt
echo "Done!"
