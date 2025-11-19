"""
Generated Code Metadata:
========================
Original URL: https://scroll-faqs.gitbook.io
Prompt: Write a program to calculate the marks cutoff for $SCR airdrop eligibility based on participation in Scroll activities, including Sessions and Canvas/badges.
Generated: DETERMINISTIC_733c0efb79c66bff
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union

class AirdropCalculator:
    """
    Calculates the marks cutoff for SCR airdrop eligibility based on Scroll activities.
    Activities include Sessions participation and Canvas/badges collection.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the calculator with configuration.
        
        Args:
            config_path: Path to the configuration file containing scoring rules.
        """
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise ValueError(f"Configuration file {config_path} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in configuration file {config_path}")
            
        self.validate_config()
    
    def validate_config(self) -> None:
        """Validate the configuration file structure."""
        required_keys = ['session_weights', 'badge_weights', 'cutoff_threshold']
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
    
    def calculate_session_score(self, sessions: List[Dict[str, Union[int, str]]]) -> float:
        """
        Calculate score from session participation.
        
        Args:
            sessions: List of session participation records.
                     Each record should contain 'type' and 'count'.
        
        Returns:
            Total score from sessions.
        """
        total = 0.0
        weights = self.config['session_weights']
        
        for session in sessions:
            session_type = session.get('type')
            count = session.get('count', 0)
            
            if not isinstance(count, (int, float)) or count < 0:
                raise ValueError("Session count must be a non-negative number")
                
            if session_type not in weights:
                raise ValueError(f"Unknown session type: {session_type}")
                
            total += weights[session_type] * count
            
        return total
    
    def calculate_badge_score(self, badges: List[Dict[str, Union[int, str]]]) -> float:
        """
        Calculate score from badge collection.
        
        Args:
            badges: List of badge records.
                   Each record should contain 'tier' and 'count'.
        
        Returns:
            Total score from badges.
        """
        total = 0.0
        weights = self.config['badge_weights']
        
        for badge in badges:
            tier = badge.get('tier')
            count = badge.get('count', 0)
            
            if not isinstance(count, (int, float)) or count < 0:
                raise ValueError("Badge count must be a non-negative number")
                
            if tier not in weights:
                raise ValueError(f"Unknown badge tier: {tier}")
                
            total += weights[tier] * count
            
        return total
    
    def calculate_total_score(
        self,
        sessions: Optional[List[Dict[str, Union[int, str]]]] = None,
        badges: Optional[List[Dict[str, Union[int, str]]]] = None
    ) -> float:
        """
        Calculate total eligibility score.
        
        Args:
            sessions: Optional list of session participation records.
            badges: Optional list of badge records.
        
        Returns:
            Total eligibility score.
        """
        total = 0.0
        
        if sessions:
            total += self.calculate_session_score(sessions)
            
        if badges:
            total += self.calculate_badge_score(badges)
            
        return total
    
    def is_eligible(self, total_score: float) -> bool:
        """
        Check if the total score meets the cutoff threshold.
        
        Args:
            total_score: Calculated total score.
        
        Returns:
            True if eligible, False otherwise.
        """
        return total_score >= self.config['cutoff_threshold']


# Example usage
if __name__ == "__main__":
    try:
        # Initialize calculator
        calculator = AirdropCalculator()
        
        # Example user data
        user_sessions = [
            {"type": "weekly", "count": 3},
            {"type": "monthly", "count": 1}
        ]
        
        user_badges = [
            {"tier": "gold", "count": 2},
            {"tier": "silver", "count": 5}
        ]
        
        # Calculate scores
        session_score = calculator.calculate_session_score(user_sessions)
        badge_score = calculator.calculate_badge_score(user_badges)
        total_score = calculator.calculate_total_score(user_sessions, user_badges)
        
        # Check eligibility
        is_eligible = calculator.is_eligible(total_score)
        
        # Print results
        print(f"Session Score: {session_score}")
        print(f"Badge Score: {badge_score}")
        print(f"Total Score: {total_score}")
        print(f"Eligible: {'Yes' if is_eligible else 'No'}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
