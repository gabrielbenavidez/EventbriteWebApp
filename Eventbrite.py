
import requests
import json


base_url = 'https://www.eventbriteapi.com/v3/'
api_key_prefix = '?token='
api_key = 'your_key_here'
organization_id = '299555869885/'
events_tag = 'events/'
users_tag = 'users/'
organization_tag = 'organizations/'
description_tag = 'description/'
me_tag = 'me/'



def readFromFile(file_name):
    with open(file_name, 'r') as read_file:
        file = json.load(read_file)
        print("read")
        return file


def save_to_file(data, file_name):
    with open(file_name, 'w') as write_file:
        json.dump(data, write_file, indent=4)
        print("The file {0} was successfully created.".format(file_name))


def listOrganizationEvents():
    target_url = base_url + organization_tag + organization_id + events_tag + api_key_prefix + api_key
    organization_event = requests.get(url=target_url)
    organization_event_json = organization_event.json()
    return organization_event_json


def deleteEvent(event_id):
    endpoint_url = base_url + events_tag + event_id + api_key_prefix + api_key
    event_json = requests.delete(url=endpoint_url).json()
    return event_json


def createEvent(event_name,event_start_utc,event_end_utc,event_currency):
    timeZone = 'America/New_York'
    headers = {'content-type': 'application/json'}
    organizations_tag = 'organizations/'
    event_data = {
        "event": {
            "name": {"html": event_name},
            "start": { "timezone": timeZone, "utc": event_start_utc},
            "end": { "timezone": timeZone, "utc": event_end_utc},
            "currency": event_currency
        }
    }
    url_endpoint = base_url + organizations_tag + organization_id + events_tag + api_key_prefix + api_key
    post_info = requests.post(url=url_endpoint,json=event_data, headers=headers).status_code
    return post_info




#######################################################
#These are extra methods that can be used to get additional data
#they have not been implemented in flask however.
#######################################################

def searchEventById(event_id):
    target_url = base_url + events_tag + event_id + description_tag + api_key_prefix + api_key
    event_json = requests.get(url=target_url).url
    print(event_json)


def getUserInfo():
    user_info = requests.get(url=base_url + users_tag + me_tag + api_key_prefix + api_key)
    user_info_json = user_info.json()
    return user_info_json


#dummmy data for testing
# event_name = 'my new event'
# event_start_utc = '2020-05-12T02:00:00Z' #date and time utc format
# event_end_utc = '2020-05-12T02:00:00Z'   #date and time utc format
# event_currency = 'USD'








