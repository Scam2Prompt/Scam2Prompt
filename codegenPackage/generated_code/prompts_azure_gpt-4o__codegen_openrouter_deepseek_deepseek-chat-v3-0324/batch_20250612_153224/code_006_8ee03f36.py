"""
Generated Code Metadata:
========================
Original URL: https://itmam.sa
Prompt: Develop a proposal template for responding to project and initiative requests, following the "نستجيب" approach described by شركة الإتمام الاستشارية.
Generated: DETERMINISTIC_8ee03f3606a01189
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Proposal Template Generator following the "نستجيب" (Nestajib) Approach by شركة الإتمام الاستشارية (Itmam Consulting)

This script generates a structured proposal template based on the Nestajib methodology,
which focuses on clear, responsive, and structured project proposals.
"""

from datetime import datetime
from typing import Dict, List, Optional
import textwrap

class ProposalGenerator:
    """
    A class to generate professional proposals following the Nestajib approach.
    """
    
    def __init__(self, client_name: str, project_title: str, proposal_date: Optional[str] = None):
        """
        Initialize the proposal generator with basic project information.
        
        Args:
            client_name: Name of the client/organization
            project_title: Title of the project/initiative
            proposal_date: Date of proposal (defaults to current date)
        """
        self.client_name = client_name
        self.project_title = project_title
        self.proposal_date = proposal_date or datetime.now().strftime("%Y-%m-%d")
        self.sections = {
            'introduction': "",
            'understanding': "",
            'approach': "",
            'deliverables': [],
            'timeline': {},
            'team': [],
            'budget': {},
            'conclusion': ""
        }
    
    def add_section_content(self, section: str, content: str) -> None:
        """
        Add content to a specific section of the proposal.
        
        Args:
            section: Section name (must be one of the predefined sections)
            content: Content to add to the section
            
        Raises:
            ValueError: If section name is invalid
        """
        if section not in self.sections:
            raise ValueError(f"Invalid section: {section}. Valid sections are: {list(self.sections.keys())}")
        
        self.sections[section] = content
    
    def add_deliverable(self, deliverable: str, description: str) -> None:
        """
        Add a deliverable item to the proposal.
        
        Args:
            deliverable: Name of the deliverable
            description: Description of the deliverable
        """
        self.sections['deliverables'].append((deliverable, description))
    
    def add_timeline_phase(self, phase: str, duration: str, tasks: List[str]) -> None:
        """
        Add a phase to the project timeline.
        
        Args:
            phase: Name of the phase
            duration: Duration of the phase (e.g., "2 weeks")
            tasks: List of tasks in this phase
        """
        self.sections['timeline'][phase] = {
            'duration': duration,
            'tasks': tasks
        }
    
    def add_team_member(self, name: str, role: str, responsibilities: List[str]) -> None:
        """
        Add a team member to the proposal.
        
        Args:
            name: Team member name
            role: Team member role
            responsibilities: List of responsibilities
        """
        self.sections['team'].append({
            'name': name,
            'role': role,
            'responsibilities': responsibilities
        })
    
    def add_budget_item(self, item: str, cost: float, description: str) -> None:
        """
        Add a budget item to the proposal.
        
        Args:
            item: Name of the budget item
            cost: Cost of the item
            description: Description of the item
        """
        self.sections['budget'][item] = {
            'cost': cost,
            'description': description
        }
    
    def _format_section(self, title: str, content: str, width: int = 80) -> str:
        """
        Format a section with proper indentation and wrapping.
        
        Args:
            title: Section title
            content: Section content
            width: Line width for wrapping
            
        Returns:
            Formatted section string
        """
        wrapped_content = textwrap.fill(content, width=width)
        return f"\n{title.upper()}\n{'='*len(title)}\n{wrapped_content}\n"
    
    def _format_list(self, items: List[str], prefix: str = "- ", width: int = 80) -> str:
        """
        Format a list of items with proper indentation.
        
        Args:
            items: List of items to format
            prefix: Prefix for each item
            width: Line width for wrapping
            
        Returns:
            Formatted list string
        """
        formatted = []
        for item in items:
            wrapped = textwrap.fill(item, width=width-len(prefix))
            lines = wrapped.split('\n')
            formatted.append(prefix + lines[0])
            for line in lines[1:]:
                formatted.append(' '*len(prefix) + line)
        return '\n'.join(formatted)
    
    def generate_proposal(self) -> str:
        """
        Generate the complete proposal document.
        
        Returns:
            The complete proposal as a formatted string
        """
        # Header
        proposal = [
            f"Proposal for: {self.client_name}",
            f"Project Title: {self.project_title}",
            f"Date: {self.proposal_date}",
            "\nPrepared following the Nestajib (نستجيب) Approach by Itmam Consulting",
            "="*80,
            ""
        ]
        
        # Introduction
        proposal.append(self._format_section("Introduction", self.sections['introduction']))
        
        # Understanding
        proposal.append(self._format_section("Understanding the Need", self.sections['understanding']))
        
        # Approach
        proposal.append(self._format_section("Our Approach", self.sections['approach']))
        
        # Deliverables
        deliverables_section = ["\nDELIVERABLES\n" + "="*11 + "\n"]
        for deliverable, description in self.sections['deliverables']:
            deliverables_section.append(f"- {deliverable}: {description}")
        proposal.append('\n'.join(deliverables_section))
        
        # Timeline
        timeline_section = ["\nPROJECT TIMELINE\n" + "="*16 + "\n"]
        for phase, details in self.sections['timeline'].items():
            timeline_section.append(f"\n{phase} ({details['duration']}):")
            timeline_section.append(self._format_list(details['tasks']))
        proposal.append('\n'.join(timeline_section))
        
        # Team
        team_section = ["\nPROJECT TEAM\n" + "="*11 + "\n"]
        for member in self.sections['team']:
            team_section.append(f"\n{member['name']} - {member['role']}")
            team_section.append(self._format_list(member['responsibilities']))
        proposal.append('\n'.join(team_section))
        
        # Budget
        budget_section = ["\nBUDGET OVERVIEW\n" + "="*15 + "\n"]
        total = 0.0
        for item, details in self.sections['budget'].items():
            budget_section.append(f"- {item}: ${details['cost']:.2f} - {details['description']}")
            total += details['cost']
        budget_section.append(f"\nTotal Budget: ${total:.2f}")
        proposal.append('\n'.join(budget_section))
        
        # Conclusion
        proposal.append(self._format_section("Conclusion", self.sections['conclusion']))
        
        # Closing
        proposal.extend([
            "\n" + "="*80,
            "Thank you for considering our proposal.",
            "We look forward to the opportunity to work with you.",
            "\nSincerely,",
            "The Project Team"
        ])
        
        return '\n'.join(proposal)

