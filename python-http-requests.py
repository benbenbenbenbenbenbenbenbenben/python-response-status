#!/usr/bin/env python3

#description     :Validate API Response and print status code 
#author          :Ben Kersnovske
#usage           :python3 python-http-requests.py
#python_version  :3.7.4 

# Import the modules needed to run the script.
import json
import requests

apikey = '' #Add your API Key
headers = {'X-Cisco-Meraki-API-Key': apikey, 'Content-Type': 'application/json'}

api_url = 'https://api.meraki.com/api/v0/organizations' 

def get_request():
    response = requests.get(api_url, headers=headers)
    print(f'Get Request URL:   {api_url}')
    # print(response.request.headers)       #Uncomment to print request header
    # print(response.headers)               #Uncomment to print response header
    validate_response(response)
    return None

# Validate Request Response for Error Codes
def validate_response(response):
    print('Response Status:')
    if response.status_code >= 500:
        print(f'Server Error: {response.status_code}')
        return None
    elif response.status_code == 404:
        print(f'Not Found: {response.status_code}')
        return None  
    elif response.status_code == 400:
        print(f'Bad Request: {response.status_code}')
        return None
    elif response.status_code >= 400:
        print(f'Other Client Side Error: {response.status_code}')
        return None
    elif response.status_code >= 300:
        print(f'Redirct: {response.status_code}') 
        #Check if the response has a redirect URL     
        if 'Location' in response.headers:          
            print('Redirect URL: ' + response.headers['Location'])
        return None
    elif response.status_code >= 200:
        print(f'OK: {response.status_code}')
        #Check if response has JSON data
        if 'application/json' in response.headers['content-type']:  
            json_data = response.json()
            print(json_data)
        return None
    else:
        print(f'Unexpected Error: {response.status_code, response.content}')
    return None

get = get_request()


