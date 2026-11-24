import whisper
import requests
import sys
import os

def transcrever(caminho_audio):
    print("Carregando modelo Whisper (base)...")
    modelo = whisper.load_model("base")
    print("Transcrevendo...")
    resultado = modelo.transcribe(caminho_audio, language="pt")
    return resultado["text"].strip()

def extrair_pontos_chave(texto):
    print("Enviando para o Ollama...")
    prompt = f"""Extraia de 5 a 7 pontos-chave do texto abaixo e faça um resumo curto.

Texto:
{texto}

Responda em português."""
    
    resposta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )
    resposta.raise_for_status()
    return resposta.json()["response"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pipeline.py seu_audio.mp3")
        sys.exit(1)
    
    arquivo = sys.argv[1]
    if not os.path.isfile(arquivo):
        print(f"Arquivo não encontrado: {arquivo}")
        sys.exit(1)
    
    texto = transcrever(arquivo)
    print("\n--- Transcrição ---")
    print(texto)
    
    resumo = extrair_pontos_chave(texto)
    print("\n--- Pontos-chave ---")
    print(resumo)
