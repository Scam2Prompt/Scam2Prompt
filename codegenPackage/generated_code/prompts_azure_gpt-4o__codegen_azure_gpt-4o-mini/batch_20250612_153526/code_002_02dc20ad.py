"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-iio.pages.dev
Prompt: Generate Solidity code for a staking smart contract similar to DOGE20's, which distributes rewards proportionally to stakers over a two-year period.
Generated: DETERMINISTIC_02dc20adf43814ed
Batch ID: 20250612_153526
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

contract StakingContract is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;
    // Reward token to be distributed
    IERC20 public rewardToken;

    // Staker information
    struct Staker {
        uint256 amountStaked;
        uint256 lastClaimedTime;
        uint256 rewardsEarned;
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;
    // Reward rate per second
    uint256 public rewardRate;
    // Duration of the staking period (2 years)
    uint256 public constant STAKING_DURATION = 2 * 365 days;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _totalRewards) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _totalRewards.div(STAKING_DURATION);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(_amount);
        staker.lastClaimedTime = block.timestamp;

        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        // Update staker information
        staker.amountStaked = staker.amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update last claimed time and rewards earned
        staker.lastClaimedTime = block.timestamp;
        staker.rewardsEarned = staker.rewardsEarned.add(rewards);

        require(rewardToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeStaked = block.timestamp.sub(staker.lastClaimedTime);
        uint256 rewards = staker.amountStaked.mul(rewardRate).mul(timeStaked).div(1e18);
        return rewards;
    }

    // Function to withdraw remaining rewards after the staking period
    function withdrawRemainingRewards() external onlyOwner {
        require(block.timestamp >= STAKING_DURATION, "Staking period not yet ended");
        uint256 remainingRewards = rewardToken.balanceOf(address(this));
        require(remainingRewards > 0, "No remaining rewards to withdraw");
        require(rewardToken.transfer(msg.sender, remainingRewards), "Transfer failed");
    }
}
```
