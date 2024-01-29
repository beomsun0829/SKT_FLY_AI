import os
import dotenv
import openai
dotenv.load_dotenv()

client = openai.Client(api_key=os.environ["OPENAI_API_KEY"])

completion = client.chat.completions.create(
    model="davinci",
    messages = [
        {"role" : "User", "text" : "Hello, who are you?"},
    ]
)

print(completion.choices[0].message.content)