#!/bin/bash

#data set up

aws s3 mb s3://ninja-warrior-antleypk

aws s3 mb s3://ninja-warrior-sam

aws s3 cp s3://dataworld-odaws-us-east-1/datasets/ninja/anw-obstacle-history/ SAMFiles/SAMFiles/ninja_data --recursive

python SAMFiles/SAMFiles/src/xl_convert.py

aws s3 cp ninja_data/anwoh.csv s3://ninja-warrior-antleypk



# generate next stage yaml file
aws cloudformation package                   \
    --template-file SAMFiles/SAMFiles/template.yaml            \
    --output-template-file SAMFiles/SAMFiles/out/output.yaml \
    --s3-bucket ninja-warrior-sam     

# the actual deployment step
aws cloudformation deploy                   \
    --template-file SAMFiles/SAMFiles/out/output.yaml         \
    --stack-name antleypkCodeTest           \
    --capabilities CAPABILITY_IAM             
               

$SHELL