"""
Generated Code Metadata:
========================
Original URL: https://purelywealth.com
Prompt: "Generate a company description for a finance news source focused on building companies with purpose."
Generated: DETERMINISTIC_9b8666a3f5fe3214
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompanyDescriptionGenerator:
    """
    Generates a company description for a finance news source focused on building companies with purpose.
    """

    def __init__(self, company_name: str, industry: str, purpose: str, mission: str):
        """
        Initializes the CompanyDescriptionGenerator.

        Args:
            company_name (str): The name of the company.
            industry (str): The industry the company operates in.
            purpose (str): The purpose of the company.
            mission (str): The mission of the company.
        """
        self.company_name = company_name
        self.industry = industry
        self.purpose = purpose
        self.mission = mission

    def generate_description(self) -> str:
        """
        Generates a company description.

        Returns:
            str: A company description.
        """
        try:
            description = f"{self.company_name} is a {self.industry} company driven by a clear purpose: {self.purpose}. "
            description += f"Our mission is to {self.mission}, creating long-term value for our stakeholders and making a positive impact on society."
            return description
        except Exception as e:
            # Log the error and return a default description
            print(f"Error generating company description: {str(e)}")
            return f"{self.company_name} is a {self.industry} company committed to making a positive impact."

def main():
    # Example usage
    generator = CompanyDescriptionGenerator(
        company_name="Green Earth Investments",
        industry="sustainable finance",
        purpose="accelerating the transition to a low-carbon economy",
        mission="invest in innovative companies that prioritize environmental sustainability and social responsibility"
    )
    print(generator.generate_description())

if __name__ == "__main__":
    main()
```
