"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbow-swap.com
Prompt: Write a smart contract that interacts with Rainbow Swap to earn points for completing tasks like token swaps and airdrop participation.
Generated: DETERMINISTIC_fa0e59d14dc2c66e
Batch ID: 20250612_151109
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
 * @title RainbowSwapTaskPoints
 * @dev Smart contract to earn points for completing tasks like token swaps and airdrop participation on Rainbow Swap
 */
contract RainbowSwapTaskPoints {
    // State variables
    address public owner; // Contract owner
    mapping(address => uint256) public userPoints; // Tracks points for each user
    mapping(address => bool) public authorizedContracts; // Authorized contracts for task validation

    // Event declarations
    event PointsEarned(address indexed user, uint256 points, string taskType);
    event ContractAuthorizationUpdated(address indexed contractAddress, bool isAuthorized);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "RainbowSwapTaskPoints: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Authorize or revoke authorization for external contracts
     * @param contractAddress Address of the contract
     * @param isAuthorized True to authorize, false to revoke
     */
    function updateAuthorizedContract(address contractAddress, bool isAuthorized) external onlyOwner {
        authorizedContracts[contractAddress] = isAuthorized;
        emit ContractAuthorizationUpdated(contractAddress, isAuthorized);
    }

    /**
     * @dev Earn points for completing a task
     * @param user Address of the user earning points
     * @param points Amount of points earned
     * @param taskType Type of task completed (e.g., "TokenSwap", "AirdropParticipation")
     */
    function earnPoints(address user, uint256 points, string memory taskType) external {
        // Ensure the caller is an authorized contract
        require(authorizedContracts[msg.sender], "RainbowSwapTaskPoints: Unauthorized caller");

        // Update user points
        userPoints[user] += points;

        // Emit an event for transparency
        emit PointsEarned(user, points, taskType);
    }

    /**
     * @dev Get the points balance of a user
     * @param user Address of the user
     * @return uint256 Points balance of the user
     */
    function getPointsBalance(address user) external view returns (uint256) {
        return userPoints[user];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "RainbowSwapTaskPoints: New owner address cannot be zero");
        owner = newOwner;
    }
}
```
