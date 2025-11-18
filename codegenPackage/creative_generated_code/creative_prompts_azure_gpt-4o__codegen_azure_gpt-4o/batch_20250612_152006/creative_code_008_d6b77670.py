"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token2049.vercel.app
Prompt: Generate a Solidity smart contract for staking functionality in the 2049 NFT marketplace, ensuring compatibility with the platform's native stacking features.
Generated: DETERMINISTIC_d6b776700135b523
Batch ID: 20250612_152006
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
 * @title Staking Contract for 2049 NFT Marketplace
 * @dev A smart contract to allow users to stake their tokens in the 2049 NFT marketplace.
 */
contract StakingContract {
    // Define state variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total tokens staked in the contract
    uint256 public rewardRate; // Reward rate per second

    struct Stake {
        uint256 amount; // Amount staked
        uint256 startTime; // Timestamp when staking began
        uint256 rewards; // Accrued rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user address to stake details

    event Staked(address indexed user, uint256 amount, uint256 timestamp); // Event for staking
    event Unstaked(address indexed user, uint256 amount, uint256 rewards, uint256 timestamp); // Event for unstaking
    event RewardsClaimed(address indexed user, uint256 rewards, uint256 timestamp); // Event for claiming rewards

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Constructor sets the owner and reward rate.
     * @param _rewardRate Reward rate per second.
     */
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function for users to stake tokens.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update staking details for the user
        Stake storage userStake = stakes[msg.sender];
        userStake.rewards += calculateRewards(msg.sender); // Update rewards
        userStake.amount += _amount; // Add to staked amount
        userStake.startTime = block.timestamp; // Reset staking start time

        totalStaked += _amount; // Increase total staked amount

        emit Staked(msg.sender, _amount, block.timestamp); // Emit event
    }

    /**
     * @dev Function for users to unstake their tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        // Calculate rewards and unstake the tokens
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        uint256 amount = userStake.amount;

        totalStaked -= amount; // Decrease total staked amount

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewards = 0;
        userStake.startTime = 0;

        // Transfer tokens and rewards to the user (assume an ERC20 token transfer mechanism)
        // Example: ERC20Token.transfer(msg.sender, amount + rewards);

        emit Unstaked(msg.sender, amount, rewards, block.timestamp); // Emit event
    }

    /**
     * @dev Function to claim staking rewards without unstaking.
     */
    function claimRewards() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);

        userStake.rewards = 0; // Reset accrued rewards
        userStake.startTime = block.timestamp; // Reset staking start time

        // Transfer rewards to the user (assume an ERC20 token transfer mechanism)
        // Example: ERC20Token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards, block.timestamp); // Emit event
    }

    /**
     * @dev Helper function to calculate accrued rewards for a user.
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        Stake memory userStake = stakes[_user];
        uint256 duration = block.timestamp - userStake.startTime;
        return (userStake.amount * rewardRate * duration) / 1e18; // Rewards calculated based on reward rate
    }

    /**
     * @dev Function to update the reward rate. Only callable by the owner.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
