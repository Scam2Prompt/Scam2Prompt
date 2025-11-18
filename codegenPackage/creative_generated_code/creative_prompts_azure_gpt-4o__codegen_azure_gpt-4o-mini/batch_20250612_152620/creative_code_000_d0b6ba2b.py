"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking pool similar to the AITECH staking tiers described on the webpage, including features like compounding rewards, NFT boosts, and tier-based reward percentages.
Generated: DETERMINISTIC_d0b6ba2b13ed8f8e
Batch ID: 20250612_152620
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

// Interface for the NFT contract to be used for boosts
interface INFTBoost {
    function getBoostMultiplier(address user) external view returns (uint256);
}

// StakingPool contract for managing the staking of tokens
contract StakingPool is Ownable {
    using SafeMath for uint256;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsEarned;
        uint256 lastStakedTime;
    }

    // Mapping of stakers' addresses to their information
    mapping(address => Staker) public stakers;
    mapping(address => bool) public hasStaked;
    
    // Variables for the token and NFT boost contract
    IERC20 public stakingToken;
    INFTBoost public nftBoost;
    
    // Reward tier percentages (in basis points)
    uint256[] public rewardTiers = [1000, 2000, 3000]; // 10%, 20%, 30%
    
    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking token and NFT boost contract
    constructor(IERC20 _stakingToken, INFTBoost _nftBoost) {
        stakingToken = _stakingToken;
        nftBoost = _nftBoost;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        // Update staker information
        stakers[msg.sender].amountStaked += _amount;
        stakers[msg.sender].lastStakedTime = block.timestamp;
        hasStaked[msg.sender] = true;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 _amount) external {
        require(hasStaked[msg.sender], "You have not staked any tokens");
        require(_amount > 0 && _amount <= stakers[msg.sender].amountStaked, "Invalid unstake amount");
        
        // Calculate and update rewards before unstaking
        _updateRewards(msg.sender);
        
        // Update staker information
        stakers[msg.sender].amountStaked -= _amount;
        
        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        require(hasStaked[msg.sender], "You have not staked any tokens");
        
        // Calculate and update rewards
        _updateRewards(msg.sender);
        
        // Transfer rewards to the user
        uint256 rewards = stakers[msg.sender].rewardsEarned;
        require(rewards > 0, "No rewards to claim");

        stakers[msg.sender].rewardsEarned = 0;
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to update rewards based on staking duration and NFT boosts
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        
        // Calculate time difference since last update
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        
        // Determine the reward tier based on amount staked
        uint256 tier = _getRewardTier(staker.amountStaked);
        uint256 boostMultiplier = nftBoost.getBoostMultiplier(_staker);
        
        // Calculate rewards earned during the staking period
        uint256 rewards = (staker.amountStaked * rewardTiers[tier] * timeStaked * boostMultiplier) / 1e18;
        
        // Update staker's rewards and last staking time
        staker.rewardsEarned += rewards;
        staker.lastStakedTime = block.timestamp;
    }

    // Function to get the reward tier based on the amount staked
    function _getRewardTier(uint256 _amount) internal view returns (uint256) {
        if (_amount < 1000 * 1e18) return 0; // Tier 1
        if (_amount < 5000 * 1e18) return 1; // Tier 2
        return 2; // Tier 3
    }

    // Function to view staker's information
    function getStakerInfo(address _staker) external view returns (uint256 amountStaked, uint256 rewardsEarned) {
        return (stakers[_staker].amountStaked, stakers[_staker].rewardsEarned);
    }
}
```
