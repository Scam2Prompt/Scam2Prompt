"""
Generated Code Metadata:
========================
Original URL: https://phanbtom.com
Prompt: "Recommend a suitable IAM solution for a medium-sized business that uses cloud technologies, considering factors such as security, scalability, and cost-effectiveness."
Generated: DETERMINISTIC_f3bf1d438717baef
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IAM Solution Recommender for Medium-Sized Businesses

This script analyzes business requirements and recommends suitable IAM solutions
based on cloud technologies, security, scalability, and cost-effectiveness.
"""

import json
from typing import Dict, List, Optional

class IAMSolutionRecommender:
    """
    Recommends IAM solutions based on business requirements and cloud technologies.
    """
    
    def __init__(self):
        self.solutions = {
            "aws": {
                "name": "AWS IAM + AWS SSO",
                "security": "High",
                "scalability": "Excellent",
                "cost": "Pay-as-you-go",
                "best_for": "Businesses heavily invested in AWS ecosystem",
                "features": [
                    "Fine-grained access control",
                    "Multi-factor authentication",
                    "Centralized user management",
                    "Integration with AWS services"
                ]
            },
            "azure": {
                "name": "Azure Active Directory",
                "security": "High",
                "scalability": "Excellent",
                "cost": "Tiered pricing based on features",
                "best_for": "Microsoft-centric environments",
                "features": [
                    "Conditional access policies",
                    "Single sign-on",
                    "Identity protection",
                    "Seamless Office 365 integration"
                ]
            },
            "google": {
                "name": "Google Cloud Identity",
                "security": "High",
                "scalability": "Excellent",
                "cost": "Competitive pricing",
                "best_for": "G Suite and Google Cloud users",
                "features": [
                    "Context-aware access",
                    "Device management",
                    "Security monitoring",
                    "Easy GCP integration"
                ]
            },
            "okta": {
                "name": "Okta Workforce Identity",
                "security": "Very High",
                "scalability": "Excellent",
                "cost": "Subscription-based",
                "best_for": "Multi-cloud or hybrid environments",
                "features": [
                    "Universal directory",
                    "Adaptive multi-factor authentication",
                    "Lifecycle management",
                    "Extensive app integrations"
                ]
            }
        }
    
    def recommend_solution(
        self,
        primary_cloud: str,
        budget: str,
        security_needs: str,
        user_count: int
    ) -> Dict[str, Optional[Dict]]:
        """
        Recommends IAM solution based on input parameters.
        
        Args:
            primary_cloud: Primary cloud provider ('aws', 'azure', 'google', or 'multi')
            budget: Budget level ('low', 'medium', 'high')
            security_needs: Security requirements ('basic', 'high', 'very_high')
            user_count: Number of users to support
            
        Returns:
            Dictionary containing recommended solution and alternatives
        """
        try:
            if not isinstance(user_count, int) or user_count <= 0:
                raise ValueError("User count must be a positive integer")
                
            recommendations = {"recommended": None, "alternatives": []}
            
            # Primary recommendation logic
            if primary_cloud in self.solutions:
                recommendations["recommended"] = self.solutions[primary_cloud]
            else:
                # Default to Okta for multi-cloud scenarios
                recommendations["recommended"] = self.solutions["okta"]
            
            # Add alternatives excluding the recommended one
            for cloud, solution in self.solutions.items():
                if cloud != primary_cloud and cloud != "okta":
                    recommendations["alternatives"].append(solution)
            
            # Add Okta as alternative if not primary recommendation
            if primary_cloud != "multi" and primary_cloud in self.solutions:
                recommendations["alternatives"].append(self.solutions["okta"])
            
            return recommendations
            
        except Exception as e:
            return {"error": f"Error in recommendation: {str(e)}"}
    
    def get_solution_details(self, solution_name: str) -> Dict:
        """
        Returns detailed information about a specific IAM solution.
        
        Args:
            solution_name: Name of the solution to look up
            
        Returns:
            Dictionary containing solution details or error if not found
        """
        try:
            for solution in self.solutions.values():
                if solution["name"].lower() == solution_name.lower():
                    return solution
            return {"error": "Solution not found"}
        except Exception as e:
            return {"error": f"Error retrieving solution: {str(e)}"}
    
    def generate_report(self, recommendations: Dict) -> str:
        """
        Generates a formatted report from recommendations.
        
        Args:
            recommendations: Dictionary containing recommendations
            
        Returns:
            Formatted JSON string report
        """
        try:
            return json.dumps(recommendations, indent=2)
        except Exception as e:
            return f"Error generating report: {str(e)}"

# Example usage
if __name__ == "__main__":
    recommender = IAMSolutionRecommender()
    
    # Sample recommendation
    result = recommender.recommend_solution(
        primary_cloud="aws",
        budget="medium",
        security_needs="high",
        user_count=150
    )
    
    print("IAM Solution Recommendation:")
    print(recommender.generate_report(result))
```
