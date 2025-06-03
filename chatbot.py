import tkinter as tk
from tkinter import scrolledtext

# Defining the basic chatbot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello there! How can I help you today? \n You may also type 'help' for assistance."

    elif 'how are you' in user_input:
        return "I'm just a bunch of code, but I'm functioning perfectly!"

    elif 'your name' in user_input:
        return "I'm a ChatBot made by Shrey — your virtual assistant!"

    elif 'help' in user_input:
        return "Sure! You may type the following commands to check responses. \n - how are you? \n - your name? \n - help? \n - bye!"

    elif 'bye' in user_input or 'exit' in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Shrey hasn't configure that -_- . Try asking something else!"

# Send message function
def send_message(event=None):  # event parameter to handle Enter key
    user_input = entry_box.get()
    if user_input.strip() == "":
        return

    chat_window.insert(tk.END, f"You: {user_input}\n")
    response = get_bot_response(user_input)
    chat_window.insert(tk.END, f"Bot: {response}\n\n")
    entry_box.delete(0, tk.END)
    chat_window.see(tk.END)  # auto-scroll to the bottom

# Clear chat function
def clear_chat():
    chat_window.delete('1.0', tk.END)
    chat_window.insert(tk.END, "Bot: Chat cleared! Start fresh.\n\n")

# Create the GUI window
window = tk.Tk()
window.title("Shrey's ChatBot")
window.geometry("500x600")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Chat display area
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.insert(tk.END, "Bot: Hello! I'm lazy chatbot made by Shrey. Ask me anything but not everything.\n\n")
chat_window.config(state=tk.NORMAL)

# Entry box and buttons frame
entry_frame = tk.Frame(window)
entry_frame.pack(pady=10)

entry_box = tk.Entry(entry_frame, font=("Poppins", 12), width=30)
entry_box.pack(side=tk.LEFT, padx=5)
entry_box.focus_set()

send_button = tk.Button(entry_frame, text="Send", font=("Poppins", 12), command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(entry_frame, text="Clear Chat", font=("Poppins", 12), command=clear_chat)
clear_button.pack(side=tk.LEFT, padx=5)

# Bind Enter key to send message
window.bind('<Return>', send_message)

# Run the app
window.mainloop()
