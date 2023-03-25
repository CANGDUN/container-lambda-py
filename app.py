import boto3
import json

def handler(event, context):
    sts = boto3.client('sts')
    account_id = sts.get_caller_identity()['Account']

    message = f'''Hello from Container Lambda!
Your Account ID is {account_id}'''

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
