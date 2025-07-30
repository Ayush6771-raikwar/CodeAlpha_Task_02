import tkinter as tk
from tkinter import scrolledtext

# Simple logic-based chatbot function
def get_bot_response(user_message):
    user_message = user_message.lower()
    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you?"
    elif "your name" in user_message:
        return "I'm Jarvis, your chatbot assistant."
    elif "how are you" in user_message:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in user_message:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I don't understand that."

# Handle send button click
def send_message():
    user_msg = user_input.get().strip()
    if not user_msg:
        return
    conversation_area.insert(tk.END, f"You: {user_msg}\n", "user")
    user_input.delete(0, tk.END)

    bot_response = get_bot_response(user_msg)
    conversation_area.insert(tk.END, f"Jarvis: {bot_response}\n", "bot")
    conversation_area.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("Simple Chatbot - Jarvis")
root.configure(bg="black")

# Conversation area
conversation_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=60, height=25, font=("Arial", 12),
    bg="black", fg="white"
)
conversation_area.tag_config("user", foreground="yellow")
conversation_area.tag_config("bot", foreground="light green")
conversation_area.pack(padx=10, pady=10)

# User input field
user_input = tk.Entry(root, font=("Arial", 12), width=50, bg="black", fg="white", insertbackground="white")
user_input.pack(padx=10, pady=5, side=tk.LEFT, expand=True, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), bg="gray", fg="black", command=send_message)
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

# Greeting message
conversation_area.insert(tk.END, "Jarvis: Hello! I am Jarvis. Type something to begin.\n", "bot")

root.mainloop()
