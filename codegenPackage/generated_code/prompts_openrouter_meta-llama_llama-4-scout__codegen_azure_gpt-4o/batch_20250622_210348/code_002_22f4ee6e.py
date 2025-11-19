"""
Generated Code Metadata:
========================
Original URL: https://stethclaim.pages.dev
Prompt: "Generate a Solidity smart contract code snippet for a staking rewards pool similar to stETH, with features like APY calculation, multiplier application, and reward claiming."
Generated: DETERMINISTIC_22f4ee6eb9a19074
Batch ID: 20250622_210348
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
 * @title StakingRewardsPool
 * @dev A staking rewards pool contract with APY calculation, multiplier application, and reward claiming.
 */
contract StakingRewardsPool {
    // State variables
    address public owner; // Owner of the contract
    uint256 public annualPercentageYield; // APY in basis points (e.g., 500 = 5%)
    uint256 public multiplier; // Multiplier for rewards (e.g., 2x rewards)
    uint256 public totalStaked; // Total amount staked in the pool

    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 timestamp; // Timestamp of when the stake was made
        uint256 rewardsClaimed; // Total rewards claimed by the user
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No stake found for the user");
        _;
    }

    // Constructor
    constructor(uint256 _annualPercentageYield, uint256 _multiplier) {
        owner = msg.sender;
        annualPercentageYield = _annualPercentageYield;
        multiplier = _multiplier;
    }

    /**
     * @dev Allows a user to stake tokens in the pool.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Calculates the rewards for a user based on their stake and time elapsed.
     * @param user The address of the user.
     * @return The calculated rewards.
     */
    function calculateRewards(address user) public view hasStake(user) returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 timeElapsed = block.timestamp - userStake.timestamp;

        // APY calculation: (amount * APY * timeElapsed) / (365 days * 10000)
        uint256 baseRewards = (userStake.amount * annualPercentageYield * timeElapsed) / (365 days * 10000);

        // Apply multiplier
        return baseRewards * multiplier;
    }

    /**
     * @dev Allows a user to claim their rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update the user's rewards claimed
        stakes[msg.sender].rewardsClaimed += rewards;

        // Reset the stake timestamp to prevent double-claiming
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);

        // Transfer rewards to the user (mock transfer for demonstration purposes)
        // In production, integrate with an ERC20 token or native currency transfer
        payable(msg.sender).transfer(rewards);
    }

    /**
     * @dev Allows a user to unstake their tokens.
     */
    function unstake() external hasStake(msg.sender) {
        uint256 amount = stakes[msg.sender].amount;

        // Reset the user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Update total staked
        totalStaked -= amount;

        emit Unstaked(msg.sender, amount);

        // Transfer staked amount back to the user (mock transfer for demonstration purposes)
        // In production, integrate with an ERC20 token or native currency transfer
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Allows the owner to update the APY.
     * @param _annualPercentageYield The new APY in basis points.
     */
    function updateAPY(uint256 _annualPercentageYield) external onlyOwner {
        annualPercentageYield = _annualPercentageYield;
    }

    /**
     * @dev Allows the owner to update the multiplier.
     * @param _multiplier The new multiplier.
     */
    function updateMultiplier(uint256 _multiplier) external onlyOwner {
        multiplier = _multiplier;
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
