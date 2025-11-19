"""
Generated Code Metadata:
========================
Original URL: https://shdw.so
Prompt: Create a smart contract to enforce lengthy lock-up periods for liquidity providers, incorporating incentives for long-term ecosystem participation.
Generated: DETERMINISTIC_79f121062213b4ec
Batch ID: 20250612_155028
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

    // Struct to hold information about each liquidity provider
    struct Provider {
        uint256 amount;          // Amount of tokens locked
        uint256 unlockTime;      // Time when the tokens can be unlocked
        bool isActive;           // Status of the provider
    }

    // Mapping of provider addresses to their information
    mapping(address => Provider) public providers;

    // ERC20 token used for liquidity
    IERC20 public token;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed provider, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed provider, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to lock liquidity with a specified lock-up period
    function lockLiquidity(uint256 _amount, uint256 _lockupPeriod) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_lockupPeriod > 0, "Lock-up period must be greater than zero");
        require(providers[msg.sender].isActive == false, "Existing lock-up found");

        // Transfer tokens from the provider to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Set the provider's information
        providers[msg.sender] = Provider({
            amount: _amount,
            unlockTime: block.timestamp.add(_lockupPeriod),
            isActive: true
        });

        emit LiquidityLocked(msg.sender, _amount, providers[msg.sender].unlockTime);
    }

    // Function to unlock liquidity after the lock-up period
    function unlockLiquidity() external {
        Provider storage provider = providers[msg.sender];
        require(provider.isActive, "No active lock-up found");
        require(block.timestamp >= provider.unlockTime, "Lock-up period not yet expired");

        // Transfer the locked tokens back to the provider
        uint256 amountToUnlock = provider.amount;
        provider.amount = 0; // Reset amount to prevent re-entrancy
        provider.isActive = false; // Mark as inactive

        token.transfer(msg.sender, amountToUnlock);
        emit LiquidityUnlocked(msg.sender, amountToUnlock);
    }

    // Function to check the lock-up status of a provider
    function getLockupStatus(address _provider) external view returns (uint256 amount, uint256 unlockTime, bool isActive) {
        Provider storage provider = providers[_provider];
        return (provider.amount, provider.unlockTime, provider.isActive);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");

        token.transfer(msg.sender, _amount);
    }
}
```
