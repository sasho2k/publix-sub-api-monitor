import json
import requests
from services.sub_info import sub


# 200 = error with the api
# 201 = error with the server
# This is my code so idc if u dont like it sorry bro go fork the repo if u think ur steve wozniak
def grab_sale_api_json(storeNumber=None):
    if not storeNumber:
        url = "http://157.230.182.224:3000/get-sale/"
    else:
        url = "http://157.230.182.224:3000/get-sale/" + storeNumber

    try:
        request = requests.get(url)
        if (request.status_code != 200) or (request.content is None):
            return 200
    except:
        return 201

    return request.json()


def grab_subs_api_json(storeNumber):
    url = "http://157.230.182.224:3000/get-subs/" + storeNumber
    try:
        request = requests.get(url)
        if (request.status_code != 200) or (request.content is None):
            return 200
    except:
        return 201

    return request.json()


def return_parsed_objs(storeNumber):
    subs = []
    resp = grab_subs_api_json(storeNumber)
    if (resp == 200) or (resp == 201):
        return resp

    for json_sub in resp:
        subs.append(sub().set_sub(json_sub['name'], json_sub['price'], json_sub['savingMsg'], json_sub['description'],
                                  json_sub['productID'], json_sub['itemCode']))

    return subs


def return_parsed_obj(storeNumber=None):
    resp = grab_sale_api_json(storeNumber)
    if (resp == 200) or (resp == 201):
        return resp

    sub_obj = sub().set_sub(resp['name'], resp['price'], resp['savingMsg'],
                            resp['description'], resp['productID'], resp['itemCode'])

    return sub_obj
