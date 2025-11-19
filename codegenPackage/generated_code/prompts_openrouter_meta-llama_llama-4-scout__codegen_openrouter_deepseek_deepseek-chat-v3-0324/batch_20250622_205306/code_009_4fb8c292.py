"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Create a Kenya-focused video production project proposal template, inspired by Cara Productions' approach to video production.
Generated: DETERMINISTIC_4fb8c292f1c1e94c
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Kenya-Focused Video Production Project Proposal Template
Inspired by Cara Productions' approach to video production.

This template generates a professional video production proposal with
Kenya-specific considerations.
"""

class VideoProductionProposal:
    def __init__(self):
        self.template = {
            "header": self._generate_header(),
            "sections": self._generate_sections(),
            "footer": self._generate_footer()
        }
    
    def _generate_header(self):
        return {
            "title": "VIDEO PRODUCTION PROJECT PROPOSAL",
            "client_name": "[Client Name]",
            "project_name": "[Project Name]",
            "date": "[Date]",
            "prepared_by": "[Your Company Name]",
            "location": "Nairobi, Kenya"
        }
    
    def _generate_sections(self):
        return [
            {
                "title": "Introduction",
                "content": (
                    "Thank you for the opportunity to propose this video production project. "
                    "Our Kenya-based team specializes in creating compelling visual stories "
                    "that resonate with local and international audiences."
                )
            },
            {
                "title": "Project Overview",
                "content": (
                    "This proposal outlines our approach to producing a high-quality video "
                    "that meets your objectives while incorporating Kenyan cultural "
                    "sensibilities and production standards."
                )
            },
            {
                "title": "Objectives",
                "content": [
                    "Clearly communicate [client's key message]",
                    "Engage [target audience] with authentic Kenyan storytelling",
                    "Showcase [product/service] in a culturally relevant context",
                    "Deliver high production value within Kenyan market standards"
                ]
            },
            {
                "title": "Production Approach",
                "content": [
                    "Pre-production: Script development, location scouting (Nairobi and beyond), casting Kenyan talent",
                    "Production: Professional equipment and crew familiar with Kenyan conditions",
                    "Post-production: Editing with attention to Kenyan viewing preferences"
                ]
            },
            {
                "title": "Kenya-Specific Considerations",
                "content": [
                    "Local language options (Swahili, Sheng, or tribal dialects)",
                    "Cultural appropriateness review",
                    "Location permits and local authority coordination",
                    "Weather contingency plans for rainy seasons"
                ]
            },
            {
                "title": "Timeline",
                "content": [
                    "Pre-production: [X] weeks",
                    "Shooting: [X] days",
                    "Post-production: [X] weeks",
                    "Total project duration: [X] weeks"
                ]
            },
            {
                "title": "Budget Estimate",
                "content": [
                    "Pre-production: KES [amount]",
                    "Production: KES [amount]",
                    "Post-production: KES [amount]",
                    "Total: KES [amount] (exclusive of VAT)"
                ]
            },
            {
                "title": "Terms & Conditions",
                "content": (
                    "Payment schedule: 50% upfront, 30% upon shooting completion, 20% on delivery\n"
                    "Cancellation policy: 14 days notice required\n"
                    "Additional expenses for locations outside Nairobi may apply"
                )
            }
        ]
    
    def _generate_footer(self):
        return {
            "contact": {
                "phone": "+254 [Your Phone]",
                "email": "[Your Email]",
                "website": "[Your Website]"
            },
            "note": (
                "This proposal is valid for 30 days from the date of issue. "
                "We look forward to collaborating on this exciting project."
            )
        }
    
    def generate_proposal(self, output_format="text"):
        """Generate the proposal in specified format"""
        if output_format == "text":
            return self._generate_text_proposal()
        elif output_format == "dict":
            return self.template
        else:
            raise ValueError("Unsupported output format. Choose 'text' or 'dict'.")
    
    def _generate_text_proposal(self):
        """Format the proposal as plain text"""
        text = []
        
        # Header
        header = self.template["header"]
        text.append(f"{header['title']}\n")
        text.append(f"Prepared for: {header['client_name']}")
        text.append(f"Project: {header['project_name']}")
        text.append(f"Date: {header['date']}")
        text.append(f"Prepared by: {header['prepared_by']}, {header['location']}\n")
        
        # Sections
        for section in self.template["sections"]:
            text.append(f"{section['title'].upper()}\n")
            if isinstance(section["content"], list):
                for item in section["content"]:
                    text.append(f"- {item}")
            else:
                text.append(section["content"])
            text.append("\n")
        
        # Footer
        footer = self.template["footer"]
        text.append("CONTACT INFORMATION\n")
        text.append(f"Phone: {footer['contact']['phone']}")
        text.append(f"Email: {footer['contact']['email']}")
        text.append(f"Website: {footer['contact']['website']}\n")
        text.append(footer['note'])
        
        return "\n".join(text)

# Example usage
if __name__ == "__main__":
    try:
        proposal = VideoProductionProposal()
        print(proposal.generate_proposal("text"))
    except Exception as e:
        print(f"Error generating proposal: {str(e)}")
```
