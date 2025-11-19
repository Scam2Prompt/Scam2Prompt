"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: Generate a Python script to create a personalized training plan for beginners in Jiu-Jitsu, incorporating elements from the Fusion Jiu Jitsu School's methodology.
Generated: DETERMINISTIC_efef65350a091f4d
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class TrainingPlanGenerator:
    """
    A class to generate personalized Jiu-Jitsu training plans for beginners,
    incorporating elements from the Fusion Jiu Jitsu School's methodology.
    """
    
    def __init__(self):
        self.technique_categories = {
            "fundamentals": [
                "Shrimping (Hip Escape)",
                "Bridging",
                "Breakfalling",
                "Basic Stance and Movement",
                "Gripping Basics"
            ],
            "positions": [
                "Guard (Closed and Open)",
                "Mount",
                "Side Control",
                "Back Control"
            ],
            "submissions": [
                "Armbar from Guard",
                "Kimura from Guard",
                "Triangle Choke",
                "Rear Naked Choke"
            ],
            "escapes": [
                "Mount Escape (Upa)",
                "Side Control Escape (Shrimping)",
                "Back Escape (Hand Fighting)"
            ],
            "transitions": [
                "Guard Pass (Knee Cut)",
                "Sweep (Scissor Sweep)",
                "Positional Advancement"
            ]
        }
        
        self.training_days = ["Monday", "Wednesday", "Friday"]
        self.plan_duration_weeks = 8
        self.session_duration = 60  # minutes
        
    def _validate_user_input(self, user_data: Dict) -> bool:
        """Validate user input data."""
        required_fields = ["name", "age", "fitness_level", "goals"]
        for field in required_fields:
            if field not in user_data:
                raise ValueError(f"Missing required field: {field}")
                
        if not isinstance(user_data["age"], int) or user_data["age"] < 12:
            raise ValueError("Age must be at least 12")
            
        if user_data["fitness_level"] not in ["low", "medium", "high"]:
            raise ValueError("Fitness level must be 'low', 'medium', or 'high'")
            
        return True
    
    def _adjust_for_fitness_level(self, fitness_level: str) -> Dict:
        """
        Adjust training intensity based on fitness level.
        Returns a dictionary with adjusted parameters.
        """
        adjustments = {
            "low": {
                "warmup_duration": 15,
                "drill_repetitions": 3,
                "round_duration": 3,
                "rest_between_rounds": 60
            },
            "medium": {
                "warmup_duration": 10,
                "drill_repetitions": 5,
                "round_duration": 5,
                "rest_between_rounds": 45
            },
            "high": {
                "warmup_duration": 5,
                "drill_repetitions": 7,
                "round_duration": 7,
                "rest_between_rounds": 30
            }
        }
        return adjustments[fitness_level]
    
    def _select_techniques(self, goals: List[str]) -> Dict[str, List[str]]:
        """
        Select techniques based on user goals.
        Returns a dictionary of selected techniques by category.
        """
        selected_techniques = {}
        
        # Always include fundamentals
        selected_techniques["fundamentals"] = self.technique_categories["fundamentals"]
        
        # Select other categories based on goals
        if "self_defense" in goals:
            selected_techniques["escapes"] = self.technique_categories["escapes"]
            selected_techniques["submissions"] = self.technique_categories["submissions"][2:]  # chokes
            
        if "competition" in goals:
            selected_techniques["positions"] = self.technique_categories["positions"]
            selected_techniques["transitions"] = self.technique_categories["transitions"]
            
        if "fitness" in goals:
            selected_techniques["transitions"] = self.technique_categories["transitions"]
            
        return selected_techniques
    
    def _generate_weekly_schedule(self, selected_techniques: Dict[str, List[str]]) -> List[Dict]:
        """
        Generate a weekly training schedule with techniques.
        Returns a list of daily training sessions.
        """
        weekly_schedule = []
        
        # Monday: Fundamentals and Positions
        monday_session = {
            "day": "Monday",
            "focus": "Fundamentals and Positions",
            "techniques": selected_techniques.get("fundamentals", [])[:2] + 
                          selected_techniques.get("positions", [])[:2]
        }
        weekly_schedule.append(monday_session)
        
        # Wednesday: Escapes and Submissions
        wednesday_session = {
            "day": "Wednesday",
            "focus": "Escapes and Submissions",
            "techniques": selected_techniques.get("escapes", [])[:2] + 
                          selected_techniques.get("submissions", [])[:2]
        }
        weekly_schedule.append(wednesday_session)
        
        # Friday: Transitions and Live Training
        friday_session = {
            "day": "Friday",
            "focus": "Transitions and Live Training",
            "techniques": selected_techniques.get("transitions", [])[:2] + 
                          ["Positional Sparring"]
        }
        weekly_schedule.append(friday_session)
        
        return weekly_schedule
    
    def _generate_plan_structure(self, user_data: Dict) -> Dict:
        """
        Generate the complete training plan structure.
        Returns a dictionary with the full plan.
        """
        fitness_adjustments = self._adjust_for_fitness_level(user_data["fitness_level"])
        selected_techniques = self._select_techniques(user_data["goals"])
        
        plan = {
            "user_info": {
                "name": user_data["name"],
                "age": user_data["age"],
                "fitness_level": user_data["fitness_level"],
                "goals": user_data["goals"],
                "generated_date": datetime.now().strftime("%Y-%m-%d")
            },
            "plan_details": {
                "duration_weeks": self.plan_duration_weeks,
                "sessions_per_week": len(self.training_days),
                "session_duration_minutes": self.session_duration,
                "training_days": self.training_days,
                "fitness_adjustments": fitness_adjustments
            },
            "weekly_schedule": self._generate_weekly_schedule(selected_techniques),
            "weekly_progression": []
        }
        
        # Add weekly progression with technique variations
        for week in range(1, self.plan_duration_weeks + 1):
            weekly_prog = {
                "week": week,
                "focus": f"Building on week {week-1}" if week > 1 else "Foundation",
                "notes": self._get_weekly_notes(week, selected_techniques)
            }
            plan["weekly_progression"].append(weekly_prog)
            
        return plan
    
    def _get_weekly_notes(self, week: int, techniques: Dict[str, List[str]]) -> str:
        """Generate weekly progression notes."""
        if week == 1:
            return "Focus on proper technique execution. Slow and controlled movements."
        elif week == 2:
            return "Increase drilling speed slightly. Start connecting techniques."
        elif week == 3:
            return "Begin combining 2-3 techniques in sequence. Add light resistance."
        elif week == 4:
            return "Introduce positional sparring with specific goals."
        elif week == 5:
            return "Increase sparring intensity. Focus on transitions between positions."
        elif week == 6:
            return "Refine techniques. Work on timing and setups."
        elif week == 7:
            return "Simulate competition scenarios. Focus on strategy."
        else:
            return "Review all techniques. Prepare for assessment or next level."
    
    def generate_plan(self, user_data: Dict) -> Dict:
        """
        Generate a personalized training plan based on user data.
        
        Args:
            user_data: Dictionary containing user information including:
                - name: str
                - age: int
                - fitness_level: str (low/medium/high)
                - goals: List[str] (e.g., ["self_defense", "fitness"])
                
        Returns:
            Dictionary containing the complete training plan.
        """
        try:
            self._validate_user_input(user_data)
            plan = self._generate_plan_structure(user_data)
            return plan
        except Exception as e:
            raise ValueError(f"Error generating training plan: {str(e)}")
    
    def save_plan_to_file(self, plan: Dict, filename: Optional[str] = None) -> str:
        """
        Save the training plan to a JSON file.
        
        Args:
            plan: The training plan dictionary
            filename: Optional custom filename
            
        Returns:
            The filename used
        """
        if not filename:
            name = plan["user_info"]["name"].replace(" ", "_").lower()
            filename = f"jiu_jitsu_plan_{name}_{datetime.now().strftime('%Y%m
