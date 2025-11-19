"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Illustrate how to use a library to generate a scorecard report for evaluating business advocacy efforts, similar to the IACI Scorecard mentioned on their site.
Generated: DETERMINISTIC_e5aa88232788f2ed
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Optional

class AdvocacyScorecard:
    """
    A class to generate a business advocacy scorecard report.
    """
    
    def __init__(self, company_name: str, year: int):
        """
        Initialize the scorecard with company name and evaluation year.
        
        Args:
            company_name (str): Name of the company being evaluated
            year (int): Year of evaluation
        """
        self.company_name = company_name
        self.year = year
        self.categories: Dict[str, float] = {}
        self.weights: Dict[str, float] = {}
        self.max_scores: Dict[str, float] = {}
        self.notes: Dict[str, str] = {}
        
    def add_category(self, category: str, weight: float, max_score: float, note: str = "") -> None:
        """
        Add an evaluation category to the scorecard.
        
        Args:
            category (str): Name of the evaluation category
            weight (float): Weight of this category (0-1)
            max_score (float): Maximum possible score for this category
            note (str, optional): Additional notes about the category
        """
        if weight < 0 or weight > 1:
            raise ValueError("Weight must be between 0 and 1")
        if max_score <= 0:
            raise ValueError("Max score must be positive")
            
        self.categories[category] = 0.0
        self.weights[category] = weight
        self.max_scores[category] = max_score
        self.notes[category] = note
        
    def set_score(self, category: str, score: float) -> None:
        """
        Set the score for a specific category.
        
        Args:
            category (str): Category to score
            score (float): Score to assign
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found")
        if score < 0 or score > self.max_scores[category]:
            raise ValueError(f"Score must be between 0 and {self.max_scores[category]}")
            
        self.categories[category] = score
        
    def calculate_total_score(self) -> float:
        """
        Calculate the weighted total score.
        
        Returns:
            float: Weighted total score
        """
        if not self.categories:
            raise ValueError("No categories have been added")
            
        total = 0.0
        for category, score in self.categories.items():
            weighted_score = (score / self.max_scores[category]) * self.weights[category]
            total += weighted_score
            
        return total * 100  # Convert to percentage
    
    def generate_report(self, output_file: Optional[str] = None) -> pd.DataFrame:
        """
        Generate a scorecard report as a DataFrame and optionally save to file.
        
        Args:
            output_file (str, optional): Path to save report as CSV. Defaults to None.
            
        Returns:
            pd.DataFrame: The generated report
        """
        report_data = []
        for category in self.categories:
            normalized_score = (self.categories[category] / self.max_scores[category]) * 100
            report_data.append({
                "Category": category,
                "Score": self.categories[category],
                "Max Score": self.max_scores[category],
                "Normalized Score (%)": normalized_score,
                "Weight": self.weights[category],
                "Weighted Contribution": normalized_score * self.weights[category],
                "Notes": self.notes[category]
            })
            
        df = pd.DataFrame(report_data)
        total_score = self.calculate_total_score()
        
        # Add summary row
        summary_row = pd.DataFrame([{
            "Category": "TOTAL",
            "Score": "",
            "Max Score": "",
            "Normalized Score (%)": total_score,
            "Weight": sum(self.weights.values()),
            "Weighted Contribution": total_score,
            "Notes": f"Scorecard for {self.company_name} - {self.year}"
        }])
        
        df = pd.concat([df, summary_row], ignore_index=True)
        
        if output_file:
            df.to_csv(output_file, index=False)
            
        return df
    
    def plot_scorecard(self, output_file: Optional[str] = None) -> None:
        """
        Generate a visual representation of the scorecard.
        
        Args:
            output_file (str, optional): Path to save the plot. Defaults to None.
        """
        df = self.generate_report()
        df = df[df["Category"] != "TOTAL"]  # Exclude summary row
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Scores by category
        df.plot.bar(x="Category", y="Normalized Score (%)", ax=ax1, color='skyblue')
        ax1.set_title(f"{self.company_name} Advocacy Scores by Category ({self.year})")
        ax1.set_ylabel("Score (%)")
        ax1.set_ylim(0, 110)
        ax1.axhline(100, color='red', linestyle='--', alpha=0.3)
        
        # Weighted contributions
        df.plot.bar(x="Category", y="Weighted Contribution", ax=ax2, color='lightgreen')
        ax2.set_title("Weighted Contributions to Total Score")
        ax2.set_ylabel("Weighted Score")
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file)
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize scorecard
        scorecard = AdvocacyScorecard(company_name="TechCorp", year=2023)
        
        # Add evaluation categories
        scorecard.add_category("Policy Engagement", 0.3, 50, "Participation in policy discussions")
        scorecard.add_category("Legislative Support", 0.25, 40, "Support for key legislation")
        scorecard.add_category("Regulatory Compliance", 0.2, 30, "Adherence to regulations")
        scorecard.add_category("Industry Collaboration", 0.15, 20, "Partnerships with industry groups")
        scorecard.add_category("Public Advocacy", 0.1, 10, "Public statements and campaigns")
        
        # Set scores
        scorecard.set_score("Policy Engagement", 42)
        scorecard.set_score("Legislative Support", 35)
        scorecard.set_score("Regulatory Compliance", 28)
        scorecard.set_score("Industry Collaboration", 18)
        scorecard.set_score("Public Advocacy", 9)
        
        # Generate and display report
        report = scorecard.generate_report("techcorp_scorecard_2023.csv")
        print(report)
        
        # Generate visualization
        scorecard.plot_scorecard("techcorp_scorecard_2023.png")
        
    except Exception as e:
        print(f"Error generating scorecard: {str(e)}")
```
