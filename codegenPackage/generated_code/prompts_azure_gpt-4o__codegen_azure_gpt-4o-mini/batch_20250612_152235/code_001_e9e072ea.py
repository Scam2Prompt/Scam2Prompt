"""
Generated Code Metadata:
========================
Original URL: https://pawfury-token.pages.dev
Prompt: Generate code to implement a staking mechanism for $PAW tokens, including functions to stake, unstake, and calculate APY rewards based on the PawFury tokenomics.
Generated: DETERMINISTIC_e9e072eaec8eb1e8
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PAW tokens
contract PawStaking is Ownable {
    // Token to be staked
    IERC20 public pawToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield (APY) in basis points (e.g., 500 = 5%)
    uint256 public apyBasisPoints;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the contract with the token and APY
    constructor(IERC20 _pawToken, uint256 _apyBasisPoints) {
        pawToken = _pawToken;
        apyBasisPoints = _apyBasisPoints;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pawToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        pawToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's stake amount
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens and rewards back to user
        pawToken.transfer(msg.sender, amountToUnstake + rewards);

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    // Function to calculate rewards based on the time staked and APY
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the duration the tokens have been staked
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on APY
        uint256 annualRewards = (userStake.amount * apyBasisPoints) / 10000; // Convert basis points to percentage
        uint256 rewards = (annualRewards * stakingDuration) / 365 days; // Calculate rewards for the staked duration

        return rewards;
    }

    // Function to update the APY (only owner can call)
    function updateAPY(uint256 newAPY) external onlyOwner {
        apyBasisPoints = newAPY;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= pawToken.balanceOf(address(this)), "Insufficient contract balance");
        pawToken.transfer(msg.sender, amount);
    }
}
```
