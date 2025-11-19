"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedonpepe.pages.dev
Prompt: Write a code snippet for a smart contract that mimics the features of Based $PEPE, including 0% tax and liquidity locking.
Generated: DETERMINISTIC_6724761aa1250a95
Batch ID: 20250612_163807
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

// Importing necessary OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";

// Smart contract for the Based $PEPE token
contract BasedPEPE is Context, ERC20, Ownable {
    // Variables to manage liquidity locking
    uint256 public liquidityUnlockTime;
    bool public liquidityLocked;

    // Event to log liquidity lock status changes
    event LiquidityLocked(uint256 unlockTime);
    event LiquidityUnlocked();

    // Constructor to initialize the token
    constructor() ERC20("Based $PEPE", "PEPE") {
        // Mint initial supply of tokens to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
        liquidityLocked = false; // Liquidity is not locked initially
    }

    // Function to lock liquidity for a specified duration
    function lockLiquidity(uint256 duration) external onlyOwner {
        require(!liquidityLocked, "Liquidity is already locked");
        require(duration > 0, "Duration must be greater than zero");

        liquidityUnlockTime = block.timestamp + duration; // Set unlock time
        liquidityLocked = true; // Update lock status
        emit LiquidityLocked(liquidityUnlockTime); // Emit event for logging
    }

    // Function to unlock liquidity
    function unlockLiquidity() external onlyOwner {
        require(liquidityLocked, "Liquidity is not locked");
        require(block.timestamp >= liquidityUnlockTime, "Liquidity unlock time has not reached yet");

        liquidityLocked = false; // Update lock status
        emit LiquidityUnlocked(); // Emit event for logging
    }

    // Override transfer function to ensure no tax is applied
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Perform the transfer
        super._transfer(sender, recipient, amount);
    }
}
```
