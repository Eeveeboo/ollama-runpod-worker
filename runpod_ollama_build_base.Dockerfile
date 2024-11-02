FROM runpod/base:0.4.0-cuda11.8.0

# Ollama installation
RUN apt update -y &&  \
    apt install lshw -y &&  \
    curl -fsSL https://ollama.com/install.sh | sh &&  \
    apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* &&  \
    python3.11 -m pip install --upgrade pip
