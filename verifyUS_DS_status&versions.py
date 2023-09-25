import requests
import jsonpath
import json

us_status = "http://qaupdates-auto.365scores.com/statistics.aspx"
ds_status = "https://qa-auto.365scores.com/status"
ds_version = "7.3.0.0"
us_version = "4.33.4.0"


def test_verify_status_DS():
    try:
        v_response = requests.get(ds_status)
        assert v_response.status_code == 200
        json_data = json.loads(v_response.text)
        v_version = jsonpath.jsonpath(json_data, 'Version')
        # assert option_1 - comparing as chars of strings ?
        assert v_version[0] >= ds_version
        # assert option_2 - comparing as lists of integers
        assert list(map(int, v_version[0].split('.'))) >= list(map(int, ds_version.split('.')))
        # Verify the state is running:
        v_run_time = jsonpath.jsonpath(json_data, 'TimeRunning')
        assert v_run_time[0] > 0
    except ConnectionError as e:
        print(e)


def test_verify_US():
    try:
        v_response = requests.get(us_status)
        assert v_response.status_code == 200
        json_data = json.loads(v_response.text)
        v_version = jsonpath.jsonpath(json_data, 'UpdatesService Version')
        assert v_version[0] >= us_version
        # verify the state is running:
        assert "Working for" in v_version[0]
    except ConnectionError as e:
        print(e)
