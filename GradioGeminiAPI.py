import gradio as gr
from openai import OpenAI

"""
Get your API key from openrouter.ai
Credits to https://huggingface.co/spaces/rishikasharma/Chatbot
But modified to remove deprecated non Messages in ChatInterface
"""
def respond(
    message,
    history,
    system_message,
    max_tokens,
    temperature,
    APIKEY,
):
    # Start the call always with the System Message
    messages = [{"role": "system", "content": system_message}]     
    # Set communication with open router API endpoint
    client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=APIKEY,
            )
    # Include previous conversation history
    for val in history:
        messages.append({"role": val['role'], "content": val['content']})
    messages.append({"role": "user", "content": message})
    # Prepare generation
    reply = []
    reply.append({"role": "assistant", "content": ""})
    for message in client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://thepoorgpuguy.substack.com/", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "Fabio Matricardi is The Poor GPU Guy", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model="google/gemini-2.0-flash-lite-preview-02-05:free",        
        messages=messages,
        max_tokens=max_tokens,
        stream=True,
        temperature=temperature,
    ):
        if message.choices[0].delta.content:
            reply[-1]['content'] += message.choices[0].delta.content

        yield reply

"""
For information on how to customize the ChatInterface, cehck the 
gradio docs: https://www.gradio.app/docs/chatinterface
"""

example = """#### Example for Image Generation help
```
I want to create an image with Flux but I need assistance for a good prompt. 
The image should be about '''[userinput]'''. Comic art style.
```
### ⚠️ Remember to put your API key for Open Router
> you can find the field in the Additional Inputs<br>
> you can get an API key for free from [openrouter.ai](https://openrouter.ai/settings/keys)
<br>Starting settings: `Temperature=0.45` `Max_Length=1100`
"""
# Customize the chatbot
chatbot = gr.Chatbot(type="messages",show_copy_button = True,
                    avatar_images=['https://png.pngtree.com/png-vector/20190710/ourlarge/pngtree-user-vector-avatar-png-image_1541962.jpg','https://clipartcraft.com/images/transparent-background-google-logo-brand-2.png'],
                    height=450, layout='panel') 
# https://www.gradio.app/guides/chatinterface-examples
demo = gr.ChatInterface(
    respond,
    additional_inputs=[
        gr.Textbox(value="You are a friendly Chatbot.", label="System message"),
        gr.Slider(minimum=250, maximum=4096, value=1100, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.45, step=0.1, label="Temperature"),
        gr.Textbox(value="", 
                   label="Open Router API key",
                   type='password',placeholder='Paste your API key',)
    ],
    title="Chat with Gemini 2.0 Flash Lite - works also in China",
    description=example,
    save_history=True,
    type='messages',
    chatbot=chatbot, 
    theme=gr.themes.Ocean(), 
)
# RUN THE MAIN
if __name__ == "__main__":
    demo.launch()