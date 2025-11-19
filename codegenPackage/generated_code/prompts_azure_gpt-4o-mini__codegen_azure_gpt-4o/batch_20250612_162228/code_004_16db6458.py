"""
Generated Code Metadata:
========================
Original URL: https://elephantrewards.pages.dev
Prompt: Illustrate how to implement lossless liquidity management in a smart contract for a dual staking model similar to Elephant Money Farms.
Generated: DETERMINISTIC_16db6458d507540c
Batch ID: 20250612_162228
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
 * @title DualStakingLiquidityManager
 * @dev A smart contract for managing lossless liquidity in a dual staking model.
 * Inspired by Elephant Money Farms. This contract allows users to stake two tokens
 * and earn rewards while ensuring liquidity is preserved.
 */
contract DualStakingLiquidityManager {
    // State variables
    address public owner; // Contract owner
    IERC20 public tokenA; // First token for staking
    IERC20 public tokenB; // Second token for staking
    uint256 public totalStakedTokenA; // Total staked amount of Token A
    uint256 public totalStakedTokenB; // Total staked amount of Token B

    struct Stake {
        uint256 amountTokenA;
        uint256 amountTokenB;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastRewardBlock; // Last block when rewards were distributed
    uint256 public accRewardPerShare; // Accumulated rewards per share

    // Events
    event Staked(address indexed user, uint256 amountTokenA, uint256 amountTokenB);
    event Unstaked(address indexed user, uint256 amountTokenA, uint256 amountTokenB);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier updateRewards() {
        if (block.number > lastRewardBlock) {
            uint256 multiplier = block.number - lastRewardBlock;
            uint256 reward = multiplier * rewardRate;
            if (totalStakedTokenA + totalStakedTokenB > 0) {
                accRewardPerShare += (reward * 1e12) / (totalStakedTokenA + totalStakedTokenB);
            }
            lastRewardBlock = block.number;
        }
        _;
    }

    // Constructor
    constructor(address _tokenA, address _tokenB, uint256 _rewardRate) {
        owner = msg.sender;
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        rewardRate = _rewardRate;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amountTokenA Amount of Token A to stake.
     * @param amountTokenB Amount of Token B to stake.
     */
    function stake(uint256 amountTokenA, uint256 amountTokenB) external updateRewards {
        require(amountTokenA > 0 && amountTokenB > 0, "Invalid stake amounts");

        // Transfer tokens to the contract
        require(tokenA.transferFrom(msg.sender, address(this), amountTokenA), "Token A transfer failed");
        require(tokenB.transferFrom(msg.sender, address(this), amountTokenB), "Token B transfer failed");

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amountTokenA += amountTokenA;
        userStake.amountTokenB += amountTokenB;
        userStake.rewardDebt = (userStake.amountTokenA + userStake.amountTokenB) * accRewardPerShare / 1e12;

        // Update total staked amounts
        totalStakedTokenA += amountTokenA;
        totalStakedTokenB += amountTokenB;

        emit Staked(msg.sender, amountTokenA, amountTokenB);
    }

    /**
     * @dev Unstake tokens from the contract.
     */
    function unstake() external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amountTokenA > 0 || userStake.amountTokenB > 0, "No tokens to unstake");

        // Transfer staked tokens back to the user
        require(tokenA.transfer(msg.sender, userStake.amountTokenA), "Token A transfer failed");
        require(tokenB.transfer(msg.sender, userStake.amountTokenB), "Token B transfer failed");

        // Update total staked amounts
        totalStakedTokenA -= userStake.amountTokenA;
        totalStakedTokenB -= userStake.amountTokenB;

        emit Unstaked(msg.sender, userStake.amountTokenA, userStake.amountTokenB);

        // Reset user stake
        userStake.amountTokenA = 0;
        userStake.amountTokenB = 0;
        userStake.rewardDebt = 0;
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = (userStake.amountTokenA + userStake.amountTokenB) * accRewardPerShare / 1e12 - userStake.rewardDebt;
        require(pendingReward > 0, "No rewards to claim");

        // Update reward debt
        userStake.rewardDebt = (userStake.amountTokenA + userStake.amountTokenB) * accRewardPerShare / 1e12;

        // Transfer rewards to the user
        payable(msg.sender).transfer(pendingReward);

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _rewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Fallback function to accept Ether for rewards.
     */
    receive() external payable {}

    /**
     * @dev Emergency withdrawal of tokens. Only callable by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        require(tokenA.transfer(owner, tokenA.balanceOf(address(this))), "Token A transfer failed");
        require(tokenB.transfer(owner, tokenB.balanceOf(address(this))), "Token B transfer failed");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
