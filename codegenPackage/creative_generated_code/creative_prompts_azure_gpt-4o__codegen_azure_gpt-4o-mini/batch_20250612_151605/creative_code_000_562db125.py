"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Write a smart contract in Solidity that integrates a reward distribution system for Ethereum users based on predictions, ensuring compatibility with EVM wallets.
Generated: DETERMINISTIC_562db125bf7ac055
Batch ID: 20250612_151605
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
 * @title PredictionReward
 * @dev A smart contract for distributing rewards based on user predictions.
 */
contract PredictionReward {
    address public owner;
    uint256 public totalRewards; // Total rewards pool
    mapping(address => uint256) public userPredictions; // Store user predictions
    mapping(address => uint256) public userRewards; // Store user rewards
    mapping(address => bool) public hasClaimed; // Track if a user has claimed rewards

    event PredictionSubmitted(address indexed user, uint256 prediction);
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier hasNotClaimed() {
        require(!hasClaimed[msg.sender], "Rewards already claimed");
        _;
    }

    modifier validPrediction(uint256 prediction) {
        require(prediction > 0, "Prediction must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the total rewards pool.
     * @param _totalRewards The initial total rewards amount.
     */
    constructor(uint256 _totalRewards) {
        owner = msg.sender;
        totalRewards = _totalRewards;
    }

    /**
     * @dev Function to submit a prediction.
     * @param prediction The user's prediction value.
     */
    function submitPrediction(uint256 prediction) external 
        validPrediction(prediction) 
    {
        userPredictions[msg.sender] = prediction;
        emit PredictionSubmitted(msg.sender, prediction);
    }

    /**
     * @dev Function to distribute rewards based on a winning condition.
     * @param winningPrediction The correct prediction to check against.
     */
    function distributeRewards(uint256 winningPrediction) external onlyOwner {
        for (uint256 i = 0; i < userPredictions.length; i++) {
            address user = userPredictions.keys[i];
            if (userPredictions[user] == winningPrediction) {
                userRewards[user] += totalRewards / userPredictions.length; // Distributing equally
            }
        }
    }

    /**
     * @dev Function to claim rewards by the user.
     */
    function claimRewards() external hasNotClaimed {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        hasClaimed[msg.sender] = true;
        payable(msg.sender).transfer(rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        totalRewards += msg.value; // Increase total rewards pool
    }

    /**
     * @dev Function to withdraw remaining funds by the owner.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Function to check the contract's balance.
     * @return Contract's balance in wei.
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
