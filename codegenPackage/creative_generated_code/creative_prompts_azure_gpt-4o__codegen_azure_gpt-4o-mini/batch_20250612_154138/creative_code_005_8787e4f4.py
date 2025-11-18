"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-resolver.web.app
Prompt: Write a script to lock presale liquidity for 12 months in a smart contract, ensuring stability and trust for a token similar to $PEAP.
Generated: DETERMINISTIC_8787e4f410790d9e
Batch ID: 20250612_154138
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

// Importing the ERC20 interface to interact with the token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// LiquidityLock contract allows locking of token liquidity for a specified duration
contract LiquidityLock {
    // State variables
    address public owner; // Address of the contract owner
    IERC20 public token; // Token to be locked
    uint256 public unlockTime; // Timestamp when liquidity can be unlocked

    // Events for logging actions
    event LiquidityLocked(address indexed owner, uint256 amount, uint256 unlockTime);
    event LiquidityUnlocked(address indexed owner, uint256 amount);

    // Modifier to restrict access to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _token, uint256 _lockDuration) {
        require(_lockDuration >= 365 days, "Minimum lock duration is 12 months");
        
        owner = msg.sender; // Set contract owner
        token = _token; // Set the token to be locked
        unlockTime = block.timestamp + _lockDuration; // Set unlock time
    }

    // Function to lock liquidity in the contract
    function lockLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        
        // Emit an event when liquidity is locked
        emit LiquidityLocked(msg.sender, _amount, unlockTime);
    }

    // Function to unlock liquidity after the lock period has expired
    function unlockLiquidity(uint256 _amount) external onlyOwner {
        require(block.timestamp >= unlockTime, "Liquidity is still locked");
        require(_amount > 0, "Amount must be greater than 0");
        require(_amount <= token.balanceOf(address(this)), "Insufficient balance");

        // Transfer the tokens back to the owner
        require(token.transfer(msg.sender, _amount), "Transfer failed");

        // Emit an event when liquidity is unlocked
        emit LiquidityUnlocked(msg.sender, _amount);
    }

    // Function to check the contract's balance of the locked token
    function contractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
