FROM eeveeb00/runpod-ollama-chat:build_base

# Ollama Model Installation
RUN ollama serve & sleep 1 && ollama pull llama3.2

# Python dependencies
COPY builder/requirements.txt /requirements.txt
RUN python3.11 -m pip install --upgrade -r /requirements.txt --no-cache-dir && \
    rm /requirements.txt

ADD src .

CMD ollama serve & python3.11 -u /handler.py
