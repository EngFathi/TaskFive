import openai

# Set your OpenAI API key
OPENAI_API_KEY = ''

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        error_message = f"Error: {str(e)}"
        if "insufficient_quota" in error_message:
            return "Your credit balance is too low to access the GPT API. Please go to Plans & Billing to upgrade or purchase credits."
        return error_message

def main():
    print("Welcome to the OpenAI Chatbot!")
    while True:
        print("\nMenu:")
        print("1. Start the chatbot")
        print("0. Exit")
        start_input = input("Your choice: ")

        if start_input == '0':
            print("Exiting the chatbot. Goodbye!")
            break
        elif start_input == '1':
            print("Chatbot: Hello! How can I assist you today?")
            while True:
                user_input = input("You: ")
                if user_input.lower() in ['0', 'exit', 'quit']:
                    print("Chatbot: Goodbye!")
                    break

                response = chat_with_gpt(user_input)
                if response.startswith("Error:"):
                    print(f"Chatbot encountered an error: {response}")
                else:
                    print(f"Chatbot: {response}")
        else:
            print("Invalid input. Please enter 1 to start or 0 to exit.")

if __name__ == "__main__":
    main()
