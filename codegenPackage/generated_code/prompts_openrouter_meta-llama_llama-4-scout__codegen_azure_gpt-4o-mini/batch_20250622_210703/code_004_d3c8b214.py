"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-en.web.app
Prompt: Develop a simple smart contract in Solidity for staking Poodl Inu tokens on the Ethereum blockchain, including functions for staking, claiming rewards, and checking balances.
Generated: DETERMINISTIC_d3c8b214f7888ceb
Batch ID: 20250622_210703
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

// Importing the ERC20 interface for Poodl Inu token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Poodl Inu tokens
contract PoodlStaking is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // The Poodl Inu token contract
    IERC20 public poodlToken;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the Poodl Inu token address and reward rate
    constructor(IERC20 _poodlToken, uint256 _rewardRate) {
        poodlToken = _poodlToken;
        rewardRate = _rewardRate;
    }

    // Function to stake Poodl Inu tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(poodlToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate and claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked tokens");

        // Calculate rewards based on the time staked
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update the staker's reward debt
        staker.rewardDebt += rewards;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the staker
        require(poodlToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (timeStaked * rewardRate * staker.amountStaked) / 1e18; // Adjust for precision
    }

    // Function to check the staked balance of a user
    function stakedBalance(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to check the pending rewards of a user
    function pendingRewards(address user) external view returns (uint256) {
        return calculateRewards(user) + stakers[user].rewardDebt;
    }

    // Function to withdraw staked tokens (only owner can withdraw)
    function withdrawStakedTokens(uint256 amount) external onlyOwner {
        require(amount <= totalStaked, "Insufficient staked tokens");
        totalStaked -= amount;
        require(poodlToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
