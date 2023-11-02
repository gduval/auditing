import boto3
from botocore.exceptions import ClientError
import json
from datetime import datetime, timezone
import base64

REGION_NAME = "us-east-2"


def get_parameter(parameter_name):
    client = boto3.client(service_name='ssm', region_name=REGION_NAME)
    get_parameter_value_reponse = client.get_parameter(Name=parameter_name, WithDecryption=False)

    return json.loads(get_parameter_value_reponse['Parameter']['Value'])

def get_secret(secret_key):
    client = boto3.client(service_name='secretsmanager', region_name=REGION_NAME)
    secret_response = client.get_secret_value(SecretId=secret_key)

    return json.loads(secret_response['SecretString'])

def get_secret_string(secret_key):
    client = boto3.client(service_name='secretsmanager', region_name=REGION_NAME)
    secret_response = client.get_secret_value(SecretId=secret_key)

    return secret_response['SecretString']
