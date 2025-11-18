"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wavecall.io
Prompt: Create a demo application that showcases WaveCall's core features: real-time voice translation, live transcription, and natural AI voice playback.
Generated: DETERMINISTIC_d8e0ea7af0b18a1e
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import threading
import queue
import time
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

# Constants for supported languages
SOURCE_LANGUAGE = "en"  # English
TARGET_LANGUAGE = "es"  # Spanish

# Shared queue for real-time processing
transcription_queue = queue.Queue()

# Initialize translator
translator = Translator()

# Function to capture voice input and transcribe it using SpeechRecognition
def voice_to_text(recognizer, microphone):
    """
    Captures voice input and transcribes it into text using SpeechRecognition.
    Pushes the transcription to a shared queue for translation and playback.
    """
    try:
        print("Listening for voice input...")
        audio = recognizer.listen(microphone, timeout=5, phrase_time_limit=10)
        transcription = recognizer.recognize_google(audio, language=SOURCE_LANGUAGE)
        print(f"Transcription: {transcription}")
        transcription_queue.put(transcription)
    except sr.WaitTimeoutError:
        print("No speech detected (timeout).")
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError as e:
        print(f"Error with speech recognition service: {e}")

# Function to translate text using Google Translate library
def translate_text(text, target_language):
    """
    Translates the given text into the target language.
    """
    try:
        translation = translator.translate(text, src=SOURCE_LANGUAGE, dest=target_language)
        print(f"Translated Text: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

# Function to play back translated text as speech using GTTS
def play_translated_voice(translated_text):
    """
    Converts translated text into audio using Google Text-to-Speech (GTTS) and plays it back.
    """
    try:
        tts = gTTS(text=translated_text, lang=TARGET_LANGUAGE, slow=False)
        tts_filename = "translated_audio.mp3"
        tts.save(tts_filename)
        playsound.playsound(tts_filename)
        os.remove(tts_filename)
    except Exception as e:
        print(f"Audio playback error: {e}")

# Worker thread to continuously process transcriptions from the queue
def process_transcriptions():
    """
    Processes transcriptions from the shared queue by translating them and playing back the translated audio.
    """
    while True:
        try:
            transcription = transcription_queue.get(timeout=1)  # Wait for transcription
            translated_text = translate_text(transcription, TARGET_LANGUAGE)
            if translated_text:
                play_translated_voice(translated_text)
        except queue.Empty:
            time.sleep(0.1)
        except Exception as e:
            print(f"Error processing transcription: {e}")

def main():
    """
    Main function to start the demo application showcasing WaveCall's core features:
    real-time voice translation, live transcription, and natural AI voice playback.
    """
    # Initialize speech recognizer and microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Start worker thread for processing transcriptions
    transcription_thread = threading.Thread(target=process_transcriptions, daemon=True)
    transcription_thread.start()

    print("WaveCall Demo Application")
    print("--------------------------")
    print("Features: Real-time voice translation, live transcription, AI voice playback")
    print("Speak into the microphone to see the app in action.")

    try:
        while True:
            voice_to_text(recognizer, microphone)
    except KeyboardInterrupt:
        print("\nExiting WaveCall Demo Application...")
        transcription_thread.join()

if __name__ == "__main__":
    main()
```
