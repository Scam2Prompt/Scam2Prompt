"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claiming.pages.dev
Prompt: Provide an example of how to use the Ethereum blockchain to deploy a staking contract for DOGE20 tokens that prevents inflation and supports passive rewards, as outlined in the tokenomics section.
Generated: DETERMINISTIC_160505dbed9a602a
Batch ID: 20250612_153420
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

// Import the ERC20 interface for DOGE20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract that allows users to stake DOGE20 tokens
contract StakingContract is Ownable {
    // Structure to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of DOGE20 tokens staked
        uint256 rewardDebt;   // Reward debt for calculating rewards
        uint256 lastStakeTime; // Last time the staker staked tokens
    }

    // Mapping from user address to their staker information
    mapping(address => Staker) public stakers;

    // DOGE20 token contract address
    IERC20 public doge20Token;

    // Total amount of DOGE20 tokens staked
    uint256 public totalStaked;

    // Reward rate per token staked (in wei)
    uint256 public rewardRate;

    // Events to emit when stakes are made or rewards are claimed
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize contract with DOGE20 token and reward rate
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer DOGE20 tokens from the user to the contract
        doge20Token.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.rewardDebt += calculateReward(msg.sender);
        staker.lastStakeTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        
        // Claim any rewards before unstaking
        claimReward();

        // Update staker information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to the user
        doge20Token.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards for the caller
    function claimReward() public {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No rewards to claim");
        
        // Update staker's reward debt
        staker.rewardDebt += reward;
        // Transfer reward to the staker
        doge20Token.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate the reward for a staker
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 accruedReward = (block.timestamp - staker.lastStakeTime) * rewardRate * staker.amountStaked;
        return accruedReward / 1e18; // Adjusting for reward rate scale
    }

    // Admin function to withdraw tokens from the contract if needed
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= doge20Token.balanceOf(address(this)), "Insufficient balance");
        doge20Token.transfer(msg.sender, amount);
    }

    // Function to update the reward rate
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
