"""
Generated Code Metadata:
========================
Original URL: https://azt3c-st.webflow.io
Prompt: Provide an example of a grant proposal for contributing to Noir libraries and tooling, based on Aztec's Grants Program guidelines.
Generated: DETERMINISTIC_19977ac3d319e171
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grant Proposal for Noir Libraries and Tooling Contribution

This script generates a grant proposal template following Aztec's Grants Program guidelines.
The proposal is for contributing to Noir libraries and tooling development.
"""

class GrantProposal:
    """
    A class representing a grant proposal for Noir development contributions.
    """
    
    def __init__(self):
        """
        Initialize the grant proposal with default sections.
        """
        self.sections = {
            "title": "Noir Libraries and Tooling Development Grant Proposal",
            "applicant": {
                "name": "",
                "email": "",
                "github": "",
                "previous_contributions": []
            },
            "project": {
                "name": "",
                "description": "",
                "category": "Noir Libraries/Tooling",
                "duration": "",
                "milestones": []
            },
            "motivation": "",
            "technical_details": "",
            "impact": "",
            "budget": {
                "total_amount": "",
                "breakdown": []
            },
            "risks": "",
            "additional_info": ""
        }
    
    def validate(self):
        """
        Validate the proposal has all required fields filled.
        Raises ValueError if any required field is missing.
        """
        required_fields = [
            "applicant.name",
            "applicant.email",
            "project.name",
            "project.description",
            "motivation",
            "technical_details",
            "impact",
            "budget.total_amount"
        ]
        
        for field in required_fields:
            parts = field.split('.')
            current = self.sections
            for part in parts:
                if part not in current or not current[part]:
                    raise ValueError(f"Missing required field: {field}")
                current = current[part]
    
    def to_markdown(self):
        """
        Convert the proposal to markdown format.
        Returns:
            str: The proposal in markdown format
        """
        try:
            self.validate()
        except ValueError as e:
            return f"Proposal incomplete: {str(e)}"
        
        md = []
        md.append(f"# {self.sections['title']}\n")
        
        # Applicant Section
        md.append("## Applicant Information\n")
        md.append(f"- **Name:** {self.sections['applicant']['name']}")
        md.append(f"- **Email:** {self.sections['applicant']['email']}")
        md.append(f"- **GitHub:** {self.sections['applicant']['github']}")
        if self.sections['applicant']['previous_contributions']:
            md.append("- **Previous Contributions:**")
            for contrib in self.sections['applicant']['previous_contributions']:
                md.append(f"  - {contrib}")
        md.append("")
        
        # Project Section
        md.append("## Project Information\n")
        md.append(f"- **Project Name:** {self.sections['project']['name']}")
        md.append(f"- **Category:** {self.sections['project']['category']}")
        md.append(f"- **Duration:** {self.sections['project']['duration']}")
        md.append(f"- **Description:** {self.sections['project']['description']}")
        if self.sections['project']['milestones']:
            md.append("- **Milestones:**")
            for i, milestone in enumerate(self.sections['project']['milestones'], 1):
                md.append(f"  {i}. {milestone['name']} - {milestone['description']}")
        md.append("")
        
        # Other Sections
        sections_order = [
            ("Motivation", "motivation"),
            ("Technical Details", "technical_details"),
            ("Impact", "impact"),
            ("Budget", "budget"),
            ("Risks", "risks"),
            ("Additional Information", "additional_info")
        ]
        
        for title, key in sections_order:
            if self.sections[key]:
                md.append(f"## {title}\n")
                if isinstance(self.sections[key], dict):
                    if key == "budget":
                        md.append(f"- **Total Amount:** {self.sections[key]['total_amount']}")
                        if self.sections[key]['breakdown']:
                            md.append("- **Breakdown:**")
                            for item in self.sections[key]['breakdown']:
                                md.append(f"  - {item['item']}: {item['amount']}")
                else:
                    md.append(self.sections[key])
                md.append("")
        
        return '\n'.join(md)

# Example usage
if __name__ == "__main__":
    proposal = GrantProposal()
    
    # Fill in proposal details
    proposal.sections["applicant"].update({
        "name": "Jane Developer",
        "email": "jane@example.com",
        "github": "@janedev",
        "previous_contributions": [
            "Contributed to Noir standard library",
            "Maintained noir-analyzer tool"
        ]
    })
    
    proposal.sections["project"].update({
        "name": "Noir Debugger Tool",
        "description": "Development of a debugging tool for Noir smart contracts with breakpoints, variable inspection, and step-through execution.",
        "duration": "3 months",
        "milestones": [
            {
                "name": "Phase 1",
                "description": "Basic debugging functionality"
            },
            {
                "name": "Phase 2",
                "description": "Integration with VS Code"
            },
            {
                "name": "Phase 3",
                "description": "Advanced features and documentation"
            }
        ]
    })
    
    proposal.sections.update({
        "motivation": "Debugging Noir contracts is currently challenging without proper tooling. This tool will significantly improve developer experience.",
        "technical_details": "The debugger will be built as a VS Code extension using the Language Server Protocol. It will interface with the Noir compiler to provide debugging capabilities.",
        "impact": "This tool will make Noir more accessible to developers and accelerate adoption of the language.",
        "budget": {
            "total_amount": "$15,000",
            "breakdown": [
                {"item": "Development", "amount": "$10,000"},
                {"item": "Testing", "amount": "$3,000"},
                {"item": "Documentation", "amount": "$2,000"}
            ]
        },
        "risks": "Potential challenges include compiler integration and performance overhead during debugging.",
        "additional_info": "I have prior experience developing developer tools and have contributed to Noir before."
    })
    
    # Generate and print the proposal
    print(proposal.to_markdown())
```
