import json
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
topic = input("Enter Topic: ")
prompt = (f"Generate an Instagram post:\\n- A short, upbeat caption about \"{topic}\".\\n" "- Include 5 relevant hashtags.\\nFormat as JSON with keys caption and hashtags.")
resp = openai.ChatCompletion.create(model="gpt-3.5-turbo",
messages=[{"role":"user","content":prompt}])
result = resp.choices[0].message.content
post = json.loads(result)
print("Caption:", post["caption"])
print("Hashtags:", post["hashtags"])

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result)
