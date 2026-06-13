import time

print("Welcome to AI ChatBot!")

while True:
    user = input("You: ").lower()

    if user == "hii" or user == "hello":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: I am ChatBot.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("Bot: Commands: hi, hello, how are you, time, thank you, bye")

    elif user == "time":
        print("Bot:", time.strftime("%H:%M:%S"))

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")