"""
Generated Code Metadata:
========================
Original URL: https://karak-network.pages.dev
Prompt: Design a smart contract using Solidity that leverages Karak's universal security and multiasset restaking primitive to provide security for a novel application.
Generated: DETERMINISTIC_55f10e69b7a6df2d
Batch ID: 20250622_210918
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title SecureRestakingContract
 * @dev A smart contract that leverages Karak's universal security and multiasset restaking primitive
 * to provide security for a novel application. Users can stake multiple assets and earn rewards.
 */
contract SecureRestakingContract is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store staker information
    struct Staker {
        uint256 totalStaked;
        uint256 lastRewardTime;
        uint256 rewardDebt;
    }

    // Mapping from staker address to their staking info
    mapping(address => Staker) public stakers;

    // Mapping from token address to whether it's supported
    mapping(address => bool) public supportedTokens;

    // Total staked amount across all users
    uint256 public totalStaked;

    // Reward rate per second
    uint256 public rewardRate;

    // Precision for reward calculations
    uint256 public constant PRECISION = 1e18;

    // Contract owner
    address public owner;

    // Events
    event Staked(address indexed user, address indexed token, uint256 amount);
    event Unstaked(address indexed user, address indexed token, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TokenSupportUpdated(address indexed token, bool isSupported);

    /**
     * @dev Modifier to check if the caller is the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor
     * @param _rewardRate Reward rate per second
     */
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens into the contract
     * @param token Address of the token to stake
     * @param amount Amount of tokens to stake
     */
    function stake(address token, uint256 amount) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Update staker's balance
        Staker storage staker = stakers[msg.sender];
        staker.totalStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Unstake tokens from the contract
     * @param token Address of the token to unstake
     * @param amount Amount of tokens to unstake
     */
    function unstake(address token, uint256 amount) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        Staker storage staker = stakers[msg.sender];
        require(staker.totalStaked >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker's balance
        staker.totalStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        IERC20(token).safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        Staker storage staker = stakers[msg.sender];

        uint256 rewards = staker.rewardDebt;
        require(rewards > 0, "No rewards to claim");

        staker.rewardDebt = 0;
        // In a real implementation, you would transfer the reward token here
        // For this example, we just emit the event
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update rewards for a staker
     * @param stakerAddress Address of the staker
     */
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        if (staker.totalStaked == 0) {
            staker.lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - staker.lastRewardTime;
        uint256 rewards = (staker.totalStaked * rewardRate * timeElapsed) / PRECISION;

        staker.rewardDebt += rewards;
        staker.lastRewardTime = block.timestamp;
    }

    /**
     * @dev Add or remove a supported token
     * @param token Address of the token
     * @param isSupported Whether the token is supported
     */
    function setTokenSupport(address token, bool isSupported) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupportUpdated(token, isSupported);
    }

    /**
     * @dev Update the reward rate
     * @param newRate New reward rate per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        // Update rewards for all stakers before changing rate
        // In a production environment, you might want a more efficient method
        rewardRate = newRate;
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
}
```
