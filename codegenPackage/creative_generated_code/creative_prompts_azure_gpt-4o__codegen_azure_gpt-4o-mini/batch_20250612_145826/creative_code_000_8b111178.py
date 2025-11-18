"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Write a smart contract for a multichain token similar to $FROP, ensuring transparency and security. Include functionality for staking and rewards as described in the Popo ecosystem.
Generated: DETERMINISTIC_8b111178c907c577
Batch ID: 20250612_145826
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the staking functionality
interface IStaking {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function calculateRewards(address staker) external view returns (uint256);
}

// Multichain Token contract with staking and rewards functionality
contract MultiChainToken is ERC20, Ownable, IStaking {
    using SafeMath for uint256;

    // Mapping to track staked balances and rewards
    mapping(address => uint256) private stakedBalances;
    mapping(address => uint256) private rewards;
    
    // Total staked balance
    uint256 private totalStaked;
    
    // Reward rate per block
    uint256 public rewardRate = 1e18; // Example: 1 token per block

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    constructor() ERC20("MultiChainToken", "MCT") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10**decimals());
    }

    // Function to stake tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Update staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        
        // Emit event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external override {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);
        
        // Emit event
        emit Unstaked(msg.sender, amount);
    }

    // Calculate rewards for a specific staker
    function calculateRewards(address staker) external view override returns (uint256) {
        return (block.number - rewards[staker]) * rewardRate; // Placeholder for actual reward calculation
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer rewards to the user
        _mint(msg.sender, reward);

        // Reset rewards
        rewards[msg.sender] = block.number;

        // Emit event
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to view staked balance
    function stakedBalanceOf(address account) external view returns (uint256) {
        return stakedBalances[account];
    }

    // Function to view total staked tokens
    function totalStakedTokens() external view returns (uint256) {
        return totalStaked;
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 rate) external onlyOwner {
        rewardRate = rate;
    }
}
```
