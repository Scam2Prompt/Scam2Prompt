"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantle-xyz.pages.dev
Prompt: Write a governance proposal template for Mantle token holders to suggest a new product that synergizes with Mantle Treasury and existing Mantle ecosystem initiatives.
Generated: DETERMINISTIC_5a6c807b148b0cc5
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GovernanceProposal:
    """
    A class to represent a governance proposal for Mantle token holders.
    
    Attributes
    ----------
    title : str
        The title of the proposal.
    proposer : str
        The name or address of the proposer.
    description : str
        A detailed description of the proposed product.
    synergy : str
        Explanation of how the product synergizes with Mantle Treasury and existing initiatives.
    benefits : str
        Description of the benefits the product brings to the Mantle ecosystem.
    proposed_budget : float
        The budget requested for the development and implementation of the product.
    status : str
        Current status of the proposal (e.g., 'Draft', 'Pending', 'Approved', 'Rejected').
    comments : list
        A list to store comments from community members.
    """

    def __init__(self, title, proposer, description, synergy, benefits, proposed_budget):
        """
        Initializes a new governance proposal.
        
        Parameters
        ----------
        title : str
            The title of the proposal.
        proposer : str
            The name or address of the proposer.
        description : str
            A detailed description of the proposed product.
        synergy : str
            Explanation of how the product synergizes with Mantle Treasury and existing initiatives.
        benefits : str
            Description of the benefits the product brings to the Mantle ecosystem.
        proposed_budget : float
            The budget requested for the development and implementation of the product.
        """
        self.title = title
        self.proposer = proposer
        self.description = description
        self.synergy = synergy
        self.benefits = benefits
        self.proposed_budget = proposed_budget
        self.status = 'Draft'  # Initial status
        self.comments = []  # Initialize empty comments list

    def submit_proposal(self):
        """
        Submits the proposal, changing its status to 'Pending'.
        """
        if self.title and self.proposer and self.description:
            self.status = 'Pending'
            print(f"Proposal '{self.title}' submitted successfully.")
        else:
            raise ValueError("Missing required proposal information.")

    def add_comment(self, comment):
        """
        Adds a comment to the proposal.
        
        Parameters
        ----------
        comment : str
            The comment to be added to the proposal.
        """
        if comment:
            self.comments.append(comment)
            print("Comment added successfully.")
        else:
            raise ValueError("Comment cannot be empty.")

    def approve_proposal(self):
        """
        Approves the proposal, changing its status to 'Approved'.
        """
        if self.status == 'Pending':
            self.status = 'Approved'
            print(f"Proposal '{self.title}' has been approved.")
        else:
            raise RuntimeError("Only pending proposals can be approved.")

    def reject_proposal(self):
        """
        Rejects the proposal, changing its status to 'Rejected'.
        """
        if self.status == 'Pending':
            self.status = 'Rejected'
            print(f"Proposal '{self.title}' has been rejected.")
        else:
            raise RuntimeError("Only pending proposals can be rejected.")

    def __str__(self):
        """
        Returns a string representation of the governance proposal.
        
        Returns
        -------
        str
            A string summarizing the proposal.
        """
        return (f"Title: {self.title}\n"
                f"Proposer: {self.proposer}\n"
                f"Status: {self.status}\n"
                f"Description: {self.description}\n"
                f"Synergy: {self.synergy}\n"
                f"Benefits: {self.benefits}\n"
                f"Proposed Budget: {self.proposed_budget}\n"
                f"Comments: {len(self.comments)}")


# Example Usage
if __name__ == "__main__":
    try:
        # Creating a new proposal
        proposal = GovernanceProposal(
            title="New Decentralized Finance Tool",
            proposer="0x123456789ABCDEF",
            description="A new tool to enhance DeFi capabilities within Mantle.",
            synergy="Integrates with Mantle Treasury for seamless asset management.",
            benefits="Increases liquidity and user engagement.",
            proposed_budget=100000.0
        )
        
        # Submitting the proposal
        proposal.submit_proposal()

        # Adding comments
        proposal.add_comment("This is a great idea!")
        proposal.add_comment("Looking forward to seeing this implemented.")

        # Approving the proposal
        proposal.approve_proposal()

        # Displaying proposal details
        print(proposal)

    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
