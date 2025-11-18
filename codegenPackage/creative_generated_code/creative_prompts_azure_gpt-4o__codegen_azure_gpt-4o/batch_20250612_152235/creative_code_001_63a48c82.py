"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a smart contract in Solidity for staking OMEME tokens on the Binance Smart Chain, ensuring the staking rewards are dynamically calculated based on the 652% reward percentage described.
Generated: DETERMINISTIC_63a48c82378dbdd2
Batch ID: 20250612_152235
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
 * @title OMEME Token Staking Contract
 * @dev A contract for staking OMEME tokens and earning rewards at a dynamic rate.
 *      Reward rate is 652% annually, distributed proportionately to staking duration.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OMEMEStaking is Ownable {
    // ERC20 token contract interface
    IERC20 public omemeToken;

    // Annual reward rate (652%)
    uint256 public constant ANNUAL_REWARD_RATE = 652;

    // Number of seconds in a year
    uint256 public constant SECONDS_IN_YEAR = 365 days;

    // Struct to store staking details
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 startTime;      // Timestamp of when staking started
        uint256 lastClaimed;    // Timestamp of last reward claim
    }

    // Mapping of user address to their stake details
    mapping(address => Stake) public stakes;

    // Events for staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the staking contract with the OMEME token address.
     * @param _omemeToken Address of the OMEME token contract.
     */
    constructor(IERC20 _omemeToken) {
        omemeToken = _omemeToken;
    }

    /**
     * @dev Stake OMEME tokens.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(omemeToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // If user already has a stake, claim pending rewards before updating staking info
        if (userStake.amount > 0) {
            claimRewards();
        }

        // Update user stake
        userStake.amount += amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Calculate the pending rewards for a user.
     * @return The reward amount that can be claimed.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Time elapsed since last claim
        uint256 timeElapsed = block.timestamp - userStake.lastClaimed;

        // Calculate reward based on annual reward rate and elapsed time
        uint256 reward = (userStake.amount * ANNUAL_REWARD_RATE * timeElapsed) / SECONDS_IN_YEAR / 100;
        return reward;
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() public {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate pending rewards
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update last claimed timestamp
        userStake.lastClaimed = block.timestamp;

        // Transfer rewards to the user
        require(omemeToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Unstake OMEME tokens and claim any pending rewards.
     */
    function unstakeTokens() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Claim pending rewards before unstaking
        claimRewards();

        // Transfer staked tokens back to the user
        uint256 amount = userStake.amount;
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.lastClaimed = 0;

        require(omemeToken.transfer(msg.sender, amount), "Unstake transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Emergency function to withdraw tokens sent to the contract by mistake.
     *      Only callable by the contract owner.
     * @param token Address of the token to withdraw.
     * @param recipient Address to receive the withdrawn tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(
        IERC20 token, 
        address recipient, 
        uint256 amount
    ) external onlyOwner {
        require(token.transfer(recipient, amount), "Emergency withdrawal failed");
    }
}
```
