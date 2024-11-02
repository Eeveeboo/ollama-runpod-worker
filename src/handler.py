import runpod
import ollama

def handler(job):
    """ Handler function that will be used to process jobs. """
    job_input = job['input']

    mode = job_input.get('mode', 'chat') # "chat" or "generate"

    model = job_input.get('model', '') # either mode
    output_format = job_input.get('format', '') # either mode
    options = job_input.get('options', None) # either mode

    messages = job_input.get('messages', None) # chat only
    tools = job_input.get('tools', None) # chat only

    template = job_input.get('template', '') # generate only
    images = job_input.get('images', None) # generate only
    suffix = job_input.get('suffix', None) # generate only
    prompt = job_input.get('prompt', None) # generate only
    context = job_input.get('context', None) # generate only


    if mode == 'generate':
        response = ollama.generate(model=model, format=output_format, options=options, suffix=suffix, context=context, template=template, prompt=prompt, images=images)
        return response
    else:
        response = ollama.chat(model=model, messages=messages, options=options, format=output_format, tools=tools)
        return response


runpod.serverless.start({"handler": handler})
