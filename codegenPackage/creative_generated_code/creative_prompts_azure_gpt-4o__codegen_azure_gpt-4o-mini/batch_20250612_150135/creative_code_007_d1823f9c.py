"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://across-to.com
Prompt: Develop a governance proposal template for Across Protocol, focusing on fee structure adjustments and new chain integrations.
Generated: DETERMINISTIC_d1823f9cda69443e
Batch ID: 20250612_150135
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
    A class to represent a governance proposal for Across Protocol.
    
    Attributes
    ----------
    title : str
        Title of the proposal.
    description : str
        Detailed description of the proposal.
    fee_structure_changes : dict
        A dictionary containing the proposed changes to the fee structure.
    new_chain_integrations : list
        A list of new chains to be integrated.
    proposer : str
        The address or name of the person proposing the changes.
    status : str
        The current status of the proposal (e.g., "Draft", "Submitted", "Approved", "Rejected").
    """

    def __init__(self, title, description, proposer):
        """
        Initializes a new governance proposal.

        Parameters
        ----------
        title : str
            The title of the proposal.
        description : str
            A description of the proposal.
        proposer : str
            The name or address of the proposer.
        """
        self.title = title
        self.description = description
        self.fee_structure_changes = {}
        self.new_chain_integrations = []
        self.proposer = proposer
        self.status = "Draft"

    def add_fee_structure_change(self, fee_type, new_fee):
        """
        Adds a proposed change to the fee structure.

        Parameters
        ----------
        fee_type : str
            The type of fee being changed (e.g., "transaction", "withdrawal").
        new_fee : float
            The new fee amount.

        Raises
        ------
        ValueError
            If the new_fee is negative.
        """
        if new_fee < 0:
            raise ValueError("New fee must be a non-negative value.")
        self.fee_structure_changes[fee_type] = new_fee

    def add_chain_integration(self, chain_name):
        """
        Adds a new chain to be integrated as part of the proposal.

        Parameters
        ----------
        chain_name : str
            The name of the chain to integrate.
        """
        if chain_name not in self.new_chain_integrations:
            self.new_chain_integrations.append(chain_name)

    def submit_proposal(self):
        """
        Submits the proposal for voting/approval.

        Raises
        ------
        Exception
            If the proposal is already submitted or has been rejected.
        """
        if self.status in ["Submitted", "Approved", "Rejected"]:
            raise Exception("Proposal cannot be submitted again.")
        self.status = "Submitted"

    def approve_proposal(self):
        """
        Approves the proposal, changing its status.

        Raises
        ------
        Exception
            If the proposal is not submitted.
        """
        if self.status != "Submitted":
            raise Exception("Proposal must be submitted before it can be approved.")
        self.status = "Approved"

    def reject_proposal(self):
        """
        Rejects the proposal, changing its status.

        Raises
        ------
        Exception
            If the proposal is not submitted.
        """
        if self.status != "Submitted":
            raise Exception("Proposal must be submitted before it can be rejected.")
        self.status = "Rejected"

    def __str__(self):
        """
        Returns a string representation of the governance proposal.
        """
        return f"Governance Proposal: {self.title}\n" \
               f"Proposer: {self.proposer}\n" \
               f"Status: {self.status}\n" \
               f"Description: {self.description}\n" \
               f"Fee Structure Changes: {self.fee_structure_changes}\n" \
               f"New Chain Integrations: {self.new_chain_integrations}"
```
