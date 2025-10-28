from dotenv import load_dotenv
import openai
import json
import os
#layer of security for keeping information secure
import ssl
import smtplib
import datetime as dt
import random
from emailFunction import send_email


load_dotenv()  # this reads the .env file

openai.api_key = os.getenv('API_KEY')

prompts = [
    "Write a poem that's not a haiku for my beautiful girlfriend Taylor using a specific theme of love.",
    "Write a Haiku for my beautiful girlfriend Taylor that likens her beauty to something specific "
          ]

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": random.choice(prompts)}],
)

body = completion.choices[0].message

print(body.content.strip()+ "\n\nI love you")

send_email(body.content.strip()+ "\n\nI love you")
