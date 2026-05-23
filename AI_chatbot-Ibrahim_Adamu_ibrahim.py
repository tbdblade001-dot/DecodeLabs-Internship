print("Kindly use simple English throughout this conversation. Type 'exit or bye' to end the chat")
while True:
    user = input("Customer: ").lower()
    if user == "hi there" or user == "hi" or user == "hello" or user == "hey" or user == "hello there" or user == "hey there":
        print("Chatbot: Hello! Welcome. How can i help you today")
    elif user == "i want to know about your products" or user == "i want to know more about your products" or user == "i want to know about your product" or user == "i want to know more about your product":
        print("Chatbot: Sure! we offer a range of products. \n " " could you tell me what you are looking for?")
    elif user == "i am looking for a laptop" or user == "i'm looking for a laptop" or user == "i am looking for a laptop" or user == "i'm looking for a laptop" or user == "i am looking for laptop" or user == "i'm looking for laptop" or user == "i want laptop" or user == "i want a laptop" or user == "i need laptop" or user == "i need a laptop" or user == "i want to buy a laptop" or user == "i want to buy laptop" or user == 'i want to purchase a laptop' or user == "i want to purchase laptop" or user == "laptop":
        print("Are you interested in a laptop for studying, programming, gaming, or general use")
    elif user == "programming and school work" or user == "programming" or user == "gaming" or user == "school work" or user == "school" or user == "general use":
        print("Chatbot: could you please send your phone number so i can send you the pictures via whatsapp?")
    elif user.isdigit():
            print("Chatbot: Great, i have send you the pictures with the manager's phone number. kindly take your time and select the laptop of your choice.\n Also, send the laptop of your choice to the manager for more detail information")
    elif user == "thanks" or user == "ok" or user == "thank you" or user == "alright" or user == "great" or user == "cool" or user == "nice" or user == 'okay' or user == "hmm":
        print("Chatbot: is there anything i can do for you")
    elif user == "yes":
        print("I'm here for you, what else do you want?")
    elif user == "no" or user == "no, thanks" or user == "no, thank you" or user == "thank you" or user == "nah" or user == "not at all":
        print("Chatbot: Great.")
    elif user == "bye" or user == "exit":
        print("Chatbot: Have a nice day")
        break
    else:
        print("Sorry i don't understand. can you please use simple and direct English")
