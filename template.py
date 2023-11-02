#dbutils.widgets.removeAll()

# COMMAND ----------
import requests
import json
import boto3
import base64
from botocore.exceptions import ClientError
import pandas as pd
from pandas.io.json import json_normalize
from commons.utils.aws_utils import *

# COMMAND ----------
secrets = get_secret(secret_path)
token = secrets['login_or_token']

# COMMAND ----------
url = ''
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': token
}

# COMMAND ----------
response = requests.request("GET", url, headers=headers)
new_res = response.json()

# COMMAND ----------
output_json = json.dumps(new_res)
df = spark.read.json(sc.parallelize([output_json]))
target = ''
df.write.option("overwriteSchema", "true").mode("append").saveAsTable(target)
