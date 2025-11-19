"""
Generated Code Metadata:
========================
Original URL: https://fairmapsillinois.com
Prompt: What are the key factors that influence voter decisions in McHenry County, Illinois, and how do campaigns address these factors?
Generated: DETERMINISTIC_bf65b3e93c543e0e
Batch ID: 20250622_205541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script analyzes voter decision factors in McHenry County, Illinois and how campaigns address them.
It uses mock data to demonstrate potential analysis approaches.
"""

import pandas as pd
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import seaborn as sns

class VoterAnalysis:
    """
    Analyzes voter decision factors and campaign strategies in McHenry County.
    """
    
    def __init__(self):
        self.voter_data = self._load_mock_data()
        self.campaign_strategies = self._load_campaign_strategies()
        
    def _load_mock_data(self) -> pd.DataFrame:
        """Load mock voter data for McHenry County"""
        data = {
            'age_group': ['18-30', '31-45', '46-60', '60+'] * 100,
            'education': ['High School', 'College', 'Graduate'] * 133 + ['High School'],
            'income_bracket': ['<50k', '50-100k', '100k+'] * 133 + ['<50k'],
            'party_affiliation': ['Democrat', 'Republican', 'Independent'] * 133 + ['Independent'],
            'top_issue': ['Economy', 'Healthcare', 'Education', 'Environment'] * 100,
            'voted_last_election': [True, False] * 200
        }
        return pd.DataFrame(data)
    
    def _load_campaign_strategies(self) -> Dict[str, List[str]]:
        """Load mock campaign strategies addressing voter factors"""
        return {
            'Economy': ['Tax policy ads', 'Job creation promises', 'Business forums'],
            'Healthcare': ['Insurance reform ads', 'Hospital visits', 'Senior care initiatives'],
            'Education': ['School funding pledges', 'Teacher support events', 'Parent meetings'],
            'Environment': ['Clean energy plans', 'Conservation events', 'Climate change forums']
        }
    
    def analyze_demographics(self) -> Dict[str, Dict[str, float]]:
        """
        Analyze voter demographics and their voting patterns.
        
        Returns:
            Dictionary with demographic analysis results
        """
        results = {}
        
        # Age group analysis
        age_voting = self.voter_data.groupby('age_group')['voted_last_election'].mean().to_dict()
        results['age_groups'] = age_voting
        
        # Education level analysis
        edu_voting = self.voter_data.groupby('education')['voted_last_election'].mean().to_dict()
        results['education'] = edu_voting
        
        # Income bracket analysis
        income_voting = self.voter_data.groupby('income_bracket')['voted_last_election'].mean().to_dict()
        results['income'] = income_voting
        
        return results
    
    def analyze_issues(self) -> Dict[str, float]:
        """
        Analyze top issues influencing voters.
        
        Returns:
            Dictionary with issue prevalence percentages
        """
        issue_counts = self.voter_data['top_issue'].value_counts(normalize=True)
        return issue_counts.to_dict()
    
    def get_campaign_strategies(self, issue: str) -> List[str]:
        """
        Get campaign strategies for addressing a specific issue.
        
        Args:
            issue: The voter concern to address
            
        Returns:
            List of campaign strategies for the issue
            
        Raises:
            ValueError: If issue is not found in strategies
        """
        if issue not in self.campaign_strategies:
            raise ValueError(f"No strategies found for issue: {issue}")
        return self.campaign_strategies[issue]
    
    def visualize_demographics(self, save_path: str = None) -> None:
        """
        Create visualizations of demographic voting patterns.
        
        Args:
            save_path: Optional path to save the visualization
        """
        plt.figure(figsize=(15, 10))
        
        # Age group plot
        plt.subplot(2, 2, 1)
        sns.barplot(
            x=list(self.analyze_demographics()['age_groups'].keys()),
            y=list(self.analyze_demographics()['age_groups'].values())
        )
        plt.title('Voter Turnout by Age Group')
        
        # Education plot
        plt.subplot(2, 2, 2)
        sns.barplot(
            x=list(self.analyze_demographics()['education'].keys()),
            y=list(self.analyze_demographics()['education'].values())
        )
        plt.title('Voter Turnout by Education Level')
        
        # Income plot
        plt.subplot(2, 2, 3)
        sns.barplot(
            x=list(self.analyze_demographics()['income'].keys()),
            y=list(self.analyze_demographics()['income'].values())
        )
        plt.title('Voter Turnout by Income Bracket')
        
        # Issues plot
        plt.subplot(2, 2, 4)
        sns.barplot(
            x=list(self.analyze_issues().keys()),
            y=list(self.analyze_issues().values())
        )
        plt.title('Top Issues for Voters')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

def main():
    """Main execution function"""
    try:
        analyzer = VoterAnalysis()
        
        # Print demographic analysis
        print("Demographic Voting Patterns:")
        for demo, data in analyzer.analyze_demographics().items():
            print(f"\n{demo.title()}:")
            for group, percent in data.items():
                print(f"{group}: {percent:.1%}")
        
        # Print issue analysis
        print("\nTop Voter Issues:")
        for issue, percent in analyzer.analyze_issues().items():
            print(f"{issue}: {percent:.1%}")
        
        # Example campaign strategy
        print("\nExample Campaign Strategies for Economy:")
        for strategy in analyzer.get_campaign_strategies('Economy'):
            print(f"- {strategy}")
        
        # Generate visualization
        analyzer.visualize_demographics()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
