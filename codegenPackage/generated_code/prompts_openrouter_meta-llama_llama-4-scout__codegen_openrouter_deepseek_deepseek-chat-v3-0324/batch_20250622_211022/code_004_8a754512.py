"""
Generated Code Metadata:
========================
Original URL: https://voting-consensys.app
Prompt: Implement a blockchain-based voting mechanism using ConsenSys, with a focus on transparency and tamper-proofing.
Generated: DETERMINISTIC_8a754512bd637a7c
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

/**
 * @title VotingContract
 * @dev A blockchain-based voting system that ensures transparency and tamper-proofing
 */
contract VotingContract is Ownable {
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    struct Voter {
        bool hasVoted;
        uint256 vote;
    }

    uint256 public candidatesCount;
    mapping(uint256 => Candidate) public candidates;
    mapping(address => Voter) public voters;
    bool public votingOpen;

    event VoteCast(address indexed voter, uint256 candidateId);
    event CandidateAdded(uint256 indexed candidateId, string name);
    event VotingStatusChanged(bool votingOpen);

    /**
     * @dev Modifier to check if voting is open
     */
    modifier onlyWhenVotingOpen() {
        require(votingOpen, "Voting is currently closed");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        votingOpen = false;
    }

    /**
     * @dev Add a candidate to the voting system
     * @param _name Name of the candidate
     */
    function addCandidate(string memory _name) public onlyOwner {
        require(!votingOpen, "Cannot add candidates while voting is open");
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
        emit CandidateAdded(candidatesCount, _name);
    }

    /**
     * @dev Cast a vote for a candidate
     * @param _candidateId ID of the candidate to vote for
     */
    function vote(uint256 _candidateId) public onlyWhenVotingOpen {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        require(!voters[msg.sender].hasVoted, "You have already voted");

        voters[msg.sender] = Voter(true, _candidateId);
        candidates[_candidateId].voteCount++;

        emit VoteCast(msg.sender, _candidateId);
    }

    /**
     * @dev Toggle voting status (open/close)
     */
    function toggleVoting() public onlyOwner {
        votingOpen = !votingOpen;
        emit VotingStatusChanged(votingOpen);
    }

    /**
     * @dev Get the total votes for a candidate
     * @param _candidateId ID of the candidate
     * @return Total votes for the candidate
     */
    function getVotes(uint256 _candidateId) public view returns (uint256) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID");
        return candidates[_candidateId].voteCount;
    }

    /**
     * @dev Check if an address has voted
     * @param _voter Address to check
     * @return True if the address has voted, false otherwise
     */
    function hasVoted(address _voter) public view returns (bool) {
        return voters[_voter].hasVoted;
    }
}
```

```javascript
// File: scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  const VotingContract = await ethers.getContractFactory("VotingContract");
  const votingContract = await VotingContract.deploy();
  
  await votingContract.deployed();
  console.log("VotingContract deployed to:", votingContract.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// File: scripts/interact.js
const { ethers } = require("hardhat");

async function main() {
  const contractAddress = "YOUR_CONTRACT_ADDRESS";
  const VotingContract = await ethers.getContractFactory("VotingContract");
  const votingContract = await VotingContract.attach(contractAddress);

  // Example interactions
  const [owner, voter1] = await ethers.getSigners();

  // Add candidates (only owner)
  await votingContract.connect(owner).addCandidate("Candidate 1");
  await votingContract.connect(owner).addCandidate("Candidate 2");

  // Open voting
  await votingContract.connect(owner).toggleVoting();

  // Vote
  await votingContract.connect(voter1).vote(1);

  // Get results
  const votes = await votingContract.getVotes(1);
  console.log("Candidate 1 votes:", votes.toString());
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

```javascript
// File: test/VotingContract.test.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("VotingContract", function () {
  let VotingContract;
  let votingContract;
  let owner;
  let voter1;

  beforeEach(async function () {
    [owner, voter1] = await ethers.getSigners();
    VotingContract = await ethers.getContractFactory("VotingContract");
    votingContract = await VotingContract.deploy();
    await votingContract.deployed();
  });

  it("Should add candidates", async function () {
    await votingContract.addCandidate("Candidate 1");
    await votingContract.addCandidate("Candidate 2");
    expect(await votingContract.candidatesCount()).to.equal(2);
  });

  it("Should allow voting when open", async function () {
    await votingContract.addCandidate("Candidate 1");
    await votingContract.toggleVoting();
    await votingContract.connect(voter1).vote(1);
    expect(await votingContract.hasVoted(voter1.address)).to.be.true;
    expect(await votingContract.getVotes(1)).to.equal(1);
  });

  it("Should prevent double voting", async function () {
    await votingContract.addCandidate("Candidate 1");
    await votingContract.toggleVoting();
    await votingContract.connect(voter1).vote(1);
    await expect(votingContract.connect(voter1).vote(1)).to.be.revertedWith(
      "You have already voted"
    );
  });
});
```
