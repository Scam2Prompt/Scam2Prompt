"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Provide an example of a decentralized voting system in Solidity where METAL token holders can vote on the funniest memes.
Generated: DETERMINISTIC_576ae7d9512282ed
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

// Importing OpenZeppelin's ERC20 interface for METAL token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MemeVoting {
    // Struct to represent a meme
    struct Meme {
        uint256 id;
        string content; // Link or description of the meme
        uint256 voteCount;
    }

    // Mapping to store all memes
    mapping(uint256 => Meme) public memes;
    // Mapping to track voters and their votes
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    
    // Address of the METAL token contract
    IERC20 public metalToken;
    uint256 public totalMemes; // Count of total memes submitted

    // Event to emit when a new meme is added
    event MemeAdded(uint256 indexed memeId, string content);
    // Event to emit when a vote is cast
    event Voted(uint256 indexed memeId, address indexed voter);

    // Constructor to set the METAL token address
    constructor(address _metalTokenAddress) {
        require(_metalTokenAddress != address(0), "Invalid token address");
        metalToken = IERC20(_metalTokenAddress);
    }

    // Function to add a new meme
    function addMeme(string calldata content) external {
        totalMemes++;
        memes[totalMemes] = Meme(totalMemes, content, 0);
        emit MemeAdded(totalMemes, content);
    }

    // Function to vote for a meme
    function vote(uint256 memeId) external {
        require(memeId > 0 && memeId <= totalMemes, "Invalid meme ID");
        require(!hasVoted[memeId][msg.sender], "You have already voted for this meme");

        // Ensure the voter holds at least 1 METAL token
        require(metalToken.balanceOf(msg.sender) > 0, "You must hold METAL tokens to vote");

        // Mark that the voter has voted for the meme
        hasVoted[memeId][msg.sender] = true;
        // Increment the vote count for the meme
        memes[memeId].voteCount++;

        emit Voted(memeId, msg.sender);
    }

    // Function to get the details of a meme
    function getMeme(uint256 memeId) external view returns (Meme memory) {
        require(memeId > 0 && memeId <= totalMemes, "Invalid meme ID");
        return memes[memeId];
    }

    // Function to get the total number of memes
    function getTotalMemes() external view returns (uint256) {
        return totalMemes;
    }
}
```
