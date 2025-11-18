"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchainrewards.pages.dev
Prompt: Write a smart contract in Solidity to manage voting and reward distribution in a decentralized web3 application, similar to the "RewardClaim" platform.
Generated: DETERMINISTIC_c74578629b415d68
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Voting and Reward Distribution Smart Contract
/// @author Your Name
/// @notice This contract allows users to vote and claim rewards based on their vote weight.
contract RewardClaim {

    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    mapping(uint => Candidate) public candidates; // Maps candidate ID to Candidate struct
    mapping(address => uint) public rewards; // Maps user address to their claimable rewards
    mapping(address => bool) public hasVoted; // Tracks if an address has already voted

    uint public candidatesCount; // Total number of candidates
    uint public totalVotes; // Total votes cast
    address public owner; // Contract owner

    event CandidateAdded(uint id, string name);
    event Voted(address indexed voter, uint indexed candidateId);
    event RewardClaimed(address indexed claimant, uint amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasNotVoted() {
        require(!hasVoted[msg.sender], "You have already voted");
        _;
    }

    /// @dev Constructor to set the contract creator as the owner
    constructor() {
        owner = msg.sender;
    }

    /// @dev Adds a new candidate to the election
    /// @param _name The name of the candidate
    function addCandidate(string memory _name) public onlyOwner {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
        emit CandidateAdded(candidatesCount, _name);
    }

    /// @dev Allows a user to cast their vote for a candidate
    /// @param _candidateId The ID of the candidate to vote for
    function vote(uint _candidateId) public hasNotVoted {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");

        // Update the candidate's vote count and total votes
        candidates[_candidateId].voteCount++;
        totalVotes++;
        hasVoted[msg.sender] = true;

        // Calculate rewards based on votes
        rewards[msg.sender] += calculateReward(candidates[_candidateId].voteCount);
        
        emit Voted(msg.sender, _candidateId);
    }

    /// @dev Calculates reward based on the number of votes received by the candidate
    /// @param _voteCount The number of votes received by the candidate
    /// @return The calculated reward
    function calculateReward(uint _voteCount) internal pure returns (uint) {
        // Simple reward system: 1 token per vote
        return _voteCount; // Adjust logic as needed for production use
    }

    /// @dev Allows a user to claim their rewards
    function claimReward() public {
        uint rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward balance
        rewards[msg.sender] = 0;

        // Logic for transferring rewards (e.g., ERC20 token transfer) goes here
        // For example, ERC20(tokenAddress).transfer(msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /// @dev Returns the total number of votes for a candidate
    /// @param _candidateId The ID of the candidate
    /// @return The total number of votes for the candidate
    function getCandidateVotes(uint _candidateId) public view returns (uint) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[_candidateId].voteCount;
    }
}
```
