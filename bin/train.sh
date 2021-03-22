#!/usr/bin/env bash

set -exu

config_file=$1
is_parallel=${2-False}

python -m src.train -c $config_file -p $is_parallel
