"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flokidongerapp.com
Prompt: How can I implement a smart contract for the FLOKIDONGER token that allows users to connect their wallets and earn passive tokens with an 8% APR?
Generated: DETERMINISTIC_a584d60626a2b2da
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is an implementation of the requested smart contract written in Solidity, suitable for deploying on the Ethereum blockchain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FLOKIDONGER Token Staking Contract
 * @dev A smart contract for staking FLOKIDONGER tokens and earning passive rewards with an 8% APR.
 */
contract FlokiDongerStaking {
    // State variables
    address public owner; // Owner of the contract
    uint256 public constant APR = 8; // Annual Percentage Rate set to 8%
    uint256 public constant REWARD_INTERVAL = 365 days; // Period for calculating APR rewards
    IERC20 public flokiDongerToken; // FLOKIDONGER token contract address

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastClaimed; // Timestamp of the last reward claim
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event TokensUnstaked(address indexed user, uint256 amount);

    // Constructor
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        owner = msg.sender;
        flokiDongerToken = IERC20(tokenAddress);
    }

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No active stake found");
        _;
    }

    /**
     * @dev Allows users to stake their FLOKIDONGER tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from user to the contract
        require(
            flokiDongerToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update stake details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastClaimed = block.timestamp;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Calculates the reward for a given user based on their stake and APR.
     * @param user The address of the user.
     * @return reward The calculated reward amount.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake memory userStake = stakes[user];
        uint256 stakingDuration = block.timestamp - userStake.lastClaimed;
        reward =
            (userStake.amount * APR * stakingDuration) /
            (REWARD_INTERVAL * 100);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update last claimed timestamp
        stakes[msg.sender].lastClaimed = block.timestamp;

        // Transfer rewards to the user
        require(
            flokiDongerToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to unstake their tokens and withdraw their stake.
     */
    function unstakeTokens() external hasStake(msg.sender) {
        // Claim any pending rewards
        claimRewards();

        // Retrieve staked amount
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Reset stake details
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].lastClaimed = 0;

        // Transfer staked tokens back to the user
        require(
            flokiDongerToken.transfer(msg.sender, stakedAmount),
            "Unstake transfer failed"
        );

        emit TokensUnstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Emergency withdrawal by the contract owner in case of contract issues.
     * Withdraw all tokens held by the contract.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = flokiDongerToken.balanceOf(address(this));
        require(
            flokiDongerToken.transfer(owner, contractBalance),
            "Emergency withdrawal failed"
        );
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```

This implementation follows best practices for Solidity development, including proper error handling, modularization, and documentation.
