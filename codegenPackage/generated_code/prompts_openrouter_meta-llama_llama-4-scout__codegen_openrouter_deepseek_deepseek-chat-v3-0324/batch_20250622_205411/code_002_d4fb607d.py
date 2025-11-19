"""
Generated Code Metadata:
========================
Original URL: https://mintsolutions.io
Prompt: Create a customer journey map (CJM) for a new product launch, including research, product development, and testing, and provide recommendations for improvement.
Generated: DETERMINISTIC_d4fb607d51656edd
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Customer Journey Map (CJM) Analyzer for Product Launch

This script models and analyzes the customer journey for a new product launch,
covering research, development, and testing phases. It provides visualization
and recommendations for improvement.
"""

import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum, auto
from typing import List, Dict, Optional
from dataclasses import dataclass

class PhaseType(Enum):
    """Enum representing different phases of the customer journey"""
    AWARENESS = auto()
    RESEARCH = auto()
    DEVELOPMENT = auto()
    TESTING = auto()
    PURCHASE = auto()
    POST_PURCHASE = auto()

@dataclass
class JourneyPhase:
    """Data class representing a single phase in the customer journey"""
    phase_type: PhaseType
    name: str
    description: str
    touchpoints: List[str]
    pain_points: List[str]
    duration_days: int
    satisfaction_score: float  # 0-10 scale

class CustomerJourneyMap:
    """Main class representing the customer journey map"""
    
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.phases: List[JourneyPhase] = []
        self.recommendations: List[str] = []
    
    def add_phase(self, phase: JourneyPhase) -> None:
        """Add a phase to the journey map"""
        self.phases.append(phase)
    
    def analyze_journey(self) -> Dict[str, float]:
        """Analyze the journey and return key metrics"""
        if not self.phases:
            raise ValueError("No phases added to the journey map")
            
        total_duration = sum(phase.duration_days for phase in self.phases)
        avg_satisfaction = sum(phase.satisfaction_score for phase in self.phases) / len(self.phases)
        pain_point_count = sum(len(phase.pain_points) for phase in self.phases)
        
        return {
            "total_duration_days": total_duration,
            "average_satisfaction": avg_satisfaction,
            "total_pain_points": pain_point_count
        }
    
    def generate_recommendations(self) -> None:
        """Generate improvement recommendations based on pain points"""
        self.recommendations = []
        
        for phase in self.phases:
            if phase.pain_points:
                self.recommendations.append(
                    f"Improve {phase.name} phase by addressing: {', '.join(phase.pain_points)}"
                )
        
        # Add general recommendations
        metrics = self.analyze_journey()
        if metrics["average_satisfaction"] < 7:
            self.recommendations.append(
                "Increase overall satisfaction by improving key touchpoints"
            )
        if metrics["total_duration_days"] > 90:
            self.recommendations.append(
                "Streamline the journey to reduce total time-to-purchase"
            )
    
    def visualize_journey(self) -> None:
        """Create visualization of the customer journey"""
        if not self.phases:
            raise ValueError("No phases to visualize")
            
        phase_names = [phase.name for phase in self.phases]
        satisfaction_scores = [phase.satisfaction_score for phase in self.phases]
        durations = [phase.duration_days for phase in self.phases]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Satisfaction plot
        ax1.bar(phase_names, satisfaction_scores, color='skyblue')
        ax1.set_title(f'Customer Satisfaction Scores for {self.product_name}')
        ax1.set_ylabel('Satisfaction Score (0-10)')
        ax1.set_ylim(0, 10)
        
        # Duration plot
        ax2.bar(phase_names, durations, color='lightgreen')
        ax2.set_title('Phase Duration')
        ax2.set_ylabel('Days')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self) -> str:
        """Generate a comprehensive report of the journey"""
        self.generate_recommendations()
        metrics = self.analyze_journey()
        
        report = [
            f"Customer Journey Analysis Report for {self.product_name}",
            "=" * 50,
            f"Total Journey Duration: {metrics['total_duration_days']} days",
            f"Average Satisfaction: {metrics['average_satisfaction']:.1f}/10",
            f"Total Pain Points Identified: {metrics['total_pain_points']}",
            "\nPhases Overview:",
            "-" * 20
        ]
        
        for phase in self.phases:
            report.append(
                f"{phase.name} ({phase.duration_days} days): "
                f"Satisfaction {phase.satisfaction_score}/10"
            )
        
        report.extend(["\nRecommendations:", "-" * 20])
        report.extend(self.recommendations)
        
        return "\n".join(report)

def create_sample_journey(product_name: str) -> CustomerJourneyMap:
    """Create a sample customer journey for demonstration"""
    cjm = CustomerJourneyMap(product_name)
    
    # Add phases
    cjm.add_phase(JourneyPhase(
        phase_type=PhaseType.AWARENESS,
        name="Market Research",
        description="Initial customer discovery and needs assessment",
        touchpoints=["Surveys", "Focus groups", "Competitor analysis"],
        pain_points=["Limited participant diversity", "Vague requirements"],
        duration_days=30,
        satisfaction_score=6.5
    ))
    
    cjm.add_phase(JourneyPhase(
        phase_type=PhaseType.DEVELOPMENT,
        name="Product Development",
        description="Building the product based on research findings",
        touchpoints=["Prototypes", "Feature demos", "Developer updates"],
        pain_points=["Feature creep", "Communication gaps"],
        duration_days=60,
        satisfaction_score=7.0
    ))
    
    cjm.add_phase(JourneyPhase(
        phase_type=PhaseType.TESTING,
        name="Beta Testing",
        description="Real-world testing with select customers",
        touchpoints=["Beta releases", "Feedback forms", "Support channels"],
        pain_points=["Bug reporting friction", "Slow response times"],
        duration_days=45,
        satisfaction_score=6.0
    ))
    
    return cjm

if __name__ == "__main__":
    try:
        # Example usage
        product_name = "NextGen Productivity Suite"
        cjm = create_sample_journey(product_name)
        
        # Analyze and visualize
        print(cjm.generate_report())
        cjm.visualize_journey()
        
    except Exception as e:
        print(f"Error analyzing customer journey: {str(e)}")
```
