"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Generate a smart contract for a decentralized rewarded ads platform that enables users to earn points and redeem rewards, with a focus on environmental sustainability.
Generated: DETERMINISTIC_4263b2a604789a93
Batch ID: 20250622_210053
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
 * @title Decentralized Rewarded Ads Platform
 * @dev This smart contract allows users to earn points by interacting with ads and redeem rewards.
 *      The platform focuses on environmental sustainability by promoting eco-friendly rewards.
 */
contract RewardedAdsPlatform {
    // Owner of the contract
    address public owner;

    // Struct to represent a user
    struct User {
        uint256 points; // Points earned by the user
        bool exists;    // Flag to check if the user exists
    }

    // Mapping to store user data
    mapping(address => User) private users;

    // Struct to represent a reward
    struct Reward {
        string name;        // Name of the reward
        uint256 pointsCost; // Points required to redeem the reward
        bool isEcoFriendly; // Flag to indicate if the reward is eco-friendly
    }

    // Array to store available rewards
    Reward[] public rewards;

    // Event emitted when a user earns points
    event PointsEarned(address indexed user, uint256 points);

    // Event emitted when a reward is redeemed
    event RewardRedeemed(address indexed user, string rewardName);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to check if the user exists
    modifier userExists(address _user) {
        require(users[_user].exists, "User does not exist");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new user in the platform.
     * @param _user Address of the user to register.
     */
    function registerUser(address _user) external onlyOwner {
        require(!users[_user].exists, "User is already registered");
        users[_user] = User({points: 0, exists: true});
    }

    /**
     * @dev Add a new reward to the platform.
     * @param _name Name of the reward.
     * @param _pointsCost Points required to redeem the reward.
     * @param _isEcoFriendly Flag indicating if the reward is eco-friendly.
     */
    function addReward(string memory _name, uint256 _pointsCost, bool _isEcoFriendly) external onlyOwner {
        rewards.push(Reward({name: _name, pointsCost: _pointsCost, isEcoFriendly: _isEcoFriendly}));
    }

    /**
     * @dev Earn points by interacting with ads.
     * @param _user Address of the user earning points.
     * @param _points Number of points to add.
     */
    function earnPoints(address _user, uint256 _points) external userExists(_user) {
        require(_points > 0, "Points must be greater than zero");
        users[_user].points += _points;
        emit PointsEarned(_user, _points);
    }

    /**
     * @dev Redeem a reward using points.
     * @param _rewardIndex Index of the reward in the rewards array.
     */
    function redeemReward(uint256 _rewardIndex) external userExists(msg.sender) {
        require(_rewardIndex < rewards.length, "Invalid reward index");
        Reward memory reward = rewards[_rewardIndex];
        User storage user = users[msg.sender];

        require(user.points >= reward.pointsCost, "Insufficient points to redeem this reward");

        // Deduct points and emit event
        user.points -= reward.pointsCost;
        emit RewardRedeemed(msg.sender, reward.name);
    }

    /**
     * @dev Get the points balance of a user.
     * @param _user Address of the user.
     * @return Points balance of the user.
     */
    function getPointsBalance(address _user) external view userExists(_user) returns (uint256) {
        return users[_user].points;
    }

    /**
     * @dev Get the total number of rewards available.
     * @return Total number of rewards.
     */
    function getRewardsCount() external view returns (uint256) {
        return rewards.length;
    }

    /**
     * @dev Get details of a specific reward.
     * @param _rewardIndex Index of the reward in the rewards array.
     * @return name Name of the reward.
     * @return pointsCost Points required to redeem the reward.
     * @return isEcoFriendly Flag indicating if the reward is eco-friendly.
     */
    function getRewardDetails(uint256 _rewardIndex)
        external
        view
        returns (string memory name, uint256 pointsCost, bool isEcoFriendly)
    {
        require(_rewardIndex < rewards.length, "Invalid reward index");
        Reward memory reward = rewards[_rewardIndex];
        return (reward.name, reward.pointsCost, reward.isEcoFriendly);
    }
}
```
