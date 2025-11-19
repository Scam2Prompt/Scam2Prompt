"""
Generated Code Metadata:
========================
Original URL: https://stoneheads-staking.vercel.app
Prompt: Can you provide code examples for a staking mechanism that aligns with the features of Stone Heads?
Generated: DETERMINISTIC_8b569b7ea83df984
Batch ID: 20250612_162504
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
 * @title StakingContract
 * @dev A simple staking mechanism for Stone Heads NFTs or tokens.
 * Users can stake their tokens to earn rewards over time.
 */
contract StakingContract {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when staking started
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Update staking details
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Retrieve staking details
        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 rewards = stakes[msg.sender].rewards;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;
        stakes[msg.sender].rewards = 0;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked amount and rewards to the user
        // Note: Replace `transfer` with actual token transfer logic
        payable(msg.sender).transfer(stakedAmount + rewards);

        emit Unstaked(msg.sender, stakedAmount, rewards);
    }

    /**
     * @dev Allows users to claim their rewards without unstaking.
     */
    function claimRewards() external hasStake(msg.sender) {
        // Update rewards for the user
        _updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards available to claim");

        // Reset rewards
        stakes[msg.sender].rewards = 0;

        // Transfer rewards to the user
        // Note: Replace `transfer` with actual token transfer logic
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Updates the rewards for a user based on the time elapsed.
     * @param _user The address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount > 0) {
            uint256 timeElapsed = block.timestamp - stakeData.timestamp;
            stakeData.rewards += timeElapsed * rewardRate * stakeData.amount;
            stakeData.timestamp = block.timestamp; // Reset timestamp
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw contract balance.
     */
    function withdrawBalance() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```

This code provides a basic staking mechanism for tokens or NFTs, with features such as staking, unstaking, claiming rewards, and updating reward rates. Replace the `transfer` logic with actual token transfer logic if using ERC20 or other token standards.
