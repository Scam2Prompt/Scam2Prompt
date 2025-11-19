"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-tokens.com
Prompt: Generate code for a smart contract that allows users to stake tokens and earn $PEPE rewards through a passive income system.
Generated: DETERMINISTIC_2b87f32f8b70fcf3
Batch ID: 20250612_163149
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingRewards {
    using SafeMath for uint256;

    // State variables
    IERC20 public stakingToken;  // The token that users will stake
    IERC20 public rewardToken;   // The token that users will earn as rewards
    uint256 public rewardRate;    // Reward rate per block
    uint256 public totalStaked;   // Total staked tokens
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards;       // Rewards earned by each user
    mapping(address => uint256) public lastUpdated;    // Last block number when rewards were updated

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any staking or unstaking
    modifier updateRewards() {
        if (stakedAmount[msg.sender] > 0) {
            rewards[msg.sender] = calculateRewards(msg.sender);
            lastUpdated[msg.sender] = block.number;
        }
        _;
    }

    // Stake tokens to earn rewards
    function stake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Amount must be greater than 0");
        totalStaked = totalStaked.add(_amount);
        stakedAmount[msg.sender] = stakedAmount[msg.sender].add(_amount);
        lastUpdated[msg.sender] = block.number;

        // Transfer staking tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        
        emit Staked(msg.sender, _amount);
    }

    // Unstake tokens and claim rewards
    function unstake(uint256 _amount) external updateRewards {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= _amount, "Insufficient staked amount");

        totalStaked = totalStaked.sub(_amount);
        stakedAmount[msg.sender] = stakedAmount[msg.sender].sub(_amount);
        
        // Transfer staking tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards for the user
    function claimRewards() external updateRewards {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        rewards[msg.sender] = 0; // Reset rewards
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Calculate the rewards for a user
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 staked = stakedAmount[_user];
        uint256 blocksPassed = block.number.sub(lastUpdated[_user]);
        return staked.mul(blocksPassed).mul(rewardRate).div(1e18); // Assuming reward rate is in a fixed point format
    }

    // View function to get user's staked amount
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakedAmount[_user];
    }

    // View function to get user's earned rewards
    function getRewards(address _user) external view returns (uint256) {
        return calculateRewards(_user).add(rewards[_user]);
    }
}
```
