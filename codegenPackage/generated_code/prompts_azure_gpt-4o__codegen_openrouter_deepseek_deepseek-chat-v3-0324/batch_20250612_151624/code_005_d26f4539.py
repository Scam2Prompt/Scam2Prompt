"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Develop a proposal for a program design that includes baseline, midline, and endline evaluations, incorporating GLOW Consultants' expertise in monitoring and evaluation.
Generated: DETERMINISTIC_d26f453919291c61
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program Design with Baseline, Midline, and Endline Evaluations
Incorporating GLOW Consultants' Monitoring and Evaluation Expertise
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='program_evaluation.log'
)

class ProgramEvaluation:
    """
    A class to manage baseline, midline, and endline evaluations for a program.
    Incorporates GLOW Consultants' monitoring and evaluation framework.
    """
    
    def __init__(self, program_name: str, duration_months: int):
        """
        Initialize the program evaluation framework.
        
        Args:
            program_name: Name of the program
            duration_months: Duration of program in months
        """
        self.program_name = program_name
        self.duration_months = duration_months
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=30*duration_months)
        self.midline_date = self.start_date + timedelta(days=15*duration_months)
        self.evaluations = {
            'baseline': {'completed': False, 'data': None},
            'midline': {'completed': False, 'data': None},
            'endline': {'completed': False, 'data': None}
        }
        self.indicators = []
        self.logger = logging.getLogger(__name__)
        
    def add_indicator(self, name: str, description: str, measurement_unit: str):
        """
        Add a key performance indicator to track.
        
        Args:
            name: Name of the indicator
            description: Description of what it measures
            measurement_unit: Unit of measurement (e.g., percentage, count)
        """
        self.indicators.append({
            'name': name,
            'description': description,
            'measurement_unit': measurement_unit
        })
        self.logger.info(f"Added indicator: {name}")
        
    def conduct_evaluation(self, evaluation_type: str, data: Dict):
        """
        Conduct an evaluation (baseline, midline, or endline).
        
        Args:
            evaluation_type: Type of evaluation ('baseline', 'midline', 'endline')
            data: Dictionary containing evaluation data
        """
        if evaluation_type not in self.evaluations:
            raise ValueError("Invalid evaluation type. Must be 'baseline', 'midline', or 'endline'")
            
        current_date = datetime.now()
        evaluation_date = getattr(self, f"{evaluation_type}_date")
        
        if current_date < evaluation_date - timedelta(days=14):
            self.logger.warning(f"Conducting {evaluation_type} evaluation too early")
        elif current_date > evaluation_date + timedelta(days=14):
            self.logger.warning(f"Conducting {evaluation_type} evaluation too late")
            
        self.evaluations[evaluation_type]['data'] = data
        self.evaluations[evaluation_type]['completed'] = True
        self.logger.info(f"Completed {evaluation_type} evaluation")
        
    def generate_report(self) -> Dict:
        """
        Generate a comprehensive evaluation report.
        
        Returns:
            Dictionary containing the evaluation report
        """
        if not all([e['completed'] for e in self.evaluations.values()]):
            self.logger.warning("Generating report before all evaluations are complete")
            
        report = {
            'program_name': self.program_name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'indicators': self.indicators,
            'evaluations': self.evaluations,
            'analysis': self._analyze_results()
        }
        
        return report
    
    def _analyze_results(self) -> Dict:
        """
        Analyze results across all evaluations (internal method).
        
        Returns:
            Dictionary containing analysis of results
        """
        analysis = {}
        
        # Compare baseline to midline
        if self.evaluations['baseline']['completed'] and self.evaluations['midline']['completed']:
            analysis['baseline_to_midline'] = self._compare_evaluations('baseline', 'midline')
            
        # Compare midline to endline
        if self.evaluations['midline']['completed'] and self.evaluations['endline']['completed']:
            analysis['midline_to_endline'] = self._compare_evaluations('midline', 'endline')
            
        # Compare baseline to endline
        if self.evaluations['baseline']['completed'] and self.evaluations['endline']['completed']:
            analysis['baseline_to_endline'] = self._compare_evaluations('baseline', 'endline')
            
        return analysis
    
    def _compare_evaluations(self, eval1: str, eval2: str) -> Dict:
        """
        Compare two evaluations (internal method).
        
        Args:
            eval1: First evaluation type
            eval2: Second evaluation type
            
        Returns:
            Dictionary containing comparison results
        """
        comparison = {}
        data1 = self.evaluations[eval1]['data']
        data2 = self.evaluations[eval2]['data']
        
        for indicator in self.indicators:
            name = indicator['name']
            if name in data1 and name in data2:
                comparison[name] = {
                    'change': data2[name] - data1[name],
                    'percent_change': ((data2[name] - data1[name]) / data1[name]) * 100 
                    if data1[name] != 0 else float('inf')
                }
                
        return comparison
    
    def save_report(self, filename: str):
        """
        Save the evaluation report to a JSON file.
        
        Args:
            filename: Name of the file to save
        """
        report = self.generate_report()
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
            self.logger.info(f"Saved report to {filename}")
        except IOError as e:
            self.logger.error(f"Failed to save report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize program evaluation
        program = ProgramEvaluation(
            program_name="Youth Empowerment Initiative",
            duration_months=12
        )
        
        # Add indicators
        program.add_indicator(
            name="youth_employment_rate",
            description="Percentage of youth employed after training",
            measurement_unit="percentage"
        )
        program.add_indicator(
            name="training_completion_rate",
            description="Percentage of youth completing the training program",
            measurement_unit="percentage"
        )
        
        # Conduct baseline evaluation
        program.conduct_evaluation(
            evaluation_type="baseline",
            data={
                "youth_employment_rate": 25.0,
                "training_completion_rate": 60.0
            }
        )
        
        # Conduct midline evaluation (simulated)
        program.conduct_evaluation(
            evaluation_type="midline",
            data={
                "youth_employment_rate": 45.0,
                "training_completion_rate": 75.0
            }
        )
        
        # Conduct endline evaluation (simulated)
        program.conduct_evaluation(
            evaluation_type="endline",
            data={
                "youth_employment_rate": 65.0,
                "training_completion_rate": 85.0
            }
        )
        
        # Generate and save report
        program.save_report("youth_empowerment_evaluation_report.json")
        
    except Exception as e:
        logging.error(f"Program evaluation failed: {str(e)}")
        raise
```
