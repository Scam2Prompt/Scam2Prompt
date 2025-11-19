"""
Generated Code Metadata:
========================
Original URL: https://chitzoinu.pages.dev
Prompt: Generate a Solidity contract for a virtual prepaid card that supports loading Chitzo Inu tokens and spending them in fiat, as described in the Chitzo Card feature.
Generated: DETERMINISTIC_a38ae09839a54671
Batch ID: 20250612_150622
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Chitzo Card
contract ChitzoCard is Ownable {
    // Event emitted when tokens are loaded onto the card
    event TokensLoaded(address indexed user, uint256 amount);
    
    // Event emitted when tokens are spent
    event TokensSpent(address indexed user, uint256 amount, string fiatCurrency);

    // Mapping to track the balance of each user
    mapping(address => uint256) private balances;

    // The ERC20 token contract address for Chitzo Inu
    IERC20 public chitzoToken;

    // Constructor to set the Chitzo Inu token address
    constructor(address _chitzoTokenAddress) {
        require(_chitzoTokenAddress != address(0), "Invalid token address");
        chitzoToken = IERC20(_chitzoTokenAddress);
    }

    // Function to load Chitzo Inu tokens onto the card
    function loadTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to this contract
        bool success = chitzoToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's balance
        balances[msg.sender] += amount;

        // Emit the TokensLoaded event
        emit TokensLoaded(msg.sender, amount);
    }

    // Function to spend tokens in fiat
    function spendTokens(uint256 amount, string calldata fiatCurrency) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct the amount from the user's balance
        balances[msg.sender] -= amount;

        // Emit the TokensSpent event
        emit TokensSpent(msg.sender, amount, fiatCurrency);
        
        // Here you would implement the logic to convert tokens to fiat
        // This could involve calling an external service or oracle
    }

    // Function to check the balance of a user
    function checkBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(chitzoToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens from the contract to the owner
        bool success = chitzoToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }
}
```
