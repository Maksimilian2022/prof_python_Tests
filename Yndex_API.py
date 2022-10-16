import requests

def create_folder(path):
    TOKEN = "AQAAAABR6sW2AADLW-hiYhDRWkXIgVyXB5LPvQQ"
    URL = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
    params = {"path": path}
    put_resourses = requests.put(url=URL, params=params, headers=headers)
    return put_resourses.status_code
