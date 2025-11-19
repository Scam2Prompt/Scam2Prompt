"""
Generated Code Metadata:
========================
Original URL: https://cokiessnew.pages.dev
Prompt: "Write a smart contract in Solidity to distribute $COOKIE tokens based on user engagement and community points."
Generated: DETERMINISTIC_762bc9b664c531d3
Batch ID: 20250622_210803
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
 * @title COOKIE Token Distribution Smart Contract
 * @dev This contract distributes COOKIE tokens based on user engagement and community points.
 */
contract CookieTokenDistributor {
    // Address of the COOKIE token contract
    IERC20 public cookieToken;

    // Owner of the contract
    address public owner;

    // Mapping to store user engagement points
    mapping(address => uint256) public engagementPoints;

    // Mapping to store community points
    mapping(address => uint256) public communityPoints;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the COOKIE token address.
     * @param _cookieToken Address of the COOKIE token contract.
     */
    constructor(address _cookieToken) {
        require(_cookieToken != address(0), "Invalid token address");
        cookieToken = IERC20(_cookieToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to update engagement points for a user.
     * @param user Address of the user.
     * @param points Number of engagement points to set.
     */
    function updateEngagementPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        engagementPoints[user] = points;
    }

    /**
     * @dev Function to update community points for a user.
     * @param user Address of the user.
     * @param points Number of community points to set.
     */
    function updateCommunityPoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        communityPoints[user] = points;
    }

    /**
     * @dev Function to calculate the total points for a user.
     * @param user Address of the user.
     * @return Total points (engagement + community).
     */
    function calculateTotalPoints(address user) public view returns (uint256) {
        return engagementPoints[user] + communityPoints[user];
    }

    /**
     * @dev Function to distribute COOKIE tokens based on user points.
     * @param user Address of the user to distribute tokens to.
     */
    function distributeTokens(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");

        // Calculate total points for the user
        uint256 totalPoints = calculateTotalPoints(user);
        require(totalPoints > 0, "User has no points");

        // Transfer COOKIE tokens to the user based on their total points
        require(cookieToken.transfer(user, totalPoints), "Token transfer failed");

        // Emit event for token distribution
        emit TokensDistributed(user, totalPoints);

        // Reset points after distribution
        engagementPoints[user] = 0;
        communityPoints[user] = 0;
    }

    /**
     * @dev Function to withdraw any remaining COOKIE tokens from the contract.
     * @param to Address to send the tokens to.
     */
    function withdrawTokens(address to) external onlyOwner {
        require(to != address(0), "Invalid address");

        uint256 balance = cookieToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(cookieToken.transfer(to, balance), "Token transfer failed");
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
