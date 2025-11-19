"""
Generated Code Metadata:
========================
Original URL: https://groovesup.pages.dev
Prompt: "Write a smart contract for a music streaming platform that rewards fans with tokenized rewards for streaming and sharing their favorite artist's songs."
Generated: DETERMINISTIC_9c9c08c40a302073
Batch ID: 20250622_204943
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a music streaming platform that rewards fans with tokens
contract MusicStreamingRewards is ERC20, Ownable {
    // Mapping to track the number of streams per user
    mapping(address => uint256) public streams;

    // Event emitted when a user streams a song
    event SongStreamed(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MusicRewardToken", "MRT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to reward users for streaming a song
    function streamSong() external {
        // Increment the stream count for the user
        streams[msg.sender] += 1;

        // Reward the user with tokens for streaming
        uint256 rewardAmount = calculateReward(streams[msg.sender]);
        _mint(msg.sender, rewardAmount);

        // Emit an event for the streamed song
        emit SongStreamed(msg.sender, rewardAmount);
    }

    // Function to calculate the reward based on the number of streams
    function calculateReward(uint256 streamCount) internal pure returns (uint256) {
        // Reward logic: 10 tokens per stream
        return streamCount * 10 * 10 ** decimals();
    }

    // Function to allow users to share a song and receive rewards
    function shareSong() external {
        // Reward the user for sharing a song
        uint256 shareReward = 50 * 10 ** decimals(); // Fixed reward for sharing
        _mint(msg.sender, shareReward);

        // Emit an event for the shared song
        emit SongStreamed(msg.sender, shareReward);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to check the total streams of a user
    function getUserStreams(address user) external view returns (uint256) {
        return streams[user];
    }
}
```
