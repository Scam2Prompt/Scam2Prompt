"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-flockerz-com.pages.dev
Prompt: Provide an example of a smart contract that implements a decentralized voting system for $FLOCK token holders, ensuring rewards are distributed based on participation.
Generated: DETERMINISTIC_8645b35674b4221a
Batch ID: 20250612_154239
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DecentralizedVoting is Ownable {
    // Struct to hold information about each candidate
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Mapping from candidate ID to Candidate struct
    mapping(uint256 => Candidate) public candidates;
    uint256 public candidatesCount;

    // Mapping to track whether an address has voted
    mapping(address => bool) public hasVoted;

    // Token used for staking in the voting process
    IERC20 public flockToken;
    uint256 public rewardPerVote; // Reward distributed per vote

    // Event emitted when a new candidate is added
    event CandidateAdded(uint256 id, string name);

    // Event emitted when a vote is cast
    event VoteCast(address voter, uint256 candidateId);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address voter, uint256 amount);

    // Constructor to initialize the contract with the FLOCK token address and reward amount
    constructor(address _flockToken, uint256 _rewardPerVote) {
        flockToken = IERC20(_flockToken);
        rewardPerVote = _rewardPerVote;
    }

    // Function to add a candidate for voting
    function addCandidate(string memory _name) public onlyOwner {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
        emit CandidateAdded(candidatesCount, _name);
    }

    // Function to vote for a candidate
    function vote(uint256 _candidateId) public {
        require(!hasVoted[msg.sender], "You have already voted.");
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID.");

        // Mark that the voter has voted
        hasVoted[msg.sender] = true;

        // Increment the vote count for the candidate
        candidates[_candidateId].voteCount++;

        // Distribute rewards to the voter
        uint256 rewardAmount = rewardPerVote;
        require(flockToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance for rewards.");

        // Transfer reward tokens to the voter
        flockToken.transfer(msg.sender, rewardAmount);
        emit VoteCast(msg.sender, _candidateId);
        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    // Function to get the total votes for a candidate
    function getCandidateVoteCount(uint256 _candidateId) public view returns (uint256) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID.");
        return candidates[_candidateId].voteCount;
    }

    // Function to withdraw tokens from the contract in case of emergencies
    function withdrawTokens(address _to, uint256 _amount) public onlyOwner {
        require(_to != address(0), "Invalid address.");
        require(flockToken.balanceOf(address(this)) >= _amount, "Insufficient balance.");
        flockToken.transfer(_to, _amount);
    }

    // Function to update reward per vote
    function updateRewardPerVote(uint256 _newReward) public onlyOwner {
        rewardPerVote = _newReward;
    }
}
```
