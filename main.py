import json
from openai import OpenAI
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
topic = input("Enter Topic: ")
prompt = (f"Generate an Instagram post:\\n- A short, upbeat caption about \"{topic}\".\\n" "- Include 5 relevant hashtags.\\nFormat as JSON with keys caption and hashtags.")
resp = client.chat.completions.create(model="qwen/qwen3.6-plus-preview:free",
messages=[{"role":"user","content":prompt}])
result = resp.choices[0].message.content
post = json.loads(result)
print("Caption:", post["caption"])
print("Hashtags:", post["hashtags"])

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result)
