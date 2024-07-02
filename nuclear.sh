#!/bin/zsh

nuclei -l $1 -t $2 -silent |tee >> x9_output
