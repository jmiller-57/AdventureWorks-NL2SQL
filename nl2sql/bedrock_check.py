import os
import boto3
import json

region = os.environ.get("AWS_REGION", "us-east-2")
bedrock = boto3.client("bedrock-runtime", region_name=region)

model_id = os.environ["BEDROCK_MODEL_ID"]

payload = {
    "system": "You are a helpful assistant.",
    "messages": [
        {"role": "user", "content": "Hello, are you there?"}
    ],
    "max_tokens": 2048,
    "temperature": 1,
    "top_k": 250,
    "top_p": 0.999,
    "anthropic_version": "bedrock-2023-05-31"
}

response = bedrock.invoke_model(
    modelId=model_id,
    body=json.dumps(payload).encode("utf-8")
)

result = json.loads(response["body"].read())
print(json.dumps(result, indent=2))

