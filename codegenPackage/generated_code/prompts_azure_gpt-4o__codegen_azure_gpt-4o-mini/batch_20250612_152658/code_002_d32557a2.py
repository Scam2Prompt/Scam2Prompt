"""
Generated Code Metadata:
========================
Original URL: https://node-sophon.com
Prompt: Generate a smart contract example for deploying a loyalty program on the Sophon Chain that rewards users with SOPH tokens based on engagement metrics.
Generated: DETERMINISTIC_d32557a220492bba
Batch ID: 20250612_152658
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

// Importing the interface for the SOPH token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// LoyaltyProgram contract to manage user engagement and rewards
contract LoyaltyProgram {
    // State variables
    IERC20 public sophtoken; // SOPH token contract
    address public owner; // Owner of the contract
    mapping(address => uint256) public userPoints; // Mapping to track user points
    mapping(address => uint256) public lastClaimed; // Mapping to track last claimed timestamp

    // Events
    event PointsAwarded(address indexed user, uint256 points);
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the SOPH token address
    constructor(address _sophTokenAddress) {
        sophtoken = IERC20(_sophTokenAddress);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Function to award points to a user based on engagement metrics
    function awardPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than zero");

        userPoints[user] += points; // Increment user points
        emit PointsAwarded(user, points); // Emit event for awarded points
    }

    // Function to claim SOPH tokens based on accumulated points
    function claimTokens() external {
        uint256 points = userPoints[msg.sender]; // Get user's points
        require(points > 0, "No points to claim");

        // Calculate the amount of SOPH tokens to be claimed (1 point = 1 SOPH token)
        uint256 amountToClaim = points;

        // Reset user's points after claiming
        userPoints[msg.sender] = 0;

        // Transfer SOPH tokens to the user
        require(sophtoken.balanceOf(address(this)) >= amountToClaim, "Insufficient contract balance");
        sophtoken.transfer(msg.sender, amountToClaim);

        // Emit event for claimed tokens
        emit TokensClaimed(msg.sender, amountToClaim);
    }

    // Function to withdraw SOPH tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(sophtoken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        sophtoken.transfer(owner, amount); // Transfer tokens to the owner
    }

    // Function to check the user's points
    function getUserPoints(address user) external view returns (uint256) {
        return userPoints[user]; // Return the user's points
    }
}
```
