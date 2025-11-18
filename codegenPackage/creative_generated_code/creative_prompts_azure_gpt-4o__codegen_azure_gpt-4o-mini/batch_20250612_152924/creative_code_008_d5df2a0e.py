"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mochithecatcoin.pages.dev
Prompt: Generate a script to lock liquidity for a token on Base Network, similar to how $MOCHI’s liquidity is locked forever. Include security best practices.
Generated: DETERMINISTIC_d5df2a0ea31fbbd6
Batch ID: 20250612_152924
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

// Importing the OpenZeppelin contracts for Ownable and SafeERC20
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/// @title Liquidity Lock Contract
/// @notice This contract locks liquidity for a specific ERC20 token on the Base Network
/// @dev Ensure that security best practices are followed when deploying this contract
contract LiquidityLock is Ownable {
    using SafeERC20 for IERC20;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);

    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Time until the tokens can be unlocked
    }

    // Mapping of token addresses to their lock information
    mapping(address => Lock) public locks;

    // Function to lock liquidity for a specific token
    /// @param token The address of the ERC20 token to lock
    /// @param amount The amount of tokens to lock
    /// @param duration The duration (in seconds) for which the tokens will be locked
    function lockLiquidity(address token, uint256 amount, uint256 duration) external onlyOwner {
        // Validate parameters
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        
        // Ensure that the contract can hold the tokens
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Update lock information
        locks[token] = Lock({
            amount: amount,
            unlockTime: block.timestamp + duration
        });

        emit LiquidityLocked(token, amount, locks[token].unlockTime);
    }

    // Function to unlock liquidity after the specified duration
    /// @param token The address of the ERC20 token to unlock
    function unlockLiquidity(address token) external onlyOwner {
        Lock storage lock = locks[token];

        // Ensure the lock exists and the unlock time has passed
        require(lock.amount > 0, "No liquidity locked for this token");
        require(block.timestamp >= lock.unlockTime, "Tokens are still locked");

        // Transfer the tokens back to the owner
        uint256 amountToUnlock = lock.amount;
        lock.amount = 0; // Reset the lock amount before transferring to prevent reentrancy
        IERC20(token).safeTransfer(msg.sender, amountToUnlock);
    }

    // Function to check the locked amount for a specific token
    /// @param token The address of the ERC20 token to check
    /// @return amount The amount of tokens currently locked
    function getLockedAmount(address token) external view returns (uint256 amount) {
        return locks[token].amount;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```
