# Runpod Serverless Compatible Ollama Chat Inferrence

> 💡 C# API Wrapper Coming Soon.

### Example Request to RunPod:
```
curl -X POST https://api.runpod.ai/v2/{endpoint_id}/runsync \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer ${API_KEY}' \
    -d '{"input": {"mode": "chat", model": "llama3.2:1b", "format":"", "options":{"temperature": 1}, "messages": [{"role": "user", "content": "Why is the sky blue?"}]}}'
```

### Mode can be "generate" or "chat" (Default is "chat")

### Model can be any supported models indicated in the tag:

| Tag                                               | Supported Models        |
|---------------------------------------------------|-------------------------|
| eeveeb00/runpod-ollama-chat:llama3.2              | llama3.2                |
| eeveeb00/runpod-ollama-chat:llama3.2_llavaphi3    | llama3.2, llava-phi3    |
| eeveeb00/runpod-ollama-chat:llama3.2_moondream    | llama3.2, moondream     |
| eeveeb00/runpod-ollama-chat:llama3.2_1b           | llama3.2:1b             |
| eeveeb00/runpod-ollama-chat:llama3.2_1b_llavaphi3 | llama3.2:1b, llava-phi3 |
| eeveeb00/runpod-ollama-chat:llama3.2_1b_moondream | llama3.2:1b, moondream  |

### `format` is an optional string and can be "json" or ""

### `options` can be any extra Ollama options:

e.g. temperature, num_ctx, num_predict

### `messages` is an array of Ollama message objects: (chat mode only)

Role can be "user", "system", "tool" or "assistant"

Content is a string.

### `tools` is an array of Ollama tool function objects: (chat mode only)

### `template` is an optional string which overwrites the default MODELFILE: (generate mode only)

### `images` is an optional string array of base64 images: (generate mode only)

### `suffix` is an optional string for fill in the middle tasks: (generate mode only)

### `prompt` is a string: (generate mode only)

### `context` is an optional int array: (generate mode only)

<br/><br/>
