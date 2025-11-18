"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Develop a Solidity contract to lock liquidity for $SCOTTY tokens, ensuring rewards distribution and staking functionality for the Scotty AI cryptoverse.
Generated: DETERMINISTIC_94e66940e7466b9c
Batch ID: 20250612_152358
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
 * @title ScottyAI Liquidity Locker and Staking Contract
 * @dev This contract allows locking liquidity for $SCOTTY tokens, rewards distribution, 
 * and staking functionality within the Scotty AI cryptoverse.
 */
contract ScottyAILiquidityLocker {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when staking started
    }

    // Token contract interface
    IERC20 public scottyToken;

    // Owner of the contract
    address public owner;

    // Mapping of staker addresses to their stakes
    mapping(address => Stake) public stakes;

    // Mapping of staker addresses to their rewards
    mapping(address => uint256) public rewards;

    // Total locked liquidity
    uint256 public totalLockedLiquidity;

    // Reward rate per second (tokens)
    uint256 public rewardRate;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount);

    // Event emitted when tokens are staked
    event TokensStaked(address indexed staker, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Constructor function to initialize the contract.
     * @param _tokenAddress Address of the $SCOTTY token contract.
     * @param _rewardRate Reward rate per second for staking.
     */
    constructor(address _tokenAddress, uint256 _rewardRate) {
        scottyToken = IERC20(_tokenAddress);
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to lock liquidity into the contract.
     * @param amount Amount of $SCOTTY tokens to lock.
     */
    function lockLiquidity(uint256 amount) external {
        require(amount > 0, "Cannot lock zero tokens");

        // Transfer tokens from the sender to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        totalLockedLiquidity += amount;

        emit LiquidityLocked(msg.sender, amount);
    }

    /**
     * @dev Function to stake tokens for rewards.
     * @param amount Amount of $SCOTTY tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the sender to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        calculateRewards(msg.sender);
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate pending rewards for a staker.
     * @param staker Address of the staker.
     */
    function calculateRewards(address staker) public {
        Stake storage stakeData = stakes[staker];
        if (stakeData.amount > 0) {
            uint256 timeStaked = block.timestamp - stakeData.timestamp;
            uint256 pendingReward = timeStaked * stakeData.amount * rewardRate / 1e18;
            rewards[staker] += pendingReward;
            stakeData.timestamp = block.timestamp; // Reset timestamp for next reward calculation
        }
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() external {
        calculateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        rewards[msg.sender] = 0;

        // Transfer rewards to the staker
        require(scottyToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the owner.
     * @param newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Function to withdraw tokens from the contract. Only callable by the owner.
     * @param amount Amount of $SCOTTY tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= scottyToken.balanceOf(address(this)), "Insufficient token balance in contract");
        require(scottyToken.transfer(owner, amount), "Token transfer failed");
    }
}

/**
 * @dev IERC20 interface to interact with the token contract.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
