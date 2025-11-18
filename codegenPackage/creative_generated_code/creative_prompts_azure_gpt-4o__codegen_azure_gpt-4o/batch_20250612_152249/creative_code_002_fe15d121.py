"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicbp4v36pb5mqdwiyqegjmf62ex6eneyd5bhgvnobirakblg5rkze.ipfs.dweb.link
Prompt: Provide an example of how to implement a staking mechanism for $MEME tokens, referencing the Memeland Stakeland functionality.
Generated: DETERMINISTIC_fe15d12126d90d10
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title MEME Token Staking Contract
 * @dev Implements a staking mechanism where users can stake MEME tokens and earn rewards.
 * Inspired by Memeland Stakeland functionality.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeTokenStaking is Ownable {
    IERC20 public memeToken;

    // Struct to track staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardDebt; // Rewards already accounted for
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    uint256 public rewardRate; // Reward rate per second (tokens per second per staked token)
    uint256 public totalStaked; // Total tokens staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the contract with the MEME token address and reward rate.
     * @param _memeToken Address of the MEME token contract.
     * @param _rewardRate Reward rate in tokens per second per staked token.
     */
    constructor(IERC20 _memeToken, uint256 _rewardRate) {
        require(address(_memeToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        memeToken = _memeToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake MEME tokens in the contract to earn rewards.
     * @param amount Number of MEME tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Calculate pending rewards for the user before updating stake
        uint256 pendingReward = calculateRewards(msg.sender);
        stakes[msg.sender].rewardDebt += pendingReward;

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        totalStaked += amount;

        // Transfer MEME tokens from user to contract
        memeToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake MEME tokens and optionally claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pendingReward = calculateRewards(msg.sender);
        uint256 totalReward = stakes[msg.sender].rewardDebt + pendingReward;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;
        stakes[msg.sender].rewardDebt = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to user
        memeToken.transfer(msg.sender, stakedAmount);

        // Transfer reward to user
        if (totalReward > 0) {
            memeToken.transfer(msg.sender, totalReward);
        }

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, totalReward);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external {
        uint256 pendingReward = calculateRewards(msg.sender);
        uint256 totalReward = stakes[msg.sender].rewardDebt + pendingReward;

        require(totalReward > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;
        stakes[msg.sender].startTime = block.timestamp;

        // Transfer rewards to user
        memeToken.transfer(msg.sender, totalReward);

        emit RewardClaimed(msg.sender, totalReward);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage stakeInfo = stakes[user];
        if (stakeInfo.amount == 0 || stakeInfo.startTime == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        return (stakeInfo.amount * stakingDuration * rewardRate) / 1e18;
    }

    /**
     * @dev Update the reward rate. Only callable by the contract owner.
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be positive");
        rewardRate = _rewardRate;
    }
}
```
