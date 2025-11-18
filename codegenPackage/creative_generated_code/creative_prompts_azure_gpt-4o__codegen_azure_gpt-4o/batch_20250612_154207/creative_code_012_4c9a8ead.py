"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://43jeeil.pages.dev
Prompt: Write a Solidity contract that leverages Scroll's zkEVM compatibility to implement a decentralized voting system. Include deployment steps.
Generated: DETERMINISTIC_4c9a8eadf3369b8a
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title Decentralized Voting System
 * @dev A decentralized voting system that leverages zkEVM compatibility for efficient on-chain computation.
 */
contract DecentralizedVoting {

    // Struct to represent a candidate
    struct Candidate {
        string name;         // Candidate's name
        uint256 voteCount;   // Number of votes received
    }

    // Struct to represent voter details
    struct Voter {
        bool hasVoted;       // Tracks if the voter has already voted
        uint256 candidateId; // Candidate ID the voter voted for
    }

    // Array of candidates
    Candidate[] public candidates;

    // Mapping to track voter details
    mapping(address => Voter) public voters;

    // Address of the contract owner
    address public owner;

    // Event for logging when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed candidateId);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param candidateNames Names of the candidates participating in the election.
     */
    constructor(string[] memory candidateNames) {
        owner = msg.sender;
        for (uint256 i = 0; i < candidateNames.length; i++) {
            candidates.push(Candidate({
                name: candidateNames[i],
                voteCount: 0
            }));
        }
    }

    /**
     * @dev Function to cast a vote.
     * @param candidateId ID of the candidate to vote for (index in the candidates array).
     */
    function vote(uint256 candidateId) external {
        // Ensure the candidate ID is valid
        require(candidateId < candidates.length, "Invalid candidate ID.");

        // Ensure the voter has not already voted
        require(!voters[msg.sender].hasVoted, "You have already voted.");

        // Record the voter's details
        voters[msg.sender] = Voter({
            hasVoted: true,
            candidateId: candidateId
        });

        // Increment the vote count for the selected candidate
        candidates[candidateId].voteCount++;

        // Emit the event for logging
        emit VoteCast(msg.sender, candidateId);
    }

    /**
     * @dev Function to retrieve the total number of candidates.
     * @return The number of candidates.
     */
    function getCandidateCount() external view returns (uint256) {
        return candidates.length;
    }

    /**
     * @dev Function to retrieve details of a specific candidate.
     * @param candidateId ID of the candidate (index in the candidates array).
     * @return Candidate details (name and vote count).
     */
    function getCandidate(uint256 candidateId) external view returns (string memory name, uint256 voteCount) {
        require(candidateId < candidates.length, "Invalid candidate ID.");
        Candidate memory candidate = candidates[candidateId];
        return (candidate.name, candidate.voteCount);
    }

    /**
     * @dev Function to retrieve if the voter has voted and for whom.
     * @param voter Address of the voter.
     * @return Voter details (hasVoted and candidateId).
     */
    function getVoter(address voter) external view returns (bool hasVoted, uint256 candidateId) {
        Voter memory voterDetails = voters[voter];
        return (voterDetails.hasVoted, voterDetails.candidateId);
    }
}
```

### Deployment Steps:

1. **Set up the development environment**:
   Install the required tools such as Node.js, npm, Hardhat, and the Scroll zkEVM-compatible network configuration.

2. **Install dependencies**:
   ```bash
   npm install --save-dev hardhat @openzeppelin/contracts
   ```

3. **Create the deployment script**:
   Add a `deploy.js` file in the `scripts` directory.
   ```javascript
   const hre = require("hardhat");

   async function main() {
       const VotingContract = await hre.ethers.getContractFactory("DecentralizedVoting");
       const candidateNames = ["Alice", "Bob", "Charlie"];
       const votingContract = await VotingContract.deploy(candidateNames);

       await votingContract.deployed();
       console.log("Voting contract deployed to:", votingContract.address);
   }

   main().catch((error) => {
       console.error(error);
       process.exitCode = 1;
   });
   ```

4. **Configure Scroll zkEVM network** in Hardhat:
   Update the `hardhat.config.js` file to include Scroll's zkEVM configuration.

5. **Compile the contract**:
   ```bash
   npx hardhat compile
   ```

6. **Deploy the contract**:
   ```bash
   npx hardhat run scripts/deploy.js --network scroll
   ```
