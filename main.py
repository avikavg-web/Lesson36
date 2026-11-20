from groq import generate_response

def propmt_engineering_activity():

    print ("Welcome to AI propmt engineering tutorial!")

    vague = input("Enter a vague propmt: ")

    print("\nAi's response to vague response: ")

    print(generate_response(vague))

    specific = input("\nWow now make it more specific")

    print("\nAi's response to specific prompt: ")

    print(generate_response(specific))

    context = input("\nNow add more context to that")

    print("\nAI's contextual answer: ")

    print(generate_response(context))

    print("---Reflection---")

    print("How did the AI's response change when the propmt was more specific? ")

    print("How did the AI's response improve with the added context? ")

    print("Which propmt produced the most relevant and tailored response? Why? ")

if __name__ == "__main__":

    propmt_engineering_activity()