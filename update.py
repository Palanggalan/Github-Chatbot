import json
import re

kb_path = 'c:/Users/ABDULWAHID/Documents/GitHub/Github-Chatbot/github_kb.json'
with open(kb_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if 'content' in item:
        item['content'] = item['content'].replace('Desktop', 'Desktop App')
        item['content'] = item['content'].replace('desktop', 'desktop app')

with open(kb_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
