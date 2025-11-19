"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Generate a course outline for a diploma in accounting and taxation in Peru, including topics such as financial statements, tax returns, and labor laws."
Generated: DETERMINISTIC_48d804badc7b81d3
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Course Outline Generator for Diploma in Accounting and Taxation in Peru.

This script generates a structured course outline covering key topics such as financial statements,
tax returns, and labor laws, tailored for a diploma program in Peru.
"""

class CourseOutlineGenerator:
    """Generates a diploma course outline for Accounting and Taxation in Peru."""

    def __init__(self):
        """Initialize the course outline with default modules."""
        self.course_title = "Diploma in Accounting and Taxation (Peru)"
        self.duration = "6 months"
        self.modules = []

    def add_module(self, title, topics):
        """Add a module to the course outline.
        
        Args:
            title (str): Title of the module.
            topics (list): List of topics covered in the module.
        """
        self.modules.append({
            "title": title,
            "topics": topics
        })

    def generate_outline(self):
        """Generate and return the course outline as a structured dictionary.
        
        Returns:
            dict: Structured course outline with title, duration, and modules.
        """
        return {
            "course_title": self.course_title,
            "duration": self.duration,
            "modules": self.modules
        }

def create_peru_accounting_taxation_outline():
    """Create a predefined course outline for Accounting and Taxation in Peru.
    
    Returns:
        dict: Complete course outline.
    """
    generator = CourseOutlineGenerator()

    # Module 1: Fundamentals of Accounting
    generator.add_module(
        "Fundamentals of Accounting",
        [
            "Introduction to Accounting Principles",
            "Double-Entry Bookkeeping",
            "Chart of Accounts (Peruvian Standards)",
            "Accounting Cycle",
            "Financial Transactions Recording"
        ]
    )

    # Module 2: Financial Statements
    generator.add_module(
        "Financial Statements",
        [
            "Balance Sheet Preparation",
            "Income Statement",
            "Cash Flow Statement",
            "Notes to Financial Statements",
            "Financial Statement Analysis"
        ]
    )

    # Module 3: Peruvian Taxation System
    generator.add_module(
        "Peruvian Taxation System",
        [
            "Overview of Peruvian Tax Laws",
            "Income Tax (IR) for Individuals and Companies",
            "General Sales Tax (IGV)",
            "Taxpayer Obligations and Deadlines",
            "Tax Incentives and Exemptions"
        ]
    )

    # Module 4: Tax Returns and Compliance
    generator.add_module(
        "Tax Returns and Compliance",
        [
            "Monthly and Annual Tax Returns",
            "Electronic Invoicing (Facturación Electrónica)",
            "Tax Withholding and Payments",
            "Sunat Procedures and Platforms",
            "Tax Audits and Penalties"
        ]
    )

    # Module 5: Labor Laws and Payroll
    generator.add_module(
        "Labor Laws and Payroll",
        [
            "Peruvian Labor Code Overview",
            "Employee Benefits and Obligations",
            "Payroll Processing and Deductions",
            "Social Security (EsSalud, ONP)",
            "Labor Inspections and Compliance"
        ]
    )

    # Module 6: Practical Applications
    generator.add_module(
        "Practical Applications",
        [
            "Case Studies in Accounting and Taxation",
            "Software Tools (e.g., CONCAR, SQL Contabilidad)",
            "Real-World Tax Filing Scenarios",
            "Final Project: Comprehensive Financial Report"
        ]
    )

    return generator.generate_outline()

# Example usage
if __name__ == "__main__":
    outline = create_peru_accounting_taxation_outline()
    print("Course Outline:")
    print(f"Title: {outline['course_title']}")
    print(f"Duration: {outline['duration']}")
    print("\nModules:")
    for module in outline['modules']:
        print(f"\nModule: {module['title']}")
        print("Topics:")
        for topic in module['topics']:
            print(f"- {topic}")
```
