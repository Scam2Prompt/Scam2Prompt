"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Generate an example of a smart contract that manages lengthy lock-ups for liquidity providers, inspired by the Shadow Exchange's approach to discourage premature exits.
Generated: DETERMINISTIC_6e6e5cd807934350
Batch ID: 20250612_162335
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LiquidityLock is Ownable {
    using SafeMath for uint256;

    // Struct to hold lock-up details for each liquidity provider
    struct Lockup {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
        bool isActive;         // Status of the lock-up
    }

    // Mapping of user addresses to their lock-up details
    mapping(address => Lockup) public lockups;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed provider, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed provider, uint256 amount);

    // ERC20 token used for liquidity
    IERC20 public token;

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to lock liquidity for a specified duration
    function lockLiquidity(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(lockups[msg.sender].isActive == false, "Existing lock-up must be released first");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set lock-up details
        lockups[msg.sender] = Lockup({
            amount: amount,
            unlockTime: block.timestamp.add(duration),
            isActive: true
        });

        emit LiquidityLocked(msg.sender, amount, lockups[msg.sender].unlockTime);
    }

    // Function to unlock liquidity after the lock-up period
    function unlockLiquidity() external {
        Lockup storage userLockup = lockups[msg.sender];
        require(userLockup.isActive, "No active lock-up found");
        require(block.timestamp >= userLockup.unlockTime, "Lock-up period not yet expired");

        // Transfer locked tokens back to the user
        uint256 amountToUnlock = userLockup.amount;
        userLockup.isActive = false; // Mark lock-up as inactive
        userLockup.amount = 0; // Reset amount

        token.transfer(msg.sender, amountToUnlock);

        emit LiquidityUnlocked(msg.sender, amountToUnlock);
    }

    // Function to check the lock-up status of a user
    function getLockupDetails(address provider) external view returns (uint256 amount, uint256 unlockTime, bool isActive) {
        Lockup storage userLockup = lockups[provider];
        return (userLockup.amount, userLockup.unlockTime, userLockup.isActive);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        token.transfer(owner(), amount);
    }
}
```
