#!/bin/bash

INFILE=$1
OUTFILE=$2

tr -c '[:alnum:]' '[\n*]' < $INFILE | sort | uniq -c | sort -nr | head -100 > $OUTFILE
