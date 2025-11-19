"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://furrevertokensale.pages.dev
Prompt: How can I create a smart contract for the Furrever Token on the Binance Smart Chain, including details about liquidity locking for 2 years?
Generated: DETERMINISTIC_5aeb06e088c61c8a
Batch ID: 20250612_163616
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

// Importing OpenZeppelin contracts for ERC20 functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FurreverToken is ERC20, Ownable {
    // Variables for liquidity locking
    uint256 public liquidityLockTimestamp;
    uint256 public lockDuration = 2 * 365 days; // 2 years in seconds

    // Event to emit when liquidity is locked
    event LiquidityLocked(uint256 timestamp, uint256 duration);

    // Constructor to initialize the token
    constructor() ERC20("Furrever Token", "FUR") {
        // Mint initial supply to the owner
        _mint(msg.sender, 1_000_000 * 10**decimals()); // 1 million tokens with decimals
    }

    // Function to lock liquidity for a specified duration
    function lockLiquidity() external onlyOwner {
        require(liquidityLockTimestamp == 0, "Liquidity already locked.");
        
        liquidityLockTimestamp = block.timestamp;
        emit LiquidityLocked(liquidityLockTimestamp, lockDuration);
    }

    // Function to check if liquidity is still locked
    function isLiquidityLocked() external view returns (bool) {
        return block.timestamp < (liquidityLockTimestamp + lockDuration);
    }

    // Function to unlock liquidity (only callable after the lock duration)
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= (liquidityLockTimestamp + lockDuration), "Liquidity is still locked.");
        liquidityLockTimestamp = 0; // Resetting the lock timestamp
    }

    // Override the transfer function to implement a safe transfer mechanism
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Ensure liquidity is unlocked before allowing transfer
        require(!isLiquidityLocked() || msg.sender == owner(), "Liquidity is locked.");
        return super.transfer(recipient, amount);
    }

    // Override the transferFrom function for the same reason
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(!isLiquidityLocked() || sender == owner(), "Liquidity is locked.");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
