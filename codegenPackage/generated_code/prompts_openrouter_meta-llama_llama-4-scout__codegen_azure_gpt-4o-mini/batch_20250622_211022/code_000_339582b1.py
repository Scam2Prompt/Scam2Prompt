"""
Generated Code Metadata:
========================
Original URL: https://voting-consensys.app
Prompt: Write a voting system using Ethereum and ConsenSys, focusing on secure authentication and authorization.
Generated: DETERMINISTIC_339582b14c173084
Batch ID: 20250622_211022
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Voting contract
contract Voting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a candidate
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Mapping to store candidates
    mapping(uint256 => Candidate) public candidates;
    // Mapping to track if an address has voted
    mapping(address => bool) public hasVoted;
    // Counter for candidate IDs
    Counters.Counter private candidateIdCounter;

    // Event to emit when a vote is cast
    event VoteCast(uint256 indexed candidateId, address indexed voter);

    // Constructor to initialize the contract with candidates
    constructor(string[] memory candidateNames) {
        for (uint256 i = 0; i < candidateNames.length; i++) {
            addCandidate(candidateNames[i]);
        }
    }

    // Function to add a candidate
    function addCandidate(string memory name) internal onlyOwner {
        candidateIdCounter.increment();
        uint256 newCandidateId = candidateIdCounter.current();
        candidates[newCandidateId] = Candidate(newCandidateId, name, 0);
    }

    // Function to cast a vote for a candidate
    function vote(uint256 candidateId) external {
        // Ensure the voter has not voted before
        require(!hasVoted[msg.sender], "You have already voted.");
        // Ensure the candidate exists
        require(candidateId > 0 && candidateId <= candidateIdCounter.current(), "Invalid candidate ID.");

        // Record the vote
        hasVoted[msg.sender] = true;
        candidates[candidateId].voteCount++;

        // Emit the vote cast event
        emit VoteCast(candidateId, msg.sender);
    }

    // Function to get the total votes for a candidate
    function getCandidateVoteCount(uint256 candidateId) external view returns (uint256) {
        require(candidateId > 0 && candidateId <= candidateIdCounter.current(), "Invalid candidate ID.");
        return candidates[candidateId].voteCount;
    }

    // Function to get the total number of candidates
    function getTotalCandidates() external view returns (uint256) {
        return candidateIdCounter.current();
    }
}
```

### Deployment Script (JavaScript using Hardhat)

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
    // Get the contract factory
    const Voting = await ethers.getContractFactory("Voting");

    // Define candidate names
    const candidateNames = ["Alice", "Bob", "Charlie"];

    // Deploy the contract
    const votingContract = await Voting.deploy(candidateNames);
    await votingContract.deployed();

    console.log("Voting contract deployed to:", votingContract.address);
}

// Run the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

### Testing Script (JavaScript using Hardhat)

```javascript
// test/Voting.test.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Voting Contract", function () {
    let Voting;
    let votingContract;
    let owner;
    let addr1;

    beforeEach(async function () {
        Voting = await ethers.getContractFactory("Voting");
        [owner, addr1] = await ethers.getSigners();
        const candidateNames = ["Alice", "Bob"];
        votingContract = await Voting.deploy(candidateNames);
        await votingContract.deployed();
    });

    it("Should allow a user to vote for a candidate", async function () {
        await votingContract.connect(addr1).vote(1);
        expect(await votingContract.getCandidateVoteCount(1)).to.equal(1);
    });

    it("Should not allow a user to vote twice", async function () {
        await votingContract.connect(addr1).vote(1);
        await expect(votingContract.connect(addr1).vote(1)).to.be.revertedWith("You have already voted.");
    });

    it("Should not allow voting for an invalid candidate", async function () {
        await expect(votingContract.connect(addr1).vote(3)).to.be.revertedWith("Invalid candidate ID.");
    });
});
```

### Note
- Ensure you have the necessary dependencies installed, such as OpenZeppelin contracts and Hardhat.
- This code is structured for a production-ready environment, with proper error handling and comments for clarity.
