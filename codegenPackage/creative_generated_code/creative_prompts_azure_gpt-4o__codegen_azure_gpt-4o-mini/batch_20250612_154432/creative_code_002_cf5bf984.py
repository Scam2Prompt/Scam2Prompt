"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-qdclhqzos-miketoken.vercel.app
Prompt: Generate code for creating a staking pool smart contract on the BNBChain, inspired by Mike Token's farming launch roadmap.
Generated: DETERMINISTIC_cf5bf9841bb443b9
Batch ID: 20250612_154432
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

contract StakingPool is Ownable {
    // Struct to store user staking details
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stake details
    mapping(address => Stake) public stakes;

    // Total amount of staked tokens
    uint256 public totalStaked;

    // The ERC20 token that can be staked
    IERC20 public stakingToken;

    // Reward rate per staked token per second
    uint256 public rewardRate;

    // Total rewards pool
    uint256 public totalRewards;

    // Event for staking
    event Staked(address indexed user, uint256 amount);

    // Event for unstaking
    event Unstaked(address indexed user, uint256 amount);

    // Event for claiming rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, uint256 _rewardRate, uint256 _totalRewards) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        totalRewards = _totalRewards;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update stake details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update stake details
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }
        return (userStake.amount * rewardRate * (block.timestamp - userStake.timestamp)) / 1e18;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");
        require(totalRewards >= rewards, "Not enough rewards in pool");

        // Update user's stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;
        totalRewards -= rewards;

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw remaining rewards by owner
    function withdrawRemainingRewards() external onlyOwner {
        uint256 remainingRewards = totalRewards;
        totalRewards = 0;
        stakingToken.transfer(msg.sender, remainingRewards);
    }
}
```
