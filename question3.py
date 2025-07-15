import boto3
from botocore.exceptions import ClientError

def check_api_success():
    try:
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("API call successful")
            return response
        else:
            print(f"Unexpected status code: {response['ResponseMetadata']['HTTPStatusCode']}")
           
    except ClientError as e:
        print(f"API call failed: {e}")
        return None
