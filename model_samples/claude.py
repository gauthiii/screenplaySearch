# This won't work because this model is not supported and we have to use Messages API

import boto3
import json
from botocore.exceptions import ClientError

brt = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

prompt = "Describe the concept of blackholes to a 10 year old"

body = json.dumps({
    "prompt": f"\n\nHuman:{prompt}\n\nAssistant:",
    "max_tokens_to_sample": 300,
    "temperature": 0.1,
    "top_p": 0.9,
})

modelId = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
accept = 'application/json'
contentType = 'application/json'

try:

    response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{modelId}'. Reason: {e}")
    exit(1)

response_body = json.loads(response.get('body').read())

# text
print(response_body.get('completion'))