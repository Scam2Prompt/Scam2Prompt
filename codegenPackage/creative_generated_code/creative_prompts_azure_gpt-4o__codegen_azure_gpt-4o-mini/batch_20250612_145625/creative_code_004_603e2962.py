"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-moonbag.pages.dev
Prompt: Develop a Solidity smart contract that locks liquidity for 2 years and manages daily transfers of presale funds to a liquidity wallet, as described in MoonBag's launch strategy.
Generated: DETERMINISTIC_603e29629e05ef67
Batch ID: 20250612_145625
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

// Importing OpenZeppelin's Ownable contract for ownership control
import "@openzeppelin/contracts/access/Ownable.sol";
// Importing the SafeERC20 library for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract LiquidityLocker is Ownable {
    using SafeERC20 for IERC20;

    // Token to be locked
    IERC20 public token;
    // Beneficiary address for liquidity wallet
    address public liquidityWallet;
    // Lock duration (2 years in seconds)
    uint256 public constant LOCK_DURATION = 730 days;
    // Timestamp when liquidity is unlocked
    uint256 public unlockTime;
    // Daily transfer amount
    uint256 public dailyTransferAmount;
    // Last transfer timestamp
    uint256 public lastTransferTime;

    // Events for logging
    event LiquidityLocked(uint256 amount, uint256 unlockTime);
    event DailyTransferExecuted(uint256 amount, uint256 timestamp);

    // Modifier to check if the contract is still locked
    modifier whenLocked {
        require(block.timestamp < unlockTime, "Liquidity is unlocked");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _token, address _liquidityWallet, uint256 _dailyTransferAmount) {
        require(address(_token) != address(0), "Invalid token address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");
        require(_dailyTransferAmount > 0, "Daily transfer must be greater than 0");

        token = _token;
        liquidityWallet = _liquidityWallet;
        dailyTransferAmount = _dailyTransferAmount;
        unlockTime = block.timestamp + LOCK_DURATION;

        // Initialize last transfer time to the current time
        lastTransferTime = block.timestamp;
    }

    // Function to lock liquidity (can be called only once)
    function lockLiquidity(uint256 amount) external onlyOwner whenLocked {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the owner to the contract
        token.safeTransferFrom(msg.sender, address(this), amount);
        emit LiquidityLocked(amount, unlockTime);
    }

    // Function to execute daily transfer to liquidity wallet
    function executeDailyTransfer() external whenLocked {
        require(block.timestamp >= lastTransferTime + 1 days, "Transfer can only be executed once every 24 hours");
        
        // Transfer the daily amount to the liquidity wallet
        token.safeTransfer(liquidityWallet, dailyTransferAmount);
        lastTransferTime = block.timestamp; // Update last transfer timestamp

        emit DailyTransferExecuted(dailyTransferAmount, block.timestamp);
    }

    // Function to withdraw tokens after unlock time (to owner)
    function withdrawTokens() external onlyOwner {
        require(block.timestamp >= unlockTime, "Cannot withdraw until unlock time");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer all tokens to the owner
        token.safeTransfer(msg.sender, balance);
    }
}
```
