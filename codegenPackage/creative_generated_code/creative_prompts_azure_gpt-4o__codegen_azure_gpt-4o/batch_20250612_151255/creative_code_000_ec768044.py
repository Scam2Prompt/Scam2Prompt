"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Write a smart contract in Solidity that implements a staking mechanism similar to WienerAI, allowing users to stake tokens and earn rewards with a customizable APY.
Generated: DETERMINISTIC_ec768044faf91c6a
Batch ID: 20250612_151255
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
 * @dev Implements a staking mechanism allowing users to stake ERC20 tokens and earn rewards based on a customizable APY.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Struct to store stake details for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp of when the stake started
    }

    // Mapping to store stakes of each user
    mapping(address => Stake) public stakes;

    // Token used for staking
    IERC20 public stakingToken;

    // Annual Percentage Yield (APY), scaled by 100 (e.g., 500 = 5%)
    uint256 public apy;

    // Reward calculation divisor for scaling APY to seconds (365 days in seconds)
    uint256 private constant REWARD_DIVISOR = 365 days * 100;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event APYUpdated(uint256 newAPY);

    /**
     * @dev Constructor to initialize the staking token and APY.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _apy Initial APY for rewards calculation (scaled by 100).
     */
    constructor(IERC20 _stakingToken, uint256 _apy) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        stakingToken = _stakingToken;
        apy = _apy;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer staking tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");

        // Calculate reward
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * apy * stakingDuration) / REWARD_DIVISOR;

        // Transfer staked tokens back to user
        require(stakingToken.transfer(msg.sender, userStake.amount), "Token transfer failed");

        // Transfer reward tokens to user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Reset user stake
        userStake.amount = 0;
        userStake.startTime = 0;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Update the APY for staking rewards.
     * @param newAPY New APY, scaled by 100 (e.g., 500 = 5%).
     */
    function updateAPY(uint256 newAPY) external onlyOwner {
        require(newAPY > 0, "APY must be greater than zero");

        apy = newAPY;

        emit APYUpdated(newAPY);
    }

    /**
     * @dev Retrieve the reward amount for a user based on their stake details.
     * @param user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * apy * stakingDuration) / REWARD_DIVISOR;
        return reward;
    }
}
```
