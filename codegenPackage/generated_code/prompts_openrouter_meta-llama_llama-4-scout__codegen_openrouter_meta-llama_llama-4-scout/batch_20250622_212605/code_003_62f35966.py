"""
Generated Code Metadata:
========================
Original URL: https://thesoniclabs.pages.dev
Prompt: Design a decentralized application (dApp) that leverages Sonic's scalability, storage, and low latency features, and provide a code snippet in Vyper to demonstrate the dApp's functionality.
Generated: DETERMINISTIC_62f35966decbed0c
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vyper
# @version ^0.2.0

# Import necessary libraries
import vyper
from vyper.interfaces import ERC20

# Define the dApp's interface
# @external
# @nonreentrant
contract DecentralizedApp:
    """
    A decentralized application leveraging Sonic's scalability, storage, and low latency features.

    This contract demonstrates a simple decentralized voting system.
    """

    # Define the voting system structure
    struct Vote:
        voter: address
        vote: bool

    # Define the mapping of users to their votes
    votes: public(map(address, Vote))

    # Define the mapping of proposals to their vote counts
    proposals: public(map(bytes32, uint256))

    # Define the event for voting
    event VoteCast(address indexed voter, bytes32 indexed proposal, bool vote)

    # Define the event for proposal creation
    event ProposalCreated(bytes32 indexed proposal)

    # Create a new proposal
    @external
    def create_proposal(_proposal: bytes32) -> None:
        """
        Creates a new proposal.

        :param _proposal: The hash of the proposal
        """
        # Check if the proposal already exists
        if _proposal in self.proposals:
            raise Exception("Proposal already exists")

        # Initialize the vote count to 0
        self.proposals[_proposal] = 0

        # Emit the ProposalCreated event
        log ProposalCreated(_proposal)

    # Cast a vote on a proposal
    @external
    def cast_vote(_proposal: bytes32, _vote: bool) -> None:
        """
        Casts a vote on a proposal.

        :param _proposal: The hash of the proposal
        :param _vote: The vote (True for yes, False for no)
        """
        # Check if the proposal exists
        if _proposal not in self.proposals:
            raise Exception("Proposal does not exist")

        # Get the sender's address
        sender: address = msg.sender

        # Check if the sender has already voted
        if sender in self.votes:
            raise Exception("Sender has already voted")

        # Initialize the vote
        self.votes[sender] = Vote(sender, _vote)

        # Update the vote count
        if _vote:
            self.proposals[_proposal] += 1

        # Emit the VoteCast event
        log VoteCast(sender, _proposal, _vote)

    # Get the vote count for a proposal
    @view
    @external
    def get_vote_count(_proposal: bytes32) -> uint256:
        """
        Gets the vote count for a proposal.

        :param _proposal: The hash of the proposal
        :return: The vote count
        """
        # Check if the proposal exists
        if _proposal not in self.proposals:
            raise Exception("Proposal does not exist")

        # Return the vote count
        return self.proposals[_proposal]

    # Get the user's vote
    @view
    @external
    def get_user_vote(_user: address) -> Vote:
        """
        Gets the user's vote.

        :param _user: The user's address
        :return: The user's vote
        """
        # Check if the user has voted
        if _user not in self.votes:
            raise Exception("User has not voted")

        # Return the user's vote
        return self.votes[_user]
```
