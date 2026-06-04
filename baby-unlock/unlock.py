import sounddevice as sd
from scipy.io.wavfile import write
from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import time

SAMPLE_RATE = 16000
DURATION = 4

encoder = VoiceEncoder()

stored_embedding = np.load("voice_profile.npy")

def record():
    print("Listening...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write("live.wav", SAMPLE_RATE, audio)
    return "live.wav"

def verify(file):
    wav = preprocess_wav(file)
    embedding = encoder.embed_utterance(wav)

    similarity = np.dot(embedding, stored_embedding) / (
        np.linalg.norm(embedding) * np.linalg.norm(stored_embedding)
    )

    print("Similarity:", similarity)

    return similarity > 0.75

while True:
    input("Press ENTER then say: 'hey baby' + command\n")

    file = record()

    if verify(file):
        print("YES DADDY 😈 (UNLOCK SIMULATED)")
    else:
        print("DENIED ❌")

    time.sleep(1)