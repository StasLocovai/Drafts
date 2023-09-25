import requests
import json
import jsonpath
import time

baseURL = "https://startcmsqa.sportifier.com/"
endPoint = 'qaauto'
pending = "Desired count updated to 1. Wait 2-5 minutes and then try to connect"
triggered = "Desired count is already set to 1"
invalidEndpoint = "ECS service not found \n Please check your spelling and Case-Sensitivity."


def call():
    try:
        response = requests.get(baseURL + endPoint)
        assert response.status_code == 200
        return response.text
    except ConnectionError as e:
        print(e)
        print("CHECK YOUR CONNECTION")


def test_service_response():
    message = call()
    if message == triggered:
        print("Success !\nLog in to CMS")
    elif message == pending:
        time.sleep(5)
        call()
        assert message == triggered
    elif message in invalidEndpoint:
        raise AssertionError('Invalid url or endPoint')
