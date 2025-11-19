"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Create a governance smart contract for a project on StarkNet, referencing the ecosystem's unique features.
Generated: DETERMINISTIC_bc77ad4076e4a177
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
# Governance Smart Contract for StarkNet
# This contract allows token holders to propose and vote on governance decisions.

%lang starknet

# Import necessary libraries
from starkware.cairo.common.math import assert_le
from starkware.cairo.common.uint256 import Uint256

# Contract storage variables
@storage_var
func total_proposals() -> (total: felt):
end

@storage_var
func proposal_details(proposal_id: felt) -> (description: felt, votes_for: felt, votes_against: felt, proposer: felt):
end

@storage_var
func has_voted(proposal_id: felt, voter: felt) -> (voted: felt):
end

# Events
@event
func ProposalCreated(proposal_id: felt, description: felt, proposer: felt):
end

@event
func VoteCast(proposal_id: felt, voter: felt, vote: felt):
end

@event
func ProposalExecuted(proposal_id: felt, result: felt):
end

# Contract constructor
@constructor
func constructor():
    # Initialize total proposals to 0
    total_proposals.write(0)
end

# Function to create a new proposal
@external
func create_proposal(description: felt):
    # Get the current total proposals
    let (current_total) = total_proposals.read()
    
    # Increment the total proposals
    let new_total = current_total + 1
    total_proposals.write(new_total)
    
    # Store the proposal details
    proposal_details.write(new_total, description, 0, 0, signer)
    
    # Emit ProposalCreated event
    ProposalCreated.emit(new_total, description, signer)
end

# Function to vote on a proposal
@external
func vote(proposal_id: felt, vote: felt):
    # Ensure the vote is valid (1 for "for", 0 for "against")
    assert_le(vote, 1)
    
    # Check if the voter has already voted
    let (voted) = has_voted.read(proposal_id, signer)
    if voted != 0:
        return_error("Already voted on this proposal")
    end
    
    # Mark the voter as having voted
    has_voted.write(proposal_id, signer, 1)
    
    # Update the vote counts
    let (description, votes_for, votes_against, proposer) = proposal_details.read(proposal_id)
    if vote == 1:
        proposal_details.write(proposal_id, description, votes_for + 1, votes_against, proposer)
    else:
        proposal_details.write(proposal_id, description, votes_for, votes_against + 1, proposer)
    end
    
    # Emit VoteCast event
    VoteCast.emit(proposal_id, signer, vote)
end

# Function to execute a proposal
@external
func execute_proposal(proposal_id: felt):
    # Retrieve proposal details
    let (description, votes_for, votes_against, proposer) = proposal_details.read(proposal_id)
    
    # Ensure the proposal has more votes for than against
    if votes_for <= votes_against:
        return_error("Proposal rejected")
    end
    
    # Emit ProposalExecuted event
    ProposalExecuted.emit(proposal_id, 1)  # 1 indicates success
end

# Helper function for error handling
func return_error(message: felt):
    # Emit an error message (optional, depending on StarkNet's event system)
    # Error.emit(message)
    return ()
end
```
