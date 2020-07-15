import json
# import time
# import boto3


def hello(event, context):
    # print("hi !")
    # print("first update")
    # print("second update")
    # time.sleep(4)
    # return "hello-world"

    # client = boto3.client('lambda')
    # response = client.list_functions()
    # return response

    # serverless default
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    # return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
