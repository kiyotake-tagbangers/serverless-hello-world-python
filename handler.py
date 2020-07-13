import json
import time


def hello(event, context):
    # print("hi !")
    # print("first update")
    print("second update")
    time.sleep(4)
    return "hello-world"