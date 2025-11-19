"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: What are some examples of UX design case studies for healthcare wearables, specifically onboarding experiences?
Generated: DETERMINISTIC_df709edbf4d1b3d3
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script simulates a healthcare wearable onboarding UX case study analysis
# It includes mock data and visualizations for common onboarding patterns

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict, Optional

class OnboardingCaseStudy:
    """
    Represents a UX case study for healthcare wearable onboarding
    """
    
    def __init__(self, study_name: str, device_type: str, user_group: str):
        self.study_name = study_name
        self.device_type = device_type
        self.user_group = user_group
        self.steps = []
        self.dropoff_rates = {}
        self.success_metrics = {}
        
    def add_onboarding_step(self, step_name: str, description: str, 
                           dropoff_rate: float, duration_sec: float) -> None:
        """Adds an onboarding step with metrics"""
        self.steps.append({
            'name': step_name,
            'description': description,
            'dropoff_rate': dropoff_rate,
            'duration': duration_sec
        })
        self.dropoff_rates[step_name] = dropoff_rate
        
    def set_success_metrics(self, completion_rate: float, 
                          time_to_complete: float, 
                          satisfaction_score: float) -> None:
        """Sets overall success metrics for the onboarding"""
        self.success_metrics = {
            'completion_rate': completion_rate,
            'time_to_complete': time_to_complete,
            'satisfaction_score': satisfaction_score
        }
        
    def visualize_dropoff(self) -> None:
        """Generates a visualization of dropoff rates"""
        if not self.steps:
            raise ValueError("No onboarding steps added")
            
        step_names = [step['name'] for step in self.steps]
        dropoffs = [step['dropoff_rate'] for step in self.steps]
        
        plt.figure(figsize=(10, 6))
        plt.plot(step_names, dropoffs, marker='o', linestyle='-', color='r')
        plt.title(f"Onboarding Dropoff Rates - {self.study_name}")
        plt.xlabel("Onboarding Step")
        plt.ylabel("Dropoff Rate (%)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    def generate_report(self) -> Dict:
        """Generates a summary report of the case study"""
        return {
            'study_name': self.study_name,
            'device_type': self.device_type,
            'user_group': self.user_group,
            'steps': self.steps,
            'success_metrics': self.success_metrics
        }

# Example case studies
def create_diabetes_monitor_case() -> OnboardingCaseStudy:
    """Creates a case study for a diabetes monitoring wearable"""
    case = OnboardingCaseStudy(
        "Diabetes Monitor Onboarding v2.1",
        "Continuous Glucose Monitor",
        "Type 2 Diabetes Patients"
    )
    
    case.add_onboarding_step(
        "Device Pairing",
        "Bluetooth connection to smartphone app",
        12.5,
        45.2
    )
    case.add_onboarding_step(
        "Sensor Application",
        "Applying sensor to body",
        8.2,
        120.0
    )
    case.add_onboarding_step(
        "Calibration",
        "Initial glucose level calibration",
        15.7,
        180.5
    )
    case.add_onboarding_step(
        "Notification Setup",
        "Configuring alerts and thresholds",
        5.1,
        90.3
    )
    
    case.set_success_metrics(
        completion_rate=82.3,
        time_to_complete=436.0,
        satisfaction_score=4.2
    )
    
    return case

def create_cardiac_monitor_case() -> OnboardingCaseStudy:
    """Creates a case study for a cardiac monitoring wearable"""
    case = OnboardingCaseStudy(
        "Cardiac Monitor Onboarding v1.5",
        "ECG Smartwatch",
        "Post-Cardiac Event Patients"
    )
    
    case.add_onboarding_step(
        "Wearable Fit",
        "Adjusting strap and positioning",
        18.3,
        75.0
    )
    case.add_onboarding_step(
        "App Registration",
        "Creating user profile",
        22.1,
        150.0
    )
    case.add_onboarding_step(
        "ECG Tutorial",
        "Learning to take readings",
        9.7,
        210.0
    )
    case.add_onboarding_step(
        "Emergency Contacts",
        "Setting up emergency response",
        14.2,
        60.0
    )
    
    case.set_success_metrics(
        completion_rate=76.8,
        time_to_complete=495.0,
        satisfaction_score=4.0
    )
    
    return case

# Main analysis function
def analyze_case_studies() -> List[Dict]:
    """Analyzes and compares multiple onboarding case studies"""
    cases = [
        create_diabetes_monitor_case(),
        create_cardiac_monitor_case()
    ]
    
    results = []
    for case in cases:
        print(f"\nAnalyzing: {case.study_name}")
        print(f"Device: {case.device_type}")
        print(f"User Group: {case.user_group}")
        
        # Visualize dropoff
        try:
            case.visualize_dropoff()
        except ValueError as e:
            print(f"Visualization error: {e}")
        
        # Generate report
        report = case.generate_report()
        results.append(report)
        
    return results

if __name__ == "__main__":
    analyze_case_studies()
```
