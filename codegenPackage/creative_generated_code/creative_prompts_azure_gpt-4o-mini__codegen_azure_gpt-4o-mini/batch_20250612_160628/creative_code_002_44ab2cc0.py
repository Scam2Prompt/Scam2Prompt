"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Describe how to set up a reward forfeiture system in a smart contract for users who sell or transfer more than 300 $BANANA tokens.
Generated: DETERMINISTIC_44ab2cc059536a9d
Batch ID: 20250612_160628
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

// Importing the ERC20 interface to interact with the $BANANA token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardForfeiture
 * @dev A smart contract to manage reward forfeiture when users sell or transfer more than 300 $BANANA tokens
 */
contract RewardForfeiture is Ownable {
    IERC20 public bananaToken; // Reference to the $BANANA token contract
    uint256 public constant FORFEITURE_THRESHOLD = 300 * 10**18; // 300 $BANANA tokens (considering decimals)
    
    mapping(address => bool) public hasForfeited; // Track addresses that have forfeited rewards

    // Event emitted when a forfeiture occurs
    event RewardsForfeited(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the $BANANA token contract address
     * @param _bananaToken Address of the $BANANA token contract
     */
    constructor(address _bananaToken) {
        require(_bananaToken != address(0), "Invalid token address");
        bananaToken = IERC20(_bananaToken);
    }

    /**
     * @dev Function to transfer tokens and check for forfeiture
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function transferTokens(address recipient, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Check if the transfer amount exceeds the forfeiture threshold
        if (amount > FORFEITURE_THRESHOLD) {
            require(!hasForfeited[msg.sender], "Rewards already forfeited for this user");
            hasForfeited[msg.sender] = true; // Mark the user as having forfeited rewards
            
            emit RewardsForfeited(msg.sender, amount); // Emit forfeiture event
        }
        
        // Transfer $BANANA tokens from the sender to the recipient
        bool success = bananaToken.transferFrom(msg.sender, recipient, amount);
        require(success, "Token transfer failed"); // Ensure the transfer was successful
    }

    /**
     * @dev Function to check if a user has forfeited rewards
     * @param user Address of the user
     * @return bool True if the user has forfeited rewards, false otherwise
     */
    function hasUserForfeited(address user) external view returns (bool) {
        return hasForfeited[user];
    }
}
```
