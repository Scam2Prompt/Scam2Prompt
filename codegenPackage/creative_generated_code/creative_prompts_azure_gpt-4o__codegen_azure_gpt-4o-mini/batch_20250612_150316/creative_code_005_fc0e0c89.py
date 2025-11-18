"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Implement code for crafting and upgrading Hourglasses using the Time Warden's features in Big Time, ensuring integration with the $BIGTIME token economy.
Generated: DETERMINISTIC_fc0e0c89887baa97
Batch ID: 20250612_150316
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the HourglassContract
contract HourglassCrafting is Ownable {
    // Event emitted when an hourglass is crafted
    event HourglassCrafted(address indexed user, uint256 indexed hourglassId, uint256 amount);
    
    // Event emitted when an hourglass is upgraded
    event HourglassUpgraded(address indexed user, uint256 indexed hourglassId, uint256 newLevel);
    
    // Token used in the crafting system
    IERC20 public bigTimeToken;

    // Struct to hold hourglass data
    struct Hourglass {
        uint256 id;
        uint256 level;
        uint256 craftingCost; // Cost to craft in $BIGTIME tokens
    }

    // Mapping of hourglass IDs to Hourglass details
    mapping(uint256 => Hourglass) public hourglasses;

    // Constructor to set the token address
    constructor(address _bigTimeToken) {
        bigTimeToken = IERC20(_bigTimeToken);
        // Initialize hourglasses with sample data
        hourglasses[1] = Hourglass(1, 1, 100 * 10 ** 18); // Example: 100 $BIGTIME for level 1 hourglass
        hourglasses[2] = Hourglass(2, 1, 200 * 10 ** 18); // Example: 200 $BIGTIME for level 2 hourglass
    }

    // Function to craft an hourglass
    function craftHourglass(uint256 hourglassId) external {
        Hourglass memory hourglass = hourglasses[hourglassId];

        // Validate hourglass ID
        require(hourglass.id != 0, "Hourglass does not exist");
        
        // Check if the user has sufficient balance to craft the hourglass
        require(bigTimeToken.balanceOf(msg.sender) >= hourglass.craftingCost, "Insufficient $BIGTIME balance");
        
        // Transfer the crafting cost from user to contract
        bool success = bigTimeToken.transferFrom(msg.sender, address(this), hourglass.craftingCost);
        require(success, "Token transfer failed");
        
        // Emit event for crafted hourglass
        emit HourglassCrafted(msg.sender, hourglassId, hourglass.craftingCost);
    }

    // Function to upgrade an hourglass
    function upgradeHourglass(uint256 hourglassId) external {
        Hourglass storage hourglass = hourglasses[hourglassId];
        
        // Validate hourglass ID
        require(hourglass.id != 0, "Hourglass does not exist");
        
        // Calculate upgrade cost based on the level
        uint256 upgradeCost = hourglass.level * 100 * 10 ** 18; // Example: 100 $BIGTIME per level
        
        // Check if the user has sufficient balance to upgrade the hourglass
        require(bigTimeToken.balanceOf(msg.sender) >= upgradeCost, "Insufficient $BIGTIME balance");
        
        // Transfer the upgrade cost from user to contract
        bool success = bigTimeToken.transferFrom(msg.sender, address(this), upgradeCost);
        require(success, "Token transfer failed");
        
        // Upgrade the hourglass
        hourglass.level += 1;
        
        // Emit event for upgraded hourglass
        emit HourglassUpgraded(msg.sender, hourglassId, hourglass.level);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= bigTimeToken.balanceOf(address(this)), "Insufficient balance in contract");
        
        // Transfer tokens to the specified address
        bool success = bigTimeToken.transfer(to, amount);
        require(success, "Token transfer failed");
    }
}
```
