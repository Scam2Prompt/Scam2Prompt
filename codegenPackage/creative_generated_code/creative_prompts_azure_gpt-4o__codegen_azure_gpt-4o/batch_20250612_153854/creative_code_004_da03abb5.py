"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophan.xyz
Prompt: Write a smart contract that utilizes SOPH tokens to reward users for engagement in loyalty programs, as described in Sophon's platform features.
Generated: DETERMINISTIC_da03abb5493298ca
Batch ID: 20250612_153854
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
 * @title LoyaltyRewardsContract
 * @dev A smart contract that uses SOPH tokens to reward users for engagement in loyalty programs.
 */
contract LoyaltyRewardsContract {
    // Address of the SOPH token contract
    IERC20 public sophToken;

    // Mapping to store user engagement points
    mapping(address => uint256) public userPoints;

    // Owner of the contract (platform administrator)
    address public owner;

    // Event to log rewards distributed
    event RewardDistributed(address indexed user, uint256 amount);
    event PointsAdded(address indexed user, uint256 points);

    /**
     * @dev Modifier to restrict certain functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the SOPH token address.
     * @param _sophToken Address of the deployed SOPH token contract.
     */
    constructor(address _sophToken) {
        require(_sophToken != address(0), "Invalid SOPH token address");
        sophToken = IERC20(_sophToken);
        owner = msg.sender;
    }

    /**
     * @dev Add engagement points to a user's account.
     * @param user Address of the user.
     * @param points Number of points to add.
     */
    function addPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than zero");

        userPoints[user] += points;
        emit PointsAdded(user, points);
    }

    /**
     * @dev Distribute SOPH tokens to users based on engagement points.
     * @param user Address of the user to be rewarded.
     * @param tokenAmount Amount of SOPH tokens to transfer.
     */
    function distributeRewards(address user, uint256 tokenAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(sophToken.balanceOf(address(this)) >= tokenAmount, "Insufficient contract token balance");

        // Reset user points after reward distribution
        userPoints[user] = 0;

        // Transfer SOPH tokens to the user
        bool success = sophToken.transfer(user, tokenAmount);
        require(success, "Token transfer failed");

        emit RewardDistributed(user, tokenAmount);
    }

    /**
     * @dev Withdraw SOPH tokens from the contract (only by the owner).
     * @param amount Number of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(sophToken.balanceOf(address(this)) >= amount, "Insufficient contract token balance");

        bool success = sophToken.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }
}

/**
 * @dev Interface definition for the SOPH token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
