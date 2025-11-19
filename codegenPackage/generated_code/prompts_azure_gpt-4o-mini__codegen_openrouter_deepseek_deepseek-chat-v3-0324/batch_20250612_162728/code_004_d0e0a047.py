"""
Generated Code Metadata:
========================
Original URL: https://workspace-207.com
Prompt: How can I customize the CAPTCHA challenge to enhance user experience while ensuring security?
Generated: DETERMINISTIC_d0e0a0473b6d7f25
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# CAPTCHA Customization Module

```python
import random
import string
from io import BytesIO
from typing import Tuple, Optional
from PIL import Image, ImageDraw, ImageFont
import hashlib
import time
import json
from pathlib import Path

class CaptchaGenerator:
    """
    A customizable CAPTCHA generator that balances security and user experience.
    Features include:
    - Adjustable difficulty levels
    - Multiple CAPTCHA types (text, math, image)
    - Accessibility options
    - Anti-bot measures
    """
    
    def __init__(self):
        self._font_path = str(Path(__file__).parent / 'assets' / 'fonts' / 'arial.ttf')
        self._default_settings = {
            'length': 6,
            'width': 200,
            'height': 80,
            'difficulty': 'medium',
            'type': 'text',
            'background_color': (255, 255, 255),
            'text_color': (0, 0, 0),
            'noise_level': 0.3,
            'distortion': True,
            'expiry': 300  # seconds
        }
        
    def generate_captcha(self, settings: Optional[dict] = None) -> Tuple[str, Image.Image]:
        """
        Generate a CAPTCHA challenge based on provided settings.
        
        Args:
            settings: Dictionary containing customization options
            
        Returns:
            Tuple containing (challenge_text, image_data)
        """
        config = {**self._default_settings, **(settings or {})}
        
        if config['type'] == 'math':
            challenge, answer = self._generate_math_captcha(config['difficulty'])
        else:
            challenge = self._generate_text_captcha(config['length'], config['difficulty'])
            answer = challenge
            
        image = self._generate_image(challenge, config)
        
        # Store the answer hash with timestamp for validation
        self._store_captcha_answer(answer)
        
        return challenge, image
    
    def _generate_text_captcha(self, length: int, difficulty: str) -> str:
        """Generate random text CAPTCHA based on difficulty."""
        if difficulty == 'easy':
            chars = string.ascii_uppercase
        elif difficulty == 'medium':
            chars = string.ascii_letters + string.digits
        else:  # hard
            chars = string.ascii_letters + string.digits + '!@#$%^&*'
            
        return ''.join(random.choice(chars) for _ in range(length))
    
    def _generate_math_captcha(self, difficulty: str) -> Tuple[str, str]:
        """Generate math CAPTCHA challenge."""
        if difficulty == 'easy':
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            op = random.choice(['+', '-'])
        elif difficulty == 'medium':
            a = random.randint(10, 99)
            b = random.randint(1, 9)
            op = random.choice(['+', '-', '*'])
        else:  # hard
            a = random.randint(10, 99)
            b = random.randint(10, 99)
            op = random.choice(['+', '-', '*', '/'])
            
        challenge = f"{a} {op} {b}"
        answer = str(int(eval(challenge)))
        return challenge, answer
    
    def _generate_image(self, text: str, config: dict) -> Image.Image:
        """Generate CAPTCHA image with distortions."""
        image = Image.new('RGB', (config['width'], config['height']), config['background_color'])
        draw = ImageDraw.Draw(image)
        
        try:
            font = ImageFont.truetype(self._font_path, size=min(config['height']//2, 40))
        except IOError:
            font = ImageFont.load_default()
            
        # Draw text with random positioning
        text_width, text_height = draw.textsize(text, font=font)
        x = (config['width'] - text_width) / 2 * random.uniform(0.8, 1.2)
        y = (config['height'] - text_height) / 2 * random.uniform(0.8, 1.2)
        
        draw.text((x, y), text, fill=config['text_color'], font=font)
        
        # Add noise
        if config['noise_level'] > 0:
            self._add_noise(image, config)
            
        # Add distortion
        if config['distortion']:
            image = self._distort_image(image)
            
        return image
    
    def _add_noise(self, image: Image.Image, config: dict):
        """Add visual noise to the CAPTCHA."""
        pixels = image.load()
        width, height = image.size
        
        for _ in range(int(config['width'] * config['height'] * config['noise_level'])):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            pixels[x, y] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
    
    def _distort_image(self, image: Image.Image) -> Image.Image:
        """Apply wave distortion to the image."""
        width, height = image.size
        distorted = Image.new('RGB', (width, height))
        
        x_offset = int(5 * random.random())
        y_offset = int(3 * random.random())
        
        for y in range(height):
            for x in range(width):
                nx = x + int(x_offset * math.sin(2 * math.pi * y / 60))
                ny = y + int(y_offset * math.sin(2 * math.pi * x / 90))
                
                if 0 <= nx < width and 0 <= ny < height:
                    distorted.putpixel((x, y), image.getpixel((nx, ny)))
                    
        return distorted
    
    def _store_captcha_answer(self, answer: str):
        """Store CAPTCHA answer with timestamp and hash."""
        timestamp = int(time.time())
        captcha_id = hashlib.sha256(f"{answer}{timestamp}".encode()).hexdigest()
        
        # In production, this would use a proper storage solution
        captcha_data = {
            'answer': answer,
            'timestamp': timestamp,
            'id': captcha_id
        }
        
        # Store in temporary file (replace with database in production)
        with open(f"captcha_{captcha_id}.json", 'w') as f:
            json.dump(captcha_data, f)
            
        return captcha_id
    
    def validate_captcha(self, user_input: str, captcha_id: str) -> bool:
        """
        Validate user's CAPTCHA response.
        
        Args:
            user_input: User's answer to the CAPTCHA
            captcha_id: The CAPTCHA identifier
            
        Returns:
            bool: True if validation succeeds
        """
        try:
            with open(f"captcha_{captcha_id}.json", 'r') as f:
                captcha_data = json.load(f)
                
            # Check expiry
            current_time = int(time.time())
            if current_time - captcha_data['timestamp'] > self._default_settings['expiry']:
                return False
                
            # Case-insensitive comparison for text CAPTCHAs
            if isinstance(captcha_data['answer'], str):
                return user_input.lower() == captcha_data['answer'].lower()
                
            return user_input == captcha_data['answer']
            
        except (FileNotFoundError, json.JSONDecodeError):
            return False
```

Example usage:

```python
# Example usage
if __name__ == "__main__":
    captcha = CaptchaGenerator()
    
    # Generate a text CAPTCHA
    challenge, image = captcha.generate_captcha({
        'type': 'text',
        'difficulty': 'medium',
        'length': 5
    })
    image.save("captcha.png")
    print(f"Text CAPTCHA: {challenge}")
    
    # Generate a math CAPTCHA
    challenge, image = captcha.generate_captcha({
        'type': 'math',
        'difficulty': 'hard'
    })
    image.save("math_captcha.png")
    print(f"Math CAPTCHA: {challenge}")
    
    # Validate a CAPTCHA (simulated)
    # In real usage, you'd get captcha_id from the generation step
    is_valid = captcha.validate_captcha("user_input", "simulated_id")
    print(f"Validation result: {is_valid}")
```
