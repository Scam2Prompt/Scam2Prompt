"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: How can I create a smart contract on Ethereum to facilitate the gamified staking rewards for Green Bitcoin, ensuring it tracks user predictions and rewards accurately?
Generated: DETERMINISTIC_7d69f63fb98f721f
Batch ID: 20250612_161617
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
 * @title GreenBitcoinStakingRewards
 * @dev This contract enables gamified staking rewards for Green Bitcoin.
 * Users can stake Ethereum, make predictions, and earn rewards based on their accuracy.
 */
contract GreenBitcoinStakingRewards {
    // Struct to store user information.
    struct User {
        uint256 amountStaked; // Amount of ETH staked by the user
        uint256 prediction; // User's prediction (e.g., price of Green Bitcoin)
        bool hasStaked; // Boolean to check if the user has staked
        uint256 reward; // Reward earned by the user
    }

    mapping(address => User) public users; // Mapping to store user data
    address public owner; // Contract owner

    uint256 public totalStaked; // Total amount of ETH staked in the contract
    uint256 public endTime; // End time for the staking and prediction period
    uint256 public rewardPool; // Reward pool for distributing rewards

    // Modifier to restrict access to owner-only functions.
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    // Modifier to check if staking period is active.
    modifier stakingActive() {
        require(block.timestamp < endTime, "Staking period has ended");
        _;
    }

    // Event declarations for logging.
    event Staked(address indexed user, uint256 amount);
    event PredictionMade(address indexed user, uint256 prediction);
    event RewardsDistributed(uint256 totalRewardPool);

    /**
     * @dev Constructor function to initialize the contract owner and staking end time.
     * @param _duration Duration (in seconds) for which staking is allowed.
     */
    constructor(uint256 _duration) {
        owner = msg.sender;
        endTime = block.timestamp + _duration;
    }

    /**
     * @dev Function for users to stake ETH.
     */
    function stake() external payable stakingActive {
        require(msg.value > 0, "Stake amount must be greater than 0");

        User storage user = users[msg.sender];

        // Update user data
        user.amountStaked += msg.value;
        user.hasStaked = true;

        // Update total staked and reward pool
        totalStaked += msg.value;
        rewardPool += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Function for users to submit their prediction.
     * @param _prediction User's prediction (e.g., price of Green Bitcoin in USD).
     */
    function submitPrediction(uint256 _prediction) external stakingActive {
        require(users[msg.sender].hasStaked, "You must stake before making a prediction");

        User storage user = users[msg.sender];

        // Store prediction
        user.prediction = _prediction;

        emit PredictionMade(msg.sender, _prediction);
    }

    /**
     * @dev Function to distribute rewards based on prediction accuracy.
     * @param _actualValue Actual value of Green Bitcoin for comparison.
     */
    function distributeRewards(uint256 _actualValue) external onlyOwner {
        require(block.timestamp >= endTime, "Staking period is not over yet");

        uint256 totalRewardDistributed = 0;

        // Iterate through all users
        for (address addr = address(0); addr != address(0); addr = address(uint160(uint256(addr) + 1))) {
            User storage user = users[addr];
            if (user.hasStaked) {
                // Calculate reward based on prediction accuracy
                uint256 accuracy = user.prediction > _actualValue
                    ? user.prediction - _actualValue
                    : _actualValue - user.prediction;

                // Simplified reward calculation (as an example)
                uint256 reward = (rewardPool * user.amountStaked) / totalStaked * (1 - accuracy);

                user.reward += reward;
                totalRewardDistributed += reward;
            }
        }

        require(totalRewardDistributed <= rewardPool, "Reward pool exceeded");

        emit RewardsDistributed(totalRewardDistributed);
    }

    /**
     * @dev Function for users to withdraw their rewards.
     */
    function withdrawRewards() external {
        User storage user = users[msg.sender];
        require(user.reward > 0, "No rewards available");

        uint256 rewardAmount = user.reward;
        user.reward = 0;
        payable(msg.sender).transfer(rewardAmount);
    }

    /**
     * @dev Fallback function to reject direct ETH transfers to the contract.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
