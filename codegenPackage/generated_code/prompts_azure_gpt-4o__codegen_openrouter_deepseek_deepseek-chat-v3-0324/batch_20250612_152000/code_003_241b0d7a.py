"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Create a script to analyze the potential benefits of joint ventures between Indian aerospace companies and foreign manufacturers, as described by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_241b0d7a17a85c83
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple

class JointVentureAnalyzer:
    """
    Analyzes potential benefits of joint ventures between Indian aerospace companies and foreign manufacturers.
    """
    
    def __init__(self, indian_companies: List[Dict], foreign_companies: List[Dict]):
        """
        Initialize the analyzer with company data.
        
        Args:
            indian_companies: List of dictionaries containing Indian company data
            foreign_companies: List of dictionaries containing foreign company data
        """
        self.indian_companies = pd.DataFrame(indian_companies)
        self.foreign_companies = pd.DataFrame(foreign_companies)
        self.validate_data()
        
    def validate_data(self) -> None:
        """
        Validate input data for required fields.
        Raises ValueError if required fields are missing.
        """
        required_fields = ['name', 'revenue', 'technology_level', 'market_share', 'specialization']
        
        for df in [self.indian_companies, self.foreign_companies]:
            missing_fields = [field for field in required_fields if field not in df.columns]
            if missing_fields:
                raise ValueError(f"Missing required fields: {missing_fields}")
    
    def calculate_compatibility_score(self, indian_company: pd.Series, foreign_company: pd.Series) -> float:
        """
        Calculate compatibility score between two companies.
        
        Args:
            indian_company: Series representing Indian company
            foreign_company: Series representing foreign company
            
        Returns:
            Compatibility score (0-1)
        """
        # Technology complementarity (higher is better)
        tech_score = 1 - abs(indian_company['technology_level'] - foreign_company['technology_level']) / 10
        
        # Market synergy (higher is better)
        market_score = (indian_company['market_share'] + foreign_company['market_share']) / 200
        
        # Specialization match (1 if matching, 0.5 if partially matching, 0 otherwise)
        specialization_score = 0
        indian_spec = set(indian_company['specialization'].lower().split(','))
        foreign_spec = set(foreign_company['specialization'].lower().split(','))
        
        if indian_spec & foreign_spec:
            specialization_score = 1
        elif any(x in y for x in indian_spec for y in foreign_spec):
            specialization_score = 0.5
            
        # Weighted average of scores
        return 0.4 * tech_score + 0.3 * market_score + 0.3 * specialization_score
    
    def find_best_matches(self, top_n: int = 5) -> pd.DataFrame:
        """
        Find top N best matches between Indian and foreign companies.
        
        Args:
            top_n: Number of top matches to return
            
        Returns:
            DataFrame containing top matches with compatibility scores
        """
        matches = []
        
        for _, indian_row in self.indian_companies.iterrows():
            for _, foreign_row in self.foreign_companies.iterrows():
                score = self.calculate_compatibility_score(indian_row, foreign_row)
                matches.append({
                    'indian_company': indian_row['name'],
                    'foreign_company': foreign_row['name'],
                    'compatibility_score': score,
                    'potential_revenue': (indian_row['revenue'] + foreign_row['revenue']) * score
                })
                
        matches_df = pd.DataFrame(matches)
        return matches_df.sort_values('compatibility_score', ascending=False).head(top_n)
    
    def analyze_joint_venture_benefits(self, indian_company_name: str, foreign_company_name: str) -> Dict:
        """
        Analyze potential benefits of a specific joint venture.
        
        Args:
            indian_company_name: Name of Indian company
            foreign_company_name: Name of foreign company
            
        Returns:
            Dictionary containing analysis results
        """
        try:
            indian_company = self.indian_companies[self.indian_companies['name'] == indian_company_name].iloc[0]
            foreign_company = self.foreign_companies[self.foreign_companies['name'] == foreign_company_name].iloc[0]
        except IndexError:
            raise ValueError("One or both companies not found in dataset")
            
        score = self.calculate_compatibility_score(indian_company, foreign_company)
        potential_revenue = (indian_company['revenue'] + foreign_company['revenue']) * score
        
        return {
            'indian_company': indian_company_name,
            'foreign_company': foreign_company_name,
            'compatibility_score': score,
            'potential_revenue': potential_revenue,
            'technology_synergy': 1 - abs(indian_company['technology_level'] - foreign_company['technology_level']) / 10,
            'market_synergy': (indian_company['market_share'] + foreign_company['market_share']) / 200,
            'specialization_match': self._get_specialization_match(indian_company, foreign_company)
        }
    
    def _get_specialization_match(self, indian_company: pd.Series, foreign_company: pd.Series) -> str:
        """
        Helper method to get specialization match description.
        """
        indian_spec = set(indian_company['specialization'].lower().split(','))
        foreign_spec = set(foreign_company['specialization'].lower().split(','))
        
        if indian_spec & foreign_spec:
            return "Exact match"
        elif any(x in y for x in indian_spec for y in foreign_spec):
            return "Partial match"
        return "No match"
    
    def generate_visual_report(self, output_file: str = 'joint_venture_analysis.png') -> None:
        """
        Generate visual report of top matches.
        
        Args:
            output_file: Path to save the visualization
        """
        top_matches = self.find_best_matches()
        
        plt.figure(figsize=(12, 8))
        
        # Bar plot of compatibility scores
        plt.subplot(2, 1, 1)
        plt.barh(
            top_matches['indian_company'] + " + " + top_matches['foreign_company'],
            top_matches['compatibility_score'],
            color='skyblue'
        )
        plt.title('Top Joint Venture Matches by Compatibility Score')
        plt.xlabel('Compatibility Score (0-1)')
        plt.xlim(0, 1)
        
        # Bar plot of potential revenue
        plt.subplot(2, 1, 2)
        plt.barh(
            top_matches['indian_company'] + " + " + top_matches['foreign_company'],
            top_matches['potential_revenue'],
            color='lightgreen'
        )
        plt.title('Potential Revenue from Joint Venture (in million USD)')
        plt.xlabel('Revenue (million USD)')
        
        plt.tight_layout()
        plt.savefig(output_file)
        plt.close()

