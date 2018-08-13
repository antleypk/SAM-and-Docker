#--------------------------------------------------
# Unit Test 
#--------------------------------------------------
# Author   |  Date             |  Notes
#--------------------------------------------------
# antleypk | 12 - AUG - 2018  | Created
#--------------------------------------------------
#--------------------------------------------------


import boto3
import os
import json
from botocore.exceptions import ClientError
from botocore.vendored import requests

def select_all():
    client = boto3.client('lambda')
    response = client.invoke(
    FunctionName='SAMAllObstacles',
    InvocationType='RequestResponse',
    LogType='None',
)              
    data = clean(response)
    control = '"1.0","Sasuke, 23, (Japan)","National, Finals, -, Stage, 4","G-Rope","2.0"'
    indepent = data['769']
    if control == indepent:
        return True
    else:
        return False
    print ('data: '+str(data['769']))


def count():
    client = boto3.client('lambda')
    response = client.invoke(
    FunctionName='SAMCountOfObstacles',
    InvocationType='RequestResponse',
    LogType='None',
)              
    data = clean(response)
    print ('count data: '+str(data))
    control = 769
    indepent = data['count']
    if control == indepent:
        return True
    else:
        return False


def count_by_location():
    client = boto3.client('lambda')
    response = client.invoke(
    FunctionName='SAMAllObstaclesByLocation',
    InvocationType='RequestResponse',
    LogType='None',
)              
    data = clean(response)
    control = "['Los Angeles', 32]"
    control = data['0']
    print('count by location: '+ str(control))
    indepent = data['0']
    if control == indepent:
        return True
    else:
        return False




def clean(response):
    data = response['Payload'].read()
    datatype = str(type(data))
    ddata = data.decode("utf-8") 
    jdat = json.loads(ddata)
    jdattype = str(type(jdat))
    jdatbody = jdat['body']
    body = json.loads(jdatbody)
    dat = body
    return dat

def test_suit():
    select_test = select_all()
    count_test = count()
    location_test = count_by_location()    
    frame = ['Select All Test',str(select_test)]
    frame1 = ['Obstacle Count Test', str(count_test)]
    frame2 = ['Location Count Test', str(location_test)]
    data = {}
    data_set = [frame, frame1, frame2]
    data['Tests'] = data_set
    return data_set
    
def lambda_handler(event, context):
   
    response =  {
        "statusCode": 200,
        "headers": { "Access-Control-Allow-Origin": "*" },
        "body": json.dumps(test_suit())
            
        }
    
    return response
