"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-io.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring double staking rewards functionality.
Generated: DETERMINISTIC_3f28537827c35bee
Batch ID: 20250612_150226
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PEPU tokens
contract PepeStaking is Ownable {
    // Token to be staked
    IERC20 public pepuToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
        bool isDoubleStaked; // Flag for double staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount, bool isDoubleStaked);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _pepuToken) {
        pepuToken = _pepuToken;
    }

    // Function to stake tokens
    function stake(uint256 amount, bool doubleStake) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pepuToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(pepuToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not set");

        // Transfer tokens from user to contract
        pepuToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            isDoubleStaked: doubleStake
        });

        emit Staked(msg.sender, amount, doubleStake);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards (dummy implementation, replace with actual logic)
        uint256 rewards = calculateRewards(msg.sender);

        // Reset user's stake
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens back to user
        pepuToken.transfer(msg.sender, amountToUnstake);

        // Transfer rewards to user
        if (rewards > 0) {
            pepuToken.transfer(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards based on staking duration and double staking
    function calculateRewards(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 duration = block.timestamp - userStake.timestamp;

        // Example reward calculation: 1% of staked amount per day
        uint256 dailyRewardRate = userStake.isDoubleStaked ? 200 : 100; // Double rewards if double staked
        uint256 rewards = (userStake.amount * dailyRewardRate * duration) / (1 days * 10000); // Adjust for percentage

        return rewards;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(pepuToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        pepuToken.transfer(msg.sender, amount);
    }
}
```
