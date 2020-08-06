'''
Created on July 17, 2018
@author: Kasey McFadden
'''
import sys
sys.path.append('../conf')
sys.path.append('../libs')
import json
from variables import nexmo_api_key, nexmo_api_secret
import nexmo

    
def rentSMS():
    client = nexmo.Client(key=nexmo_api_key, secret=nexmo_api_secret)
    options = json.loads(client.get_available_numbers("US", {"features": "SMS"}))
    v_num = options.get('numbers')[0].get('msisdn')
    response = json.loads(client.buy_number({"country": "US", "msisdn": v_num}))
    if response.get('error-code') == '200':
        return v_num
    print("Could not purchase number. Something went wrong.")
    return '123'

def sendSMS(send_to, send_from, content): 
    client = nexmo.Client(key=nexmo_api_key, secret=nexmo_api_secret)
    sms_type = 'text'

    result = client.send_message({
        'text': content,
        'from': str(send_from), 
        'to': str(send_to),
        'type': sms_type
    })

    # get returned http code from JSON data
    response = result['messages'][0]

    # return success message if code = 0 (success), otherwise indicate error
    if response['status'] == '0':
        return "Message sent to %s: '%s'" % (send_to, content)
    else:
        return 'Error:', response['error-text']
