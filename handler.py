DORMANT = False

import sys
sys.path.append('libs')
sys.path.append('conf')
sys.path.append('src')
from variables import nexmo_number
import logging
import json
from interpreter import interpreter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Default lambda response
data = {
    "statusCode": 200,
    "headers": {"Content-Type": "text/html"}, 
    "body": None
}

# Lambda entry point: handler.lambda_handler
def lambda_handler(event, context):
    if DORMANT:
        return data

    try:
        params = event.get('queryStringParameters')
        resource = event.get('path')
    except:
        params = event
        resource = '/users'

    if (resource == '/users'):
        text = params.get("text")
        msisdn = params.get("msisdn")
        v_num = params.get("to")

        # if null, request, return 200 OK and do nothing
        if not text or text == 'None':
            return data

        sent = interpreter(text, msisdn, v_num)
        data["body"] = json.dumps({"Status": "%s" % sent})
        print (data)

        return data


