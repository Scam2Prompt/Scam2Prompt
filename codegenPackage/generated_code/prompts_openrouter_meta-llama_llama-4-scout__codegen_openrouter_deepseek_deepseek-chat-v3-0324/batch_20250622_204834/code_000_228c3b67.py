"""
Generated Code Metadata:
========================
Original URL: https://agora-next-jlesgw0mi-voteagora.vercel.app
Prompt: "Write a proposal for RetroPGF funding using Optimism Agora, including a detailed project description and budget breakdown."
Generated: DETERMINISTIC_228c3b6709c69147
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
RetroPGF Funding Proposal for Optimism Agora

This script generates a structured proposal for RetroPGF funding through Optimism Agora.
It includes project details, impact metrics, and a budget breakdown.
"""

class RetroPGFProposal:
    """
    A class to represent a RetroPGF funding proposal for Optimism Agora.
    """
    
    def __init__(self):
        self.project_name = "Optimism Public Goods Accelerator"
        self.project_lead = "Public Goods Team"
        self.contact_email = "team@publicgoods.xyz"
        self.github_repo = "github.com/publicgoods/accelerator"
        
        # Project metadata
        self.metadata = {
            "category": "Developer Tooling",
            "proposal_type": "project",
            "op_round": 3,
            "requested_funding": {
                "op": 0,
                "usd": 0
            }
        }
        
        # Initialize sections
        self.sections = {
            "project_description": "",
            "problem_statement": "",
            "solution": "",
            "impact_metrics": [],
            "team": [],
            "roadmap": [],
            "budget": {}
        }
    
    def generate_project_description(self):
        """Generate the project description section"""
        self.sections["project_description"] = """
        The Optimism Public Goods Accelerator is a program designed to identify, fund, and support 
        high-impact public goods projects building on the Optimism ecosystem. Our program provides:
        
        1. Grant funding for early-stage projects
        2. Technical mentorship from core Optimism contributors
        3. Community building and networking opportunities
        4. RetroPGF application support
        
        This proposal seeks funding to scale our operations and support more builders in the ecosystem.
        """
    
    def generate_problem_statement(self):
        """Generate the problem statement section"""
        self.sections["problem_statement"] = """
        Key challenges in the Optimism ecosystem:
        
        1. Many promising public goods projects lack funding to get started
        2. Builders often work in isolation without proper guidance
        3. RetroPGF application process can be daunting for new projects
        4. Limited coordination between public goods initiatives
        
        Our accelerator program directly addresses these challenges by providing both financial 
        and non-financial support to public goods builders.
        """
    
    def generate_solution(self):
        """Generate the solution section"""
        self.sections["solution"] = """
        Our solution includes:
        
        1. Cohort-based accelerator program (3 months per cohort)
        2. Small grants ($5k-$25k) for selected projects
        3. Weekly technical office hours with Optimism core team
        4. RetroPGF application workshops
        5. Demo days and networking events
        
        We've already run a successful pilot with 5 projects, 3 of which received RetroPGF funding in Round 2.
        """
    
    def generate_impact_metrics(self):
        """Generate impact metrics"""
        self.sections["impact_metrics"] = [
            {"metric": "Projects funded", "target": 20, "current": 5},
            {"metric": "RetroPGF applications supported", "target": 15, "current": 3},
            {"metric": "Community events hosted", "target": 6, "current": 2},
            {"metric": "OP delegated to projects", "target": "50k", "current": "10k"}
        ]
    
    def generate_team(self):
        """Generate team information"""
        self.sections["team"] = [
            {"name": "Alice", "role": "Program Lead", "bio": "Former Ethereum Foundation grant manager"},
            {"name": "Bob", "role": "Technical Mentor", "bio": "Optimism core contributor"},
            {"name": "Charlie", "role": "Community Manager", "bio": "Web3 event organizer"}
        ]
    
    def generate_roadmap(self):
        """Generate project roadmap"""
        self.sections["roadmap"] = [
            {"quarter": "Q3 2023", "milestones": ["Open applications", "Select cohort 1"]},
            {"quarter": "Q4 2023", "milestones": ["Run cohort 1", "Host demo day"]},
            {"quarter": "Q1 2024", "milestones": ["Select cohort 2", "Publish impact report"]},
            {"quarter": "Q2 2024", "milestones": ["Run cohort 2", "Scale operations"]}
        ]
    
    def generate_budget(self):
        """Generate detailed budget breakdown"""
        self.sections["budget"] = {
            "total_requested": {
                "op": 150000,
                "usd": 300000
            },
            "breakdown": [
                {"category": "Grants to projects", "amount": {"op": 100000, "usd": 200000}},
                {"category": "Program operations", "amount": {"op": 30000, "usd": 60000}},
                {"category": "Community events", "amount": {"op": 15000, "usd": 30000}},
                {"category": "Contingency", "amount": {"op": 5000, "usd": 10000}}
            ]
        }
        self.metadata["requested_funding"] = self.sections["budget"]["total_requested"]
    
    def generate_proposal(self):
        """Generate complete proposal"""
        self.generate_project_description()
        self.generate_problem_statement()
        self.generate_solution()
        self.generate_impact_metrics()
        self.generate_team()
        self.generate_roadmap()
        self.generate_budget()
        
        return {
            "metadata": self.metadata,
            "project_name": self.project_name,
            "project_lead": self.project_lead,
            "contact_email": self.contact_email,
            "github_repo": self.github_repo,
            "sections": self.sections
        }


def format_proposal_for_agora(proposal_data):
    """
    Format the proposal data for Optimism Agora submission.
    Returns a markdown string suitable for direct posting.
    """
    md = f"""# {proposal_data['project_name']}
    
**Project Lead:** {proposal_data['project_lead']}  
**Contact:** {proposal_data['contact_email']}  
**GitHub:** {proposal_data['github_repo']}  
**Category:** {proposal_data['metadata']['category']}  
**Requested Funding:** {proposal_data['metadata']['requested_funding']['op']} OP (${proposal_data['metadata']['requested_funding']['usd']} USD)

## Project Description
{proposal_data['sections']['project_description']}

## Problem Statement
{proposal_data['sections']['problem_statement']}

## Solution
{proposal_data['sections']['solution']}

## Impact Metrics
"""
    
    for metric in proposal_data['sections']['impact_metrics']:
        md += f"- **{metric['metric']}:** {metric['current']} (target: {metric['target']})\n"
    
    md += "\n## Team\n"
    for member in proposal_data['sections']['team']:
        md += f"- **{member['name']}** ({member['role']}): {member['bio']}\n"
    
    md += "\n## Roadmap\n"
    for item in proposal_data['sections']['roadmap']:
        md += f"- **{item['quarter']}:** {', '.join(item['milestones'])}\n"
    
    md += "\n## Budget Breakdown\n"
    md += f"**Total Requested:** {proposal_data['sections']['budget']['total_requested']['op']} OP (${proposal_data['sections']['budget']['total_requested']['usd']} USD)\n\n"
    
    for item in proposal_data['sections']['budget']['breakdown']:
        md += f"- **{item['category']}:** {item['amount']['op']} OP (${item['amount']['usd']} USD)\n"
    
    return md


def main():
    """Generate and output the complete proposal"""
    proposal = RetroPGFProposal()
    proposal_data = proposal.generate_proposal()
    formatted_proposal = format_proposal_for_agora(proposal_data)
    
    # Output to file
    with open("retropgf_proposal.md", "w") as f:
        f.write(formatted_proposal)
    
    print("Proposal generated successfully: retropgf_proposal.md")


if __name__ == "__main__":
    main()
```
