"""
Generated Code Metadata:
========================
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Write a smart contract to enable cross-chain staking of uniTokens (uniETH, uniBTC, uniIOTX) on Bedrock, ensuring compatibility with IoTeX and DePIN.
Generated: DETERMINISTIC_bdce71b8eabe900d
Batch ID: 20250612_150228
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainStaking
 * @dev Enables cross-chain staking of uniTokens (uniETH, uniBTC, uniIOTX) with compatibility for IoTeX and DePIN
 */
contract CrossChainStaking is ReentrancyGuard, Ownable {
    // Struct to store staking details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    // Supported uniTokens
    enum UniToken { uniETH, uniBTC, uniIOTX }

    // Mapping from user address to token type to Stake
    mapping(address => mapping(UniToken => Stake)) public stakes;

    // Reward rates per token (reward per second per token)
    mapping(UniToken => uint256) public rewardRates;

    // Total staked amounts per token
    mapping(UniToken => uint256) public totalStaked;

    // ERC20 token contracts for each uniToken
    mapping(UniToken => IERC20) public tokenContracts;

    // Last reward calculation time per token
    mapping(UniToken => uint256) public lastRewardTime;

    // Accumulated rewards per share per token
    mapping(UniToken => uint256) public accRewardPerShare;

    // Events
    event Staked(address indexed user, UniToken indexed token, uint256 amount);
    event Unstaked(address indexed user, UniToken indexed token, uint256 amount);
    event RewardClaimed(address indexed user, UniToken indexed token, uint256 amount);
    event RewardRateUpdated(UniToken indexed token, uint256 newRate);

    /**
     * @dev Constructor initializes token contracts
     * @param uniETHAddress Address of uniETH token
     * @param uniBTCAddress Address of uniBTC token
     * @param uniIOTXAddress Address of uniIOTX token
     */
    constructor(
        address uniETHAddress,
        address uniBTCAddress,
        address uniIOTXAddress
    ) {
        tokenContracts[UniToken.uniETH] = IERC20(uniETHAddress);
        tokenContracts[UniToken.uniBTC] = IERC20(uniBTCAddress);
        tokenContracts[UniToken.uniIOTX] = IERC20(uniIOTXAddress);
    }

    /**
     * @dev Stake uniTokens
     * @param token Type of uniToken to stake
     * @param amount Amount to stake
     */
    function stake(UniToken token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update rewards before staking
        _updateRewards(token);

        // Transfer tokens from user to contract
        require(
            tokenContracts[token].transferFrom(msg.sender, address(this, amount),
            "Token transfer failed"
        );

        // Update stake details
        Stake storage userStake = stakes[msg.sender][token];
        if (userStake.amount > 0) {
            userStake.rewardDebt = userStake.amount * accRewardPerShare[token] / 1e18;
        } else {
            userStake.startTime = block.timestamp;
        }

        userStake.amount += amount;
        totalStaked[token] += amount;

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Unstake uniTokens and claim rewards
     * @param token Type of uniToken to unstake
     * @param amount Amount to unstake
     */
    function unstake(UniToken token, uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender][token];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(token);

        // Calculate pending rewards
        uint256 pending = (userStake.amount * accRewardPerShare[token] / 1e18) - userStake.rewardDebt;

        // Update stake details
        userStake.amount -= amount;
        totalStaked[token] -= amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare[token] / 1e18;

        // Transfer tokens back to user
        require(
            tokenContracts[token].transfer(msg.sender, amount),
            "Token transfer failed"
        );

        // Transfer rewards if any
        if (pending > 0) {
            // In a real implementation, you would transfer the reward token here
            // For simplicity, we're emitting an event
            emit RewardClaimed(msg.sender, token, pending);
        }

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @dev Claim rewards without unstaking
     * @param token Type of uniToken to claim rewards for
     */
    function claimRewards(UniToken token) external nonReentrant {
        _updateRewards(token);

        Stake storage userStake = stakes[msg.sender][token];
        uint256 pending = (userStake.amount * accRewardPerShare[token] / 1e18) - userStake.rewardDebt;

        require(pending > 0, "No rewards to claim");

        userStake.rewardDebt = userStake.amount * accRewardPerShare[token] / 1e18;

        // In a real implementation, you would transfer the reward token here
        // For simplicity, we're emitting an event
        emit RewardClaimed(msg.sender, token, pending);
    }

    /**
     * @dev Update reward parameters for a token
     * @param token Type of uniToken to update
     */
    function _updateRewards(UniToken token) internal {
        if (totalStaked[token] == 0) {
            lastRewardTime[token] = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime[token];
        if (timeElapsed > 0) {
            uint256 rewards = timeElapsed * rewardRates[token];
            accRewardPerShare[token] += rewards * 1e18 / totalStaked[token];
            lastRewardTime[token] = block.timestamp;
        }
    }

    /**
     * @dev Set reward rate for a token (only owner)
     * @param token Type of uniToken to update
     * @param rate New reward rate (reward per second per token)
     */
    function setRewardRate(UniToken token, uint256 rate) external onlyOwner {
        _updateRewards(token);
        rewardRates[token] = rate;
        emit RewardRateUpdated(token, rate);
    }

    /**
     * @dev Get pending rewards for a user and token
     * @param user Address of the user
     * @param token Type of uniToken
     * @return Pending rewards
     */
    function pendingRewards(address user, UniToken token) external view returns (uint256) {
        Stake storage userStake = stakes[user][token];
        uint256 currentAccRewardPerShare = accRewardPerShare[token];

        if (totalStaked[token] > 0 && block.timestamp > lastRewardTime[token]) {
            uint256 timeElapsed = block.timestamp - lastRewardTime[token];
            uint256 rewards = timeElapsed * rewardRates[token];
            currentAccRewardPerShare += rewards * 1e18 / totalStaked[token];
        }

        return (userStake.amount * currentAccRewardPerShare / 1e18) - userStake.rewardDebt;
    }

    /**
     * @dev Emergency withdraw tokens without claiming rewards (only owner)
     * @param tokenAddress Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
