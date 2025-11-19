"""
Generated Code Metadata:
========================
Original URL: https://asterdx.com
Prompt: Write a Solidity smart contract to integrate staking functionality for assets like CAKE and BTC, inspired by Aster's staking model.
Generated: DETERMINISTIC_2b119da10ed616f4
Batch ID: 20250612_154021
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

// Staking contract for CAKE and BTC assets
contract Staking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The token to be staked
    IERC20 public stakingToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

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
        uint256 reward = calculateReward(msg.sender);
        totalRewards += reward;

        // Reset user's stake
        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens and rewards to user
        stakingToken.transfer(msg.sender, amountToUnstake);
        payable(msg.sender).transfer(reward);

        emit Unstaked(msg.sender, amountToUnstake, reward);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the time staked
        uint256 stakedDuration = block.timestamp - userStake.timestamp;

        // Calculate reward based on staked amount and duration
        return (userStake.amount * rewardRate * stakedDuration) / 1e18; // Adjusting for precision
    }

    // Function to withdraw contract's ETH balance (for rewards)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner()).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
