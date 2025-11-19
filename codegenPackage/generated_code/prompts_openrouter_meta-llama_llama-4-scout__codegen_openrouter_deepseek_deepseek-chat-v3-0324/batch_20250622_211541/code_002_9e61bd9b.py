"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Develop a smart contract using Solidity that enables multi-token, multi-chain meme coin staking, similar to the MemeVault protocol.
Generated: DETERMINISTIC_9e61bd9b6c65c819
Batch ID: 20250622_211541
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeVaultStaking
 * @dev A multi-token, multi-chain meme coin staking contract inspired by MemeVault protocol
 */
contract MemeVaultStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a staking position
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    // Struct to represent a supported token
    struct TokenInfo {
        address tokenAddress;
        uint256 rewardRate; // Rewards per second per token
        bool isActive;
    }

    // Mapping from token address to TokenInfo
    mapping(address => TokenInfo) public supportedTokens;

    // Mapping from user address to token address to Stake
    mapping(address => mapping(address => Stake)) public userStakes;

    // Total staked amount per token
    mapping(address => uint256) public totalStaked;

    // Owner address
    address public owner;

    // Events
    event TokenAdded(address indexed tokenAddress, uint256 rewardRate);
    event TokenRemoved(address indexed tokenAddress);
    event Staked(address indexed user, address indexed token, uint256 amount);
    event Unstaked(address indexed user, address indexed token, uint256 amount);
    event RewardClaimed(address indexed user, address indexed token, uint256 amount);
    event RewardRateUpdated(address indexed token, uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier validToken(address tokenAddress) {
        require(supportedTokens[tokenAddress].isActive, "Token not supported");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new supported token for staking
     * @param tokenAddress Address of the token
     * @param rewardRate Reward rate per second per token (in wei)
     */
    function addToken(address tokenAddress, uint256 rewardRate) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(rewardRate > 0, "Reward rate must be positive");
        require(!supportedTokens[tokenAddress].isActive, "Token already added");

        supportedTokens[tokenAddress] = TokenInfo({
            tokenAddress: tokenAddress,
            rewardRate: rewardRate,
            isActive: true
        });

        emit TokenAdded(tokenAddress, rewardRate);
    }

    /**
     * @dev Remove a supported token
     * @param tokenAddress Address of the token to remove
     */
    function removeToken(address tokenAddress) external onlyOwner validToken(tokenAddress) {
        require(totalStaked[tokenAddress] == 0, "Cannot remove token with active stakes");
        
        delete supportedTokens[tokenAddress];
        emit TokenRemoved(tokenAddress);
    }

    /**
     * @dev Update reward rate for a token
     * @param tokenAddress Address of the token
     * @param newRate New reward rate per second per token (in wei)
     */
    function updateRewardRate(address tokenAddress, uint256 newRate) external onlyOwner validToken(tokenAddress) {
        require(newRate > 0, "Reward rate must be positive");
        
        supportedTokens[tokenAddress].rewardRate = newRate;
        emit RewardRateUpdated(tokenAddress, newRate);
    }

    /**
     * @dev Stake tokens
     * @param tokenAddress Address of the token to stake
     * @param amount Amount to stake
     */
    function stake(address tokenAddress, uint256 amount) external nonReentrant validToken(tokenAddress) {
        require(amount > 0, "Amount must be positive");

        Stake storage stakeInfo = userStakes[msg.sender][tokenAddress];
        TokenInfo memory tokenInfo = supportedTokens[tokenAddress];

        // Claim any pending rewards first
        if (stakeInfo.amount > 0) {
            _claimRewards(msg.sender, tokenAddress);
        }

        // Transfer tokens from user to contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Update stake information
        stakeInfo.amount = stakeInfo.amount.add(amount);
        stakeInfo.startTime = block.timestamp;
        stakeInfo.rewardDebt = stakeInfo.amount.mul(tokenInfo.rewardRate).mul(block.timestamp);

        // Update total staked
        totalStaked[tokenAddress] = totalStaked[tokenAddress].add(amount);

        emit Staked(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param tokenAddress Address of the staked token
     * @param amount Amount to unstake
     */
    function unstake(address tokenAddress, uint256 amount) external nonReentrant validToken(tokenAddress) {
        require(amount > 0, "Amount must be positive");
        Stake storage stakeInfo = userStakes[msg.sender][tokenAddress];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        // Claim rewards first
        _claimRewards(msg.sender, tokenAddress);

        // Update stake information
        stakeInfo.amount = stakeInfo.amount.sub(amount);

        // Transfer tokens back to user
        IERC20(tokenAddress).transfer(msg.sender, amount);

        // Update total staked
        totalStaked[tokenAddress] = totalStaked[tokenAddress].sub(amount);

        emit Unstaked(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Claim accumulated rewards
     * @param tokenAddress Address of the staked token
     */
    function claimRewards(address tokenAddress) external nonReentrant validToken(tokenAddress) {
        _claimRewards(msg.sender, tokenAddress);
    }

    /**
     * @dev Internal function to calculate and claim rewards
     * @param user Address of the user
     * @param tokenAddress Address of the staked token
     */
    function _claimRewards(address user, address tokenAddress) internal {
        Stake storage stakeInfo = userStakes[user][tokenAddress];
        if (stakeInfo.amount == 0) return;

        TokenInfo memory tokenInfo = supportedTokens[tokenAddress];
        uint256 reward = calculateReward(user, tokenAddress);

        if (reward > 0) {
            // Update reward debt
            stakeInfo.rewardDebt = stakeInfo.amount.mul(tokenInfo.rewardRate).mul(block.timestamp);

            // Transfer rewards (in the same token)
            IERC20(tokenAddress).transfer(user, reward);

            emit RewardClaimed(user, tokenAddress, reward);
        }
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the user
     * @param tokenAddress Address of the staked token
     * @return Amount of pending rewards
     */
    function calculateReward(address user, address tokenAddress) public view validToken(tokenAddress) returns (uint256) {
        Stake memory stakeInfo = userStakes[user][tokenAddress];
        if (stakeInfo.amount == 0) return 0;

        TokenInfo memory tokenInfo = supportedTokens[tokenAddress];
        uint256 currentDebt = stakeInfo.amount.mul(tokenInfo.rewardRate).mul(block.timestamp);
        return currentDebt.sub(stakeInfo.rewardDebt);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
