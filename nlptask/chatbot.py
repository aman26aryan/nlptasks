import json

# load the LM
with open("city_minibot_lm.json", "r", encoding="utf-8") as f:
    lm_data = json.load(f)

entries = lm_data["entries"]

print("🤖 Chatbot is ready! (type 'exit' to quit)\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    found = False

    for entry in entries:
        topic = entry["topic"].lower()

        # simple keyword matching
        if topic in user_input:
            print("Bot:", entry["answer"])
            found = True
            break

    if not found:
        print("Bot: Sorry, I don't have information about that.")
