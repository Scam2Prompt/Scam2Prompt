"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Generate a grant proposal template in Python based on the techniques outlined in PDMA's Grant Writing Professional course.
Generated: DETERMINISTIC_8ea7ea06d3a86df6
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Grant Proposal Template Generator
Based on PDMA's Grant Writing Professional course techniques
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict
import json
import textwrap

@dataclass
class Organization:
    name: str
    address: str
    phone: str
    email: str
    website: Optional[str] = None
    ein: Optional[str] = None

@dataclass
class Project:
    title: str
    description: str
    objectives: List[str]
    methods: str
    timeline: Dict[str, str]
    budget: Dict[str, float]
    evaluation_plan: str
    sustainability_plan: str

@dataclass
class GrantProposal:
    funder_name: str
    program_name: str
    proposal_title: str
    organization: Organization
    project: Project
    amount_requested: float
    submission_date: str
    contact_person: str
    attachments: List[str] = None

    def __post_init__(self):
        if self.attachments is None:
            self.attachments = []

    def to_dict(self):
        return {
            "funder_name": self.funder_name,
            "program_name": self.program_name,
            "proposal_title": self.proposal_title,
            "organization": {
                "name": self.organization.name,
                "address": self.organization.address,
                "phone": self.organization.phone,
                "email": self.organization.email,
                "website": self.organization.website,
                "ein": self.organization.ein
            },
            "project": {
                "title": self.project.title,
                "description": self.project.description,
                "objectives": self.project.objectives,
                "methods": self.project.methods,
                "timeline": self.project.timeline,
                "budget": self.project.budget,
                "evaluation_plan": self.project.evaluation_plan,
                "sustainability_plan": self.project.sustainability_plan
            },
            "amount_requested": self.amount_requested,
            "submission_date": self.submission_date,
            "contact_person": self.contact_person,
            "attachments": self.attachments
        }

    def to_json(self, indent=2):
        return json.dumps(self.to_dict(), indent=indent)

    def generate_proposal_text(self) -> str:
        """Generate a formatted grant proposal document"""
        proposal = f"""
        GRANT PROPOSAL
        ==============

        Submitted to: {self.funder_name}
        Program: {self.program_name}
        Date: {self.submission_date}
        Amount Requested: ${self.amount_requested:,.2f}

        ORGANIZATION INFORMATION
        ------------------------
        Name: {self.organization.name}
        Address: {self.organization.address}
        Phone: {self.organization.phone}
        Email: {self.organization.email}
        Website: {self.organization.website or 'N/A'}
        EIN: {self.organization.ein or 'N/A'}
        Contact Person: {self.contact_person}

        PROJECT SUMMARY
        ---------------
        Title: {self.project.title}
        Description:
        {textwrap.fill(self.project.description, width=70)}

        PROJECT OBJECTIVES
        ------------------
        {self._format_list(self.project.objectives)}

        METHODS
        -------
        {textwrap.fill(self.project.methods, width=70)}

        TIMELINE
        --------
        {self._format_dict(self.project.timeline)}

        BUDGET
        ------
        {self._format_budget()}

        EVALUATION PLAN
        ---------------
        {textwrap.fill(self.project.evaluation_plan, width=70)}

        SUSTAINABILITY PLAN
        -------------------
        {textwrap.fill(self.project.sustainability_plan, width=70)}

        ATTACHMENTS
        -----------
        {self._format_list(self.attachments) if self.attachments else 'None'}
        """

        return textwrap.dedent(proposal).strip()

    def _format_list(self, items: List[str]) -> str:
        return "\n".join(f"- {item}" for item in items)

    def _format_dict(self, items: Dict[str, str]) -> str:
        return "\n".join(f"- {key}: {value}" for key, value in items.items())

    def _format_budget(self) -> str:
        total = sum(self.project.budget.values())
        budget_lines = [f"- {category}: ${amount:,.2f}" 
                       for category, amount in self.project.budget.items()]
        budget_lines.append(f"\nTOTAL: ${total:,.2f}")
        return "\n".join(budget_lines)

def create_sample_proposal() -> GrantProposal:
    """Create a sample grant proposal for demonstration"""
    org = Organization(
        name="Community Health Initiative",
        address="123 Main St, Anytown, ST 12345",
        phone="(555) 123-4567",
        email="info@communityhealth.org",
        website="www.communityhealth.org",
        ein="12-3456789"
    )

    project = Project(
        title="Youth Mental Health Awareness Program",
        description="A comprehensive program to educate high school students about mental health issues and provide resources for those in need.",
        objectives=[
            "Train 50 teachers in mental health first aid",
            "Provide workshops to 1,000 students",
            "Establish peer support groups in 10 schools"
        ],
        methods="The program will use evidence-based curriculum delivered by trained professionals, with follow-up support through school-based peer groups.",
        timeline={
            "Month 1-2": "Teacher training",
            "Month 3-6": "Student workshops",
            "Month 7-12": "Peer group implementation"
        },
        budget={
            "Personnel": 45000,
            "Materials": 10000,
            "Training": 15000,
            "Evaluation": 5000
        },
        evaluation_plan="Pre- and post-surveys will measure knowledge gains. Attendance and participation will be tracked. Follow-up surveys at 6 months will assess long-term impact.",
        sustainability_plan="The program will train school staff to continue the program. We will seek ongoing funding from school budgets and local foundations."
    )

    return GrantProposal(
        funder_name="National Mental Health Foundation",
        program_name="Youth Mental Health Initiative",
        proposal_title="Youth Mental Health Awareness Program for Anytown Schools",
        organization=org,
        project=project,
        amount_requested=75000,
        submission_date=datetime.date.today().strftime("%m/%d/%Y"),
        contact_person="Jane Doe, Program Director",
        attachments=[
            "IRS 501(c)(3) determination letter",
            "Board of Directors list",
            "Organization budget"
        ]
    )

def save_proposal_to_file(proposal: GrantProposal, filename: str):
    """Save proposal to a text file"""
    try:
        with open(filename, 'w') as f:
            f.write(proposal.generate_proposal_text())
    except IOError as e:
        print(f"Error saving proposal: {e}")

def main():
    """Main function to demonstrate the template"""
    proposal = create_sample_proposal()
    print(proposal.generate_proposal_text())
    
    # Save to file
    save_proposal_to_file(proposal, "grant_proposal.txt")
    print("\nProposal saved to grant_proposal.txt")

if __name__ == "__main__":
    main()
```
