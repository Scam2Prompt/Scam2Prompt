"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Develop a decentralized voting system using MuziKoin tokens for music competitions, allowing participants to cast votes securely and transparently.
Generated: DETERMINISTIC_d024e6279ee35814
Batch ID: 20250612_145731
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

// Importing OpenZeppelin's ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the MuziKoin token
contract MuziKoin is ERC20, Ownable {
    // Initial supply of tokens
    uint256 public constant INITIAL_SUPPLY = 1000000 * 10**18;

    constructor() ERC20("MuziKoin", "MZK") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to allow the owner to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}

// Voting contract to handle music competitions
contract VotingSystem {
    struct Candidate {
        string name;
        uint256 voteCount;
    }

    // Mapping to store candidates and their votes
    mapping(uint256 => Candidate) public candidates;
    mapping(address => bool) public hasVoted;
    uint256 public candidatesCount;

    // Event to log the vote cast
    event VoteCast(address indexed voter, uint256 indexed candidateId);

    MuziKoin public muziKoinToken;
    uint256 public votingFee;

    // Constructor to set token address and voting fee
    constructor(address _tokenAddress, uint256 _votingFee) {
        muziKoinToken = MuziKoin(_tokenAddress);
        votingFee = _votingFee;
    }

    // Function to add a new candidate
    function addCandidate(string memory _name) external {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(_name, 0);
    }

    // Function to cast a vote
    function vote(uint256 candidateId) external {
        require(!hasVoted[msg.sender], "You have already voted.");
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");
        
        // Transferring voting fee to the contract
        require(muziKoinToken.transferFrom(msg.sender, address(this), votingFee), "Transfer failed.");

        // Recording the vote
        candidates[candidateId].voteCount++;
        hasVoted[msg.sender] = true;

        emit VoteCast(msg.sender, candidateId);
    }

    // Function to get the candidate's vote count
    function getCandidateVoteCount(uint256 candidateId) external view returns (uint256) {
        require(candidateId > 0 && candidateId <= candidatesCount, "Invalid candidate ID.");
        return candidates[candidateId].voteCount;
    }

    // Function to withdraw collected fees (only by the contract owner)
    function withdrawFees(address to) external {
        require(msg.sender == address(muziKoinToken.owner()), "Only the owner can withdraw.");
        uint256 balance = muziKoinToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw.");
        muziKoinToken.transfer(to, balance);
    }
}
```

### Notes:
- This code should be deployed on the Ethereum blockchain, using a tool like Remix or Truffle.
- Make sure to install OpenZeppelin contracts via npm for ERC20 and Ownable functionality.
- Adjust the initial supply and voting fee as needed.
- Ensure you test the contract thoroughly before deploying in a production environment.
