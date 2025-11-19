"""
Generated Code Metadata:
========================
Original URL: https://healthwithdiagnostics.com
Prompt: Develop a program that models heart attack risk factors, inspired by the "Dil Se Fit" heart health information on "Health With Diagnostics."
Generated: DETERMINISTIC_b27a1e683fbb00af
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Heart Attack Risk Factor Model
Inspired by "Dil Se Fit" heart health information from "Health With Diagnostics"

This program calculates an individual's risk of heart attack based on various health factors.
"""

import sys
from enum import Enum
from typing import Dict, List, Optional, Tuple


class RiskLevel(Enum):
    """Enum representing different risk levels for heart attack."""
    LOW = "Low Risk"
    MODERATE = "Moderate Risk"
    HIGH = "High Risk"
    VERY_HIGH = "Very High Risk"


class HeartRiskCalculator:
    """
    A calculator for determining heart attack risk based on multiple health factors.
    """
    
    def __init__(self):
        self.factors = {
            'age': {
                'description': 'Age in years',
                'ranges': [(0, 30, 0), (31, 45, 1), (46, 60, 2), (61, 120, 3)]
            },
            'blood_pressure': {
                'description': 'Blood Pressure (mmHg)',
                'ranges': [
                    ('Normal', (90, 120), (60, 80), 0),
                    ('Elevated', (121, 129), (60, 80), 1),
                    ('Hypertension Stage 1', (130, 139), (80, 89), 2),
                    ('Hypertension Stage 2', (140, 180), (90, 120), 3),
                    ('Hypertensive Crisis', (181, 300), (121, 300), 4)
                ]
            },
            'cholesterol': {
                'description': 'Total Cholesterol (mg/dL)',
                'ranges': [(0, 200, 0), (201, 239, 1), (240, 300, 2)]
            },
            'hdl': {
                'description': 'HDL Cholesterol (mg/dL)',
                'ranges': [(60, 100, 0), (40, 59, 1), (0, 39, 2)]
            },
            'smoking': {
                'description': 'Smoking status',
                'options': [('Non-smoker', 0), ('Former smoker', 1), ('Current smoker', 2)]
            },
            'diabetes': {
                'description': 'Diabetes status',
                'options': [('No diabetes', 0), ('Prediabetes', 1), ('Diabetes', 2)]
            },
            'physical_activity': {
                'description': 'Physical activity level',
                'options': [
                    ('Active (5+ days/week)', 0),
                    ('Moderately active (3-4 days/week)', 1),
                    ('Sedentary (<2 days/week)', 2)
                ]
            },
            'family_history': {
                'description': 'Family history of heart disease',
                'options': [('No', 0), ('One relative', 1), ('Multiple relatives', 2)]
            },
            'bmi': {
                'description': 'Body Mass Index (BMI)',
                'ranges': [(0, 18.5, 0), (18.5, 24.9, 0), (25, 29.9, 1), (30, 100, 2)]
            }
        }
    
    def calculate_risk_score(self, user_data: Dict[str, float]) -> Tuple[int, RiskLevel]:
        """
        Calculate the total risk score based on user data.
        
        Args:
            user_data: Dictionary containing user's health metrics
            
        Returns:
            Tuple of (total_score, risk_level)
        """
        total_score = 0
        
        try:
            # Age
            age = user_data.get('age', 0)
            total_score += self._get_score('age', age)
            
            # Blood Pressure
            systolic = user_data.get('systolic_bp', 0)
            diastolic = user_data.get('diastolic_bp', 0)
            total_score += self._get_blood_pressure_score(systolic, diastolic)
            
            # Cholesterol
            cholesterol = user_data.get('cholesterol', 0)
            total_score += self._get_score('cholesterol', cholesterol)
            
            # HDL
            hdl = user_data.get('hdl', 0)
            total_score += self._get_score('hdl', hdl)
            
            # Smoking
            smoking = user_data.get('smoking', 0)
            total_score += self._get_option_score('smoking', smoking)
            
            # Diabetes
            diabetes = user_data.get('diabetes', 0)
            total_score += self._get_option_score('diabetes', diabetes)
            
            # Physical Activity
            activity = user_data.get('physical_activity', 0)
            total_score += self._get_option_score('physical_activity', activity)
            
            # Family History
            family_history = user_data.get('family_history', 0)
            total_score += self._get_option_score('family_history', family_history)
            
            # BMI
            bmi = user_data.get('bmi', 0)
            total_score += self._get_score('bmi', bmi)
            
            # Determine risk level
            risk_level = self._determine_risk_level(total_score)
            
            return total_score, risk_level
            
        except Exception as e:
            print(f"Error calculating risk score: {str(e)}", file=sys.stderr)
            raise
    
    def _get_score(self, factor: str, value: float) -> int:
        """Get score for a factor with numeric ranges."""
        ranges = self.factors[factor]['ranges']
        for range_def in ranges:
            if len(range_def) == 3:  # Single value range
                min_val, max_val, score = range_def
                if min_val <= value <= max_val:
                    return score
            elif len(range_def) == 4:  # BP range (handled separately)
                continue
        return 0
    
    def _get_blood_pressure_score(self, systolic: float, diastolic: float) -> int:
        """Get score for blood pressure factor."""
        for range_def in self.factors['blood_pressure']['ranges']:
            _, (s_min, s_max), (d_min, d_max), score = range_def
            if (s_min <= systolic <= s_max) and (d_min <= diastolic <= d_max):
                return score
        return 0
    
    def _get_option_score(self, factor: str, option_index: int) -> int:
        """Get score for a factor with discrete options."""
        options = self.factors[factor]['options']
        if 0 <= option_index < len(options):
            return options[option_index][1]
        return 0
    
    def _determine_risk_level(self, score: int) -> RiskLevel:
        """Determine risk level based on total score."""
        if score <= 5:
            return RiskLevel.LOW
        elif 6 <= score <= 10:
            return RiskLevel.MODERATE
        elif 11 <= score <= 15:
            return RiskLevel.HIGH
        else:
            return RiskLevel.VERY_HIGH
    
    def get_factors_info(self) -> Dict[str, Dict]:
        """Return information about all risk factors."""
        return self.factors


