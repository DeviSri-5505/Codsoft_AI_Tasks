# chatbot.py

print("Hello! I am RuleBot 🤖. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()

    # Keyword-based matching
    if "hello" in user_input or "hi" in user_input:
        print("RuleBot: Hi there! How can I assist you today?")
    elif "how are you" in user_input:
        print("RuleBot: I'm doing great, thanks for asking! 😊")
    elif "name" in user_input:
        print("RuleBot: I am RuleBot, your friendly AI.")
    elif "help" in user_input:
        print("RuleBot: I can help you with simple questions. Try asking me something!")
    elif "bye" in user_input:
        print("RuleBot: Goodbye! Have a wonderful day! 👋")
        break
    else:
        print("RuleBot: I'm not sure how to respond to that. Try asking something else.")
