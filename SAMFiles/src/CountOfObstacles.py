#--------------------------------------------------
# Title : Count Of Obstacles
#--------------------------------------------------
#--------------------------------------------------
# Author   |  Date             |  Notes
#--------------------------------------------------
# antleypk | 10 - AUG - 2018   | Created
#--------------------------------------------------
#--------------------------------------------------

import boto3
import json
import csv

s3_client = boto3.client('s3', 'us-east-1')

# returns the count of all featured Obstacles in the data set

def get_count_of_obstacles():
    key = 'anwoh.csv'
    bucket = 'ninja-warrior-antleypk'
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket,key,'/tmp/local.csv')
    data = {}
    with open('/tmp/local.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter = ' ', quotechar ='|')
        counter = -1
        for row in reader:
          # s=', '.join(row)
          # print (s)
          # data[counter] = s
           counter+=1
        data['count'] = counter
    return data


def lambda_handler(event, context):


    return {
        'statusCode':200,
        'headers': {'Content-Type': 'application/json'},
        'body' : json.dumps(get_count_of_obstacles())
    }
