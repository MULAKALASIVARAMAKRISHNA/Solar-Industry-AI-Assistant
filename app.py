import os
import gradio as gr
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Validate API Key
if not API_KEY:
    raise ValueError("⚠️ ERROR: OPENROUTER_API_KEY environment variable not set!")

# Define system prompt for AI behavior
SYSTEM_PROMPT = """You are a Solar Industry Expert AI Assistant. Provide accurate information about:
- Solar Panel Technology
- Installation Processes
- Maintenance Requirements
- Cost & ROI Analysis
- Industry Regulations
- Market Trends

Tailor responses to the user's technical level. Be professional and polite. Decline non-solar questions."""

# Define function to call OpenRouter API
def call_openrouter(user_input, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Ensure history format is correct (list of tuples)
    if isinstance(history, list) and all(isinstance(msg, tuple) and len(msg) == 2 for msg in history):
        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})
    else:
        history = []  # Reset history if incorrectly formatted

    # Append latest user message
    messages.append({"role": "user", "content": user_input})

    # Prepare API request headers
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/solar-ai-assistant",
        "X-Title": "Solar Consultant"
    }

    # Define request payload
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7
    }

    try:
        # Send request to OpenRouter API
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()  # Raise error for bad responses
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# Define chatbot response function
def respond(message, chat_history):
    MAX_LENGTH = 500  # Limit input length

    # Check for long messages
    if len(message) > MAX_LENGTH:
        return f"⚠️ Message too long! Please limit to {MAX_LENGTH} characters.", chat_history

    # Ensure chat history is a list
    if not isinstance(chat_history, list):
        chat_history = []

    # Get AI response
    bot_response = call_openrouter(message, chat_history)

    # Append conversation to history
    chat_history.append((message, bot_response))

    return "", chat_history

# Build Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("# ☀️ Solar Industry AI Assistant")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(label="Your Question", placeholder="Ask about solar energy...")
    clear = gr.Button("Clear Chat")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot, queue=False)

# Launch application
if __name__ == "__main__":
    app.launch(share=True)  # Public link for easy access
