"""
Generated Code Metadata:
========================
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Write a smart contract to implement a voting mechanism similar to the Mitosis Rewards system.
Generated: DETERMINISTIC_b5012785b551fa8e
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MitosisVoting is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    // Struct to represent a voter
    struct Voter {
        bool voted;
        uint256 vote;
        uint256 weight;
    }

    // Mapping of proposal ID to Proposal
    mapping(uint256 => Proposal) public proposals;
    
    // Mapping of voter address to Voter
    mapping(address => Voter) public voters;
    
    // Array of all proposal IDs
    uint256[] public proposalIds;
    
    // Minimum voting duration in seconds
    uint256 public minVotingDuration;
    
    // Maximum voting duration in seconds
    uint256 public maxVotingDuration;
    
    // Total number of proposals
    uint256 public proposalCount;
    
    // Event emitted when a new proposal is created
    event ProposalCreated(
        uint256 id,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    
    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 proposalId, uint256 weight);
    
    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    constructor(uint256 _minVotingDuration, uint256 _maxVotingDuration) {
        require(_minVotingDuration > 0, "Duration must be positive");
        require(_maxVotingDuration > _minVotingDuration, "Max must be greater than min");
        
        minVotingDuration = _minVotingDuration;
        maxVotingDuration = _maxVotingDuration;
    }

    /**
     * @dev Create a new proposal
     * @param _description Description of the proposal
     * @param _duration Duration of the voting period in seconds
     */
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(_duration >= minVotingDuration && _duration <= maxVotingDuration, "Invalid duration");
        
        uint256 proposalId = proposalCount++;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime.add(_duration);
        
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: _description,
            voteCount: 0,
            startTime: startTime,
            endTime: endTime,
            executed: false
        });
        
        proposalIds.push(proposalId);
        emit ProposalCreated(proposalId, _description, startTime, endTime);
    }

    /**
     * @dev Vote for a proposal
     * @param _proposalId ID of the proposal to vote for
     * @param _weight Voting weight (e.g., token amount)
     */
    function vote(uint256 _proposalId, uint256 _weight) external nonReentrant {
        require(_proposalId < proposalCount, "Invalid proposal ID");
        require(_weight > 0, "Weight must be positive");
        
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.executed, "Proposal already executed");
        
        Voter storage voter = voters[msg.sender];
        require(!voter.voted, "Already voted");
        
        voter.voted = true;
        voter.vote = _proposalId;
        voter.weight = _weight;
        
        proposal.voteCount = proposal.voteCount.add(_weight);
        
        emit VoteCast(msg.sender, _proposalId, _weight);
    }

    /**
     * @dev Execute a proposal after voting has ended
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external nonReentrant {
        require(_proposalId < proposalCount, "Invalid proposal ID");
        
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > 0, "No votes cast");
        
        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example, distributing rewards or executing a function call
        
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get all proposal IDs
     * @return Array of proposal IDs
     */
    function getAllProposalIds() external view returns (uint256[] memory) {
        return proposalIds;
    }

    /**
     * @dev Get proposal details by ID
     * @param _proposalId ID of the proposal
     * @return Proposal details
     */
    function getProposal(uint256 _proposalId) external view returns (
        uint256 id,
        string memory description,
        uint256 voteCount,
        uint256 startTime,
        uint256 endTime,
        bool executed
    ) {
        require(_proposalId < proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (
            proposal.id,
            proposal.description,
            proposal.voteCount,
            proposal.startTime,
            proposal.endTime,
            proposal.executed
        );
    }

    /**
     * @dev Update voting duration limits (only owner)
     * @param _min New minimum duration
     * @param _max New maximum duration
     */
    function updateVotingDurations(uint256 _min, uint256 _max) external onlyOwner {
        require(_min > 0, "Duration must be positive");
        require(_max > _min, "Max must be greater than min");
        
        minVotingDuration = _min;
        maxVotingDuration = _max;
    }
}
```
