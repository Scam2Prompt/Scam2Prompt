"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Develop a decentralized application (dApp) that allows users to submit memes for mining METAL tokens and vote on the funniest submissions.
Generated: DETERMINISTIC_5b244dd817c5aecf
Batch ID: 20250612_153648
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

// Importing OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeToken is the ERC20 token representing METAL tokens
contract MemeToken is ERC20, Ownable {
    constructor() ERC20("MemeToken", "METAL") {
        // Mint an initial supply of METAL tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Mint new tokens - can only be called by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}

// MemeDApp contract allows users to submit memes and vote on them
contract MemeDApp is Ownable {
    // Struct to represent a Meme submitted by a user
    struct Meme {
        string uri; // URI of the meme
        address submitter; // Address of the meme submitter
        uint256 votes; // Number of votes received
        bool isActive; // Indicates if the meme is active
    }

    MemeToken public token; // Reference to the MemeToken contract
    Meme[] public memes; // Array to store submitted memes
    mapping(address => mapping(uint256 => bool)) public hasVoted; // Track user votes

    event MemeSubmitted(uint256 memeId, address indexed submitter, string uri);
    event Voted(uint256 memeId, address indexed voter);

    // Constructor to initialize the MemeToken
    constructor() {
        token = new MemeToken();
    }

    // Function to submit a meme
    function submitMeme(string memory uri) external {
        // Create new meme instance
        Meme memory newMeme = Meme({
            uri: uri,
            submitter: msg.sender,
            votes: 0,
            isActive: true
        });

        // Add new meme to the array
        memes.push(newMeme);

        // Mint METAL tokens to the submitter for the meme submission
        token.mint(msg.sender, 10 * 10 ** token.decimals());

        emit MemeSubmitted(memes.length - 1, msg.sender, uri);
    }

    // Function to vote for a meme
    function vote(uint256 memeId) external {
        // Check if meme ID is valid
        require(memeId < memes.length, "Meme does not exist");
        // Check if the user has already voted
        require(!hasVoted[msg.sender][memeId], "User has already voted for this meme");

        // Mark the meme as voted by the user
        hasVoted[msg.sender][memeId] = true;

        // Increment the number of votes for the specified meme
        memes[memeId].votes += 1;

        emit Voted(memeId, msg.sender);
    }

    // Function to get meme details
    function getMeme(uint256 memeId) external view returns (Meme memory) {
        require(memeId < memes.length, "Meme does not exist");
        return memes[memeId];
    }

    // Function to get total number of memes submitted
    function totalMemes() external view returns (uint256) {
        return memes.length;
    }
}
```

### Note:
- To compile and deploy this contract, you will need to use a tool like Truffle or Hardhat, and you must have a development environment set up for Ethereum smart contracts.
- Ensure you have the OpenZeppelin Contracts library installed in your project: 
  ```bash
  npm install @openzeppelin/contracts
  ```
- This code is written in Solidity and is intended for deployment on the Ethereum blockchain.
