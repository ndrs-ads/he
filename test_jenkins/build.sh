#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
array=`find $DIR -maxdepth 1 -type f -name 'ut*.py'`

for file in $array; do
    python "$file"
done
