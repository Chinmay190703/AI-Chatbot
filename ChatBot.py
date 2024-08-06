import openai
import time

# Set OpenAI API key
openai.api_key = 'your-api-key-here'

# Initialize messages list
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    try:
        # Get user input
        message = input("You: ")
        if message.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break

        messages.append({"role": "user", "content": message})

        # Generate chat completion
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            timeout=10  # optional timeout for the request
        )

        # Extract and print the assistant's reply
        reply = chat.choices[0].message
        print("Assistant:", reply["content"])

        # Append assistant's reply to messages
        messages.append(reply)

    except openai.error.RateLimitError:
        print("Rate limit exceeded. Waiting for 60 seconds before retrying...")
        time.sleep(60)

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        if str(e).lower().startswith("401"):
            print("Unauthorized access. Please check your API key.")
        elif str(e).lower().startswith("429"):
            print("Too many requests. Please wait before making more requests.")
        elif str(e).lower().startswith("500"):
            print("Internal server error. Please try again later.")
        else:
            print("An unexpected error occurred. Please try again.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
