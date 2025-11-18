"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspad.pages.dev
Prompt: Write code for a staking mechanism that allows users to earn rewards by staking CINU tokens, as outlined in Cheemspad's staking functionality.
Generated: DETERMINISTIC_df98aa1c91cb7e58
Batch ID: 20250612_152527
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
 * @title Cheemspad Staking Mechanism for CINU Tokens
 * @dev This contract allows users to stake CINU tokens and earn rewards over time.
 * Rewards are distributed based on the amount of tokens staked and the staking duration.
 */
contract CINUStaking {
    // Token contract interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public cinuToken; // CINU token contract address
    uint256 public rewardRate; // Reward rate (e.g., tokens rewarded per second)
    address public owner; // Contract owner

    // Structure to store staking data for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardsEarned; // Rewards earned but not yet claimed
    }

    mapping(address => Stake) public stakes; // Mapping to store staking info for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewardsClaimed);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to initialize the contract with CINU token address and reward rate
    constructor(IERC20 _cinuToken, uint256 _rewardRate) {
        cinuToken = _cinuToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake CINU tokens to participate in the staking pool and earn rewards.
     * @param amount The amount of CINU tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        
        // Transfer CINU tokens from the user to the contract
        require(cinuToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking data for the user
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardsEarned += calculateRewards(msg.sender); // Update rewards
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewardsToClaim = calculateRewards(msg.sender) + userStake.rewardsEarned;

        // Transfer staked tokens and rewards
        require(cinuToken.transfer(msg.sender, userStake.amount), "Token transfer failed");
        if (rewardsToClaim > 0) {
            require(cinuToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, userStake.amount, rewardsToClaim);

        // Reset user's stake data
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardsEarned = 0;
    }

    /**
     * @dev Claim rewards without unstaking tokens.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 rewardsToClaim = calculateRewards(msg.sender) + userStake.rewardsEarned;

        require(rewardsToClaim > 0, "No rewards available to claim");
        require(cinuToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);

        // Reset rewards data
        userStake.rewardsEarned = 0;
        userStake.startTime = block.timestamp;
    }

    /**
     * @dev Calculate the rewards earned by a user based on their staking duration.
     * @param user The address of the user.
     * @return The amount of rewards earned.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0 || userStake.startTime == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * stakingDuration * rewardRate) / (1 ether); // Reward calculation formula
    }

    /**
     * @dev Update the reward rate. Only the contract owner can call this function.
     * @param newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Withdraw tokens from the contract. Only the contract owner can call this function.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(cinuToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(cinuToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
