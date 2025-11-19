"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki-reward.com
Prompt: Create a smart contract for staking FLOKI tokens that rewards users with the TOKEN sister token.
Generated: DETERMINISTIC_1b06a0a5f206f41f
Batch ID: 20250612_135654
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

// Importing necessary dependencies from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for FLOKI token that rewards users with TOKEN
contract FlokiStaking is Ownable {
    // State variables
    IERC20 public flokiToken; // The FLOKI token contract
    IERC20 public rewardToken; // The TOKEN contract that rewards users
    uint256 public rewardRate; // Rewards per block for staking
    uint256 public totalStaked; // Total amount of FLOKI tokens staked

    // Staker information
    struct Staker {
        uint256 amount; // Amount of FLOKI staked
        uint256 rewardDebt; // Reward debt for the staker
    }
    
    mapping(address => Staker) public stakers; // Mapping to track stakers

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ClaimedReward(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the contract with token addresses and reward rate
    constructor(IERC20 _flokiToken, IERC20 _rewardToken, uint256 _rewardRate) {
        flokiToken = _flokiToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake FLOKI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(flokiToken.balanceOf(msg.sender) >= amount, "Insufficient FLOKI balance");
        
        // Transfer FLOKI tokens from user to contract
        flokiToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt += calculatePendingReward(msg.sender);
        
        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake FLOKI tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update staker's information
        staker.rewardDebt += calculatePendingReward(msg.sender);
        staker.amount -= amount;
        totalStaked -= amount;

        // Transfer FLOKI tokens back to the user
        flokiToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards in TOKEN
    function claimReward() external {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculatePendingReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update reward debt
        staker.rewardDebt = 0;

        // Transfer reward tokens to the user
        rewardToken.transfer(msg.sender, reward);

        emit ClaimedReward(msg.sender, reward);
    }

    // Internal function to calculate pending rewards
    function calculatePendingReward(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amount * rewardRate) - staker.rewardDebt;
    }

    // Function to withdraw tokens in case of contract termination
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }

    // Function to update the reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
