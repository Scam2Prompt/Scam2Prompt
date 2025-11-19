"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: Provide a code example for implementing the governance voting mechanism in the Rangers Protocol, focusing on proposal submission and voting.
Generated: DETERMINISTIC_3d7446f51ba86bd1
Batch ID: 20250612_135144
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Governance is Ownable {
    using SafeMath for uint256;

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 createTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    // Minimum voting period in seconds (e.g., 3 days)
    uint256 public constant MIN_VOTING_PERIOD = 3 days;
    
    // Minimum quorum required for proposal to pass (e.g., 30%)
    uint256 public constant QUORUM_PERCENTAGE = 30;
    
    // Minimum votes required for proposal to pass (e.g., 51%)
    uint256 public constant VOTE_THRESHOLD = 51;

    // Array of all proposals
    Proposal[] public proposals;
    
    // Mapping of proposal ID to proposal index
    mapping(uint256 => uint256) public proposalIndex;

    // Event declarations
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 createTime,
        uint256 endTime
    );
    
    event VoteCast(
        address indexed voter,
        uint256 indexed proposalId,
        bool support,
        uint256 weight
    );
    
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _votingPeriod Duration of voting period in seconds
     */
    function createProposal(
        string memory _description,
        uint256 _votingPeriod
    ) external {
        require(
            _votingPeriod >= MIN_VOTING_PERIOD,
            "Voting period too short"
        );
        require(
            bytes(_description).length > 0,
            "Description cannot be empty"
        );

        uint256 proposalId = proposals.length;
        uint256 endTime = block.timestamp.add(_votingPeriod);

        Proposal storage newProposal = proposals.push();
        newProposal.id = proposalId;
        newProposal.proposer = msg.sender;
        newProposal.description = _description;
        newProposal.createTime = block.timestamp;
        newProposal.endTime = endTime;
        newProposal.forVotes = 0;
        newProposal.againstVotes = 0;
        newProposal.executed = false;

        proposalIndex[proposalId] = proposalId;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            _description,
            block.timestamp,
            endTime
        );
    }

    /**
     * @dev Cast a vote on a proposal
     * @param _proposalId ID of the proposal
     * @param _support True if voting in support, false if voting against
     */
    function castVote(uint256 _proposalId, bool _support) external {
        require(
            _proposalId < proposals.length,
            "Invalid proposal ID"
        );
        
        Proposal storage proposal = proposals[_proposalId];
        
        require(
            block.timestamp <= proposal.endTime,
            "Voting period has ended"
        );
        
        require(
            !proposal.voters[msg.sender],
            "Already voted"
        );

        // In a real implementation, you would check token balance or stake here
        uint256 voteWeight = 1; // Simplified - assume each address gets 1 vote

        if (_support) {
            proposal.forVotes = proposal.forVotes.add(voteWeight);
        } else {
            proposal.againstVotes = proposal.againstVotes.add(voteWeight);
        }

        proposal.voters[msg.sender] = true;

        emit VoteCast(
            msg.sender,
            _proposalId,
            _support,
            voteWeight
        );
    }

    /**
     * @dev Execute a proposal if voting was successful
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(
            _proposalId < proposals.length,
            "Invalid proposal ID"
        );
        
        Proposal storage proposal = proposals[_proposalId];
        
        require(
            block.timestamp > proposal.endTime,
            "Voting period not ended"
        );
        
        require(
            !proposal.executed,
            "Proposal already executed"
        );

        uint256 totalVotes = proposal.forVotes.add(proposal.againstVotes);
        uint256 quorum = totalVotes.mul(QUORUM_PERCENTAGE).div(100);
        
        require(
            totalVotes >= quorum,
            "Quorum not reached"
        );
        
        require(
            proposal.forVotes.mul(100).div(totalVotes) >= VOTE_THRESHOLD,
            "Vote threshold not reached"
        );

        proposal.executed = true;

        // In a real implementation, you would execute the proposal actions here
        // For example: call another contract, transfer funds, etc.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get proposal count
     * @return Number of proposals created
     */
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details
     * @param _proposalId ID of the proposal
     * @return id, proposer, description, createTime, endTime, forVotes, againstVotes, executed
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        address proposer,
        string memory description,
        uint256 createTime,
        uint256 endTime,
        uint256 forVotes,
        uint256 againstVotes,
        bool executed
    ) {
        require(
            _proposalId < proposals.length,
            "Invalid proposal ID"
        );
        
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.proposer,
            proposal.description,
            proposal.createTime,
            proposal.endTime,
            proposal.forVotes,
            proposal.againstVotes,
            proposal.executed
        );
    }
}
```
