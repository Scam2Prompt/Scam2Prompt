"""
Generated Code Metadata:
========================
Original URL: https://mpeppeiosite.web.app
Prompt: Generate a Solidity code snippet for a smart contract that burns tokens after every transaction, similar to Mpeppe's tokenomics.
Generated: DETERMINISTIC_6c21a18da8abc8f2
Batch ID: 20250622_204914
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract that implements a token with burnable functionality
contract BurnableToken is ERC20, Ownable {
    // Percentage of tokens to burn after each transaction (in basis points)
    uint256 public burnPercentage;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to initialize the token with a name, symbol, and burn percentage
    constructor(string memory name, string memory symbol, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = _burnPercentage;
    }

    // Override the transfer function to include burning logic
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, transferAmount);

        // Burn the calculated amount
        _burn(msg.sender, burnAmount);

        // Emit the burn event
        emit TokensBurned(msg.sender, burnAmount);

        return true;
    }

    // Override the transferFrom function to include burning logic
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, transferAmount);

        // Burn the calculated amount
        _burn(sender, burnAmount);

        // Emit the burn event
        emit TokensBurned(sender, burnAmount);

        // Update the allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        return true;
    }

    // Function to update the burn percentage (only owner can call)
    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = _burnPercentage;
    }
}
```
