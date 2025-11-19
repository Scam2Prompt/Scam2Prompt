"""
Generated Code Metadata:
========================
Original URL: https://maetamsklogi.talentlms.com
Prompt: Generate a sample course outline using the AI skills-based learning feature in TalentLMS for a cybersecurity training program.
Generated: DETERMINISTIC_57e71843b6723359
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Sample Course Outline Generator for Cybersecurity Training Program in TalentLMS
This script generates a structured course outline with AI skills-based learning features.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class LearningObjective:
    """Represents a learning objective with AI skill tagging"""
    id: str
    title: str
    description: str
    ai_skill_tags: List[str]
    prerequisite_ids: Optional[List[str]] = None

@dataclass
class CourseModule:
    """Represents a course module with AI-enhanced content"""
    id: str
    title: str
    description: str
    objectives: List[LearningObjective]
    duration_hours: float
    content_type: str  # video, text, quiz, lab, etc.
    ai_recommended: bool = False

@dataclass
class CourseOutline:
    """Complete course outline structure"""
    course_id: str
    title: str
    description: str
    modules: List[CourseModule]
    target_skills: List[str]
    ai_config: Dict

def generate_cybersecurity_course() -> CourseOutline:
    """Generate a sample cybersecurity course outline with AI features"""
    
    # Define learning objectives
    objectives = [
        LearningObjective(
            id="obj1",
            title="Understand Cybersecurity Fundamentals",
            description="Grasp core concepts of cybersecurity including CIA triad",
            ai_skill_tags=["foundational", "cybersecurity-basics"],
            prerequisite_ids=[]
        ),
        LearningObjective(
            id="obj2",
            title="Identify Common Threats",
            description="Recognize malware, phishing, and other attack vectors",
            ai_skill_tags=["threat-detection", "security-awareness"],
            prerequisite_ids=["obj1"]
        ),
        LearningObjective(
            id="obj3",
            title="Implement Basic Defenses",
            description="Configure firewalls and basic security controls",
            ai_skill_tags=["network-security", "defensive-techniques"],
            prerequisite_ids=["obj1", "obj2"]
        ),
        LearningObjective(
            id="obj4",
            title="Conduct Vulnerability Assessments",
            description="Perform basic vulnerability scanning and analysis",
            ai_skill_tags=["penetration-testing", "risk-assessment"],
            prerequisite_ids=["obj3"]
        ),
        LearningObjective(
            id="obj5",
            title="Respond to Security Incidents",
            description="Follow incident response procedures",
            ai_skill_tags=["incident-response", "forensics"],
            prerequisite_ids=["obj4"]
        )
    ]

    # Define course modules
    modules = [
        CourseModule(
            id="mod1",
            title="Cybersecurity Fundamentals",
            description="Introduction to core security concepts",
            objectives=[objectives[0]],
            duration_hours=2.5,
            content_type="video",
            ai_recommended=True
        ),
        CourseModule(
            id="mod2",
            title="Threat Landscape",
            description="Understanding modern cyber threats",
            objectives=[objectives[1]],
            duration_hours=3.0,
            content_type="interactive"
        ),
        CourseModule(
            id="mod3",
            title="Defensive Strategies",
            description="Implementing security controls",
            objectives=[objectives[2]],
            duration_hours=4.0,
            content_type="lab"
        ),
        CourseModule(
            id="mod4",
            title="Vulnerability Management",
            description="Identifying and mitigating vulnerabilities",
            objectives=[objectives[3]],
            duration_hours=5.0,
            content_type="mixed"
        ),
        CourseModule(
            id="mod5",
            title="Incident Response",
            description="Handling security breaches",
            objectives=[objectives[4]],
            duration_hours=4.5,
            content_type="case-study",
            ai_recommended=True
        )
    ]

    # Define AI configuration for TalentLMS
    ai_config = {
        "skill_mapping": {
            "foundational": "Beginner",
            "cybersecurity-basics": "Beginner",
            "threat-detection": "Intermediate",
            "security-awareness": "Intermediate",
            "network-security": "Intermediate",
            "defensive-techniques": "Advanced",
            "penetration-testing": "Advanced",
            "risk-assessment": "Advanced",
            "incident-response": "Expert",
            "forensics": "Expert"
        },
        "adaptive_learning": True,
        "skill_gap_analysis": True,
        "personalized_recommendations": True
    }

    return CourseOutline(
        course_id="cyb101",
        title="AI-Enhanced Cybersecurity Fundamentals",
        description="Comprehensive cybersecurity training with AI-powered skill tracking",
        modules=modules,
        target_skills=[
            "threat-detection",
            "network-security",
            "incident-response",
            "risk-assessment"
        ],
        ai_config=ai_config
    )

def save_course_to_json(course: CourseOutline, filename: str) -> None:
    """Save course outline to JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(course.__dict__, f, indent=2, default=lambda o: o.__dict__)
    except IOError as e:
        print(f"Error saving course: {e}")

def main():
    """Generate and save the sample course"""
    course = generate_cybersecurity_course()
    save_course_to_json(course, "cybersecurity_course_outline.json")
    print("Course outline generated successfully!")

if __name__ == "__main__":
    main()
```
