"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Generate a study plan for UPSC Civil Services Exam preparation, incorporating the personalized mentorship and topic-wise study material from Shield IAS.
Generated: DETERMINISTIC_86766f9b97ab1d03
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates a personalized UPSC Civil Services Exam study plan incorporating Shield IAS mentorship and materials:

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class StudyPlanGenerator:
    """
    Generates a personalized UPSC Civil Services Exam study plan with Shield IAS resources.
    """
    
    def __init__(self):
        self.subjects = {
            "Prelims": {
                "General Studies Paper I": [
                    "Current Affairs", "History", "Geography", 
                    "Polity", "Economy", "Environment", 
                    "Science & Technology", "General Knowledge"
                ],
                "General Studies Paper II (CSAT)": [
                    "Comprehension", "Interpersonal Skills", 
                    "Logical Reasoning", "Decision Making", 
                    "General Mental Ability", "Basic Numeracy"
                ]
            },
            "Mains": {
                "Essay": ["Practice Essays", "Current Topics"],
                "General Studies I": ["Indian Heritage", "History", "Geography", "Society"],
                "General Studies II": ["Governance", "Constitution", "Polity", "Social Justice"],
                "General Studies III": ["Technology", "Economic Development", "Security", "Disaster Management"],
                "General Studies IV": ["Ethics", "Integrity", "Aptitude"],
                "Optional Subject": ["Optional Paper I", "Optional Paper II"]
            },
            "Interview": ["Personality Test", "Current Affairs", "Communication Skills"]
        }
        
        self.shield_ias_resources = {
            "Current Affairs": ["Daily Current Affairs PDF", "Monthly Magazine", "Editorial Analysis"],
            "History": ["Ancient India Notes", "Medieval India Notes", "Modern India Notes"],
            "Polity": ["Constitution Explained", "Laxmikant Summary", "Important Judgments"],
            "Economy": ["Basic Concepts", "Budget Analysis", "Economic Survey Summary"],
            "Environment": ["Shield IAS Environment Primer", "PYQ Analysis", "Current Issues"],
            "Essay": ["Model Essays", "Previous Year Topics", "Feedback Sessions"]
        }
        
    def generate_study_plan(
        self, 
        start_date: str, 
        end_date: str, 
        hours_per_day: int,
        weak_areas: Optional[List[str]] = None,
        optional_subject: Optional[str] = None
    ) -> Dict:
        """
        Generates a personalized study plan between given dates.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            hours_per_day: Number of study hours per day
            weak_areas: List of topics to focus more on
            optional_subject: Optional subject name if known
            
        Returns:
            Dictionary containing the study plan
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            if start >= end:
                raise ValueError("End date must be after start date")
                
            if hours_per_day < 1 or hours_per_day > 12:
                raise ValueError("Hours per day should be between 1 and 12")
                
            total_days = (end - start).days + 1
            study_plan = {
                "metadata": {
                    "start_date": start_date,
                    "end_date": end_date,
                    "total_days": total_days,
                    "hours_per_day": hours_per_day,
                    "weak_areas": weak_areas or [],
                    "optional_subject": optional_subject or "Not Selected"
                },
                "daily_plans": []
            }
            
            # Distribute subjects across the available days
            prelims_days = int(total_days * 0.4)
            mains_days = int(total_days * 0.5)
            interview_days = max(1, total_days - prelims_days - mains_days)
            
            current_date = start
            day_counter = 0
            
            # Generate Prelims plan
            for day in range(prelims_days):
                if current_date > end:
                    break
                    
                subjects = self._get_daily_subjects("Prelims", day, prelims_days)
                daily_plan = self._create_daily_entry(current_date, "Prelims", subjects, hours_per_day, weak_areas)
                study_plan["daily_plans"].append(daily_plan)
                current_date += timedelta(days=1)
                day_counter += 1
            
            # Generate Mains plan
            for day in range(mains_days):
                if current_date > end:
                    break
                    
                subjects = self._get_daily_subjects("Mains", day, mains_days)
                daily_plan = self._create_daily_entry(current_date, "Mains", subjects, hours_per_day, weak_areas)
                
                # Add optional subject if specified
                if optional_subject and day % 3 == 0:  # Every 3rd day
                    daily_plan["subjects"].append({
                        "name": f"Optional: {optional_subject}",
                        "hours": 2,
                        "resources": self._get_resources(optional_subject),
                        "mentorship": "Optional Subject Doubt Session"
                    })
                    
                study_plan["daily_plans"].append(daily_plan)
                current_date += timedelta(days=1)
                day_counter += 1
            
            # Generate Interview plan
            for day in range(interview_days):
                if current_date > end:
                    break
                    
                subjects = self._get_daily_subjects("Interview", day, interview_days)
                daily_plan = self._create_daily_entry(current_date, "Interview", subjects, hours_per_day, weak_areas)
                study_plan["daily_plans"].append(daily_plan)
                current_date += timedelta(days=1)
                day_counter += 1
            
            # Add revision days (every 7 days)
            for i, day_plan in enumerate(study_plan["daily_plans"]):
                if i > 0 and i % 7 == 0:
                    day_plan["subjects"].append({
                        "name": "Revision",
                        "hours": 1,
                        "resources": ["Previous Days Notes"],
                        "mentorship": "Weekly Revision with Mentor"
                    })
            
            return study_plan
            
        except Exception as e:
            raise ValueError(f"Error generating study plan: {str(e)}")
    
    def _get_daily_subjects(self, phase: str, day: int, total_days: int) -> List[str]:
        """Selects subjects for a given day based on phase and progress."""
        if phase == "Prelims":
            paper = "General Studies Paper I" if day % 2 == 0 else "General Studies Paper II (CSAT)"
            subjects = self.subjects["Prelims"][paper]
            return subjects[:3]  # 3 subjects per day for Prelims
        elif phase == "Mains":
            # Rotate through Mains papers
            papers = list(self.subjects["Mains"].keys())
            selected_paper = papers[day % len(papers)]
            return self.subjects["Mains"][selected_paper]
        else:  # Interview
            return self.subjects["Interview"]
    
    def _create_daily_entry(
        self, 
        date: datetime, 
        phase: str, 
        subjects: List[str], 
        hours: int, 
        weak_areas: Optional[List[str]] = None
    ) -> Dict:
        """Creates a daily study plan entry."""
        weak_areas = weak_areas or []
        date_str = date.strftime("%Y-%m-%d")
        daily_plan = {
            "date": date_str,
            "phase": phase,
            "subjects": []
        }
        
        hours_per_subject = max(1, hours // len(subjects))
        
        for subject in subjects:
            resources = self._get_resources(subject)
            mentorship = self._get_mentorship_suggestion(subject, phase)
            
            # Allocate more time to weak areas
            subject_hours = hours_per_subject * 2 if subject in weak_areas else hours_per_subject
            
            daily_plan["subjects"].append({
                "name": subject,
                "hours": subject_hours,
                "resources": resources,
                "mentorship": mentorship
            })
        
        return daily_plan
    
    def _get_resources(self, subject: str) -> List[str]:
        """Gets Shield IAS resources for a subject."""
        return self.shield_ias_resources.get(subject, ["Shield IAS Core Material"])
    
    def _get_mentorship_suggestion(self, subject: str, phase: str) -> str:
        """Provides mentorship suggestions based on subject and phase."""
        if phase == "Prelims":
            return f"Prelims Test Series Discussion - {subject}"
        elif phase == "Mains":
            return f"Mains Answer Writing Practice - {subject}"
        else:
            return "Mock Interview Session"
    
    def save_study_plan(self, study_plan: Dict,
