
# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import Anthropic
from anthropic import Anthropic

# Create API client
client = Anthropic()

# Select model
model = "claude-sonnet-5-5"
response = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is Python? Explain in one sentence."
        }
    ]
)

# Step 6: Print Claude's response
# print(response.content[0].text)
message.content[0].text