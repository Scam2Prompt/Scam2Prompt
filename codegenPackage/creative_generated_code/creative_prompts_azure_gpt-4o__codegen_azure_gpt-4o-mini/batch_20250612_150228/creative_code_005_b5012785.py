"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiczpwanmgphpygnz5deao4wexw2ip67u6bkdknegn5xbeqqzgg5re.ipfs.dweb.link
Prompt: Write a smart contract to implement a voting mechanism similar to the Mitosis Rewards system.
Generated: DETERMINISTIC_b5012785b551fa8e
Batch ID: 20250612_150228
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

contract MitosisVoting {
    // State variables
    struct Candidate {
        string name;
        uint voteCount;
    }

    address public owner;
    mapping(uint => Candidate) public candidates;
    mapping(address => bool) public voters;
    uint public candidatesCount;
    uint public totalVotes;

    // Events
    event CandidateAdded(uint candidateId, string name);
    event Voted(uint candidateId, address voter);

    // Modifier to restrict functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to add a candidate
    function addCandidate(string memory _name) public onlyOwner {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(_name, 0);
        emit CandidateAdded(candidatesCount, _name);
    }

    // Function to vote for a specific candidate
    function vote(uint _candidateId) public {
        // Ensure the voter hasn't voted before
        require(!voters[msg.sender], "You have already voted");
        // Ensure the candidate ID is valid
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");

        // Update the vote count and mark the voter as having voted
        candidates[_candidateId].voteCount++;
        voters[msg.sender] = true;
        totalVotes++;

        emit Voted(_candidateId, msg.sender);
    }

    // Function to get the candidate's details
    function getCandidate(uint _candidateId) public view returns (string memory name, uint voteCount) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        Candidate memory candidate = candidates[_candidateId];
        return (candidate.name, candidate.voteCount);
    }

    // Function to get the total number of votes
    function getTotalVotes() public view returns (uint) {
        return totalVotes;
    }

    // Function to check if an address has voted
    function hasVoted(address _voter) public view returns (bool) {
        return voters[_voter];
    }
}
```
