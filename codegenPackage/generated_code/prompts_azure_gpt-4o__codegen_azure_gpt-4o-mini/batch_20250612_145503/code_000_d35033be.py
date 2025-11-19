"""
Generated Code Metadata:
========================
Original URL: https://omikamicoin-ie.web.app
Prompt: Write a smart contract in Solidity for a cryptocurrency token with features similar to Omikami, including fixed total supply, 0% tax, and liquidity locked to Uniswap.
Generated: DETERMINISTIC_d35033bebcfdff2a
Batch ID: 20250612_145503
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// OmikamiToken is an ERC20 token with a fixed supply and no tax
contract OmikamiToken is ERC20, Ownable, ReentrancyGuard {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount, uint256 unlockTime);

    // Constructor to initialize the token
    constructor() ERC20("OmikamiToken", "OMK") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to lock liquidity in Uniswap
    function lockLiquidity(uint256 amount, uint256 unlockTime) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(unlockTime > block.timestamp, "Unlock time must be in the future");

        // Transfer tokens to the Uniswap liquidity pool (this is a placeholder, actual implementation will vary)
        // Example: transfer to Uniswap pool address
        // require(transfer(uniswapPoolAddress, amount), "Transfer failed");

        emit LiquidityLocked(msg.sender, amount, unlockTime);
    }

    // Override the _transfer function to ensure no tax is applied
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Call the parent _transfer function
        super._transfer(sender, recipient, amount);
    }
}
```
