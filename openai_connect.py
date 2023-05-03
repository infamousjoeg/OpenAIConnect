import os
import json
import boto3
import openai

def lambda_handler(event, context):
    # Extract the user input from the Amazon Lex event
    user_input = event['inputTranscript']

    # Send user input to OpenAI API
    response = openai.Completion.create(
        model=os.getenv("OPENAI_MODEL_ID"),
        prompt=user_input,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response
    davinci_response = response.choices[0].text.strip()

    # Return the response to Amazon Lex
    return {
        'sessionState': {
            'dialogAction': {
                'type': 'ElicitIntent',
            }
        },
        'messages': [
            {
                'contentType': 'PlainText',
                'content': davinci_response
            }
        ]
    }
