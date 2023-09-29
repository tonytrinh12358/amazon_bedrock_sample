import os
import boto3 #import aws sdk and supporting libraries
import json
import base64
from io import BytesIO

session = boto3.Session(
    profile_name=os.environ.get("BWB_PROFILE_NAME")
) #sets the profile name to use for AWS credentials

bedrock = session.client(
    service_name='bedrock', #creates a Bedrock client
    region_name=os.environ.get("BWB_REGION_NAME"),
    endpoint_url=os.environ.get("BWB_ENDPOINT_URL")
)


def get_text_response(input_content): #text-to-text client function
    # "body": "{\"prompt\":\"Human: tell me a joke\\nAssistant:\",\"max_tokens_to_sample\":2048,\"temperature\":1,\"top_k\":250,\"top_p\":0.999,\"stop_sequences\":[\"\\n\\nHuman:\"]}"

    prompt = f"Human: {input_content}\\nAssistant:"
    max_tokens_to_sample = 1024
    body = json.dumps({"prompt": prompt, "max_tokens_to_sample": max_tokens_to_sample, "stop_sequences":["\\n\\nHuman:"] })
    modelId= 'anthropic.claude-v2'
    accept = '*/*'
    contentType = 'application/json'
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept,contentType=contentType)
    response_body = json.loads(response.get('body').read())

    return response_body['completion']

def get_response_image_from_payload(response): #returns the image bytes from the model response payload

    payload = json.loads(response.get('body').read()) #load the response body into a json object
    images = payload.get('artifacts') #extract the image artifacts
    image_data = base64.b64decode(images[0].get('base64')) #decode image
    return BytesIO(image_data) #return a BytesIO object for client app consumption



def get_image_response(prompt_content): #text-to-text client function

    request_body = json.dumps({"text_prompts":
                               [ {"text": prompt_content } ], #prompts to use
                               "cfg_scale": 9, #how closely the model tries to match the prompt
                               "steps": 50, }) #number of diffusion steps to perform

    bedrock_model_id = "stability.stable-diffusion-xl" #use the Stable Diffusion model

    response = bedrock.invoke_model(body=request_body, modelId=bedrock_model_id) #call the Bedrock endpoint

    output = get_response_image_from_payload(response) #convert the response payload to a BytesIO object for the client to consume

    return output

