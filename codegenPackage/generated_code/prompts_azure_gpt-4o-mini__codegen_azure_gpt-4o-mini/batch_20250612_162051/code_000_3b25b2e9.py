"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Generate a code snippet for a voice recording application that utilizes a Cad E100s microphone and SSL 2 audio interface for high-quality audio capture.
Generated: DETERMINISTIC_3b25b2e9927d5be9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pyaudio
import wave
import sys

class VoiceRecorder:
    def __init__(self, channels=2, rate=44100, chunk=1024, format=pyaudio.paInt16):
        """
        Initializes the VoiceRecorder with specified audio parameters.

        :param channels: Number of audio channels (1 for mono, 2 for stereo)
        :param rate: Sampling rate in Hz
        :param chunk: Number of frames per buffer
        :param format: Audio format (default is 16-bit PCM)
        """
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.format = format
        self.p = pyaudio.PyAudio()

    def start_recording(self, output_filename):
        """
        Starts recording audio and saves it to the specified output file.

        :param output_filename: The name of the output WAV file
        """
        try:
            # Open a stream for audio input
            stream = self.p.open(format=self.format,
                                 channels=self.channels,
                                 rate=self.rate,
                                 input=True,
                                 frames_per_buffer=self.chunk)

            print("Recording... Press Ctrl+C to stop.")

            frames = []

            while True:
                data = stream.read(self.chunk)
                frames.append(data)

        except KeyboardInterrupt:
            print("Recording stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Stop and close the stream
            stream.stop_stream()
            stream.close()
            self.p.terminate()

            # Save the recorded data as a WAV file
            self.save_recording(output_filename, frames)

    def save_recording(self, output_filename, frames):
        """
        Saves the recorded frames to a WAV file.

        :param output_filename: The name of the output WAV file
        :param frames: The recorded audio frames
        """
        try:
            with wave.open(output_filename, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.p.get_sample_size(self.format))
                wf.setframerate(self.rate)
                wf.writeframes(b''.join(frames))
            print(f"Recording saved as {output_filename}")
        except Exception as e:
            print(f"Failed to save recording: {e}")

if __name__ == "__main__":
    recorder = VoiceRecorder()
    output_file = "output.wav"  # Specify the output file name
    recorder.start_recording(output_file)
```
