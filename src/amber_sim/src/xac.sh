#! /bin/bash
if xacro $1 > $2 ; then
    echo "xacro: Successfully converted" $1 "to" $2;
fi