# Example usage
if __name__ == "__main__":
    # Sample data (in a real scenario, this would come from a database or API)
    indian_companies = [
        {
            'name': 'Aanjaneya Aerodynamics Pvt. Ltd.',
            'revenue': 150,  # in million USD
            'technology_level': 7,  # 1-10 scale
            'market_share': 12,  # percentage
            'specialization': 'Aerostructures,Composites'
        },
        {
            'name': 'Hindustan Aeronautics Ltd.',
            'revenue': 3000,
            'technology_level': 8,
            'market_share': 45,
            'specialization': 'Aircraft,Helicopters,Defense'
        }
    ]
    
    foreign_companies = [
        {
            'name': 'Boeing',
            'revenue': 60000,
            'technology_level': 9,
            'market_share': 40,
            'specialization': 'Commercial Aircraft,Defense,Space'
        },
        {
            'name': 'Airbus',
            'revenue': 55000,
            'technology_level': 9,
            'market_share': 38,
            'specialization': 'Commercial Aircraft,Helicopters,Defense'
        },
        {
            'name': 'Lockheed Martin',
            'revenue': 65000,
            'technology_level': 10,
            'market_share': 35,
            'specialization': 'Defense,Aerospace,Advanced Technology'
        }
    ]
    
    try:
        analyzer = JointVentureAnalyzer(indian_companies, foreign_companies)
        
        # Get top matches
        top_matches = analyzer.find_best_matches()
        print("Top Joint Venture Matches:")
        print(top_matches.to_string(index=False))
        
        # Analyze specific joint venture
        analysis = analyzer.analyze_joint_venture_benefits(
            'Aanjaneya Aerodynamics Pvt. Ltd.',
            'Boeing'
        )
        print("\nDetailed Analysis:")
        for k, v in analysis.items():
