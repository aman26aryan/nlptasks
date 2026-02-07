import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://en.wikipedia.org/wiki/Saurabh_Singh_Shekhawat"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

page = requests.get(BASE_URL, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

lm_data = {
    "domain": "Person Knowledge Base",
    "source": "Wikipedia",
    "person": "Saurabh Singh Shekhawat",
    "entries": []
}

current_section = None

for tag in soup.find_all(["h2", "p"]):

    if tag.name == "h2":
        current_section = tag.text.replace("[edit]", "").strip()

        # skip unwanted headings
        if current_section.lower() in ["contents", "references", "external links", "see also"]:
            current_section = None

    elif tag.name == "p":
        if current_section is None:
            continue

        text = tag.text.strip()

        if len(text) < 60:
            continue

        lm_data["entries"].append({
            "topic": current_section,
            "question": f"Tell me about {current_section.lower()} of Saurabh Singh Shekhawat",
            "answer": text
        })

        print("Added:", current_section)

with open("person_minibot_lm.json", "w", encoding="utf-8") as f:
    json.dump(lm_data, f, indent=2, ensure_ascii=False)

print("✅ Person-based Mini LM created successfully")
