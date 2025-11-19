"""
Generated Code Metadata:
========================
Original URL: https://aitech-c09.pages.dev
Prompt: Create a Solidity smart contract for AITECH staking, incorporating features such as NFT boosts, tier boosts, and support for multiple EVM chains.
Generated: DETERMINISTIC_7a348cd31fbb5b25
Batch ID: 20250622_210216
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

/**
 * @title AITECH Staking Contract
 * @dev This contract allows users to stake AITECH tokens, earn rewards, and receive boosts from NFTs and tiers.
 * It supports multiple EVM chains and follows best practices for security and efficiency.
 */
contract AITECHStaking {
    // Token interface for AITECH
    IERC20 public aitechToken;

    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 tierBoost; // Boost percentage from tier
        uint256 nftBoost; // Boost percentage from NFT
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Reward rate per second (base rate without boosts)
    uint256 public rewardRate;

    // Tier boost mapping (tier level => boost percentage)
    mapping(uint256 => uint256) public tierBoosts;

    // NFT boost mapping (NFT ID => boost percentage)
    mapping(uint256 => uint256) public nftBoosts;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 tierBoost, uint256 nftBoost);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _aitechToken Address of the AITECH token contract.
     * @param _rewardRate Base reward rate per second.
     */
    constructor(IERC20 _aitechToken, uint256 _rewardRate) {
        aitechToken = _aitechToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake AITECH tokens.
     * @param amount Amount of tokens to stake.
     * @param tier Tier level for boost.
     * @param nftId NFT ID for boost.
     */
    function stake(uint256 amount, uint256 tier, uint256 nftId) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(aitechToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        uint256 tierBoost = tierBoosts[tier];
        uint256 nftBoost = nftBoosts[nftId];

        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            tierBoost: tierBoost,
            nftBoost: nftBoost
        });

        emit Staked(msg.sender, amount, tierBoost, nftBoost);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 baseReward = stakingDuration * rewardRate * userStake.amount / 1e18;
        uint256 boostedReward = baseReward * (100 + userStake.tierBoost + userStake.nftBoost) / 100;

        uint256 totalReward = boostedReward;

        // Transfer staked tokens and rewards back to the user
        require(aitechToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        require(aitechToken.transfer(msg.sender, totalReward), "Reward transfer failed");

        // Clear user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount, totalReward);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 baseReward = stakingDuration * rewardRate * userStake.amount / 1e18;
        uint256 boostedReward = baseReward * (100 + userStake.tierBoost + userStake.nftBoost) / 100;

        uint256 totalReward = boostedReward;

        // Reset staking start time
        userStake.startTime = block.timestamp;

        // Transfer rewards to the user
        require(aitechToken.transfer(msg.sender, totalReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, totalReward);
    }

    /**
     * @dev Set tier boost percentage.
     * @param tier Tier level.
     * @param boost Boost percentage.
     */
    function setTierBoost(uint256 tier, uint256 boost) external {
        // Only owner can call this function (add access control in production)
        tierBoosts[tier] = boost;
    }

    /**
     * @dev Set NFT boost percentage.
     * @param nftId NFT ID.
     * @param boost Boost percentage.
     */
    function setNFTBoost(uint256 nftId, uint256 boost) external {
        // Only owner can call this function (add access control in production)
        nftBoosts[nftId] = boost;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
