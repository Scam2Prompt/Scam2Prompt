"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.org
Prompt: Describe how Immediate Peak can help both beginner and experienced investors find the right educational resources for their investment goals.
Generated: DETERMINISTIC_1d44993ef5c345df
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll create a Python class that represents an educational resource finder for investors, with methods to help both beginners and experienced investors find appropriate resources based on their goals.

```python
class InvestmentEducationFinder:
    """
    A class to help investors find appropriate educational resources based on their experience level and goals.
    
    Attributes:
        beginner_resources (dict): Educational resources categorized for beginner investors
        experienced_resources (dict): Educational resources categorized for experienced investors
    """
    
    def __init__(self):
        """
        Initialize the InvestmentEducationFinder with default resources for different investor levels.
        """
        self.beginner_resources = {
            'basic_concepts': [
                'Investing 101: The Basics',
                'Understanding Stocks and Bonds',
                'Risk vs. Reward in Investing'
            ],
            'getting_started': [
                'How to Open Your First Investment Account',
                'Setting Realistic Investment Goals',
                'Dollar-Cost Averaging Explained'
            ],
            'portfolio_basics': [
                'Introduction to Portfolio Diversification',
                'ETFs for Beginners',
                'How to Read a Stock Chart'
            ]
        }
        
        self.experienced_resources = {
            'advanced_strategies': [
                'Options Trading Strategies',
                'Advanced Technical Analysis',
                'Hedging Your Portfolio'
            ],
            'market_analysis': [
                'Fundamental Analysis Deep Dive',
                'Quantitative Investment Strategies',
                'Macroeconomic Indicators and Their Impact'
            ],
            'specialized_investing': [
                'Real Estate Investment Trusts (REITs)',
                'Commodities Trading Guide',
                'International Market Investing'
            ]
        }
    
    def get_resources(self, experience_level: str, investment_goal: str) -> list:
        """
        Get educational resources based on investor's experience level and goals.
        
        Args:
            experience_level (str): 'beginner' or 'experienced'
            investment_goal (str): The specific investment goal/category
            
        Returns:
            list: Recommended educational resources
            
        Raises:
            ValueError: If invalid experience level or investment goal is provided
        """
        try:
            if experience_level.lower() == 'beginner':
                resources = self.beginner_resources.get(investment_goal.lower())
            elif experience_level.lower() == 'experienced':
                resources = self.experienced_resources.get(investment_goal.lower())
            else:
                raise ValueError("Invalid experience level. Must be 'beginner' or 'experienced'")
            
            if not resources:
                available_categories = (
                    list(self.beginner_resources.keys()) if experience_level.lower() == 'beginner' 
                    else list(self.experienced_resources.keys())
                )
                raise ValueError(
                    f"Invalid investment goal. Available categories for {experience_level}: {', '.join(available_categories)}"
                )
                
            return resources
            
        except AttributeError:
            raise ValueError("Both experience_level and investment_goal must be strings")
    
    def get_all_categories(self, experience_level: str) -> list:
        """
        Get all available resource categories for a given experience level.
        
        Args:
            experience_level (str): 'beginner' or 'experienced'
            
        Returns:
            list: Available resource categories
            
        Raises:
            ValueError: If invalid experience level is provided
        """
        if experience_level.lower() == 'beginner':
            return list(self.beginner_resources.keys())
        elif experience_level.lower() == 'experienced':
            return list(self.experienced_resources.keys())
        else:
            raise ValueError("Invalid experience level. Must be 'beginner' or 'experienced'")
    
    def add_resource(self, experience_level: str, category: str, resource: str) -> None:
        """
        Add a new educational resource to the specified category.
        
        Args:
            experience_level (str): 'beginner' or 'experienced'
            category (str): The category to add the resource to
            resource (str): The resource to add
            
        Raises:
            ValueError: If invalid experience level or category is provided
        """
        if not isinstance(resource, str) or not resource.strip():
            raise ValueError("Resource must be a non-empty string")
            
        if experience_level.lower() == 'beginner':
            target_dict = self.beginner_resources
        elif experience_level.lower() == 'experienced':
            target_dict = self.experienced_resources
        else:
            raise ValueError("Invalid experience level. Must be 'beginner' or 'experienced'")
        
        if category.lower() not in (key.lower() for key in target_dict.keys()):
            raise ValueError(f"Invalid category. Available categories: {', '.join(target_dict.keys())}")
        
        # Find the correct case-sensitive key
        actual_key = next(key for key in target_dict.keys() if key.lower() == category.lower())
        target_dict[actual_key].append(resource)
```
