#!/bin/bash


ls -a
shopt -s dotglob
shopt -s nullglob
DIR_LIST=(*/)

for dir in ${DIR_LIST[@]}; do
    array=`find $dir -maxdepth 1 -type f -name 'ut_*.py'`

    for file in $array; do
        python "$file"
    done
done