def get_user_input() -> Dict[str, float]:
    """Collect user input for risk calculation."""
    print("Heart Attack Risk Assessment\n")
    print("Please provide the following information:\n")
    
    calculator = HeartRiskCalculator()
    factors_info = calculator.get_factors_info()
    user_data = {}
    
    try:
        # Age
        user_data['age'] = float(input(f"{factors_info['age']['description']}: "))
        
        # Blood Pressure
        print("\nBlood Pressure:")
        user_data['systolic_bp'] = float(input("  Systolic (upper number): "))
        user_data['diastolic_bp'] = float(input("  Diastolic (lower number): "))
        
        # Cholesterol
        user_data['cholesterol'] = float(input(f"\n{factors_info['cholesterol']['description']}: "))
        user_data['hdl'] = float(input(f"{factors_info['hdl']['description']}: "))
        
        # BMI
        user_data['bmi'] = float(input(f"\n{factors_info['bmi']['description']}: "))
        
        # Lifestyle factors
        print("\nLifestyle Factors:")
        for factor in ['smoking', 'diabetes', 'physical_activity', 'family_history']:
            info = factors_info[factor]
            print(f"\n{info['description']}:")
            for i, (desc, _) in enumerate(info['options']):
                print(f"  {i}. {desc}")
            selection = int(input("  Enter your choice (number): "))
            user_data[factor] = selection
        
        return user_data
    
    except ValueError as e:
        print(f"Invalid input: {str(e)}", file=sys.stderr)
        sys.exit(1)


def display_results(score: int, risk_level: RiskLevel) -> None:
    """Display the risk assessment results."""
    print("\n\n=== Heart Attack Risk Assessment Results ===")
    print(f"Total Risk Score: {score}")
    print(f"Risk Level: {risk_level.value
