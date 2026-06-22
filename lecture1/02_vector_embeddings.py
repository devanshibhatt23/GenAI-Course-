from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Dog chases cat."

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector embeddings:", response)
# dimensions of the model
print("Length:", len(response.data[0].embedding))