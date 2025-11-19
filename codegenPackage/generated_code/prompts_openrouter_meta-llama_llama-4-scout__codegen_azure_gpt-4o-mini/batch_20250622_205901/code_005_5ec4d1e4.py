"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-es.web.app
Prompt: Design a staking rewards system for $PEPU tokens on Pepe Unchained, taking into account the double staking rewards and 100x faster transaction processing compared to Ethereum.
Generated: DETERMINISTIC_5ec4d1e453cd2c03
Batch ID: 20250622_205901
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

// StakingRewards contract for managing staking and rewards for $PEPU tokens
contract StakingRewards is Ownable {
    // Token being staked
    IERC20 public pepuToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (in $PEPU tokens)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt += calculatePendingRewards(msg.sender);
        staker.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update the staker's information
        staker.rewardDebt += calculatePendingRewards(msg.sender);
        staker.amount -= amount;
        totalStaked -= amount;

        require(pepuToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Update the staker's reward debt
        stakers[msg.sender].rewardDebt += pendingRewards;

        require(pepuToken.transfer(msg.sender, pendingRewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to calculate pending rewards for a staker
    function calculatePendingRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amount * rewardRate * timeStaked) / 1e18; // Adjusting for precision
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(pepuToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
