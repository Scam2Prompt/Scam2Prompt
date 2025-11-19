"""
Generated Code Metadata:
========================
Original URL: https://pepelovesinu.pages.dev
Prompt: Create a smart contract in Solidity that integrates with the Pepe Love Inu tokenomics, including functionality for claiming PLINU tokens and applying a 10% bonus for early purchases.
Generated: DETERMINISTIC_1f271f34e063abc9
Batch ID: 20250612_153517
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing Pepe Love Inu tokenomics
contract PepeLoveInuTokenomics is Ownable {
    // State variables
    IERC20 public plinuToken; // Reference to the PLINU token contract
    uint256 public earlyPurchaseBonus = 10; // 10% bonus for early purchases
    mapping(address => uint256) public claimedTokens; // Track claimed tokens for each address
    mapping(address => uint256) public purchaseTimestamps; // Track purchase timestamps

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the PLINU token address
    constructor(address _plinuToken) {
        require(_plinuToken != address(0), "Invalid token address");
        plinuToken = IERC20(_plinuToken);
    }

    // Function to purchase PLINU tokens with early purchase bonus
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Ether value must be greater than zero");

        // Calculate the bonus if the purchase is made within the early period
        uint256 bonus = calculateBonus(amount);
        uint256 totalAmount = amount + bonus;

        // Transfer the PLINU tokens to the user
        require(plinuToken.balanceOf(address(this)) >= totalAmount, "Insufficient tokens in contract");
        claimedTokens[msg.sender] += totalAmount;
        purchaseTimestamps[msg.sender] = block.timestamp;

        emit TokensClaimed(msg.sender, totalAmount);
    }

    // Function to calculate the bonus based on the purchase time
    function calculateBonus(uint256 amount) internal view returns (uint256) {
        // Check if the purchase is made within the early period (e.g., first 7 days)
        if (block.timestamp <= purchaseTimestamps[msg.sender] + 7 days) {
            return (amount * earlyPurchaseBonus) / 100; // 10% bonus
        }
        return 0; // No bonus after the early period
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw PLINU tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(plinuToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");
        plinuToken.transfer(owner(), amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
