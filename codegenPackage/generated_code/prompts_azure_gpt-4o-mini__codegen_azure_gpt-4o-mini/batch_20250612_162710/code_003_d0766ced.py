"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Provide an example of a smart contract that could be used in a project developed during the ETHBerlin04 hackathon, focusing on community initiatives.
Generated: DETERMINISTIC_d0766ced5c652c2f
Batch ID: 20250612_162710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Community Initiative Fund Smart Contract
/// @notice This contract allows community members to propose and fund initiatives
/// @dev The contract uses a simple voting mechanism for proposal approval

contract CommunityInitiativeFund {
    // Struct to represent a community initiative proposal
    struct Proposal {
        uint256 id;
        string description;
        address proposer;
        uint256 fundingGoal;
        uint256 currentFunding;
        bool isActive;
        mapping(address => uint256) contributions;
    }

    // State variables
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => uint256) public balances;

    // Events
    event ProposalCreated(uint256 id, string description, address proposer, uint256 fundingGoal);
    event Funded(uint256 proposalId, address contributor, uint256 amount);
    event ProposalFinalized(uint256 proposalId, bool funded);

    /// @notice Create a new proposal for community funding
    /// @param _description The description of the initiative
    /// @param _fundingGoal The funding goal for the initiative
    function createProposal(string memory _description, uint256 _fundingGoal) public {
        require(_fundingGoal > 0, "Funding goal must be greater than zero");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.proposer = msg.sender;
        newProposal.fundingGoal = _fundingGoal;
        newProposal.isActive = true;

        emit ProposalCreated(proposalCount, _description, msg.sender, _fundingGoal);
    }

    /// @notice Contribute to a specific proposal
    /// @param _proposalId The ID of the proposal to fund
    function fundProposal(uint256 _proposalId) public payable {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.isActive, "Proposal is not active");
        require(msg.value > 0, "Contribution must be greater than zero");

        proposal.currentFunding += msg.value;
        proposal.contributions[msg.sender] += msg.value;
        balances[msg.sender] += msg.value;

        emit Funded(_proposalId, msg.sender, msg.value);

        // Check if the funding goal has been reached
        if (proposal.currentFunding >= proposal.fundingGoal) {
            finalizeProposal(_proposalId);
        }
    }

    /// @notice Finalize a proposal if the funding goal is reached
    /// @param _proposalId The ID of the proposal to finalize
    function finalizeProposal(uint256 _proposalId) internal {
        Proposal storage proposal = proposals[_proposalId];
        require(proposal.isActive, "Proposal is not active");
        require(proposal.currentFunding >= proposal.fundingGoal, "Funding goal not reached");

        proposal.isActive = false;

        // Transfer funds to the proposer
        payable(proposal.proposer).transfer(proposal.currentFunding);

        emit ProposalFinalized(_proposalId, true);
    }

    /// @notice Withdraw funds from the contract
    function withdraw() public {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No funds to withdraw");

        balances[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }

    /// @notice Get the details of a proposal
    /// @param _proposalId The ID of the proposal
    /// @return id The ID of the proposal
    /// @return description The description of the proposal
    /// @return proposer The address of the proposer
    /// @return fundingGoal The funding goal of the proposal
    /// @return currentFunding The current funding amount
    /// @return isActive The status of the proposal
    function getProposal(uint256 _proposalId) public view returns (
        uint256 id,
        string memory description,
        address proposer,
        uint256 fundingGoal,
        uint256 currentFunding,
        bool isActive
    ) {
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.proposer,
            proposal.fundingGoal,
            proposal.currentFunding,
            proposal.isActive
        );
    }
}
```
