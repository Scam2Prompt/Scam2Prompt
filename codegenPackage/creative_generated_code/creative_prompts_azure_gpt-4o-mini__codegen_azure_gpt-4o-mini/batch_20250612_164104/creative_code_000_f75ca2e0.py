"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: How can I implement staking solutions for the $MAFIA token to reward community members in a cryptocurrency ecosystem?
Generated: DETERMINISTIC_f75ca2e079015614
Batch ID: 20250612_164104
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for secure token management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for the $MAFIA token
contract MafiaStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public mafiaToken;

    // User stakes mapping
    mapping(address => uint256) public stakes;

    // Total amount of staked tokens
    uint256 public totalStaked;

    // Reward rate in tokens per block
    uint256 public rewardRate = 1e18; // 1 MAFIA token per block

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Event to emit when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event to emit when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _mafiaToken) {
        mafiaToken = IERC20(_mafiaToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(mafiaToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        mafiaToken.transferFrom(msg.sender, address(this), amount);

        // Update user and total stakes
        stakes[msg.sender] = stakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update the stakes and total staked amount
        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the user
        mafiaToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update user rewards before claiming
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        mafiaToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate the user's rewards based on their staked amount
    function calculateReward(address user) internal view returns (uint256) {
        uint256 userStake = stakes[user];
        // Calculate reward based on the staked amount and reward rate
        return userStake.mul(rewardRate).div(1e18);
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= mafiaToken.balanceOf(address(this)), "Insufficient contract balance");
        mafiaToken.transfer(msg.sender, amount);
    }

    // Function to view user's staked amount
    function getUserStake(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
