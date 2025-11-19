"""
Generated Code Metadata:
========================
Original URL: https://dvhuh.pages.dev
Prompt: Develop a staking solution for tokens on a blockchain platform, providing support for pool and farm staking, and integration with a cryptocurrency asset management application.
Generated: DETERMINISTIC_20761b52fe57b1e3
Batch ID: 20250622_212052
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

// Staking contract for token staking with pool and farm support
contract Staking is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of stakers' addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // The token being staked
    IERC20 public stakingToken;

    // Reward per block for staking
    uint256 public rewardPerBlock;

    // Total rewards distributed
    uint256 public totalRewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.rewardDebt = staker.rewardDebt.add(calculateReward(msg.sender));

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker's information
        staker.amountStaked = staker.amountStaked.sub(amount);
        staker.rewardDebt = staker.rewardDebt.add(calculateReward(msg.sender));

        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update staker's reward debt
        stakers[msg.sender].rewardDebt = stakers[msg.sender].rewardDebt.add(reward);
        totalRewards = totalRewards.add(reward);

        // Transfer rewards to the staker
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a staker
    function calculateReward(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        return staker.amountStaked.mul(rewardPerBlock).div(1e18).sub(staker.rewardDebt);
    }

    // Function to set a new reward per block (only owner)
    function setRewardPerBlock(uint256 newRewardPerBlock) external onlyOwner {
        rewardPerBlock = newRewardPerBlock;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
