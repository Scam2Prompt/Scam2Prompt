"""
Generated Code Metadata:
========================
Original URL: https://snap-metis.pages.dev
Prompt: Create a simple example of a decentralized application (dApp) that leverages Metis' Community Ecosystem Governance for decision-making processes.
Generated: DETERMINISTIC_bbafd596423912fd
Batch ID: 20250612_160656
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

import "@metis.io/contracts/community/CommunityGovernance.sol";

/**
 * @title SimpleGovernanceDAO
 * @dev A simple DAO that uses Metis' Community Ecosystem Governance for decision-making
 */
contract SimpleGovernanceDAO is CommunityGovernance {
    struct Proposal {
        string description;
        uint256 voteCount;
        uint256 deadline;
        bool executed;
        mapping(address => bool) voters;
    }

    Proposal[] public proposals;
    uint256 public proposalCount;

    // Minimum voting period in seconds (e.g., 3 days)
    uint256 public constant MIN_VOTING_PERIOD = 3 days;

    event ProposalCreated(uint256 proposalId, string description, uint256 deadline);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Initialize the contract with Metis Community Governance
     * @param _communityToken The address of the community token used for voting
     */
    constructor(address _communityToken) CommunityGovernance(_communityToken) {}

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _votingPeriod Duration of voting period in seconds
     */
    function createProposal(string memory _description, uint256 _votingPeriod) external onlyMember {
        require(_votingPeriod >= MIN_VOTING_PERIOD, "Voting period too short");
        
        uint256 deadline = block.timestamp + _votingPeriod;
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.deadline = deadline;
        newProposal.executed = false;
        
        emit ProposalCreated(proposalCount, _description, deadline);
        proposalCount++;
    }

    /**
     * @dev Vote on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _support Whether to support the proposal
     */
    function vote(uint256 _proposalId, bool _support) external onlyMember {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp <= proposal.deadline, "Voting period ended");
        require(!proposal.voters[msg.sender], "Already voted");
        
        uint256 votingPower = getVotingPower(msg.sender);
        require(votingPower > 0, "No voting power");
        
        proposal.voters[msg.sender] = true;
        if (_support) {
            proposal.voteCount += votingPower;
        }
        
        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        
        require(block.timestamp > proposal.deadline, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        
        uint256 totalSupply = getTotalSupply();
        require(proposal.voteCount > totalSupply / 2, "Not enough votes");
        
        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For this example, we just emit an event
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get voting power of an address
     * @param _member Address to check
     * @return Voting power
     */
    function getVotingPower(address _member) public view returns (uint256) {
        return balanceOf(_member);
    }

    /**
     * @dev Get total token supply
     * @return Total supply
     */
    function getTotalSupply() public view returns (uint256) {
        return totalSupply();
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return description, voteCount, deadline, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        string memory description,
        uint256 voteCount,
        uint256 deadline,
        bool executed
    ) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.description,
            proposal.voteCount,
            proposal.deadline,
            proposal.executed
        );
    }
}
```
