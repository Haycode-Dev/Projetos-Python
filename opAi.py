import openai
import os

# Create file
file_name = "ApiKey.txt"
file = open(file_name, "r")

# Define OpenAI API Key
openai.api_key = file.read()

# Set model and prompt
model_engine = "text-davinci-003"
prompt = input('enter new prompt: ')

# Response
completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,
)
response = completion.choices[0].text
print(response)