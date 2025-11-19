"""
Generated Code Metadata:
========================
Original URL: https://lensamaluku.com
Prompt: Create a detailed overview of the community activities during Idul Adha in Buru Selatan, including the distribution of sacrificial meat and the involvement of local authorities.
Generated: DETERMINISTIC_4820e42198082a33
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates a detailed report on Idul Adha community activities in Buru Selatan,
including meat distribution and local authority involvement.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class CommunityActivity:
    """Represents a community activity during Idul Adha"""
    
    def __init__(self, name: str, location: str, organizer: str):
        self.name = name
        self.location = location
        self.organizer = organizer
        self.participants: List[str] = []
        self.meat_distribution: Dict[str, int] = {}  # {recipient: kg_of_meat}
        self.authorities_involved: List[str] = []
        self.timestamp = datetime.now().isoformat()
    
    def add_participant(self, name: str) -> None:
        """Add a participant to the activity"""
        if name not in self.participants:
            self.participants.append(name)
    
    def distribute_meat(self, recipient: str, amount_kg: int) -> None:
        """Record meat distribution to a recipient"""
        if amount_kg <= 0:
            raise ValueError("Amount must be positive")
        self.meat_distribution[recipient] = amount_kg
    
    def involve_authority(self, authority_name: str) -> None:
        """Record involvement of a local authority"""
        if authority_name not in self.authorities_involved:
            self.authorities_involved.append(authority_name)
    
    def to_dict(self) -> Dict:
        """Convert activity data to dictionary for serialization"""
        return {
            "name": self.name,
            "location": self.location,
            "organizer": self.organizer,
            "participants": self.participants,
            "meat_distribution": self.meat_distribution,
            "authorities_involved": self.authorities_involved,
            "timestamp": self.timestamp
        }

class IdulAdhaReportGenerator:
    """Generates reports on Idul Adha activities in Buru Selatan"""
    
    def __init__(self):
        self.activities: List[CommunityActivity] = []
    
    def add_activity(self, activity: CommunityActivity) -> None:
        """Add a community activity to the report"""
        self.activities.append(activity)
    
    def generate_report(self) -> Dict:
        """Generate comprehensive report of all activities"""
        report = {
            "region": "Buru Selatan",
            "report_date": datetime.now().isoformat(),
            "total_activities": len(self.activities),
            "activities": [activity.to_dict() for activity in self.activities],
            "summary": self._generate_summary()
        }
        return report
    
    def _generate_summary(self) -> Dict:
        """Generate summary statistics"""
        total_meat = 0
        total_recipients = 0
        all_authorities = set()
        all_participants = set()
        
        for activity in self.activities:
            total_meat += sum(activity.meat_distribution.values())
            total_recipients += len(activity.meat_distribution)
            all_authorities.update(activity.authorities_involved)
            all_participants.update(activity.participants)
        
        return {
            "total_meat_distributed_kg": total_meat,
            "total_recipients": total_recipients,
            "total_authorities_involved": len(all_authorities),
            "total_participants": len(all_participants)
        }
    
    def save_report(self, filename: str) -> None:
        """Save report to JSON file"""
        report = self.generate_report()
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving report: {e}")

def sample_data_generator() -> IdulAdhaReportGenerator:
    """Generate sample data for demonstration"""
    report = IdulAdhaReportGenerator()
    
    # Activity 1
    activity1 = CommunityActivity(
        name="Qurban at Masjid Al-Hidayah",
        location="Namrole",
        organizer="Majelis Taklim Al-Hidayah"
    )
    activity1.add_participant("Ahmad Basri")
    activity1.add_participant("Siti Aminah")
    activity1.distribute_meat("Family A", 5)
    activity1.distribute_meat("Family B", 3)
    activity1.involve_authority("Kepala Desa Namrole")
    report.add_activity(activity1)
    
    # Activity 2
    activity2 = CommunityActivity(
        name="Qurban Bersama Kecamatan",
        location="Fena Leisela",
        organizer="Pemerintah Kecamatan Fena Leisela"
    )
    activity2.add_participant("Bupati Buru Selatan")
    activity2.add_participant("Kapolres Buru Selatan")
    activity2.distribute_meat("Panti Asuhan", 15)
    activity2.distribute_meat("Rumah Sakit", 10)
    activity2.involve_authority("Bupati Buru Selatan")
    activity2.involve_authority("Kapolres Buru Selatan")
    report.add_activity(activity2)
    
    return report

if __name__ == "__main__":
    # Generate sample report
    report_generator = sample_data_generator()
    
    # Display report
    report = report_generator.generate_report()
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    # Save to file
    report_generator.save_report("idul_adha_buru_selatan_report.json")
```
