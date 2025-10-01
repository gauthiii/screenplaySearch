# Use the Conversation API to send a text message to Meta Llama.

import boto3
from botocore.exceptions import ClientError
import json

prompt_data="""
Describe the purpose of a 'agentic ai' in one line.
"""

# Create a Bedrock Runtime client in the AWS Region of your choice.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Llama 3 70b Instruct.
model_id = "meta.llama3-70b-instruct-v1:0"

# Embed the prompt in Llama 3's instruction format.
formatted_prompt = f"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
{prompt_data}
<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>
"""

# Format the request payload.
payload={
    "prompt":formatted_prompt,
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}

# Convert the payload request to JSON.
body=json.dumps(payload)

try:
    # Invoke the model with the request.
    response = client.invoke_model(
        modelId=model_id, 
        body=body,
        accept="application/json",
        contentType="application/json"
        )

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

# Decode the response body.
model_response=json.loads(response["body"].read())

# Extract and print the response text.
response_text = model_response["generation"]

print(response_text)


