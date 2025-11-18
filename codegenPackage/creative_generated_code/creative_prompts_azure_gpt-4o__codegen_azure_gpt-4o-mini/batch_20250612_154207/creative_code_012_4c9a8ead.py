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
pragma solidity ^0.8.0;

// Importing required interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Voting contract implementing a decentralized voting system
contract DecentralizedVoting is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a candidate
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }

    // Mapping to store candidates
    mapping(uint256 => Candidate) public candidates;
    // Mapping to track voters
    mapping(address => bool) public voters;
    // Counter for candidates
    Counters.Counter private candidateIdCounter;
    // Event to emit when a new candidate is added
    event CandidateAdded(uint256 id, string name);
    // Event to emit when a new vote is cast
    event Voted(uint256 candidateId);

    // Function to add a new candidate
    function addCandidate(string memory _name) external onlyOwner {
        require(bytes(_name).length > 0, "Candidate name must not be empty.");

        candidateIdCounter.increment();
        uint256 candidateId = candidateIdCounter.current();

        candidates[candidateId] = Candidate(candidateId, _name, 0);
        emit CandidateAdded(candidateId, _name);
    }

    // Function to vote for a candidate
    function vote(uint256 _candidateId) external {
        require(!voters[msg.sender], "You have already voted.");
        require(_candidateId > 0 && _candidateId <= candidateIdCounter.current(), "Invalid candidate ID.");

        // Mark the sender as having voted
        voters[msg.sender] = true;
        // Increment the vote count for the selected candidate
        candidates[_candidateId].voteCount += 1;

        emit Voted(_candidateId);
    }

    // Function to get the total votes for a candidate
    function getCandidate(uint256 _candidateId) external view returns (string memory name, uint256 voteCount) {
        require(_candidateId > 0 && _candidateId <= candidateIdCounter.current(), "Invalid candidate ID.");

        Candidate memory candidate = candidates[_candidateId];
        return (candidate.name, candidate.voteCount);
    }

    // Function to get total number of candidates
    function getTotalCandidates() external view returns (uint256) {
        return candidateIdCounter.current();
    }
}
```

### Deployment Steps

1. **Install Dependencies**:
   Ensure you have the following installed:
   - Node.js
   - Truffle or Hardhat
   - OpenZeppelin Contracts library
   ```bash
   npm install @openzeppelin/contracts
   ```

2. **Compile the Contract**:
   If using Truffle:
   ```bash
   truffle compile
   ```

   If using Hardhat:
   ```bash
   npx hardhat compile
   ```

3. **Deploy the Contract**:
   Create a migration script in the `migrations` directory (for Truffle) or a deployment script in the `scripts` directory (for Hardhat).
   
   **Example for Truffle**:
   ```javascript
   const DecentralizedVoting = artifacts.require("DecentralizedVoting");

   module.exports = function (deployer) {
       deployer.deploy(DecentralizedVoting);
   };
   ```

   Then, deploy the contract using:
   ```bash
   truffle migrate --network <network_name>
   ```

   **Example for Hardhat**:
   Create a deployment script in `scripts/deploy.js`:
   ```javascript
   async function main() {
       const DecentralizedVoting = await ethers.getContractFactory("DecentralizedVoting");
       const voting = await DecentralizedVoting.deploy();
       console.log("DecentralizedVoting deployed to:", voting.address);
   }
   main()
       .then(() => process.exit(0))
       .catch((error) => {
           console.error(error);
           process.exit(1);
       });
   ```

   Then run:
   ```bash
   npx hardhat run scripts/deploy.js --network <network_name>
   ```

4. **Interact with the Contract**:
   Use Web3.js, Ethers.js, or a frontend framework to interact with the deployed contract, allowing users to add candidates and vote.
