def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

print("Simple Chatbot")
print("Type 'bye' to exit.")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower() == "bye":
        break