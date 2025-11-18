"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-station-2.gitbook.io
Prompt: Create a smart contract for managing $SOON token rewards in a gaming ecosystem, referencing TON Station's token utility and exchange features.
Generated: DETERMINISTIC_4fb46c3272a8c719
Batch ID: 20250612_153915
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SoonTokenRewards is Ownable {
    // Constants
    IERC20 public soonToken;  // Reference to the $SOON token contract
    uint256 public rewardRate; // Rate at which rewards are distributed

    // Mapping to store player rewards
    mapping(address => uint256) public rewards;

    // Event to log rewards distribution
    event RewardsDistributed(address indexed player, uint256 amount);

    // Error messages for revert
    error InsufficientFunds(uint256 requested, uint256 available);
    error InvalidAddress();
    error InvalidRate();

    // Constructor to initialize the token contract address and reward rate
    constructor(address _soonToken, uint256 _rewardRate) {
        if (_soonToken == address(0)) revert InvalidAddress();
        if (_rewardRate == 0) revert InvalidRate();

        soonToken = IERC20(_soonToken);
        rewardRate = _rewardRate;
    }

    // Function to distribute rewards to players
    function distributeRewards(address player, uint256 gameResult) external onlyOwner {
        if (player == address(0)) revert InvalidAddress();

        // Calculate rewards based on game result and reward rate
        uint256 rewardAmount = gameResult * rewardRate;
        rewards[player] += rewardAmount;

        // Emit event for logging
        emit RewardsDistributed(player, rewardAmount);
    }

    // Function to claim accumulated rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        if (rewardAmount == 0) revert InsufficientFunds(rewardAmount, 0);

        rewards[msg.sender] = 0;

        // Transfer $SOON tokens to the player
        bool success = soonToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");
    }

    // Function to set a new reward rate (onlyOwner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        if (newRate == 0) revert InvalidRate();
        rewardRate = newRate;
    }

    // Function to withdraw any tokens sent to the contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(soonToken), "Cannot withdraw $SOON tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw $SOON tokens from the contract (onlyOwner)
    function withdrawSoonTokens(uint256 amount) external onlyOwner {
        uint256 balance = soonToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient $SOON token balance");
        bool success = soonToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
