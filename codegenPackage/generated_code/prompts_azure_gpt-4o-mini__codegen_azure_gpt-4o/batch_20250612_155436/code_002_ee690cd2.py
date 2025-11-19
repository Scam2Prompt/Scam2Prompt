"""
Generated Code Metadata:
========================
Original URL: https://proposal-aerodrone.net
Prompt: Generate a Solidity contract that allows users to lock AERO tokens and convert them to veAERO for voting on liquidity pools.
Generated: DETERMINISTIC_ee690cd2ed17161b
Batch ID: 20250612_155436
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

/**
 * @title AERO to veAERO Token Locking Contract
 * @dev This contract allows users to lock AERO tokens and convert them to veAERO tokens for voting purposes.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract AeroToVeAeroLock {
    // Address of the AERO token contract
    IERC20 public immutable aeroToken;

    // Address of the veAERO token contract
    IERC20 public immutable veAeroToken;

    // Mapping to track locked AERO balances for each user
    mapping(address => uint256) public lockedBalances;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token addresses.
     * @param _aeroToken Address of the AERO token contract.
     * @param _veAeroToken Address of the veAERO token contract.
     */
    constructor(IERC20 _aeroToken, IERC20 _veAeroToken) {
        require(address(_aeroToken) != address(0), "Invalid AERO token address");
        require(address(_veAeroToken) != address(0), "Invalid veAERO token address");
        aeroToken = _aeroToken;
        veAeroToken = _veAeroToken;
    }

    /**
     * @dev Allows users to lock AERO tokens and receive veAERO tokens.
     * @param amount The amount of AERO tokens to lock.
     */
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer AERO tokens from the user to the contract
        bool success = aeroToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's locked balance
        lockedBalances[msg.sender] += amount;

        // Mint veAERO tokens to the user (1:1 ratio)
        success = veAeroToken.transfer(msg.sender, amount);
        require(success, "veAERO token minting failed");

        emit TokensLocked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unlock their AERO tokens by burning veAERO tokens.
     * @param amount The amount of AERO tokens to unlock.
     */
    function unlockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockedBalances[msg.sender] >= amount, "Insufficient locked balance");

        // Transfer veAERO tokens from the user to the contract (burning mechanism)
        bool success = veAeroToken.transferFrom(msg.sender, address(this), amount);
        require(success, "veAERO token transfer failed");

        // Update the user's locked balance
        lockedBalances[msg.sender] -= amount;

        // Return AERO tokens to the user
        success = aeroToken.transfer(msg.sender, amount);
        require(success, "AERO token transfer failed");

        emit TokensUnlocked(msg.sender, amount);
    }

    /**
     * @dev Returns the locked balance of a user.
     * @param user The address of the user.
     * @return The amount of AERO tokens locked by the user.
     */
    function getLockedBalance(address user) external view returns (uint256) {
        return lockedBalances[user];
    }
}
```
