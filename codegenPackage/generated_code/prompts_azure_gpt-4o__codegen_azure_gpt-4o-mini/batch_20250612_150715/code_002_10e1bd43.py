"""
Generated Code Metadata:
========================
Original URL: https://galaxyfoxs.live
Prompt: Develop a staking rewards system in Solidity inspired by Galaxy Fox, where the staking pool is funded by transaction fees and the treasury supports token deflation.
Generated: DETERMINISTIC_10e1bd4384f2fd82
Batch ID: 20250612_150715
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;
    // Reward token
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;
    // Mapping of user stakes
    mapping(address => uint256) public stakes;
    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // Reward rate per block
    uint256 public rewardRate;
    // Last update block for rewards
    mapping(address => uint256) public lastUpdateBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] = earned(account);
            lastUpdateBlock[account] = block.number;
        }
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked = totalStaked.add(amount);
        stakes[msg.sender] = stakes[msg.sender].add(amount);
        stakingToken.transferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");
        totalStaked = totalStaked.sub(amount);
        stakes[msg.sender] = stakes[msg.sender].sub(amount);
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return stakes[account]
            .mul(block.number.sub(lastUpdateBlock[account]))
            .mul(rewardRate)
            .div(1e18);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken && token != rewardToken, "Cannot withdraw staking or reward tokens");
        token.transfer(msg.sender, amount);
    }
}
```
