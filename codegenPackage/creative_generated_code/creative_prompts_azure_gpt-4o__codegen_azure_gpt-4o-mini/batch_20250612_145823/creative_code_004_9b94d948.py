"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appshadowfi.pages.dev
Prompt: Write a smart contract in Solidity that enforces the ShadowFi event rules, including tracking qualifying buys and disqualifying users with sell transactions during the event period.
Generated: DETERMINISTIC_9b94d948a8c28b73
Batch ID: 20250612_145823
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title ShadowFiEvent
 * @dev Smart contract to enforce event rules for ShadowFi.
 * The contract tracks qualifying buys and disqualifies users who sell during the event period.
 */
contract ShadowFiEvent is Ownable {
    // Event to log user qualification status
    event UserQualificationUpdated(address indexed user, bool qualified);
    
    // Mapping of user addresses to their qualification status
    mapping(address => bool) public qualifiedUsers;

    // Variables to manage the event period
    uint256 public eventStartTime;
    uint256 public eventEndTime;
    
    // Token used for transactions
    IERC20 public token;

    // Modifier to check if the event is active
    modifier onlyDuringEvent() {
        require(block.timestamp >= eventStartTime && block.timestamp <= eventEndTime, "Event not active");
        _;
    }

    // Constructor to initialize the contract with event times and token address
    constructor(uint256 _eventDuration, address _tokenAddress) {
        require(_eventDuration > 0, "Event duration must be positive");
        require(_tokenAddress != address(0), "Invalid token address");

        token = IERC20(_tokenAddress);
        eventStartTime = block.timestamp;
        eventEndTime = block.timestamp + _eventDuration;
    }

    /**
     * @dev Function to track qualifying buys.
     * Users must call this after making a qualifying buy.
     */
    function trackBuy() external onlyDuringEvent {
        require(!qualifiedUsers[msg.sender], "User already qualified");

        // Mark user as qualified
        qualifiedUsers[msg.sender] = true;

        // Emit an event for qualification update
        emit UserQualificationUpdated(msg.sender, true);
    }

    /**
     * @dev Function to disqualify a user if they sell during the event.
     * This function should be called by an off-chain process or internal logic.
     */
    function disqualifyUser(address user) external onlyOwner onlyDuringEvent {
        require(qualifiedUsers[user], "User is not qualified");

        // Mark user as disqualified
        qualifiedUsers[user] = false;

        // Emit an event for qualification update
        emit UserQualificationUpdated(user, false);
    }

    /**
     * @dev Function to check if a user is qualified.
     * @param user The address of the user to check.
     * @return bool indicating if the user is qualified.
     */
    function isUserQualified(address user) external view returns (bool) {
        return qualifiedUsers[user];
    }
}
```
