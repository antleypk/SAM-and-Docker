#--------------------------------------------------
# Title : Obstacles By Location
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

# returns JSON of all of the obstacles grouped by the Location they appeared in. JSON output

def obstacle_by_city():
    key = 'anwoh.csv'
    bucket = 'ninja-warrior-antleypk'
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket,key,'/tmp/local.csv')
    data = {}
     
    locations = []
    with open('/tmp/local.csv', 'rt') as csvfile:
        dict_read = csv.DictReader(csvfile)
        for r in dict_read:
            location = r['Location']
            locations.append(location)
    unique_locations = []
    
    for l in locations:
        present = 0
        for ul in unique_locations:
            if ul[0] == l:
                present =1
        if present == 0:
            frame = []
            frame = [l,0]
            unique_locations.append(frame)
    
    for ll in locations:
        for ull in unique_locations:
            if ull[0] == ll:
                ull[1] = ull[1]+1
    c = 0            
    for t in unique_locations:
        data[c] = t
        c+=1
        
    return data



def lambda_handler(event, context):

    return {
        'statusCode':200,
        'headers': {'Content-Type': 'application/json'},
        'body' : json.dumps(obstacle_by_city())
    }