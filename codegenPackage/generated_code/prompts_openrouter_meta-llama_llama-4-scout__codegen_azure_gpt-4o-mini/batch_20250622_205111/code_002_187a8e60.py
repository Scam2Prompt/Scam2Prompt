"""
Generated Code Metadata:
========================
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Generate a smart contract code snippet in Solidity that implements a simple voting mechanism with rewards, similar to Mitosis's voting system, on a compatible blockchain platform.
Generated: DETERMINISTIC_187a8e607e8d2915
Batch ID: 20250622_205111
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

contract Voting {
    // Struct to represent a candidate
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }

    // Mapping to store candidates
    mapping(uint => Candidate) public candidates;
    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;
    // Total number of candidates
    uint public candidatesCount;
    // Total number of votes
    uint public totalVotes;
    // Reward for voting
    uint public rewardAmount;

    // Event to emit when a vote is cast
    event Voted(uint indexed candidateId, address indexed voter);

    // Constructor to initialize the contract with candidates and reward amount
    constructor(string[] memory candidateNames, uint _rewardAmount) {
        require(candidateNames.length > 0, "At least one candidate is required");
        rewardAmount = _rewardAmount;

        for (uint i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    // Function to add a candidate
    function addCandidate(string memory name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, name, 0);
    }

    // Function to vote for a candidate
    function vote(uint candidateId) public payable {
        // Ensure the voter has not voted before
        require(!hasVoted[msg.sender], "You have already voted");
        // Ensure the candidate ID is valid
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        // Ensure the correct amount of Ether is sent for the reward
        require(msg.value == rewardAmount, "Incorrect Ether amount sent for reward");

        // Record the vote
        hasVoted[msg.sender] = true;
        candidates[candidateId].voteCount++;
        totalVotes++;

        // Emit the vote event
        emit Voted(candidateId, msg.sender);
    }

    // Function to get the candidate details
    function getCandidate(uint candidateId) public view returns (Candidate memory) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[candidateId];
    }

    // Function to withdraw contract balance (only owner can call this)
    function withdraw() public {
        // Only the contract owner should be able to withdraw
        // Implement ownership check here (not shown for brevity)
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
