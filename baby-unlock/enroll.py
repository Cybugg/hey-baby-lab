import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
DURATION = 4  # seconds

print("Speak your enrollment phrase: 'hey baby'")

audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
sd.wait()

write("enroll.wav", SAMPLE_RATE, audio)

print("Saved enrollment audio -> enroll.wav")