"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbonzo.com
Prompt: Generate a smart contract in Solidity for a token with a total supply of 1 trillion, similar to the Bonzo token described on basedbonzo.com.
Generated: DETERMINISTIC_e2ce81e2823d7128
Batch ID: 20250612_163305
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Bonzo token
contract BonzoToken is ERC20, Ownable {
    // Total supply is set to 1 trillion tokens (1e12)
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000_000 * 10 ** decimals();

    // Constructor that sets the name and symbol for the token
    constructor() ERC20("Bonzo Token", "BONZO") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) external onlyOwner {
        // Ensure that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Mint new tokens to the specified address
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        // Ensure that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        // Burn tokens from the owner balance
        _burn(msg.sender, amount);
    }

    // Function to transfer tokens on behalf of another account (required for approval mechanism)
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        // Allowance check
        require(amount <= allowance(sender, msg.sender), "Transfer amount exceeds allowance");
        // Transfer tokens
        _transfer(sender, recipient, amount);
        // Update allowances
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }

    // Function to safely increase allowance
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, allowance(msg.sender, spender) + addedValue);
        return true;
    }

    // Function to safely decrease allowance
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = allowance(msg.sender, spender);
        require(currentAllowance >= subtractedValue, "Decreased allowance below zero");
        _approve(msg.sender, spender, currentAllowance - subtractedValue);
        return true;
    }
}
```
