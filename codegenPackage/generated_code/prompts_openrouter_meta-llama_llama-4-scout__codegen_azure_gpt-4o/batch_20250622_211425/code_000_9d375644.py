"""
Generated Code Metadata:
========================
Original URL: https://grooveup.pages.dev
Prompt: Write a smart contract for a music streaming platform that rewards fans with tokenized rewards for streaming and sharing their favorite artist's songs.
Generated: DETERMINISTIC_9d375644190b6925
Batch ID: 20250622_211425
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

/**
 * @title MusicStreamingRewards
 * @dev A smart contract for a music streaming platform that rewards fans with tokenized rewards
 * for streaming and sharing their favorite artist's songs.
 */
contract MusicStreamingRewards {
    // Token used for rewards
    string public constant tokenName = "MusicFanToken";
    string public constant tokenSymbol = "MFT";
    uint8 public constant decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Mapping to track artist song streams
    mapping(address => mapping(string => uint256)) private songStreams;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are rewarded
    event TokensRewarded(address indexed user, uint256 amount);

    // Event emitted when a song is streamed
    event SongStreamed(address indexed user, string songId);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;
    }

    /**
     * @dev Function to stream a song and reward the user.
     * @param songId The ID of the song being streamed.
     */
    function streamSong(string memory songId) external {
        require(bytes(songId).length > 0, "Invalid song ID");

        // Increment the stream count for the song
        songStreams[msg.sender][songId] += 1;

        // Reward the user with tokens
        uint256 rewardAmount = calculateReward(songId);
        require(balances[owner] >= rewardAmount, "Insufficient reward tokens");

        balances[owner] -= rewardAmount;
        balances[msg.sender] += rewardAmount;

        emit SongStreamed(msg.sender, songId);
        emit TokensRewarded(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to calculate the reward for streaming a song.
     * @param songId The ID of the song being streamed.
     * @return The amount of tokens to reward.
     */
    function calculateReward(string memory songId) internal pure returns (uint256) {
        // Example reward calculation logic (can be customized)
        return 10 * (10**decimals); // Reward 10 tokens per stream
    }

    /**
     * @dev Function to check the balance of a user.
     * @param user The address of the user.
     * @return The token balance of the user.
     */
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Function to check the stream count for a specific song by a user.
     * @param user The address of the user.
     * @param songId The ID of the song.
     * @return The stream count for the song.
     */
    function getStreamCount(address user, string memory songId) external view returns (uint256) {
        return songStreams[user][songId];
    }

    /**
     * @dev Function to mint new tokens (only owner can mint).
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        totalSupply += amount;
        balances[owner] += amount;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
