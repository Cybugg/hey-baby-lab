from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np

encoder = VoiceEncoder()

wav = preprocess_wav("enroll.wav")
embedding = encoder.embed_utterance(wav)

np.save("voice_profile.npy", embedding)

print("Voice profile saved")