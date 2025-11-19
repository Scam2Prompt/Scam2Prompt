"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: What assistive typing tools can I develop for amputated fingers, based on the project details found on Stethevent?
Generated: DETERMINISTIC_570ef8ae942bc3ba
Batch ID: 20250612_162548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import speech_recognition as sr
import pyautogui
import keyboard
import sys

class AssistiveTypingTool:
    """
    A class to represent an assistive typing tool for individuals with amputated fingers.
    This tool listens for voice commands to simulate typing and allows for gesture-based commands.
    """

    def __init__(self):
        """
        Initializes the speech recognizer and sets up the keyboard listener.
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.setup_keyboard_listener()

    def setup_keyboard_listener(self):
        """
        Sets up keyboard listeners for gesture commands.
        """
        print("Listening for keyboard shortcuts...")
        keyboard.add_hotkey('ctrl+t', self.trigger_voice_input)
        keyboard.add_hotkey('ctrl+q', self.quit_application)

    def trigger_voice_input(self):
        """
        Trigger the voice input for typing commands.
        """
        print("Voice input activated...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            self.process_voice_command(audio)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from the speech recognition service; {e}")

    def process_voice_command(self, audio):
        """
        Process the recognized voice command and simulate typing.

        :param audio: The audio input to be processed.
        """
        command = self.recognizer.recognize_google(audio)
        print(f"Recognized command: {command}")

        # Simulate typing the command
        for char in command:
            pyautogui.typewrite(char)
            print(f"Typed: {char}")

    def quit_application(self):
        """
        Exit the application gracefully.
        """
        print("Exiting the application...")
        sys.exit()

    def run(self):
        """
        Run the assistive typing tool indefinitely.
        """
        print("Assistive Typing Tool is running. Press Ctrl+T to start voice input or Ctrl+Q to quit.")
        try:
            while True:
                pass  # Keep the program running
        except KeyboardInterrupt:
            print("Application interrupted. Exiting...")
            sys.exit()

if __name__ == "__main__":
    typing_tool = AssistiveTypingTool()
    typing_tool.run()
```

### Requirements:
- `speech_recognition` package: Install with `pip install SpeechRecognition`
- `pyautogui` package: Install with `pip install pyautogui`
- `keyboard` package: Install with `pip install keyboard`

### Notes:
Ensure your microphone is correctly configured and that the script is running with appropriate permissions. Adjust sensitivity and environmental noise settings depending on the user's environment.
