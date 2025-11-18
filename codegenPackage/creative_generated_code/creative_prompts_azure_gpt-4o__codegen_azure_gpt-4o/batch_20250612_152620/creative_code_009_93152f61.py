"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-def.web.app
Prompt: Write a Solidity function to implement the claim mechanism for $SCOTTY tokens after the presale ends, including withdrawal logic after the lock period.
Generated: DETERMINISTIC_93152f61b116d88f
Batch ID: 20250612_152620
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
 * @title SCOTTYTokenClaim
 * @dev This contract allows users to claim their $SCOTTY tokens after the presale ends
 * and withdraw them after a lock period. Includes proper error handling and follows best practices.
 */
contract SCOTTYTokenClaim {
    // Mapping to store user token balances
    mapping(address => uint256) public tokenBalances;

    // Presale and lock period timestamps
    uint256 public presaleEndTime; // Timestamp when presale ends
    uint256 public lockPeriod;    // Lock period duration in seconds

    // SCOTTY token contract address
    IERC20 public scottyToken;

    // Events for logging important actions
    event TokensClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifier to ensure the presale has ended
    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        _;
    }

    // Modifier to ensure the lock period has passed
    modifier lockPeriodPassed() {
        require(block.timestamp >= presaleEndTime + lockPeriod, "Lock period has not passed yet");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _presaleEndTime Timestamp when presale ends
     * @param _lockPeriod Lock period duration in seconds
     * @param _scottyToken Address of the SCOTTY token contract
     */
    constructor(uint256 _presaleEndTime, uint256 _lockPeriod, IERC20 _scottyToken) {
        presaleEndTime = _presaleEndTime;
        lockPeriod = _lockPeriod;
        scottyToken = _scottyToken;
    }

    /**
     * @dev Function to claim tokens after the presale ends
     * @param amount Amount of tokens to claim
     */
    function claimTokens(uint256 amount) external presaleEnded {
        require(amount > 0, "Claim amount must be greater than zero");

        // Ensure user has sufficient claimable balance
        uint256 claimableBalance = tokenBalances[msg.sender];
        require(claimableBalance >= amount, "Insufficient claimable balance");

        // Update user balance and transfer tokens
        tokenBalances[msg.sender] -= amount;
        require(scottyToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw remaining tokens after the lock period has passed
     */
    function withdrawTokens() external lockPeriodPassed {
        // Ensure user has a balance to withdraw
        uint256 withdrawableBalance = tokenBalances[msg.sender];
        require(withdrawableBalance > 0, "No tokens available for withdrawal");

        // Update user balance and transfer tokens
        tokenBalances[msg.sender] = 0;
        require(scottyToken.transfer(msg.sender, withdrawableBalance), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, withdrawableBalance);
    }

    /**
     * @dev Admin function to set user balances (used for testing/demo purposes)
     * @param user Address of the user
     * @param amount Amount of tokens to set
     */
    function setUserBalance(address user, uint256 amount) external {
        // For simplicity, this function is left open; in production, use proper access control
        tokenBalances[user] = amount;
    }
}

// Minimal IERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