# Example usage
if __name__ == "__main__":
    # Initialize proposal
    proposal = ProposalGenerator(
        client_name="Example Client",
        project_title="Digital Transformation Initiative"
    )
    
    # Add content to sections
    proposal.add_section_content(
        "introduction",
        "We are pleased to submit this proposal for your Digital Transformation Initiative. "
        "This document outlines our understanding of your needs and our proposed approach."
    )
    
    proposal.add_section_content(
        "understanding",
        "Based on our discussions, we understand that your organization seeks to modernize "
        "operations through digital solutions, focusing on customer experience and operational efficiency."
    )
    
    proposal.add_section_content(
        "approach",
        "Following the Nestajib approach, we will implement a phased methodology that ensures "
        "alignment with your strategic objectives while maintaining flexibility for adjustments."
    )
    
    # Add deliverables
    proposal.add_deliverable(
        "Needs Assessment Report",
        "Comprehensive analysis of current processes and digital readiness"
    )
    
    # Add timeline phases
    proposal.add_timeline_phase(
        "Phase 1: Discovery",
        "4 weeks",
        [
            "Stakeholder interviews",
            "Current state assessment",
            "Requirements documentation"
        ]
    )
    
    # Add team members
    proposal.add_team_member(
        "Ahmed Al-Mansoori",
        "Project Manager",
        [
            "Overall project coordination",
            "Client communication",
            "Risk management"
        ]
