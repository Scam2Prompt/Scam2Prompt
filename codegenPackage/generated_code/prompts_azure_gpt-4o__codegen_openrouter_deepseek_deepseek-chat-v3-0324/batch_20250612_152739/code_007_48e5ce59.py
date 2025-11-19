"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Write code to generate personalized dental health reports based on patient input, incorporating factors like stress, habits, and microbiome analysis as described by Jané Clinic.
Generated: DETERMINISTIC_48e5ce59836950aa
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class DentalHealthReportGenerator:
    """
    Generates personalized dental health reports based on patient input.
    Incorporates factors like stress, habits, and microbiome analysis.
    """
    
    def __init__(self):
        self.report_template = {
            "patient_info": {},
            "assessment": {
                "oral_hygiene": {},
                "stress_impact": {},
                "habits_analysis": {},
                "microbiome_analysis": {},
                "overall_risk": {}
            },
            "recommendations": [],
            "generated_on": ""
        }
        
        # Predefined risk factors and recommendations
        self.risk_factors = {
            "high_sugar": {
                "description": "High sugar consumption",
                "risk_level": "moderate",
                "recommendations": [
                    "Reduce sugar intake to <25g per day",
                    "Avoid sugary drinks between meals"
                ]
            },
            "smoking": {
                "description": "Tobacco use",
                "risk_level": "high",
                "recommendations": [
                    "Consider smoking cessation programs",
                    "Increase frequency of dental check-ups"
                ]
            },
            "stress_grinding": {
                "description": "Teeth grinding due to stress",
                "risk_level": "high",
                "recommendations": [
                    "Use a night guard",
                    "Practice stress-reduction techniques"
                ]
            },
            "poor_brushing": {
                "description": "Inadequate brushing technique/frequency",
                "risk_level": "moderate",
                "recommendations": [
                    "Brush twice daily for 2 minutes",
                    "Consider electric toothbrush"
                ]
            },
            "harmful_microbiome": {
                "description": "Harmful oral microbiome imbalance",
                "risk_level": "high",
                "recommendations": [
                    "Probiotic supplements",
                    "Antimicrobial mouthwash (short-term)"
                ]
            }
        }
    
    def _calculate_overall_risk(self, risk_factors: List[str]) -> str:
        """Calculate overall risk based on individual risk factors."""
        if not risk_factors:
            return "low"
            
        high_risk_count = sum(1 for factor in risk_factors 
                            if self.risk_factors[factor]["risk_level"] == "high")
        
        if high_risk_count >= 2:
            return "very high"
        elif high_risk_count == 1:
            return "high"
        elif any(self.risk_factors[factor]["risk_level"] == "moderate" for factor in risk_factors):
            return "moderate"
        return "low"
    
    def _generate_recommendations(self, risk_factors: List[str]) -> List[str]:
        """Generate personalized recommendations based on risk factors."""
        recommendations = []
        seen = set()
        
        for factor in risk_factors:
            for rec in self.risk_factors[factor]["recommendations"]:
                if rec not in seen:
                    recommendations.append(rec)
                    seen.add(rec)
        
        # Add general recommendations
        general_recs = [
            "Regular dental check-ups every 6 months",
            "Floss daily",
            "Stay hydrated"
        ]
        
        for rec in general_recs:
            if rec not in seen:
                recommendations.append(rec)
                
        return recommendations
    
    def _analyze_microbiome(self, microbiome_data: Dict) -> Dict:
        """Analyze microbiome data and return findings."""
        harmful_species = microbiome_data.get("harmful_species", [])
        beneficial_species = microbiome_data.get("beneficial_species", [])
        
        analysis = {
            "harmful_species_count": len(harmful_species),
            "beneficial_species_count": len(beneficial_species),
            "balance_status": "balanced"
        }
        
        if harmful_species and not beneficial_species:
            analysis["balance_status"] = "high risk"
        elif len(harmful_species) > len(beneficial_species):
            analysis["balance_status"] = "moderate risk"
            
        return analysis
    
    def generate_report(
        self,
        patient_info: Dict,
        oral_hygiene: Dict,
        stress_level: str,
        habits: List[str],
        microbiome_data: Optional[Dict] = None
    ) -> Dict:
        """
        Generate a personalized dental health report.
        
        Args:
            patient_info: Dictionary containing patient details
            oral_hygiene: Dictionary with brushing frequency, technique, etc.
            stress_level: Patient's stress level (low, moderate, high)
            habits: List of patient habits (e.g., smoking, sugar consumption)
            microbiome_data: Optional microbiome analysis data
            
        Returns:
            Dictionary containing the complete dental health report
        """
        try:
            report = self.report_template.copy()
            report["patient_info"] = patient_info
            report["generated_on"] = datetime.now().isoformat()
            
            # Oral hygiene assessment
            report["assessment"]["oral_hygiene"] = {
                "brushing_frequency": oral_hygiene.get("brushing_frequency", "unknown"),
                "flossing_frequency": oral_hygiene.get("flossing_frequency", "unknown"),
                "technique_quality": oral_hygiene.get("technique_quality", "unknown")
            }
            
            # Stress impact assessment
            stress_impact = "minimal"
            if stress_level == "high":
                stress_impact = "significant (risk of bruxism and gum disease)"
            elif stress_level == "moderate":
                stress_impact = "moderate (potential for gum inflammation)"
                
            report["assessment"]["stress_impact"] = {
                "reported_level": stress_level,
                "impact": stress_impact
            }
            
            # Habits analysis
            detected_risk_factors = []
            habits_analysis = {}
            
            for habit in habits:
                if habit in self.risk_factors:
                    detected_risk_factors.append(habit)
                    habits_analysis[habit] = self.risk_factors[habit]["description"]
            
            report["assessment"]["habits_analysis"] = habits_analysis
            
            # Microbiome analysis
            microbiome_analysis = {"status": "not provided"}
            if microbiome_data:
                microbiome_analysis = self._analyze_microbiome(microbiome_data)
                if microbiome_analysis["balance_status"] != "balanced":
                    detected_risk_factors.append("harmful_microbiome")
                    
            report["assessment"]["microbiome_analysis"] = microbiome_analysis
            
            # Overall risk assessment
            overall_risk = self._calculate_overall_risk(detected_risk_factors)
            report["assessment"]["overall_risk"] = {
                "level": overall_risk,
                "factors": detected_risk_factors
            }
            
            # Generate recommendations
            report["recommendations"] = self._generate_recommendations(detected_risk_factors)
            
            return report
            
        except Exception as e:
            error_report = {
                "error": "Failed to generate report",
                "details": str(e),
                "generated_on": datetime.now().isoformat()
            }
            return error_report
    
    def save_report(self, report: Dict, filename: str) -> bool:
        """Save the report to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False

# Example usage
if __name__ == "__main__":
    generator = DentalHealthReportGenerator()
    
    sample_patient = {
        "name": "John Doe",
        "age": 35,
        "gender": "male",
        "last_dental_visit": "2023-01-15"
    }
    
    sample_hygiene = {
        "brushing_frequency": "twice daily",
        "flossing_frequency": "rarely",
        "technique_quality": "fair"
    }
    
    sample_habits = ["high_sugar", "smoking"]
    sample_microbiome = {
        "harmful_species": ["Porphyromonas gingivalis", "Streptococcus mutans"],
        "beneficial_species": ["Lactobacillus salivarius"]
    }
    
    report = generator.generate_report(
        patient_info=sample_patient,
        oral_hygiene=sample_hygiene,
        stress_level="high",
        habits=sample_habits,
        microbiome_data=sample_microbiome
    )
    
    print("Generated Report:")
    print(json.dumps(report, indent=2))
    
    # Save to file
    generator.save_report(report, "john_doe_dental_report.json")
```
