"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Explain how to implement staking for $HEHE tokens to earn rewards, based on the staking details provided in the HEHE ecosystem.
Generated: DETERMINISTIC_3fe1cc621d62aaa0
Batch ID: 20250612_162325
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public HEHEToken;

    // Reward token (can be the same as HEHEToken)
    IERC20 public rewardToken;

    // Structure to hold staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastUpdated;
    }
    
    // Mapping of user addresses to their staking details
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per token staked (in rewardToken)
    uint256 public rewardPerToken;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(address _HEHEToken, address _rewardToken) {
        HEHEToken = IERC20(_HEHEToken);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(HEHEToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user stake
        updateReward(msg.sender);

        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].lastUpdated = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user reward before unstaking
        updateReward(msg.sender);

        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        require(HEHEToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");
        
        stakes[msg.sender].rewardDebt = 0;
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateReward(address user) internal {
        if (totalStaked > 0) {
            rewardPerToken = rewardPerToken.add(calculateRewardPerToken());
        }

        if (stakes[user].amount > 0) {
            uint256 pendingReward = stakes[user].amount.mul(rewardPerToken).sub(stakes[user].rewardDebt);
            stakes[user].rewardDebt = stakes[user].rewardDebt.add(pendingReward);
        }
        stakes[user].lastUpdated = block.timestamp;
    }

    // Function to calculate reward per token logic
    function calculateRewardPerToken() internal view returns (uint256) {
        // Logic for calculating the reward rate and the reward per token
        // This can be adjusted based on the tokenomics of the HEHE ecosystem
        return 1e18; // Example logic, replace with actual calculation
    }

    // Optional: Function to withdraw any mistakenly sent tokens to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(HEHEToken), "Cannot withdraw staked token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
