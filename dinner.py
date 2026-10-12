from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the API key from .env
load_dotenv()

# Initialize the OpenAI chat model
llm = ChatOpenAI(model="gpt-4o-mini")

# Specify the request and formatting rules
prompt = (
    "Provide exactly 5 different healthy South Indian dinner ideas. "
    "Format as a numbered list from 1 to 5, exactly one line per idea. "
    "Do not repeat any dinner idea. "
    "Include no preamble, introduction, or concluding remarks."
)

# Send the prompt to the model
reply = llm.invoke(prompt)

# Print only the response text
print(reply.content)