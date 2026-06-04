
# baby-unlock

> A chaotic experiment in voice authentication, questionable security decisions, and AI-powered laptop unlocking.

---

## ⚠️ WARNING

This project is **not secure**.

It is:

* vulnerable to replay attacks
* vulnerable to voice cloning
* not suitable for real authentication
* intentionally experimental

Do not use this to protect anything important.

---

## What is this?

`baby-unlock` is a voice-based authentication system that lets you:

* Say a wake phrase like **“hey baby”**
* Have your voice verified using speaker embeddings
* Trigger a response like **“yes daddy”**
* (eventually) unlock your computer

It is part security experiment, part AI playground, part social experiment.

---

## Core Idea

We treat your voice like a biometric key:

```
Voice → Audio Recording → Embedding → Similarity Check → Unlock Decision
```

But instead of pretending it's secure, we document exactly how it fails and improve it step-by-step.

---

##  Project Philosophy

This project is built as a **public engineering diary**:

We intentionally:

* start with a broken system
* break it further
* document vulnerabilities
* patch them iteratively
* post everything publicly

Because real engineering is not clean. It evolves.

---

##  Features (Current MVP)

### v0 - “The Dangerous Prototype”

* Microphone voice recording
* WAV enrollment system
* Speaker embedding generation
* Cosine similarity matching
* Basic voice authentication loop
* Console-based “unlock simulation”

---

##  Planned Evolution

### v1 - Speaker Verification

* Resemblyzer embeddings
* Voice identity matching threshold

### v2 - Wake Word Detection

* “hey baby” activation phrase
* Always-on listening mode

### v3 - Anti-Replay System

* Random challenge phrases
* “Say: purple tiger” style verification

### v4 - Liveness Detection

* Anti-spoofing heuristics
* playback detection

### v5 - System Integration

* Linux unlock integration
* optional Windows support
* local-only execution mode

---

## 🛠️ Tech Stack

* Python
* Sounddevice (audio capture)
* SciPy (audio processing)
* Resemblyzer (speaker embeddings)
* NumPy (vector math)

---

## 📦 Installation

```bash
git clone https://github.com/yourname/baby-unlock.git
cd baby-unlock

python3 -m venv venv
source venv/bin/activate

pip install sounddevice scipy numpy resemblyzer webrtcvad
```

---

## 🚀 Usage

### 1. Enroll Voice

```bash
python enroll.py
```

Speak:

> “hey baby”

---

### 2. Generate Voice Profile

```bash
python embed.py
```

---

### 3. Run Unlock System

```bash
python unlock.py
```

---

##  How It Works

### Step 1: Audio Capture

Your microphone records a short voice sample.

### Step 2: Voice Embedding

The system converts your voice into a numerical vector.

### Step 3: Comparison

It compares live voice vs stored voice using cosine similarity.

### Step 4: Decision

If similarity is high enough:

```
ACCESS GRANTED
```

Otherwise:

```
ACCESS DENIED
```

---

## 🔐 Security Reality

This system is vulnerable to:

* 🎙️ audio replay attacks
* 🤖 AI voice cloning
* 📼 recorded voice playback
* 🎧 background noise interference

### Mitigations (in progress):

* randomized challenge phrases
* liveness detection heuristics
* multi-factor verification (voice + proximity)
* local-only processing

---

##  Why this exists

Because building “serious systems” is more fun when you first build the **bad version on purpose**.

And then fix it in public.

---


## 🤝 License

MIT - but don’t blame me if your laptop starts calling you “daddy”.

---

## 👀 Author Note

This is a learning system disguised as a joke.

Underneath the humor is:

* real speech processing
* biometric authentication concepts
* security tradeoff design
* system iteration thinking

