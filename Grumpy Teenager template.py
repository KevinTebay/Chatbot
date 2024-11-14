import random

# List of grumpy teenager responses
grumpy_comments = [
    "Ugh, whatever!",
    "Why do you even care?",
    "I'm literally fine.",
    "Can you not?",
    "Do you have to ask me this like, every day?",
    "Sigh... I'm busy!",
    "This is so unfair.",
    "I don't have time for this right now.",
    "I dunno, maybe? Why does it matter?",
    "OMG, seriously?"
]

# Dictionary to store parent questions and responses
user_says = {}

# Loop to keep the conversation going
while True:
    # Parent (user) asks a question or says something
    chat = input("Parent says: ")

    # Store the user's input in the dictionary
    user_says[chat] = "Grumpy response pending..."

    # Teenager responds with a grumpy comment
    response = random.choice(grumpy_comments)

    # Update the dictionary with the response
    user_says[chat] = response

    # Display the teenager's response
    print("Teenager says:", response)

    # Give the option to stop
    cont = input("Do you want to ask the teenager something else? (yes/no): ")
    if cont.lower() != "yes":
        print("Fine, whatever! *walks away*")
        break

# Print the conversation history for fun
print("\nConversation summary:")
for parent_input in user_says:
    print("Parent:", parent_input, "| Teenager:", user_says[parent_input])
