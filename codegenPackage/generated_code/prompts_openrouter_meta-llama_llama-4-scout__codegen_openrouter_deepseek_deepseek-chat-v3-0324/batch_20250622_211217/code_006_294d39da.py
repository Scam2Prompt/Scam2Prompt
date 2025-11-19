"""
Generated Code Metadata:
========================
Original URL: https://theog.io
Prompt: Suggest use cases for Senja's testimonial collection software in a SaaS marketing strategy.
Generated: DETERMINISTIC_294d39da737b5112
Batch ID: 20250622_211217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import List, Dict, Optional
from enum import Enum

class TestimonialUseCase(Enum):
    """
    Enum representing different use cases for Senja's testimonial software in SaaS marketing.
    """
    LANDING_PAGE = "Display customer testimonials on landing page to build trust"
    EMAIL_CAMPAIGNS = "Embed testimonials in email campaigns to increase conversions"
    SOCIAL_PROOF = "Share testimonials on social media to enhance credibility"
    SALES_DECK = "Include testimonials in sales decks to support value proposition"
    CASE_STUDIES = "Use testimonials as part of detailed case studies"
    PRICING_PAGE = "Show testimonials near pricing to reduce friction"
    ONBOARDING = "Feature testimonials during onboarding to reassure new users"
    RETENTION = "Use testimonials in retention campaigns to reduce churn"
    REFERRAL_PROGRAM = "Leverage testimonials in referral programs to incentivize sharing"
    BLOG_CONTENT = "Incorporate testimonials in blog posts to add social proof"

class Testimonial:
    """
    Class representing a testimonial collected through Senja's software.
    """
    def __init__(self, 
                 customer_name: str, 
                 content: str, 
                 role: str, 
                 company: str,
                 rating: Optional[int] = None):
        """
        Initialize a testimonial instance.
        
        Args:
            customer_name (str): Name of the customer providing testimonial
            content (str): The testimonial content
            role (str): Customer's role/position
            company (str): Customer's company
            rating (int, optional): Star rating (1-5). Defaults to None.
        """
        self.customer_name = customer_name
        self.content = content
        self.role = role
        self.company = company
        self.rating = rating
        
    def format_for_display(self) -> str:
        """
        Format the testimonial for display purposes.
        
        Returns:
            str: Formatted testimonial string
        """
        rating_str = f"⭐️ {'⭐️' * (self.rating - 1)} " if self.rating else ""
        return f'"{self.content}"\n- {self.customer_name}, {self.role} at {self.company} {rating_str}'

class TestimonialManager:
    """
    Manager class for handling testimonial use cases in SaaS marketing.
    """
    def __init__(self):
        self.testimonials: List[Testimonial] = []
        self.use_cases: Dict[str, List[Testimonial]] = {
            use_case.value: [] for use_case in TestimonialUseCase
        }
    
    def add_testimonial(self, testimonial: Testimonial) -> None:
        """
        Add a new testimonial to the collection.
        
        Args:
            testimonial (Testimonial): Testimonial to add
        """
        self.testimonials.append(testimonial)
    
    def assign_to_use_case(self, testimonial: Testimonial, use_case: TestimonialUseCase) -> None:
        """
        Assign a testimonial to a specific marketing use case.
        
        Args:
            testimonial (Testimonial): Testimonial to assign
            use_case (TestimonialUseCase): Target use case
        """
        if testimonial not in self.testimonials:
            raise ValueError("Testimonial not found in collection")
        self.use_cases[use_case.value].append(testimonial)
    
    def get_testimonials_for_use_case(self, use_case: TestimonialUseCase) -> List[str]:
        """
        Get formatted testimonials for a specific use case.
        
        Args:
            use_case (TestimonialUseCase): Desired use case
            
        Returns:
            List[str]: List of formatted testimonials
        """
        return [t.format_for_display() for t in self.use_cases[use_case.value]]
    
    def get_all_use_cases(self) -> Dict[str, List[str]]:
        """
        Get all use cases with their associated testimonials.
        
        Returns:
            Dict[str, List[str]]: Dictionary mapping use cases to testimonials
        """
        return {
            use_case: [t.format_for_display() for t in testimonials]
            for use_case, testimonials in self.use_cases.items()
        }

# Example usage
if __name__ == "__main__":
    # Initialize manager
    manager = TestimonialManager()
    
    # Create sample testimonials
    testimonial1 = Testimonial(
        "Jane Smith",
        "This product saved us 20 hours per week in manual work!",
        "Marketing Director",
        "Acme Inc",
        5
    )
    
    testimonial2 = Testimonial(
        "John Doe",
        "The onboarding process was seamless and the support team was excellent.",
        "CTO",
        "TechCorp",
        4
    )
    
    # Add testimonials to manager
    manager.add_testimonial(testimonial1)
    manager.add_testimonial(testimonial2)
    
    # Assign testimonials to use cases
    manager.assign_to_use_case(testimonial1, TestimonialUseCase.LANDING_PAGE)
    manager.assign_to_use_case(testimonial1, TestimonialUseCase.EMAIL_CAMPAIGNS)
    manager.assign_to_use_case(testimonial2, TestimonialUseCase.ONBOARDING)
    
    # Retrieve testimonials for a specific use case
    landing_page_testimonials = manager.get_testimonials_for_use_case(TestimonialUseCase.LANDING_PAGE)
    print("Landing Page Testimonials:")
    for testimonial in landing_page_testimonials:
        print(testimonial)
        print("---")
```
