"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Generate a code snippet for integrating a microphone with a speaker system for a live streaming application.
Generated: DETERMINISTIC_64bb1e87c9047edf
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pyaudio
import threading

# Class to handle microphone input and speaker output
class AudioStreamer:
    def __init__(self, rate=44100, chunk_size=1024):
        """
        Initializes the AudioStreamer instance.
        
        :param rate: Sampling rate for audio data (default: 44100 Hz)
        :param chunk_size: Size of audio data chunks (default: 1024)
        """
        self.rate = rate
        self.chunk_size = chunk_size

        # PyAudio instance
        self.audio = pyaudio.PyAudio()

        # Microphone input stream
        self.input_stream = None

        # Speaker output stream
        self.output_stream = None

        # Flag to control streaming
        self.running = False

    def start_stream(self):
        """
        Starts the microphone-to-speaker audio stream.
        """
        try:
            # Open input stream for microphone
            self.input_stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.rate,
                input=True,
                frames_per_buffer=self.chunk_size
            )

            # Open output stream for speaker
            self.output_stream = self.audio.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=self.rate,
                output=True,
                frames_per_buffer=self.chunk_size
            )

            self.running = True

            # Start streaming in a separate thread
            threading.Thread(target=self._stream_audio, daemon=True).start()

        except Exception as e:
            print(f"Error starting audio stream: {e}")
            self.stop_stream()

    def _stream_audio(self):
        """
        Continuously streams audio from microphone to speaker.
        """
        try:
            while self.running:
                # Read audio data from microphone
                audio_data = self.input_stream.read(self.chunk_size, exception_on_overflow=False)
                # Play audio data through speaker
                self.output_stream.write(audio_data)
        except Exception as e:
            print(f"Error during audio streaming: {e}")
            self.stop_stream()

    def stop_stream(self):
        """
        Stops the microphone-to-speaker audio stream and cleans up resources.
        """
        self.running = False

        if self.input_stream:
            self.input_stream.stop_stream()
            self.input_stream.close()

        if self.output_stream:
            self.output_stream.stop_stream()
            self.output_stream.close()

        if self.audio:
            self.audio.terminate()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize audio streamer
        streamer = AudioStreamer()

        # Start streaming
        print("Starting audio stream. Press Ctrl+C to stop.")
        streamer.start_stream()

        # Keep the application running
        while True:
            pass

    except KeyboardInterrupt:
        print("\nStopping audio stream.")
        streamer.stop_stream()

    except Exception as e:
        print(f"Unexpected error: {e}")
```
