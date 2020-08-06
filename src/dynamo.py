DEBUG = True

# Getting set up with DynamoDB
import boto3
TABLE = 'Burner'
UID = '11234567899'
v_num = '123'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE)

def dynamo_put(UID=UID, v_num=v_num):
    item = dynamo_get(UID)
    if not item:
        response = table.put_item(
           Item={
                'UID': UID,
                'v_num_1': v_num,
            }
        )
    else:
        for i in range(1,7):
            ID = 'v_num_' + str(i)
            if not item.get(ID):
                item[ID] = v_num
                break
        response = table.put_item(Item=item)
    if DEBUG: print (response)
    return response

def dynamo_get(UID=UID):
    response = table.get_item(
        Key={
            'UID': UID,
        }
    )
    if DEBUG: print (response)
    return response.get('Item')
