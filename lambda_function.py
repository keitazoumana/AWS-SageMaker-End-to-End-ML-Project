import os
import json
import boto3

# Grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    # Assuming the input is in the format {'text': 'your text here'}
    data = json.loads(json.dumps(event))
    text = data['text']
    
    # Encode the text
    encoded_text = text.encode('utf-8')
    
    # Query the endpoint
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='application/x-text',
                                       Accept='application/json;verbose',
                                       Body=encoded_text)
    
    print("Raw response:", response)
    
    # Parse the response
    response_body = json.loads(response['Body'].read().decode())
    print("Parsed response:", response_body)
    
    probabilities = response_body['probabilities']
    labels = response_body['labels']
    predicted_label = response_body['predicted_label']
    
    # Convert predicted_label to 'Positive' or 'Negative'
    sentiment = 'Positive' if predicted_label == 1 else 'Negative'
    
    result = {
        'sentiment': sentiment,
        'probabilities': probabilities,
        'labels': labels
    }
    
    return result
