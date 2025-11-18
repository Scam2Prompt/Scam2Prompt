"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakelayerpresale.pages.dev
Prompt: Write a smart contract in Solidity for staking Bitcoin in StakeLayer's Layer 2 solution while ensuring compatibility with StakeLayer tokens.
Generated: DETERMINISTIC_6d95c8367857540d
Batch ID: 20250612_151057
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

// Importing the interface for the StakeLayer token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract StakeLayerStaking {
    // Address of the StakeLayer token contract
    IERC20 public stakeLayerToken;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping to track each staker's information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;
    
    // Reward rate (can be adjusted based on the project requirements)
    uint256 public rewardRate = 100; // Example reward rate per block

    // Event for staking
    event Staked(address indexed user, uint256 amount);
    
    // Event for unstaking 
    event Unstaked(address indexed user, uint256 amount);
    
    // Event for rewards claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the StakeLayer token address
    constructor(address _stakeLayerToken) {
        require(_stakeLayerToken != address(0), "Invalid token address");
        stakeLayerToken = IERC20(_stakeLayerToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from the user to the contract
        stakeLayerToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.rewardDebt += (_amount * rewardRate);

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update staker's information
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer the unstaked tokens back to the user
        stakeLayerToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Calculate rewards
        uint256 rewards = (staker.amountStaked * rewardRate) - staker.rewardDebt;
        require(rewards > 0, "No rewards available");

        // Update reward debt
        staker.rewardDebt += rewards;

        // Transfer rewards to the user (assume rewards are paid out in the same token)
        stakeLayerToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the staker's information
    function getStakerInfo(address _staker) external view returns (uint256 amountStaked, uint256 rewardDebt) {
        Staker storage staker = stakers[_staker];
        return (staker.amountStaked, staker.rewardDebt);
    }
}
```
