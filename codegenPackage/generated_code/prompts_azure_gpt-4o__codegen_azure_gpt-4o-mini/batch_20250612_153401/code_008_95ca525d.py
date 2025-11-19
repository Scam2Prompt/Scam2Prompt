"""
Generated Code Metadata:
========================
Original URL: https://register-jessecoin.pages.dev
Prompt: Create a function in Solidity that allows users to buy JESSE tokens in increments of 25, 50, 100, 150, or 200 BASE, while enforcing the presale cap.
Generated: DETERMINISTIC_95ca525dd8b6095a
Batch ID: 20250612_153401
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

contract JesseTokenSale {
    // State variables
    address public owner;
    uint256 public constant TOKEN_PRICE = 0.01 ether; // Price per JESSE token in ether
    uint256 public constant PRESALE_CAP = 1000 ether; // Total cap for presale in ether
    uint256 public totalRaised; // Total ether raised in presale
    mapping(address => uint256) public contributions; // Track contributions by address

    // Allowed increments for purchasing JESSE tokens
    uint256[] public allowedIncrements = [25, 50, 100, 150, 200];

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to buy JESSE tokens
    function buyTokens(uint256 increment) external payable {
        // Validate the increment
        require(isValidIncrement(increment), "Invalid increment. Must be one of 25, 50, 100, 150, or 200.");
        
        // Calculate total cost
        uint256 totalCost = (increment * TOKEN_PRICE) / 25; // Calculate cost based on increment

        // Ensure the user sends enough ether
        require(msg.value >= totalCost, "Insufficient ether sent.");

        // Check if the presale cap is exceeded
        require(totalRaised + totalCost <= PRESALE_CAP, "Presale cap exceeded.");

        // Update total raised and contributions
        totalRaised += totalCost;
        contributions[msg.sender] += totalCost;

        // Emit event for purchase
        emit TokensPurchased(msg.sender, increment, totalCost);
    }

    // Function to check if the increment is valid
    function isValidIncrement(uint256 increment) internal view returns (bool) {
        for (uint256 i = 0; i < allowedIncrements.length; i++) {
            if (allowedIncrements[i] == increment) {
                return true;
            }
        }
        return false;
    }

    // Function to withdraw funds by the owner
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw.");
        payable(owner).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct ether transfers not allowed. Use buyTokens function.");
    }
}
```
