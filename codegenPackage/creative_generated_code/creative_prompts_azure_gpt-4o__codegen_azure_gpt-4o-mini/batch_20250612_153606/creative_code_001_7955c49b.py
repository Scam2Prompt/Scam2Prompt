"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao.web.app
Prompt: Create a smart contract in Solidity that facilitates staking $MBDAO tokens and calculates ecosystem rewards based on Moonboots DAO's enhanced staking/voting rights.
Generated: DETERMINISTIC_7955c49b8d868a0e
Batch ID: 20250612_153606
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

// Interface for the MBDAO token
interface IMBDAO is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for MBDAO tokens
contract MBDAOSmartStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold user staking data
    struct Staker {
        uint256 amount;            // Amount of tokens staked
        uint256 rewardDebt;        // Reward debt for calculating pending rewards
        uint256 lastUpdate;        // Last time the user staked/updated
    }

    // Mapping of user addresses to their staking data
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token
    IMBDAO public rewardToken;

    // Reward rate per block
    uint256 public rewardRate;

    // Event for staking
    event Staked(address indexed user, uint256 amount);

    // Event for unstaking
    event Unstaked(address indexed user, uint256 amount);

    // Event for claiming rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /// @param _rewardToken Address of the MBDAO token contract
    /// @param _rewardRate Reward rate per block
    constructor(IMBDAO _rewardToken, uint256 _rewardRate) {
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /// @notice Stake tokens in the contract
    /// @param amount Amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        updateReward(msg.sender);

        staker.amount = staker.amount.add(amount);
        totalStaked = totalStaked.add(amount);
        staker.lastUpdate = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /// @notice Unstake tokens from the contract
    /// @param amount Amount of tokens to unstake
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        updateReward(msg.sender);

        staker.amount = staker.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /// @notice Claim accumulated rewards
    function claimRewards() external {
        updateReward(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 pendingReward = staker.rewardDebt;

        require(pendingReward > 0, "No rewards to claim");
        staker.rewardDebt = 0;

        rewardToken.mint(msg.sender, pendingReward);

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    /// @notice Update the reward for a user
    /// @param user Address of the user to update rewards
    function updateReward(address user) internal {
        Staker storage staker = stakers[user];
        uint256 pendingReward = calculateReward(user);
        staker.rewardDebt = pendingReward;

        // Update the last stake time
        staker.lastUpdate = block.timestamp;
    }

    /// @notice Calculate the reward based on staked amount and time
    /// @param user Address of the user
    /// @return uint256 The calculated reward
    function calculateReward(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 timeStaked = block.timestamp.sub(staker.lastUpdate);
        return staker.amount.mul(rewardRate).mul(timeStaked).div(1 days);
    }
}
```
