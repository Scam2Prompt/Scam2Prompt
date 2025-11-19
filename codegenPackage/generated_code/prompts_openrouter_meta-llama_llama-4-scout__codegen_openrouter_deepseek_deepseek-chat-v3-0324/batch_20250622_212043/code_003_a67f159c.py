"""
Generated Code Metadata:
========================
Original URL: https://itab.com
Prompt: "Generate a case study on how ITAB's solutions improved operational cost and customer experience for a grocery retailer."
Generated: DETERMINISTIC_a67f159c5e0e7562
Batch ID: 20250622_212043
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study Generator: ITAB's Solutions for Grocery Retailer

This script generates a case study demonstrating how ITAB's solutions improved
operational costs and customer experience for a fictional grocery retailer.
"""

import json
from datetime import datetime

class CaseStudyGenerator:
    """Generates professional case studies for ITAB solutions."""
    
    def __init__(self):
        """Initialize with default case study template."""
        self.template = {
            "title": "ITAB Solutions Transform Grocery Retail Operations",
            "subtitle": "How {retailer_name} Achieved {cost_reduction}% Cost Reduction and Enhanced Customer Experience",
            "introduction": {
                "challenge": "{retailer_name}, a {retailer_size} grocery retailer, faced challenges with {challenges}.",
                "solution": "ITAB implemented {solutions} to address these issues."
            },
            "results": {
                "operational_costs": {
                    "before": "€{cost_before}",
                    "after": "€{cost_after}",
                    "reduction": "{cost_reduction}%"
                },
                "customer_experience": {
                    "metrics": [
                        {"name": "Checkout Speed", "improvement": "{checkout_improvement}%"},
                        {"name": "Product Availability", "improvement": "{availability_improvement}%"},
                        {"name": "Customer Satisfaction", "improvement": "{satisfaction_improvement}%"}
                    ]
                },
                "timeframe": "{timeframe} months"
            },
            "testimonial": "\"ITAB's solutions helped us reduce costs while improving our customers' shopping experience.\" - {retailer_contact}",
            "conclusion": "This case demonstrates how ITAB's retail solutions can drive operational efficiency and customer satisfaction simultaneously.",
            "generated_on": datetime.now().strftime("%Y-%m-%d")
        }
    
    def generate_case_study(self, retailer_data):
        """
        Generate a case study based on provided retailer data.
        
        Args:
            retailer_data (dict): Dictionary containing retailer-specific data
            
        Returns:
            dict: Complete case study with all placeholders filled
        """
        try:
            case_study = self.template.copy()
            
            # Replace placeholders with actual data
            case_study["subtitle"] = case_study["subtitle"].format(
                retailer_name=retailer_data["retailer_name"],
                cost_reduction=retailer_data["cost_reduction"]
            )
            
            case_study["introduction"]["challenge"] = case_study["introduction"]["challenge"].format(
                retailer_name=retailer_data["retailer_name"],
                retailer_size=retailer_data["retailer_size"],
                challenges=retailer_data["challenges"]
            )
            
            case_study["introduction"]["solution"] = case_study["introduction"]["solution"].format(
                solutions=retailer_data["solutions"]
            )
            
            case_study["results"]["operational_costs"]["before"] = case_study["results"]["operational_costs"]["before"].format(
                cost_before=retailer_data["cost_before"]
            )
            
            case_study["results"]["operational_costs"]["after"] = case_study["results"]["operational_costs"]["after"].format(
                cost_after=retailer_data["cost_after"]
            )
            
            case_study["results"]["operational_costs"]["reduction"] = case_study["results"]["operational_costs"]["reduction"].format(
                cost_reduction=retailer_data["cost_reduction"]
            )
            
            for metric in case_study["results"]["customer_experience"]["metrics"]:
                if metric["name"] == "Checkout Speed":
                    metric["improvement"] = metric["improvement"].format(
                        checkout_improvement=retailer_data["checkout_improvement"]
                    )
                elif metric["name"] == "Product Availability":
                    metric["improvement"] = metric["improvement"].format(
                        availability_improvement=retailer_data["availability_improvement"]
                    )
                elif metric["name"] == "Customer Satisfaction":
                    metric["improvement"] = metric["improvement"].format(
                        satisfaction_improvement=retailer_data["satisfaction_improvement"]
                    )
            
            case_study["results"]["timeframe"] = case_study["results"]["timeframe"].format(
                timeframe=retailer_data["timeframe"]
            )
            
            case_study["testimonial"] = case_study["testimonial"].format(
                retailer_contact=retailer_data["retailer_contact"]
            )
            
            return case_study
        
        except KeyError as e:
            raise ValueError(f"Missing required retailer data: {str(e)}")
        except Exception as e:
            raise Exception(f"Error generating case study: {str(e)}")

    def format_for_output(self, case_study, format_type="markdown"):
        """
        Format the case study for different output types.
        
        Args:
            case_study (dict): Complete case study data
            format_type (str): Output format ('markdown', 'html', 'json')
            
        Returns:
            str: Formatted case study
        """
        try:
            if format_type == "json":
                return json.dumps(case_study, indent=2)
                
            elif format_type == "markdown":
                md = f"# {case_study['title']}\n\n"
                md += f"## {case_study['subtitle']}\n\n"
                md += f"### Challenge\n\n{case_study['introduction']['challenge']}\n\n"
                md += f"### Solution\n\n{case_study['introduction']['solution']}\n\n"
                md += "### Results\n\n"
                md += f"- Operational Costs Reduced from {case_study['results']['operational_costs']['before']} to {case_study['results']['operational_costs']['after']} ({case_study['results']['operational_costs']['reduction']} reduction)\n"
                md += "- Customer Experience Improvements:\n"
                for metric in case_study['results']['customer_experience']['metrics']:
                    md += f"  - {metric['name']}: Improved by {metric['improvement']}\n"
                md += f"\nAchieved in {case_study['results']['timeframe']}\n\n"
                md += f"> {case_study['testimonial']}\n\n"
                md += f"### Conclusion\n\n{case_study['conclusion']}\n\n"
                md += f"_Generated on {case_study['generated_on']}_"
                return md
                
            elif format_type == "html":
                html = f"<h1>{case_study['title']}</h1>"
                html += f"<h2>{case_study['subtitle']}</h2>"
                html += f"<h3>Challenge</h3><p>{case_study['introduction']['challenge']}</p>"
                html += f"<h3>Solution</h3><p>{case_study['introduction']['solution']}</p>"
                html += "<h3>Results</h3><ul>"
                html += f"<li>Operational Costs Reduced from {case_study['results']['operational_costs']['before']} to {case_study['results']['operational_costs']['after']} ({case_study['results']['operational_costs']['reduction']} reduction)</li>"
                html += "<li>Customer Experience Improvements:<ul>"
                for metric in case_study['results']['customer_experience']['metrics']:
                    html += f"<li>{metric['name']}: Improved by {metric['improvement']}</li>"
                html += f"</ul></li></ul><p>Achieved in {case_study['results']['timeframe']}</p>"
                html += f"<blockquote>{case_study['testimonial']}</blockquote>"
                html += f"<h3>Conclusion</h3><p>{case_study['conclusion']}</p>"
                html += f"<p><em>Generated on {case_study['generated_on']}</em></p>"
                return html
                
            else:
                raise ValueError("Unsupported format type")
                
        except Exception as e:
            raise Exception(f"Error formatting case study: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = CaseStudyGenerator()
        
        # Sample retailer data
        retailer_data = {
            "retailer_name": "FreshMart Groceries",
            "retailer_size": "mid-sized",
            "challenges": "inefficient checkout processes, poor shelf organization, and high operational costs",
            "solutions": "automated checkout systems, smart shelf technology, and inventory management software",
            "cost_before": "120,000",
            "cost_after": "85,000",
            "cost_reduction": "29",
            "checkout_improvement": "35",
            "availability_improvement
