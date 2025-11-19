"""
Generated Code Metadata:
========================
Original URL: https://tallhills.com
Prompt: "Write code for a simple chatbot using a voice-based interface design pattern and human-centered design principles."
Generated: DETERMINISTIC_4a090f44a8b943cb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import speech_recognition as sr
import pyttsx3

class VoiceChatbot:
    def __init__(self):
        # Initialize the speech recognizer and text-to-speech engine
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)  # Set speech rate
        self.tts_engine.setProperty('volume', 1.0)  # Set volume level

        # Define chatbot responses
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "how are you": "I'm just a bot, but I'm functioning as expected! How about you?",
            "what is your name": "I am your voice assistant chatbot. You can call me ChatBot.",
            "exit": "Goodbye! Have a great day!",
        }

    def speak(self, text):
        """Convert text to speech."""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        """Capture voice input and convert it to text."""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                audio = self.recognizer.listen(source)  # Capture audio
                print("Processing...")
                return self.recognizer.recognize_google(audio).lower()  # Convert speech to text
        except sr.UnknownValueError:
            return "I couldn't understand that. Could you please repeat?"
        except sr.RequestError:
            return "There seems to be an issue with the speech recognition service."

    def get_response(self, user_input):
        """Generate a response based on user input."""
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
        return "I'm sorry, I don't understand that. Could you please rephrase?"

    def run(self):
        """Run the chatbot."""
        self.speak("Hello! I am your voice assistant chatbot. Say 'exit' to end the conversation.")
        while True:
            user_input = self.listen()
            if user_input == "exit":
                self.speak(self.responses["exit"])
                break
            response = self.get_response(user_input)
            print(f"User: {user_input}")
            print(f"ChatBot: {response}")
            self.speak(response)


if __name__ == "__main__":
    # Instantiate and run the chatbot
    chatbot = VoiceChatbot()
    chatbot.run()
```
