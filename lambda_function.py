import json
import logging
import boto3
import botocore
logging.getLogger().setLevel(logging.INFO)
s3 = boto3.resource('s3')
BUCKET_NAME="dev-days-test"
KEY="hello.txt"



def lambda_handler(event, context):
    # TODO implement
    logging.info(event)
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, "/tmp/hello_1.txt")
        file = open("/tmp/hello_1.txt", "r")

    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == '404':
            logging.error('Object is not found')
        else:
            raise e
    return {
        'statusCode': 200,
       # 'body': json.dumps('Hello from Lambda!')
       'body': file.read()
    }
