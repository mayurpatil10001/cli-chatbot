from model_loader import load_model
from chat_memory import ChatMemory

def main():
    print("Loading model...")
    generator, tokenizer = load_model()
    memory = ChatMemory()
    print("Chatbot ready! Type '/exit' to quit.")

    while True:
        user_input = input("User: ")
        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        # Step 1: Update memory
        memory.add_turn(user_input, "")

        # Step 2: Build prompt from sliding window memory
        prompt = ""
        for user_msg, bot_msg in memory.get_history():
            prompt += f"User: {user_msg}\nBot: {bot_msg}\n"
        prompt += f"User: {user_input}\nBot:"

        # Step 3: Generate response
        response = generator(prompt, max_new_tokens=100, pad_token_id=tokenizer.eos_token_id, do_sample=True, temperature=0.7)

        bot_output = response[0]['generated_text'].split("Bot:")[-1].strip()
        print("Bot:", bot_output)

        # Step 4: Update memory with actual bot response
        memory.update_last_bot_reply(bot_output)

if __name__ == "__main__":
    main()
