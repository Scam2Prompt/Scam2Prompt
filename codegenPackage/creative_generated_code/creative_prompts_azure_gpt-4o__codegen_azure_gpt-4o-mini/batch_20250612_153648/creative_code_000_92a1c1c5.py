"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metalcoin.vercel.app
Prompt: Write a smart contract in Solidity that implements a "Proof of Hilarity" mechanism, where miners submit memes and the funniest meme is rewarded with METAL tokens.
Generated: DETERMINISTIC_92a1c1c565de3802
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

/// @title Proof of Hilarity Smart Contract
/// @author Your Name
/// @notice This contract allows users to submit memes and rewards the funniest meme with METAL tokens
/// @dev This contract is intended for educational purposes and may require further testing and auditing before production use

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ProofOfHilarity is Ownable {
    struct Meme {
        address submitter;
        string content;
        uint256 votes;
    }

    // Event to emit when a meme is submitted
    event MemeSubmitted(uint256 indexed memeId, address indexed submitter, string content);
    // Event to emit when a meme is voted on
    event MemeVoted(uint256 indexed memeId, address indexed voter);
    // Event to emit when the winner is declared
    event WinnerDeclared(uint256 indexed memeId, address indexed winner, uint256 reward);

    // Array of memes
    Meme[] public memes;
    // Mapping of voters to voted memes to prevent double voting
    mapping(address => mapping(uint256 => bool)) public hasVoted;
    // ERC20 token for rewards
    IERC20 public metalToken;
    
    // Constructor to set the METAL token contract address
    constructor(address _metalTokenAddress) {
        require(_metalTokenAddress != address(0), "Invalid token address");
        metalToken = IERC20(_metalTokenAddress);
    }

    /// @notice Submit a new meme
    /// @param content The content of the meme
    function submitMeme(string calldata content) external {
        require(bytes(content).length > 0, "Meme content cannot be empty");
        
        // Create a new meme and add it to the array
        memes.push(Meme({
            submitter: msg.sender,
            content: content,
            votes: 0
        }));
        
        emit MemeSubmitted(memes.length - 1, msg.sender, content);
    }

    /// @notice Vote for a meme
    /// @param memeId The ID of the meme to vote for
    function voteMeme(uint256 memeId) external {
        require(memeId < memes.length, "Invalid meme ID");
        require(!hasVoted[msg.sender][memeId], "You have already voted for this meme");

        // Record the vote
        memes[memeId].votes++;
        hasVoted[msg.sender][memeId] = true;

        emit MemeVoted(memeId, msg.sender);
    }

    /// @notice Declare the winner based on votes and reward them with METAL tokens
    function declareWinner() external onlyOwner {
        require(memes.length > 0, "No memes submitted");

        uint256 winningMemeId;
        uint256 highestVotes = 0;

        // Determine the meme with the highest votes
        for (uint256 i = 0; i < memes.length; i++) {
            if (memes[i].votes > highestVotes) {
                highestVotes = memes[i].votes;
                winningMemeId = i;
            }
        }

        // Check if the contract has enough METAL tokens to reward the winner
        uint256 rewardAmount = 100 * 10**18; // Reward amount, can be adjusted
        require(metalToken.balanceOf(address(this)) >= rewardAmount, "Insufficient METAL tokens in contract");

        // Transfer METAL tokens to the winner
        address winner = memes[winningMemeId].submitter;
        metalToken.transfer(winner, rewardAmount);

        emit WinnerDeclared(winningMemeId, winner, rewardAmount);
    }

    /// @notice Get the total number of memes submitted
    /// @return The total number of memes
    function getTotalMemes() external view returns (uint256) {
        return memes.length;
    }

    /// @notice Get a meme by its ID
    /// @param memeId The ID of the meme
    /// @return The meme details
    function getMeme(uint256 memeId) external view returns (Meme memory) {
        require(memeId < memes.length, "Invalid meme ID");
        return memes[memeId];
    }
}
```
