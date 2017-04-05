#!/bin/bash

repetitions=$1

for i in `seq 1 $repetitions`; do
  timeout 1 java -d32 -cp tmp Principal
done
