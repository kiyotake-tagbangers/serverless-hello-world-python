# import json
# import time
import boto3


def hello(event, context):
    # print("hi !")
    # print("first update")
    # print("second update")
    # time.sleep(4)
    # return "hello-world"

    client = boto3.client('lambda')
    response = client.list_functions()
    return response