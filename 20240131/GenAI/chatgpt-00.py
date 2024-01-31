import openai

import os
import dotenv
dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_ENDPOINT = os.getenv('OPENAI_API_ENDPOINT')
OPENAI_API_TYPE = 'azure'
OPENAI_API_VERSION = '2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

query = "Why Korean people work so hard?"

result = openai.chat.completions.create(
    model="dev-gpt-35-turbo",
    messages=[
        {"role" : "system", "content" : "you are a helpful assistant"},
        {"role" : "user", "content" : query},
    ]
)

print(result.choices[0].message.content)