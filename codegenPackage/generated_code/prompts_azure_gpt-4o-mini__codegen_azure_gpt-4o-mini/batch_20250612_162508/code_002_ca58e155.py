"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Create a smart contract in Solidity that implements the Proof of Hilarity mechanism for the METAL token, allowing miners to submit memes for rewards.
Generated: DETERMINISTIC_ca58e155dfd101d5
Batch ID: 20250612_162508
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

// Importing OpenZeppelin's ERC20 implementation for the METAL token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the METAL token with Proof of Hilarity mechanism
contract MetalToken is ERC20, Ownable {
    // Struct to hold meme submission details
    struct Meme {
        string content; // The content of the meme
        address submitter; // Address of the meme submitter
        uint256 votes; // Number of votes received
        bool exists; // Check if the meme exists
    }

    // Mapping to store memes by their ID
    mapping(uint256 => Meme) public memes;
    // Counter for meme IDs
    uint256 public memeCount;
    // Mapping to track votes for each meme
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // Event emitted when a new meme is submitted
    event MemeSubmitted(uint256 indexed memeId, address indexed submitter, string content);
    // Event emitted when a meme is voted on
    event MemeVoted(uint256 indexed memeId, address indexed voter);

    // Constructor to initialize the METAL token
    constructor() ERC20("METAL", "MTL") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to submit a meme
    function submitMeme(string memory _content) external {
        require(bytes(_content).length > 0, "Meme content cannot be empty");

        // Increment meme count and create a new meme
        memeCount++;
        memes[memeCount] = Meme({
            content: _content,
            submitter: msg.sender,
            votes: 0,
            exists: true
        });

        emit MemeSubmitted(memeCount, msg.sender, _content);
    }

    // Function to vote for a meme
    function voteMeme(uint256 _memeId) external {
        require(memes[_memeId].exists, "Meme does not exist");
        require(!hasVoted[_memeId][msg.sender], "You have already voted for this meme");

        // Record the vote
        hasVoted[_memeId][msg.sender] = true;
        memes[_memeId].votes++;

        // Reward the voter with METAL tokens
        _mint(msg.sender, 10 * 10 ** decimals()); // Reward of 10 METAL tokens

        emit MemeVoted(_memeId, msg.sender);
    }

    // Function to get the details of a meme
    function getMeme(uint256 _memeId) external view returns (Meme memory) {
        require(memes[_memeId].exists, "Meme does not exist");
        return memes[_memeId];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance");
        _transfer(address(this), msg.sender, amount);
    }
}
```
