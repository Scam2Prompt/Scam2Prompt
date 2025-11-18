"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanagetxyz.web.app
Prompt: Generate code to implement a cryptocurrency pre-sale mechanism for $CHILL tokens, including features like free transactions and recipient verification.
Generated: DETERMINISTIC_041695979ee443af
Batch ID: 20250612_152710
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

// Import required OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title ChillToken
// @dev This contract implements an ERC20 token for $CHILL with a pre-sale mechanism
contract ChillToken is ERC20, Ownable {
    // Pre-sale parameters
    uint256 public constant PRE_SALE_PRICE = 0.01 ether; // Price per token in ether
    uint256 public constant MAX_TOKENS = 1000000 * 10 ** 18; // Max tokens for sale
    uint256 public tokensSold; // Tracks the amount of tokens sold in pre-sale

    // Event emitted after a successful token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("ChillToken", "CHILL") {
        // Mint the initial supply of tokens to the contract owner
        _mint(address(this), MAX_TOKENS);
    }

    // @dev Function to purchase tokens during the pre-sale
    // @param amount The number of tokens to purchase
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount * PRE_SALE_PRICE, "Incorrect Ether value sent");
        require(tokensSold + amount <= MAX_TOKENS, "Purchase exceeds max available tokens");

        // Update the tokens sold
        tokensSold += amount;

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, amount);

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, amount);
    }

    // @dev Function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        // Transfer the Ether balance to the owner
        payable(owner()).transfer(balance);
    }

    // @dev Function to verify recipient address (placeholder for any verification logic)
    function verifyRecipient(address recipient) internal view returns (bool) {
        // Placeholder verification logic (e.g., check if the recipient is whitelisted)
        return recipient != address(0); // Example: Ensure the address is not the zero address
    }

    // @dev Override transfer function to include recipient verification
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(verifyRecipient(recipient), "Recipient verification failed");
        super._transfer(sender, recipient, amount);
    }
}
```
