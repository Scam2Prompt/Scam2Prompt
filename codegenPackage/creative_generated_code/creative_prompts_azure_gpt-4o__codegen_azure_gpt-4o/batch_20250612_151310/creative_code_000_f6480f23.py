"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described in the DOGE20 roadmap.
Generated: DETERMINISTIC_f6480f23d39801c4
Batch ID: 20250612_151310
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
 * @title StakingContract
 * @dev A smart contract for staking DOGE20 tokens and distributing rewards proportionally to stakers.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total staked amount
    uint256 public totalStaked;

    // Total rewards pool
    uint256 public totalRewards;

    // Start time of the staking period
    uint256 public immutable stakingStartTime;

    // End time of the staking period (2 years from start)
    uint256 public immutable stakingEndTime;

    // Struct to represent a staker's data
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsClaimed;
    }

    // Mapping of staker addresses to their staking data
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewards);
    event Unstaked(address indexed staker, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _totalRewards Total rewards pool to distribute.
     */
    constructor(IERC20 _doge20Token, uint256 _totalRewards) {
        doge20Token = _doge20Token;
        totalRewards = _totalRewards;
        stakingStartTime = block.timestamp;
        stakingEndTime = stakingStartTime + 2 * 365 days; // 2 years
    }

    /**
     * @dev Allows a user to stake DOGE20 tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(block.timestamp >= stakingStartTime, "Staking has not started yet");
        require(block.timestamp <= stakingEndTime, "Staking period has ended");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the staker to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker's data
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their proportional rewards.
     */
    function claimRewards() external {
        require(block.timestamp > stakingStartTime, "Staking has not started yet");
        require(block.timestamp <= stakingEndTime, "Staking period has ended");
        require(stakers[msg.sender].amountStaked > 0, "No staked amount found");

        // Calculate the staker's share of rewards
        uint256 stakerShare = (totalRewards * stakers[msg.sender].amountStaked) / totalStaked;
        uint256 claimableRewards = stakerShare - stakers[msg.sender].rewardsClaimed;

        require(claimableRewards > 0, "No rewards to claim");

        // Update staker's data
        stakers[msg.sender].rewardsClaimed += claimableRewards;

        // Transfer rewards to the staker
        require(doge20Token.transfer(msg.sender, claimableRewards), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, claimableRewards);
    }

    /**
     * @dev Allows a user to unstake their tokens after the staking period ends.
     */
    function unstake() external {
        require(block.timestamp > stakingEndTime, "Staking period has not ended yet");
        require(stakers[msg.sender].amountStaked > 0, "No staked amount found");

        uint256 amount = stakers[msg.sender].amountStaked;

        // Update staker's data
        stakers[msg.sender].amountStaked = 0;
        totalStaked -= amount;

        // Transfer staked tokens back to the staker
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any unclaimed rewards after the staking period.
     */
    function withdrawUnclaimedRewards(address recipient) external {
        require(block.timestamp > stakingEndTime, "Staking period has not ended yet");

        uint256 unclaimedRewards = totalRewards;

        for (uint256 i = 0; i < totalStaked; i++) { 
        // declare how
        ;}
