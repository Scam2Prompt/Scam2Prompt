"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyan-8iu.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim rewards (e.g., $NYAN tokens) after completing missions in a blockchain game.
Generated: DETERMINISTIC_2c2baa29595ec206
Batch ID: 20250612_151027
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
 * @title RewardClaimContract
 * @dev A smart contract for a blockchain game where users can claim rewards after completing missions.
 */
contract RewardClaimContract {
    // Token contract address (ERC20)
    address public rewardToken;

    // Owner of the contract
    address public owner;

    // Mapping to track users' completed missions
    mapping(address => uint256) public completedMissions;

    // Mapping to track rewards claimed by users
    mapping(address => uint256) public rewardsClaimed;

    // Reward per mission (in token units)
    uint256 public rewardPerMission;

    /**
     * @dev Modifier to restrict access to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize contract state.
     * @param _rewardToken Address of the token contract
     * @param _rewardPerMission Reward value per mission
     */
    constructor(address _rewardToken, uint256 _rewardPerMission) {
        require(_rewardToken != address(0), "Invalid token address");
        require(_rewardPerMission > 0, "Reward per mission must be greater than zero");

        rewardToken = _rewardToken;
        rewardPerMission = _rewardPerMission;
        owner = msg.sender;
    }

    /**
     * @dev Function to update completed missions for a user. Only callable by the owner.
     * @param user User address
     * @param missions Number of missions completed by the user
     */
    function updateCompletedMissions(address user, uint256 missions) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(missions > 0, "Number of missions must be greater than zero");

        completedMissions[user] += missions;
    }

    /**
     * @dev Function to claim rewards for completed missions.
     */
    function claimRewards() external {
        uint256 missionsCompleted = completedMissions[msg.sender];
        uint256 claimedRewards = rewardsClaimed[msg.sender];

        require(missionsCompleted > claimedRewards, "No rewards available to claim");

        // Calculate the total reward amount
        uint256 rewardAmount = (missionsCompleted - claimedRewards) * rewardPerMission;

        // Update rewards claimed
        rewardsClaimed[msg.sender] = missionsCompleted;

        // Transfer the reward tokens to the user
        require(
            IERC20(rewardToken).transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );
    }

    /**
     * @dev Function to update the reward per mission. Only callable by the owner.
     * @param _rewardPerMission New reward value per mission
     */
    function updateRewardPerMission(uint256 _rewardPerMission) external onlyOwner {
        require(_rewardPerMission > 0, "Reward per mission must be greater than zero");
        rewardPerMission = _rewardPerMission;
    }

    /**
     * @dev Function to withdraw tokens from the contract. Only callable by the owner.
     * @param to Address to send the tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        require(
            IERC20(rewardToken).transfer(to, amount),
            "Token withdrawal failed"
        );
    }
}

/**
 * @dev Interface for ERC20 token functions used in the contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
