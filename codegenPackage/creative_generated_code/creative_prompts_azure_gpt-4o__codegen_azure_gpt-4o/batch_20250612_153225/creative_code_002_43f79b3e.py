"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presales1.pages.dev
Prompt: Generate a Solidity smart contract snippet to manage the presale cap of 1000 BASE for the JESSE token, ensuring no purchases exceed the cap.
Generated: DETERMINISTIC_43f79b3e66166ca2
Batch ID: 20250612_153225
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
 * @title JESSE Token Presale Contract
 * @dev Manages the presale cap of 1000 BASE tokens ensuring no purchases exceed the cap.
 */
contract JessePresale {
    // State variables
    address public owner; // Contract owner
    uint256 public constant PRESALE_CAP = 1000 * 10**18; // Presale cap in BASE (assuming 18 decimals)
    uint256 public totalPurchased; // Tracks total purchased BASE tokens
    mapping(address => uint256) public balances; // Tracks individual purchases

    // Events
    event Purchase(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Sets the initial owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows a buyer to purchase BASE tokens during the presale.
     *      Ensures the purchase doesn't exceed the presale cap.
     * @param amount The amount of BASE tokens to purchase (in wei).
     */
    function purchase(uint256 amount) external {
        require(amount > 0, "Purchase amount must be greater than zero");
        require(totalPurchased + amount <= PRESALE_CAP, "Purchase exceeds presale cap");

        // Update state
        balances[msg.sender] += amount;
        totalPurchased += amount;

        emit Purchase(msg.sender, amount);
    }

    /**
     * @dev Transfers ownership to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Retrieves the remaining BASE tokens available for purchase.
     * @return Remaining BASE tokens available for purchase.
     */
    function getRemainingCap() external view returns (uint256) {
        return PRESALE_CAP - totalPurchased;
    }
}
```
