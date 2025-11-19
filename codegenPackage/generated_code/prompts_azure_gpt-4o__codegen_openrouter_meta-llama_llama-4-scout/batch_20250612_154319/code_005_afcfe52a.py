"""
Generated Code Metadata:
========================
Original URL: https://livesync.site
Prompt: Write code to implement a secure, on-premise speech-to-text processing system for medical dialogue, ensuring sensitive patient data remains within the clinic's local network, as highlighted by LiveSync MD.
Generated: DETERMINISTIC_afcfe52a6145b99b
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import wave
import pyaudio
import numpy as np
from scipy.io import wavfile
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch

# Set up logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SpeechToText:
    def __init__(self, model_name="facebook/wav2vec2-base-960h", 
                 device="cpu", 
                 sample_rate=16000, 
                 chunk_size=1024):
        """
        Initialize the SpeechToText class.

        Args:
        - model_name (str): The name of the pre-trained Wav2Vec2 model.
        - device (str): The device to use for inference (cpu or gpu).
        - sample_rate (int): The sample rate of the audio data.
        - chunk_size (int): The chunk size for audio processing.
        """
        self.model_name = model_name
        self.device = device
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size

        # Load pre-trained Wav2Vec2 model and processor
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)

        # Move model to device
        self.model.to(device)
        self.model.eval()

    def record_audio(self, filename="output.wav", seconds=5):
        """
        Record audio from the microphone.

        Args:
        - filename (str): The filename to save the recorded audio.
        - seconds (int): The number of seconds to record.
        """
        # Set up audio recording
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=self.sample_rate, 
                        input=True, frames_per_buffer=self.chunk_size)

        logger.info("Recording...")
        frames = []
        for i in range(0, int(self.sample_rate / self.chunk_size * seconds)):
            data = stream.read(self.chunk_size)
            frames.append(np.frombuffer(data, dtype=np.int16))

        logger.info("Finished recording.")
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save recorded audio to file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join([frame.tobytes() for frame in frames]))
        wf.close()

    def process_audio(self, filename="output.wav"):
        """
        Process the recorded audio and transcribe it to text.

        Args:
        - filename (str): The filename of the recorded audio.
        """
        # Load audio file
        sampling_rate, audio = wavfile.read(filename)

        # Preprocess audio data
        inputs = self.processor(raw_audio=audio, sampling_rate=sampling_rate, return_tensors="pt")

        # Move inputs to device
        inputs = {key: value.to(self.device) for key, value in inputs.items()}

        # Run inference
        with torch.no_grad():
            logits = self.model(**inputs).logits

        # Decode predicted ids
        predicted_ids = torch.argmax(logits, dim=-1)

        # Convert predicted ids to text
        transcription = self.processor.batch_decode(predicted_ids)

        return transcription[0]

def main():
    # Initialize SpeechToText class
    stt = SpeechToText()

    try:
        # Record audio
        stt.record_audio()

        # Process audio and transcribe to text
        transcription = stt.process_audio()

        logger.info(f"Transcription: {transcription}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
