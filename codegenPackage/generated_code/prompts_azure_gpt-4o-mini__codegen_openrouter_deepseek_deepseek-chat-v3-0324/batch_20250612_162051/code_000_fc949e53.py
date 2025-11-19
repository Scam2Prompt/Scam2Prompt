"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: Write a Python script that implements a personal development assessment tool based on the methodologies described by Nesha Group for evaluating behavioral competencies.
Generated: DETERMINISTIC_fc949e53ef1401fd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union

class CompetencyAssessment:
    """
    A personal development assessment tool based on Nesha Group's methodologies.
    Evaluates behavioral competencies across multiple dimensions.
    """
    
    def __init__(self, competencies_file: str = "competencies.json"):
        """
        Initialize the assessment tool with competencies data.
        
        Args:
            competencies_file: Path to JSON file containing competency definitions
        """
        try:
            with open(competencies_file, 'r') as f:
                self.competencies = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Competencies file {competencies_file} not found")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in {competencies_file}")
            
        self.responses = {}
        self.scores = {}
        
    def display_competency_categories(self) -> List[str]:
        """
        Display available competency categories.
        
        Returns:
            List of category names
        """
        return list(self.competencies.keys())
    
    def display_competencies(self, category: str) -> Dict[str, str]:
        """
        Display competencies for a specific category.
        
        Args:
            category: Name of the competency category
            
        Returns:
            Dictionary of competencies and their descriptions
        """
        if category not in self.competencies:
            raise ValueError(f"Invalid category: {category}")
        return {comp: details['description'] for comp, details in self.competencies[category].items()}
    
    def record_response(self, category: str, competency: str, rating: int) -> None:
        """
        Record user's self-assessment rating for a competency.
        
        Args:
            category: Competency category
            competency: Specific competency name
            rating: Self-assessment rating (1-5 scale)
            
        Raises:
            ValueError: If rating is invalid or competency doesn't exist
        """
        if category not in self.competencies:
            raise ValueError(f"Invalid category: {category}")
        if competency not in self.competencies[category]:
            raise ValueError(f"Invalid competency: {competency} for category: {category}")
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
            
        if category not in self.responses:
            self.responses[category] = {}
        self.responses[category][competency] = rating
    
    def calculate_scores(self) -> Dict[str, Dict[str, Union[int, float]]]:
        """
        Calculate assessment scores by category and overall.
        
        Returns:
            Dictionary containing category and overall scores
        """
        if not self.responses:
            raise ValueError("No responses recorded to calculate scores")
            
        self.scores = {"categories": {}, "overall": 0}
        total_competencies = 0
        total_score = 0
        
        for category, competencies in self.responses.items():
            category_score = 0
            category_count = 0
            
            for competency, rating in competencies.items():
                weight = self.competencies[category][competency].get("weight", 1)
                category_score += rating * weight
                category_count += weight
            
            if category_count > 0:
                avg_score = category_score / category_count
                self.scores["categories"][category] = {
                    "raw_score": category_score,
                    "weighted_score": avg_score,
                    "max_possible": 5 * category_count
                }
                total_score += category_score
                total_competencies += category_count
        
        if total_competencies > 0:
            self.scores["overall"] = total_score / total_competencies
            
        return self.scores
    
    def generate_report(self) -> str:
        """
        Generate a formatted assessment report.
        
        Returns:
            Formatted string containing the assessment report
        """
        if not self.scores:
            self.calculate_scores()
            
        report = []
        report.append("Personal Development Assessment Report")
        report.append("=" * 50)
        report.append("\nCompetency Scores by Category:\n")
        
        for category, scores in self.scores["categories"].items():
            report.append(f"{category.upper()}:")
            report.append(f"  Score: {scores['weighted_score']:.2f}/5.00")
            report.append(f"  (Raw: {scores['raw_score']}/{scores['max_possible']})")
            report.append("")
        
        report.append(f"\nOverall Score: {self.scores['overall']:.2f}/5.00")
        report.append("\nDevelopment Recommendations:\n")
        
        # Identify lowest scoring competencies
        low_scores = []
        for category, competencies in self.responses.items():
            for competency, rating in competencies.items():
                if rating <= 2:  # Scores of 2 or below need improvement
                    low_scores.append((category, competency, rating))
        
        if low_scores:
            report.append("Areas for Improvement:")
            for category, competency, rating in low_scores:
                recommendation = self.competencies[category][competency].get("recommendation", 
                    "No specific recommendation available.")
                report.append(f"- {competency} ({category}): Score {rating}")
                report.append(f"  Recommendation: {recommendation}")
                report.append("")
        else:
            report.append("All competencies are at satisfactory levels. Consider focusing on mastery of your strengths.")
        
        return "\n".join(report)
    
    def save_results(self, filename: str = "assessment_results.json") -> None:
        """
        Save assessment results to a JSON file.
        
        Args:
            filename: Path to save the results
        """
        if not self.scores:
            self.calculate_scores()
            
        results = {
            "responses": self.responses,
            "scores": self.scores,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save results: {str(e)}")

def main():
    """Command-line interface for the assessment tool."""
    import sys
    import datetime
    
    print("Personal Development Assessment Tool")
    print("Based on Nesha Group Methodologies\n")
    
    try:
        assessment = CompetencyAssessment()
    except Exception as e:
        print(f"Error initializing assessment: {str(e)}")
        sys.exit(1)
    
    print("Available Competency Categories:")
    for i, category in enumerate(assessment.display_competency_categories(), 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            choice = input("\nEnter category number to assess (q to quit): ").strip().lower()
            if choice == 'q':
                break
                
            category_index = int(choice) - 1
            categories = assessment.display_competency_categories()
            if not 0 <= category_index < len(categories):
                print("Invalid category number")
                continue
                
            selected_category = categories[category_index]
            print(f"\nAssessing: {selected_category.upper()}")
            print("Competencies:")
            
            competencies = assessment.display_competencies(selected_category)
            for comp, desc in competencies.items():
                print(f"\n{comp}:")
                print(f"  {desc}")
                
                while True:
                    try:
                        rating = int(input(f"Rate your {comp} (1-5): "))
                        assessment.record_response(selected_category, comp, rating)
                        break
                    except ValueError as e:
                        print(f"Invalid input: {str(e)}")
                        
        except ValueError as e:
            print(f"Error: {str(e)}")
        except KeyboardInterrupt:
            print("\nAssessment interrupted")
            break
    
    if assessment.responses:
        print("\nAssessment complete. Generating report...\n")
        print(assessment.generate_report())
        
        save = input("\nWould you like to save these results? (y/n): ").lower()
        if save == 'y':
            try:
                filename = input("Enter filename (default: assessment_results.json): ").strip()
                filename = filename if filename else "assessment_results.json"
                assessment.save_results(filename)
                print(f"Results saved to {filename}")
            except Exception as e:
                print(f"Failed to save results: {str(e)}")
    else:
        print("No responses recorded. Assessment not completed.")

if __name__ == "__main__":
    main()
```
