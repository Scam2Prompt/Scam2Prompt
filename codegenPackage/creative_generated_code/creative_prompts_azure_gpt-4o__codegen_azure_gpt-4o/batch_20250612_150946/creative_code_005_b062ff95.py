"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogeverse-com.pages.dev
Prompt: Create a Solidity function for locking $DOGEVERSE tokens in a staking contract and calculating rewards based on the dynamic rate specified in the Dogeverse staking mechanism.
Generated: DETERMINISTIC_b062ff95d637a7d8
Batch ID: 20250612_150946
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
 * @title DogeverseStaking
 * @dev Contract for staking $DOGEVERSE tokens and calculating rewards based on a dynamic rate.
 */
contract DogeverseStaking {
    IERC20 public dogeverseToken;
    address public owner;

    // Struct to store staking information
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 startTime;      // Timestamp when tokens were staked
        uint256 rewardRate;     // Dynamic reward rate at the time of staking
    }

    // Mapping to store stakes of each user
    mapping(address => Stake) public stakes;

    // Events
    event TokensStaked(address indexed user, uint256 amount, uint256 rewardRate);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event TokensUnstaked(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor
    constructor(address _dogeverseTokenAddress) {
        dogeverseToken = IERC20(_dogeverseTokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to allow users to stake $DOGEVERSE tokens.
     * @param amount Amount of tokens to stake.
     * @param rewardRate Dynamic reward rate for this staking.
     */
    function stakeTokens(uint256 amount, uint256 rewardRate) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(dogeverseToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(rewardRate > 0, "Reward rate must be greater than zero");

        // Transfer tokens from user to contract
        bool success = dogeverseToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update stake information
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            startTime: block.timestamp,
            rewardRate: rewardRate
        });

        emit TokensStaked(msg.sender, amount, rewardRate);
    }

    /**
     * @dev Function to calculate rewards for the user based on their stake.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate reward based on staking duration and dynamic reward rate
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * stakingDuration * userStake.rewardRate) / (1 days * 100);

        return reward;
    }

    /**
     * @dev Function to allow users to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Reset reward calculation
        stakes[msg.sender].startTime = block.timestamp;

        // Transfer reward tokens to the user
        bool success = dogeverseToken.transfer(msg.sender, reward);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to allow users to unstake their tokens.
     */
    function unstakeTokens() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Transfer tokens back to the user
        uint256 stakedAmount = userStake.amount;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;
        stakes[msg.sender].rewardRate = 0;

        bool success = dogeverseToken.transfer(msg.sender, stakedAmount);
        require(success, "Unstaking transfer failed");

        emit TokensUnstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Function to allow the owner to withdraw any tokens accidentally sent to the contract.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(dogeverseToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = dogeverseToken.transfer(owner, amount);
        require(success, "Withdrawal failed");
    }
}

// Minimal IERC20 interface for interacting with $DOGEVERSE token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
