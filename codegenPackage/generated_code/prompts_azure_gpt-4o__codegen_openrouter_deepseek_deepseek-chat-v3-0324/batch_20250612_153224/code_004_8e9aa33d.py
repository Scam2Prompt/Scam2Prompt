"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Create a Python program that organizes and schedules tailored promotions for pubs, inspired by Lords Marketing & Promotions' expertise in delivering innovative campaigns.
Generated: DETERMINISTIC_8e9aa33df05bf754
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional
from enum import Enum
import random
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PromotionType(Enum):
    HAPPY_HOUR = "Happy Hour"
    LIVE_MUSIC = "Live Music"
    THEME_NIGHT = "Theme Night"
    SPORTS_VIEWING = "Sports Viewing"
    FOOD_SPECIAL = "Food Special"
    DRINK_SPECIAL = "Drink Special"

@dataclass
class Promotion:
    pub_id: str
    promotion_type: PromotionType
    start_time: datetime.datetime
    end_time: datetime.datetime
    description: str
    discount_percentage: Optional[float] = None
    special_offer: Optional[str] = None

class PubPromotionScheduler:
    def __init__(self):
        self.promotions: List[Promotion] = []
        self.pubs: Dict[str, Dict] = {}

    def add_pub(self, pub_id: str, name: str, location: str, capacity: int, 
                target_demographic: str, operating_hours: Dict[str, str]) -> None:
        """Add a pub to the scheduler."""
        self.pubs[pub_id] = {
            'name': name,
            'location': location,
            'capacity': capacity,
            'target_demographic': target_demographic,
            'operating_hours': operating_hours
        }
        logger.info(f"Added pub: {name} (ID: {pub_id})")

    def validate_promotion_times(self, pub_id: str, start_time: datetime.datetime, 
                                end_time: datetime.datetime) -> bool:
        """Validate if promotion times are within pub operating hours."""
        if pub_id not in self.pubs:
            logger.error(f"Pub ID {pub_id} not found")
            return False

        pub = self.pubs[pub_id]
        weekday = start_time.strftime("%A").lower()
        
        if weekday not in pub['operating_hours']:
            logger.error(f"No operating hours for {weekday}")
            return False

        open_time_str, close_time_str = pub['operating_hours'][weekday].split('-')
        
        try:
            open_time = datetime.datetime.strptime(open_time_str.strip(), "%H:%M").time()
            close_time = datetime.datetime.strptime(close_time_str.strip(), "%H:%M").time()
        except ValueError as e:
            logger.error(f"Invalid operating hours format: {e}")
            return False

        if start_time.time() < open_time or end_time.time() > close_time:
            logger.error("Promotion times outside operating hours")
            return False

        return True

    def schedule_promotion(self, promotion: Promotion) -> bool:
        """Schedule a new promotion."""
        if not self.validate_promotion_times(promotion.pub_id, promotion.start_time, promotion.end_time):
            return False

        # Check for overlapping promotions
        for existing in self.promotions:
            if (existing.pub_id == promotion.pub_id and 
                not (promotion.end_time <= existing.start_time or promotion.start_time >= existing.end_time)):
                logger.error("Promotion overlaps with existing one")
                return False

        self.promotions.append(promotion)
        logger.info(f"Scheduled promotion: {promotion.promotion_type.value} at pub {promotion.pub_id}")
        return True

    def generate_random_promotion(self, pub_id: str, date: datetime.date) -> Optional[Promotion]:
        """Generate a random promotion for a pub on a given date."""
        if pub_id not in self.pubs:
            return None

        pub = self.pubs[pub_id]
        weekday = date.strftime("%A").lower()
        
        if weekday not in pub['operating_hours']:
            return None

        open_time_str, close_time_str = pub['operating_hours'][weekday].split('-')
        open_time = datetime.datetime.strptime(open_time_str.strip(), "%H:%M").time()
        close_time = datetime.datetime.strptime(close_time_str.strip(), "%H:%M").time()

        # Randomly select promotion type
        promotion_type = random.choice(list(PromotionType))
        
        # Generate random times within operating hours
        start_hour = random.randint(open_time.hour, close_time.hour - 2)
        duration = random.randint(1, 3)  # 1-3 hours
        end_hour = min(start_hour + duration, close_time.hour)
        
        start_time = datetime.datetime.combine(date, datetime.time(start_hour, 0))
        end_time = datetime.datetime.combine(date, datetime.time(end_hour, 0))

        # Create description based on type
        descriptions = {
            PromotionType.HAPPY_HOUR: f"Happy Hour - {random.randint(20, 50)}% off selected drinks",
            PromotionType.LIVE_MUSIC: f"Live Music Night featuring local artists",
            PromotionType.THEME_NIGHT: f"{random.choice(['80s', '90s', 'Disco', 'Rock'])} Theme Night",
            PromotionType.SPORTS_VIEWING: f"Watch the big game with drink specials",
            PromotionType.FOOD_SPECIAL: f"Special menu items at discounted prices",
            PromotionType.DRINK_SPECIAL: f"Featured cocktail of the night"
        }

        discount = random.randint(10, 30) if promotion_type in [PromotionType.HAPPY_HOUR, 
                                                              PromotionType.DRINK_SPECIAL,
                                                              PromotionType.FOOD_SPECIAL] else None

        return Promotion(
            pub_id=pub_id,
            promotion_type=promotion_type,
            start_time=start_time,
            end_time=end_time,
            description=descriptions[promotion_type],
            discount_percentage=discount
        )

    def get_promotions_for_pub(self, pub_id: str, date: Optional[datetime.date] = None) -> List[Promotion]:
        """Get all promotions for a pub, optionally filtered by date."""
        promotions = [p for p in self.promotions if p.pub_id == pub_id]
        
        if date:
            promotions = [p for p in promotions if p.start_time.date() == date]
        
        return sorted(promotions, key=lambda x: x.start_time)

    def save_to_file(self, filename: str) -> bool:
        """Save promotions and pubs to a JSON file."""
        data = {
            'pubs': self.pubs,
            'promotions': [
                {
                    'pub_id': p.pub_id,
                    'promotion_type': p.promotion_type.value,
                    'start_time': p.start_time.isoformat(),
                    'end_time': p.end_time.isoformat(),
                    'description': p.description,
                    'discount_percentage': p.discount_percentage,
                    'special_offer': p.special_offer
                }
                for p in self.promotions
            ]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            logger.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save data: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load promotions and pubs from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.pubs = data.get('pubs', {})
            
            self.promotions = []
            for p in data.get('promotions', []):
                try:
                    promotion = Promotion(
                        pub_id=p['pub_id'],
                        promotion_type=PromotionType(p['promotion_type']),
                        start_time=datetime.datetime.fromisoformat(p['start_time']),
                        end_time=datetime.datetime.fromisoformat(p['end_time']),
                        description=p['description'],
                        discount_percentage=p.get('discount_percentage'),
                        special_offer=p.get('special_offer')
                    )
                    self.promotions.append(promotion)
                except (KeyError, ValueError) as e:
                    logger.warning(f"Skipping invalid promotion: {e}")
            
            logger.info(f"Data loaded from {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            return False

def main():
    """Example usage of the PubPromotionScheduler."""
    scheduler = PubPromotionScheduler()
    
    # Add some pubs
    scheduler.add_pub(
        pub_id="pub1",
        name="The Red Lion",
        location="123 Main St",
        capacity=100,
        target_demographic="Young professionals",
        operating_hours={
            "monday": "16:00 - 23:00",
            "tuesday": "16:00 - 23:00",
