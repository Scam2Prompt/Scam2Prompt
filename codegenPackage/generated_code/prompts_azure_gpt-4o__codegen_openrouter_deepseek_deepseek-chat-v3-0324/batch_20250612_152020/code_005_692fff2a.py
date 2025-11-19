"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write code to implement a memory care activity tracker for seniors, focusing on interventions targeting attention, visual-spatial perception, and executive functioning, inspired by the Cognitive Therapeutics Method™.
Generated: DETERMINISTIC_692fff2ab1cfa4e2
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple

class ActivityTracker:
    """
    Memory care activity tracker for seniors focusing on cognitive interventions.
    Tracks activities targeting attention, visual-spatial perception, and executive functioning.
    """
    
    def __init__(self, data_file: str = "activity_data.json"):
        """
        Initialize the activity tracker with a data file.
        
        Args:
            data_file: Path to JSON file for storing activity data
        """
        self.data_file = data_file
        self.activities = {
            'attention': [
                "Number sequencing",
                "Symbol matching",
                "Sound identification"
            ],
            'visual_spatial': [
                "Puzzle assembly",
                "Shape rotation",
                "Map navigation"
            ],
            'executive': [
                "Task planning",
                "Category sorting",
                "Time estimation"
            ]
        }
        self.load_data()
    
    def load_data(self) -> None:
        """Load activity data from JSON file or initialize empty data structure."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.data = json.load(f)
            else:
                self.data = {
                    'participants': {},
                    'last_id': 0
                }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.data = {
                'participants': {},
                'last_id': 0
            }
    
    def save_data(self) -> None:
        """Save activity data to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_participant(self, name: str, age: int) -> int:
        """
        Add a new participant to the tracker.
        
        Args:
            name: Participant's name
            age: Participant's age
            
        Returns:
            Assigned participant ID
        """
        self.data['last_id'] += 1
        participant_id = self.data['last_id']
        
        self.data['participants'][participant_id] = {
            'name': name,
            'age': age,
            'activities': [],
            'progress': {
                'attention': 0,
                'visual_spatial': 0,
                'executive': 0
            }
        }
        self.save_data()
        return participant_id
    
    def record_activity(
        self,
        participant_id: int,
        domain: str,
        activity_name: str,
        duration: int,
        difficulty: int,
        notes: str = ""
    ) -> bool:
        """
        Record an activity session for a participant.
        
        Args:
            participant_id: ID of participant
            domain: Cognitive domain ('attention', 'visual_spatial', or 'executive')
            activity_name: Name of activity performed
            duration: Duration in minutes
            difficulty: Perceived difficulty (1-5 scale)
            notes: Optional notes about the session
            
        Returns:
            True if successful, False otherwise
        """
        if participant_id not in self.data['participants']:
            print(f"Participant ID {participant_id} not found")
            return False
        
        if domain not in self.activities:
            print(f"Invalid domain: {domain}")
            return False
        
        if activity_name not in self.activities[domain]:
            print(f"Invalid activity for domain {domain}: {activity_name}")
            return False
        
        if not (1 <= difficulty <= 5):
            print("Difficulty must be between 1 and 5")
            return False
        
        activity_record = {
            'date': datetime.datetime.now().isoformat(),
            'domain': domain,
            'activity': activity_name,
            'duration': duration,
            'difficulty': difficulty,
            'notes': notes
        }
        
        self.data['participants'][participant_id]['activities'].append(activity_record)
        
        # Update progress (simple count of activities in each domain)
        self.data['participants'][participant_id]['progress'][domain] += 1
        
        self.save_data()
        return True
    
    def get_participant_progress(self, participant_id: int) -> Optional[Dict[str, int]]:
        """
        Get progress summary for a participant.
        
        Args:
            participant_id: ID of participant
            
        Returns:
            Dictionary with progress counts per domain, or None if participant not found
        """
        if participant_id not in self.data['participants']:
            return None
        return self.data['participants'][participant_id]['progress']
    
    def get_recommended_activities(
        self,
        participant_id: int,
        domain: Optional[str] = None
    ) -> List[Tuple[str, str]]:
        """
        Get recommended activities for a participant, optionally filtered by domain.
        
        Args:
            participant_id: ID of participant
            domain: Optional domain to filter recommendations
            
        Returns:
            List of (domain, activity) tuples
        """
        if participant_id not in self.data['participants']:
            return []
        
        recommendations = []
        
        # If no domain specified, recommend least practiced domains first
        if domain is None:
            progress = self.data['participants'][participant_id]['progress']
            domains_sorted = sorted(
                progress.keys(),
                key=lambda k: progress[k]
            )
            for domain in domains_sorted:
                for activity in self.activities[domain]:
                    recommendations.append((domain, activity))
        else:
            if domain in self.activities:
                for activity in self.activities[domain]:
                    recommendations.append((domain, activity))
        
        return recommendations
    
    def generate_report(
        self,
        participant_id: int,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None
    ) -> Dict:
        """
        Generate an activity report for a participant within a date range.
        
        Args:
            participant_id: ID of participant
            start_date: Optional start date (ISO format)
            end_date: Optional end date (ISO format)
            
        Returns:
            Dictionary containing report data
        """
        if participant_id not in self.data['participants']:
            return {}
        
        participant = self.data['participants'][participant_id]
        report = {
            'name': participant['name'],
            'age': participant['age'],
            'total_sessions': 0,
            'by_domain': {
                'attention': {'count': 0, 'total_duration': 0},
                'visual_spatial': {'count': 0, 'total_duration': 0},
                'executive': {'count': 0, 'total_duration': 0}
            },
            'recent_activities': []
        }
        
        try:
            start = (
                datetime.datetime.fromisoformat(start_date) 
                if start_date 
                else datetime.datetime.min
            )
            end = (
                datetime.datetime.fromisoformat(end_date) 
                if end_date 
                else datetime.datetime.max
            )
        except ValueError:
            print("Invalid date format. Use ISO format (YYYY-MM-DD)")
            return report
        
        for activity in participant['activities']:
            try:
                activity_date = datetime.datetime.fromisoformat(activity['date'])
                if start <= activity_date <= end:
                    report['total_sessions'] += 1
                    domain = activity['domain']
                    report['by_domain'][domain]['count'] += 1
                    report['by_domain'][domain]['total_duration'] += activity['duration']
                    
                    # Add to recent activities (last 5)
                    if len(report['recent_activities']) < 5:
                        report['recent_activities'].append({
                            'date': activity['date'],
                            'activity': activity['activity'],
                            'duration': activity['duration'],
                            'difficulty': activity['difficulty']
                        })
            except (KeyError, ValueError):
                continue
        
        return report

# Example usage
if __name__ == "__main__":
    tracker = ActivityTracker()
    
    # Add a participant
    participant_id = tracker.add_participant("John Doe", 75)
    
    # Record some activities
    tracker.record_activity(
        participant_id,
        "attention",
        "Number sequencing",
        15,
        3,
        "Participant engaged well with the activity"
    )
    
    tracker.record_activity(
        participant_id,
        "visual_spatial",
        "Puzzle assembly",
        20,
        2
    )
    
    # Get progress
    progress = tracker.get_participant_progress(participant_id)
    print(f"Participant progress: {progress}")
    
    # Get recommendations
    recommendations = tracker.get_recommended_activities(participant_id)
    print("Recommended activities:")
    for domain, activity in recommendations:
        print(f"- {domain}: {activity}")
    
    # Generate report
    report = tracker.generate_report(participant_id)
    print("\nActivity report:")
    print(json.dumps(report, indent=2))
```
