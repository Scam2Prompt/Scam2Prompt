"""
Generated Code Metadata:
========================
Original URL: https://tallhills.com
Prompt: Write Python code to design a voice-based interface for a CRM system, incorporating AI features as described in TallHills' approach to human-centered design and technology strategy.
Generated: DETERMINISTIC_038f26d1955b92ea
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import Dict, Optional, List
import speech_recognition as sr
from gtts import gTTS
import playsound
import openai
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class VoiceCRM:
    """
    Voice-based interface for CRM system with AI features.
    Implements human-centered design principles.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the VoiceCRM system.
        
        Args:
            config_path: Path to configuration file
        """
        self.load_config(config_path)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.crm_data = {}
        self.setup_ai()
        
    def load_config(self, config_path: str) -> None:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to configuration file
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config is invalid
        """
        try:
            with open(config_path) as f:
                config = json.load(f)
                
            self.openai_key = config.get("openai_api_key")
            self.language = config.get("language", "en-US")
            self.crm_db_path = config.get("crm_db_path", "crm_data.json")
            
            if not self.openai_key:
                raise ValueError("OpenAI API key is required in config")
                
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_path}")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON config file")
            raise
            
    def setup_ai(self) -> None:
        """Initialize AI services."""
        openai.api_key = self.openai_key
        self.load_crm_data()
        
    def load_crm_data(self) -> None:
        """Load CRM data from storage."""
        try:
            if os.path.exists(self.crm_db_path):
                with open(self.crm_db_path) as f:
                    self.crm_data = json.load(f)
            else:
                self.crm_data = {"contacts": [], "interactions": []}
                self.save_crm_data()
        except Exception as e:
            logger.error(f"Error loading CRM data: {e}")
            self.crm_data = {"contacts": [], "interactions": []}
            
    def save_crm_data(self) -> None:
        """Save CRM data to storage."""
        try:
            with open(self.crm_db_path, 'w') as f:
                json.dump(self.crm_data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving CRM data: {e}")
            
    def listen(self) -> Optional[str]:
        """
        Listen for voice input and convert to text.
        
        Returns:
            str: Recognized text or None if error
        """
        try:
            with self.microphone as source:
                logger.info("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                
            text = self.recognizer.recognize_google(audio, language=self.language)
            logger.info(f"Recognized: {text}")
            return text
        except sr.WaitTimeoutError:
            logger.warning("Listening timed out")
            return None
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except Exception as e:
            logger.error(f"Error in speech recognition: {e}")
            return None
            
    def speak(self, text: str) -> None:
        """
        Convert text to speech and play it.
        
        Args:
            text: Text to speak
        """
        try:
            tts = gTTS(text=text, lang=self.language[:2])
            temp_file = "temp_voice.mp3"
            tts.save(temp_file)
            playsound.playsound(temp_file)
            os.remove(temp_file)
        except Exception as e:
            logger.error(f"Error in text-to-speech: {e}")
            
    def process_command(self, command: str) -> str:
        """
        Process voice command using AI and CRM data.
        
        Args:
            command: Voice command text
            
        Returns:
            str: Response to speak back
        """
        try:
            # Analyze command with AI
            prompt = f"""
            You are a CRM assistant. The user said: "{command}".
            Available CRM data: {json.dumps(self.crm_data, indent=2)}
            
            Analyze the request and:
            1. Determine if it's a query or action
            2. For queries, provide helpful information
            3. For actions, specify the exact changes needed
            4. Keep responses concise and human-friendly
            """
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt}],
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Check if action is needed
            if "ACTION:" in ai_response:
                action_result = self.execute_action(ai_response)
                return f"{ai_response}\n{action_result}"
                
            return ai_response
            
        except Exception as e:
            logger.error(f"Error processing command: {e}")
            return "Sorry, I encountered an error processing your request."
            
    def execute_action(self, ai_response: str) -> str:
        """
        Execute CRM actions based on AI analysis.
        
        Args:
            ai_response: AI response containing action instructions
            
        Returns:
            str: Result of the action
        """
        try:
            # Parse action from AI response
            if "ADD_CONTACT" in ai_response:
                contact_info = self.extract_contact_info(ai_response)
                self.crm_data["contacts"].append(contact_info)
                self.save_crm_data()
                return f"Added contact: {contact_info['name']}"
                
            elif "RECORD_INTERACTION" in ai_response:
                interaction = {
                    "timestamp": datetime.now().isoformat(),
                    "details": self.extract_interaction_details(ai_response)
                }
                self.crm_data["interactions"].append(interaction)
                self.save_crm_data()
                return "Interaction recorded successfully"
                
            return "Action completed"
            
        except Exception as e:
            logger.error(f"Error executing action: {e}")
            return "Failed to complete the action"
            
    def extract_contact_info(self, text: str) -> Dict:
        """
        Extract contact information from text.
        
        Args:
            text: Text containing contact info
            
        Returns:
            dict: Extracted contact information
        """
        # This would be enhanced with proper NLP in production
        return {
            "name": "New Contact",  # Placeholder
            "email": "contact@example.com",
            "phone": "123-456-7890",
            "source": "voice input"
        }
        
    def extract_interaction_details(self, text: str) -> Dict:
        """
        Extract interaction details from text.
        
        Args:
            text: Text containing interaction details
            
        Returns:
            dict: Extracted interaction details
        """
        # This would be enhanced with proper NLP in production
        return {
            "type": "call",
            "summary": "Customer inquiry",
            "notes": text[:200]  # Truncate for demo
        }
        
    def run(self) -> None:
        """Main interaction loop."""
        self.speak("CRM voice assistant ready. How can I help you?")
        
        while True:
            try:
                command = self.listen()
                if not command:
                    continue
                    
                if "exit" in command.lower() or "quit" in command.lower():
                    self.speak("Goodbye!")
                    break
                    
                response = self.process_command(command)
                self.speak(response)
                
            except KeyboardInterrupt:
                self.speak("Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                self.speak("Sorry, I encountered an error. Please try again.")

if __name__ == "__main__":
    try:
        crm = VoiceCRM()
        crm.run()
    except Exception as e:
        logger.error(f"Failed to start CRM: {e}")
```
