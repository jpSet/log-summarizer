import os
from anthropic import Anthropic
import loadCompanyPolicies

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

messages=client.messages.create(
    max_tokens=1024,
    messages=[
    {
        "role": "user",
        "content": "Hello!"
    }
    ],
    model="claude-haiku-4-5-20251001",
)

print(messages.content)


