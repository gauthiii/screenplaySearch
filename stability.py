
import boto3
import json
import base64
import io
from PIL import Image

from botocore.exceptions import ClientError

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# prompt = "A house made out of apples."

modelId='us.stability.stable-image-core-v1:0'

try:
    response = bedrock.invoke_model(
         modelId=modelId,
         body=json.dumps({
             'prompt': 'A car made out of vegetables.'
         })
     )

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{modelId}'. Reason: {e}")
    exit(1)

output_body = json.loads(response["body"].read().decode("utf-8"))
base64_output_image = output_body["images"][0]
image_data = base64.b64decode(base64_output_image)
image = Image.open(io.BytesIO(image_data))
image.save("image.png")