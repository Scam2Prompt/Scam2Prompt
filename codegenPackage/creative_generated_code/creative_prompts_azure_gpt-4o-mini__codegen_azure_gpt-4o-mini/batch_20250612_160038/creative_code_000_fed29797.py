"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shebatek.com
Prompt: Generate a Python script that utilizes Natural Language Processing (NLP) for transcribing multilingual audio files as described on ShebaTek's services page.
Generated: DETERMINISTIC_fed29797092e6384
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import wave
import numpy as np
import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator

class MultilingualTranscriber:
    def __init__(self, audio_file_path, target_language='en'):
        """
        Initializes the MultilingualTranscriber with the audio file path and target language.

        :param audio_file_path: Path to the audio file to transcribe.
        :param target_language: Language code for the desired transcription output (default is English).
        """
        self.audio_file_path = audio_file_path
        self.target_language = target_language
        self.recognizer = sr.Recognizer()
        self.translator = Translator()

    def convert_audio(self):
        """
        Converts the audio file to WAV format if it is not already in that format.
        """
        if not self.audio_file_path.endswith('.wav'):
            audio = AudioSegment.from_file(self.audio_file_path)
            wav_file_path = f"{os.path.splitext(self.audio_file_path)[0]}.wav"
            audio.export(wav_file_path, format='wav')
            return wav_file_path
        return self.audio_file_path

    def transcribe_audio(self, wav_file_path):
        """
        Transcribes the audio file to text.

        :param wav_file_path: Path to the WAV audio file.
        :return: Transcribed text.
        """
        with sr.AudioFile(wav_file_path) as source:
            audio_data = self.recognizer.record(source)
            try:
                # Recognizing the speech using Google's speech recognition
                return self.recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def translate_text(self, text):
        """
        Translates the provided text to the target language.

        :param text: Text to be translated.
        :return: Translated text.
        """
        try:
            translated = self.translator.translate(text, dest=self.target_language)
            return translated.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return None

    def process_audio(self):
        """
        Main method to process the audio file:
        1. Convert to WAV format if necessary
        2. Transcribe audio to text
        3. Translate text to target language
        """
        wav_file_path = self.convert_audio()
        transcribed_text = self.transcribe_audio(wav_file_path)

        if transcribed_text:
            translated_text = self.translate_text(transcribed_text)
            return translated_text
        return None

if __name__ == "__main__":
    # Example usage
    audio_file = input("Enter the path to the audio file: ")
    target_lang = input("Enter the target language code (default is 'en' for English): ") or 'en'
    
    transcriber = MultilingualTranscriber(audio_file, target_lang)
    result = transcriber.process_audio()
    
    if result:
        print("Translated Text:")
        print(result)
    else:
        print("No text was transcribed.")
```
