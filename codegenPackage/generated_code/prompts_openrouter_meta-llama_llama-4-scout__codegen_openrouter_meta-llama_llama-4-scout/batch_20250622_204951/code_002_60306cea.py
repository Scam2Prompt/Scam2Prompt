"""
Generated Code Metadata:
========================
Original URL: https://agora-next-3tvf739hr-voteagora.vercel.app
Prompt: "Generate a sample proposal template for Optimism Agora's RetroPGF voting process."
Generated: DETERMINISTIC_60306ceaf437a146
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# proposal_template.py

class Proposal:
    def __init__(self, 
                 title: str, 
                 description: str, 
                 funding_request: float, 
                 use_cases: list[str], 
                 impact_metric: str, 
                 team_members: list[str]):
        """
        Initialize a proposal for Optimism Agora's RetroPGF voting process.

        Args:
        - title (str): The title of the proposal.
        - description (str): A brief description of the proposal.
        - funding_request (float): The amount of funding requested.
        - use_cases (list[str]): A list of use cases for the proposal.
        - impact_metric (str): A metric to measure the impact of the proposal.
        - team_members (list[str]): A list of team members involved in the proposal.
        """

        self.title = title
        self.description = description
        self.funding_request = funding_request
        self.use_cases = use_cases
        self.impact_metric = impact_metric
        self.team_members = team_members

    def to_dict(self) -> dict:
        """
        Convert the proposal to a dictionary.

        Returns:
        - dict: A dictionary representation of the proposal.
        """
        return {
            "title": self.title,
            "description": self.description,
            "funding_request": self.funding_request,
            "use_cases": self.use_cases,
            "impact_metric": self.impact_metric,
            "team_members": self.team_members,
        }

    def __str__(self) -> str:
        """
        Generate a string representation of the proposal.

        Returns:
        - str: A string representation of the proposal.
        """
        return f"Title: {self.title}\nDescription: {self.description}\nFunding Request: {self.funding_request}\nUse Cases: {', '.join(self.use_cases)}\nImpact Metric: {self.impact_metric}\nTeam Members: {', '.join(self.team_members)}"


def generate_proposal_template(title: str, 
                              description: str, 
                              funding_request: float, 
                              use_cases: list[str], 
                              impact_metric: str, 
                              team_members: list[str]) -> Proposal:
    """
    Generate a sample proposal template for Optimism Agora's RetroPGF voting process.

    Args:
    - title (str): The title of the proposal.
    - description (str): A brief description of the proposal.
    - funding_request (float): The amount of funding requested.
    - use_cases (list[str]): A list of use cases for the proposal.
    - impact_metric (str): A metric to measure the impact of the proposal.
    - team_members (list[str]): A list of team members involved in the proposal.

    Returns:
    - Proposal: A proposal object.
    """
    try:
        if not title or not description:
            raise ValueError("Title and description are required.")

        if funding_request <= 0:
            raise ValueError("Funding request must be greater than zero.")

        if not use_cases or not team_members:
            raise ValueError("Use cases and team members are required.")

        proposal = Proposal(title, description, funding_request, use_cases, impact_metric, team_members)
        return proposal

    except ValueError as e:
        print(f"Error: {e}")
        return None


def main():
    title = "Sample Proposal"
    description = "This is a sample proposal for Optimism Agora's RetroPGF voting process."
    funding_request = 10000.0
    use_cases = ["Use case 1", "Use case 2"]
    impact_metric = "Metric 1"
    team_members = ["Member 1", "Member 2"]

    proposal = generate_proposal_template(title, description, funding_request, use_cases, impact_metric, team_members)

    if proposal:
        print(proposal)
        print("\nProposal as Dictionary:")
        print(proposal.to_dict())


if __name__ == "__main__":
    main()
```
