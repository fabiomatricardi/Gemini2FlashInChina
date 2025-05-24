# Gemini2FlashInChina
Open Router ai Gradio client for Gemini2 flash working also in China

### 20250524 - update
Add Model Routing because Gemini API endpoints are not stable
```
# UPDATE 20250524 - Gemini models lags a lot or even not respond anymore...
# ADD Model auto routing from a list (max 3 models) as per https://openrouter.ai/docs/features/model-routing
# Fabio Matricardi
```
Here below you can see that the first call was replied by Meta, the second by Gemini

<img src="https://github.com/fabiomatricardi/Gemini2FlashInChina/raw/main/20250524-modelrouting.png" width=900>

### Requirements
```
pip install -U gradio openai
```

#### Background
- Get your API key from openrouter.ai
- Credits to https://huggingface.co/spaces/rishikasharma/Chatbot
- But modified to remove deprecated non Messages in ChatInterface


### ⚠️ Remember to put your API key for Open Router
> you can find the field in the Additional Inputs<br>
> you can get an API key for free from [openrouter.ai](https://openrouter.ai/settings/keys)
<br>
Starting settings: `Temperature=0.45` `Max_Length=1100`
