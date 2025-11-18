"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_e98261c1fc748f42
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

/**
 * @title Doge20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and earn proportional rewards
 * distributed over a two-year period.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Doge20Staking {
    // State variables
    IERC20 public immutable doge20Token; // DOGE20 token contract
    uint256 public constant REWARD_PERIOD = 2 * 365 * 24 * 60 * 60; // 2 years in seconds
    uint256 public immutable startTime; // Timestamp when staking started
    uint256 public immutable endTime; // Timestamp when staking ends
    uint256 public totalStaked; // Total amount of DOGE20 tokens staked
    uint256 public rewardPool; // Total reward pool in DOGE20 tokens
    
    struct Staker {
        uint256 amountStaked;
        uint256 rewardClaimed;
    }

    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 amount);

    // Modifiers
    modifier onlyDuringStakingPeriod() {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Staking period is not active");
        _;
    }

    modifier onlyAfterStakingPeriod() {
        require(block.timestamp > endTime, "Staking period is still active");
        _;
    }

    /**
     * @dev Constructor initializes the staking contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardPool Total reward pool to distribute over the staking period.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardPool) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        doge20Token = _doge20Token;
        rewardPool = _rewardPool;
        startTime = block.timestamp; // Staking starts now
        endTime = block.timestamp + REWARD_PERIOD; // Ends after 2 years
    }

    /**
     * @dev Allows users to stake DOGE20 tokens.
     * @param _amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 _amount) external onlyDuringStakingPeriod {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer DOGE20 tokens from the staker to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their DOGE20 tokens after the staking period has ended.
     */
    function unstake() external onlyAfterStakingPeriod {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens to unstake");

        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;

        // Transfer DOGE20 tokens back to the staker
        require(doge20Token.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Allows users to claim their proportional rewards after the staking period ends.
     */
    function claimReward() external onlyAfterStakingPeriod {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No rewards to claim");

        uint256 reward = calculateReward(msg.sender);
        require(reward > staker.rewardClaimed, "No remaining rewards to claim");

        uint256 claimableReward = reward - staker.rewardClaimed;
        staker.rewardClaimed += claimableReward;

        // Transfer DOGE20 tokens as reward
        require(doge20Token.transfer(msg.sender, claimableReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, claimableReward);
    }

    /**
     * @dev Calculates the proportional reward for a staker.
     * @param _staker Address of the staker.
     * @return reward Amount of DOGE20 tokens as reward.
     */
    function calculateReward(address _staker) public view returns (uint256 reward) {
        Staker memory staker = stakers[_staker];
        if (totalStaked == 0) {
            return 0;
        }

        // Proportional reward calculation
        reward = (staker.amountStaked * rewardPool) / totalStaked;
    }

    /**
     * @dev Returns the staking details of a staker.
     * @param _staker Address of the staker.
     * @return amountStaked Amount of DOGE20 tokens staked.
     * @return rewardClaimed Amount of rewards claimed.
     */
    function getStakerInfo(address _staker) 
        external 
        view 
        returns (uint256 amountStaked, uint256 rewardClaimed) 
    {
        Staker memory staker = stakers[_staker];
        return (staker.amountStaked, staker.rewardClaimed);
    }
}
```
