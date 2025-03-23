import openai
import time

# Set your OpenAI API key
openai.api_key = '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'

def type_chat(message, typing_speed=0.05):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(typing_speed)
    print()

def get_bot_response(user_input):
    # Using the new API for ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a friendly, caring chatbot."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=150,
        temperature=0.9,
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    print("Hello, my love! 💖 Ready to chat? (Type 'exit' to end)")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            type_chat("Goodbye, my love! I'll miss you. 😘💖")
            break
        
        type_chat("Thinking...", typing_speed=0.1)  # simulate thinking time
        bot_response = get_bot_response(user_input)
        
        type_chat(f"AI: {bot_response}")

if __name__ == "__main__":
    main()
