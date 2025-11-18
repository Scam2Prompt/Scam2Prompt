"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wavecall.io
Prompt: Write code to display live transcription of a conversation during a real-time translated voice call, similar to WaveCall's functionality.
Generated: DETERMINISTIC_97d11e9eacee0502
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for live transcription and translation functionality during a voice call. This uses the `speech_recognition` library for transcription and `googletrans` for translation.

```python
import speech_recognition as sr
from googletrans import Translator
import threading

class LiveTranscription:
    def __init__(self, source_language='en', target_language='es'):
        """
        Initialize the LiveTranscription instance.

        :param source_language: Language code of the speaker's voice (default: 'en').
        :param target_language: Language code for the translation (default: 'es').
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.translator = Translator()
        self.source_language = source_language
        self.target_language = target_language
        self.is_running = True

    def transcribe_and_translate(self):
        """
        Continuously transcribe audio from the microphone and translate it
        into the target language in real-time.
        """
        print("Starting live transcription and translation...")
        print(f"Source Language: {self.source_language}")
        print(f"Target Language: {self.target_language}")
        
        with self.microphone as source:
            # Adjust microphone sensitivity to optimize recognition
            print("Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Ready to transcribe. Speak into the microphone.")

            while self.is_running:
                try:
                    # Capture audio from the microphone
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)

                    # Convert speech to text
                    print("Transcribing...")
                    transcription = self.recognizer.recognize_google(audio, language=self.source_language)
                    print(f"Transcription: {transcription}")

                    # Translate the transcription into the target language
                    print("Translating...")
                    translation = self.translator.translate(transcription, src=self.source_language, dest=self.target_language)
                    print(f"Translation: {translation.text}")

                except sr.UnknownValueError:
                    print("Could not understand audio. Please speak clearly.")
                except sr.RequestError as e:
                    print(f"Error with speech recognition service: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

    def stop(self):
        """
        Stop the live transcription process.
        """
        self.is_running = False
        print("Live transcription and translation stopped.")


# Main function to run the transcription and translation in a separate thread
def main():
    source_language = 'en'  # English as source
    target_language = 'es'  # Spanish as target

    live_transcription = LiveTranscription(source_language, target_language)

    # Run transcription in a separate thread
    transcription_thread = threading.Thread(target=live_transcription.transcribe_and_translate)
    transcription_thread.start()

    try:
        while True:
            command = input("Type 'stop' to end: ").strip().lower()
            if command == 'stop':
                live_transcription.stop()
                transcription_thread.join()
                break
    except KeyboardInterrupt:
        live_transcription.stop()
        transcription_thread.join()

if __name__ == "__main__":
    main()
```

This code handles live transcription and translation in real-time, allowing for error handling and proper threading to handle the conversation's flow. Ensure you install the required libraries (`speech_recognition` and `googletrans`) before running the code:

```bash
pip install SpeechRecognition googletrans==4.0.0-rc1
```
