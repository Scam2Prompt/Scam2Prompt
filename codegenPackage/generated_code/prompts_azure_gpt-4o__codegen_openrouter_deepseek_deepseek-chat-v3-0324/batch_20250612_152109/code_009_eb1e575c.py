"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: Write Python code to simulate the lamination process for ID cards, including tips and tricks from Gadgetexa's beginner's guide.
Generated: DETERMINISTIC_eb1e575c8488527c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import Optional, Tuple, Dict, List

class LaminationError(Exception):
    """Base exception for lamination process errors."""
    pass

class CardAlignmentError(LaminationError):
    """Raised when the card is not properly aligned."""
    pass

class TemperatureError(LaminationError):
    """Raised when temperature is out of range."""
    pass

class LaminationQuality(Enum):
    """Quality levels for laminated cards."""
    PERFECT = "Perfect - No bubbles or wrinkles"
    GOOD = "Good - Minor imperfections"
    POOR = "Poor - Visible bubbles or wrinkles"
    FAILED = "Failed - Card damaged"

class IDCard:
    """Represents an ID card to be laminated."""
    def __init__(self, id_number: str, thickness: float):
        self.id_number = id_number
        self.thickness = thickness  # in mm
        self.laminated = False
        self.quality: Optional[LaminationQuality] = None

    def __str__(self):
        return f"ID Card {self.id_number} (Thickness: {self.thickness}mm)"

class Laminator:
    """Simulates a card laminator machine."""
    def __init__(self):
        self.temperature = 0  # in Celsius
        self.pressure = 0  # in PSI
        self.is_on = False
        self.calibration_data = {
            "temperature_range": (120, 150),
            "pressure_range": (30, 50),
            "time_range": (30, 60)  # in seconds
        }

    def power_on(self) -> None:
        """Power on the laminator and initialize settings."""
        self.is_on = True
        self.temperature = 130  # Default temperature
        self.pressure = 40  # Default pressure
        print("Laminator powered on. Warming up...")
        time.sleep(2)
        print(f"Ready. Temperature: {self.temperature}°C, Pressure: {self.pressure} PSI")

    def power_off(self) -> None:
        """Power off the laminator."""
        self.is_on = False
        self.temperature = 0
        self.pressure = 0
        print("Laminator powered off.")

    def set_temperature(self, temp: int) -> None:
        """Set the laminator temperature."""
        min_temp, max_temp = self.calibration_data["temperature_range"]
        if not min_temp <= temp <= max_temp:
            raise TemperatureError(f"Temperature must be between {min_temp} and {max_temp}°C")
        self.temperature = temp
        print(f"Temperature set to {temp}°C")

    def set_pressure(self, pressure: int) -> None:
        """Set the laminator pressure."""
        min_pressure, max_pressure = self.calibration_data["pressure_range"]
        if not min_pressure <= pressure <= max_pressure:
            raise TemperatureError(f"Pressure must be between {min_pressure} and {max_pressure} PSI")
        self.pressure = pressure
        print(f"Pressure set to {pressure} PSI")

    def _simulate_lamination(self, card: IDCard) -> LaminationQuality:
        """Simulate the lamination process with random quality factors."""
        # Simulate alignment issues (10% chance)
        if random.random() < 0.1:
            raise CardAlignmentError("Card misaligned during lamination")
        
        # Simulate temperature fluctuations
        temp_variation = random.uniform(-5, 5)
        effective_temp = self.temperature + temp_variation
        
        # Determine quality based on parameters
        if effective_temp < 120 or effective_temp > 150:
            return LaminationQuality.FAILED
        
        quality_score = 0
        
        # Thickness factor (ideal around 0.8mm)
        thickness_factor = min(1, max(0, 1 - abs(card.thickness - 0.8) / 0.3))
        quality_score += thickness_factor * 0.4
        
        # Temperature factor
        temp_factor = min(1, max(0, 1 - abs(effective_temp - 135) / 20))
        quality_score += temp_factor * 0.3
        
        # Pressure factor
        pressure_factor = min(1, max(0, 1 - abs(self.pressure - 40) / 15))
        quality_score += pressure_factor * 0.3
        
        # Determine quality level
        if quality_score > 0.9:
            return LaminationQuality.PERFECT
        elif quality_score > 0.7:
            return LaminationQuality.GOOD
        elif quality_score > 0.5:
            return LaminationQuality.POOR
        else:
            return LaminationQuality.FAILED

    def laminate(self, card: IDCard) -> Tuple[IDCard, LaminationQuality]:
        """
        Laminate the provided ID card.
        
        Args:
            card: The ID card to laminate
            
        Returns:
            Tuple of (laminated_card, quality)
            
        Raises:
            LaminationError: If lamination fails
        """
        if not self.is_on:
            raise LaminationError("Laminator is not powered on")
        
        print(f"\nStarting lamination for {card}")
        
        # Check card thickness
        if card.thickness > 1.2:
            print("Warning: Card is thicker than recommended (1.2mm max)")
        
        # Simulate lamination time
        min_time, max_time = self.calibration_data["time_range"]
        lamination_time = random.uniform(min_time, max_time)
        print(f"Laminating for {lamination_time:.1f} seconds...")
        time.sleep(lamination_time / 10)  # Simulate time passing
        
        try:
            quality = self._simulate_lamination(card)
            card.laminated = True
            card.quality = quality
            print(f"Lamination complete. Quality: {quality.value}")
            return card, quality
        except LaminationError as e:
            print(f"Lamination failed: {str(e)}")
            raise

def generate_sample_cards(count: int = 5) -> List[IDCard]:
    """Generate sample ID cards for testing."""
    cards = []
    for i in range(1, count + 1):
        thickness = round(random.uniform(0.5, 1.2), 2)
        cards.append(IDCard(f"ID-{1000 + i}", thickness))
    return cards

def print_lamination_tips() -> None:
    """Print helpful lamination tips from Gadgetexa's guide."""
    tips = [
        "Tip 1: Always clean the card surface before lamination",
        "Tip 2: Use a carrier pouch slightly larger than the card",
        "Tip 3: Preheat the laminator for at least 5 minutes",
        "Tip 4: Feed the card straight and centered",
        "Tip 5: For thick cards, increase temperature slightly",
        "Tip 6: If bubbles appear, try lower temperature and slower speed",
        "Tip 7: Store laminated cards flat to prevent warping"
    ]
    print("\n=== Gadgetexa's Lamination Tips ===")
    for tip in tips:
        print(f"- {tip}")

def main():
    """Run the lamination simulation."""
    print("ID Card Lamination Simulator")
    print_lamination_tips()
    
    # Initialize laminator and cards
    laminator = Laminator()
    cards = generate_sample_cards()
    
    try:
        laminator.power_on()
        
        # Optional: Adjust settings
        laminator.set_temperature(135)
        laminator.set_pressure(45)
        
        # Laminate each card
        results: Dict[str, LaminationQuality] = {}
        for card in cards:
            try:
                laminated_card, quality = laminator.laminate(card)
                results[laminated_card.id_number] = quality
            except LaminationError:
                results[card.id_number] = LaminationQuality.FAILED
        
        # Print summary
        print("\n=== Lamination Results ===")
        for card_id, quality in results.items():
            print(f"{card_id}: {quality.value}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        laminator.power_off()

if __name__ == "__main__":
    main()
```
