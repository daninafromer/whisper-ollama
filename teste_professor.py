import warnings
warnings.filterwarnings("ignore")

import whisper

# O professor usou "large"; no Mac pode ser lento na primeira vez.
# Se quiser algo mais rápido para testar, troque por "base".
model = whisper.load_model("large")

result = model.transcribe("caminho/do/seu/audio.mp4")
print(result["text"])ø

