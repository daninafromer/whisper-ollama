# Pipeline de Transcrição e Extração de Pontos-Chave (Whisper + Ollama)

## Descrição

Este projeto implementa um pipeline que recebe um arquivo de áudio, realiza a transcrição utilizando o modelo Whisper (OpenAI, execução local) e, em
seguida, envia o texto transcrito para o Ollama, que gera um resumo destacando
os pontos-chave do conteúdo.

O objetivo é automatizar o processo de "ouvir → transcrever → resumir", útil para
reuniões, aulas, podcasts e entrevistas.

## Tecnologias

- Python 3.9+
- Whisper (openai-whisper): transcrição de áudio local
- Ollama: execução local de LLMs para sumarização
- FFmpeg: processamento de áudio (dependência do Whisper)
- Requests: comunicação HTTP com o Ollama

## Estrutura do Projeto
whisper-ollama/
├── pipeline.py # Script principal
├── README.md # Este arquivo
└── .venv/ # Ambiente virtual (não versionar)


## Instalação

### 1. Pré-requisitos do sistema (macOS)

```bash
# Ferramentas de linha de comando da Apple
xcode-select --install

# Homebrew (se ainda não tiver)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# FFmpeg
brew install ffmpeg

##Dependências Python

brew install python
mkdir ~/whisper-ollama && cd ~/whisper-ollama
python3 -m venv .venv
source .venv/bin/activate
pip install openai-whisper requests


##Ollama

Ollama
Baixe e instale em https://ollama.com/download/mac

Abra o app Ollama (ele roda em segundo plano em http://localhost:11434)

Baixe o modelo usado no script:'ollama pull llama3.2

Ative o ambiente virtual e execute o script passando o caminho do áudio: source .venv/bin/activate
python pipeline.py caminho/para/audio.mp3

Saída esperada
O script imprime no terminal:

A transcrição completa do áudio.

O resumo com os pontos-chave gerados pelo Ollama.

Como funciona
O Whisper carrega o modelo base e transcreve o áudio em português.

O texto transcrito é enviado ao Ollama via requisição HTTP (/api/generate).

O modelo llama3.2 recebe um prompt pedindo de 5 a 7 pontos-chave e um resumo curto.

A resposta é exibida no terminal.

Autora Danielle Lisboa Fontes
