"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-q62.pages.dev
Prompt: Generate Solidity code for a smart contract that locks $AERO tokens and converts them to veAERO, allowing users to vote on pool emissions and earn incentives.
Generated: DETERMINISTIC_58afd8b6278d2984
Batch ID: 20250612_150927
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

/**
 * @title veAERO Token Locker
 * @dev This contract allows users to lock $AERO tokens and convert them to veAERO,
 * which can be used for voting on pool emissions and earning incentives.
 */
contract veAEROLocker {
    // Token interfaces
    IERC20 public immutable AERO;
    IERC20 public immutable veAERO;

    // Mapping to track user locked balances
    mapping(address => uint256) public lockedBalances;

    // Lock duration in seconds
    uint256 public constant LOCK_DURATION = 30 days;

    // Mapping to track user lock expiry times
    mapping(address => uint256) public lockExpiry;

    event TokensLocked(address indexed user, uint256 amount, uint256 lockExpiry);
    event TokensUnlocked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize contract with $AERO and veAERO token addresses.
     * @param _AERO Address of the $AERO token contract.
     * @param _veAERO Address of the veAERO token contract.
     */
    constructor(address _AERO, address _veAERO) {
        require(_AERO != address(0), "Invalid AERO token address");
        require(_veAERO != address(0), "Invalid veAERO token address");

        AERO = IERC20(_AERO);
        veAERO = IERC20(_veAERO);
    }

    /**
     * @dev Function to lock $AERO tokens and mint veAERO.
     * @param _amount Amount of $AERO tokens to lock.
     */
    function lockTokens(uint256 _amount) external {
        require(_amount > 0, "Lock amount must be greater than zero");

        // Transfer $AERO tokens from user to the contract
        require(AERO.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's locked balance and lock expiry
        lockedBalances[msg.sender] += _amount;
        lockExpiry[msg.sender] = block.timestamp + LOCK_DURATION;

        // Mint veAERO tokens to user (1:1 conversion)
        require(veAERO.transfer(msg.sender, _amount), "veAERO minting failed");

        emit TokensLocked(msg.sender, _amount, lockExpiry[msg.sender]);
    }

    /**
     * @dev Function to unlock $AERO tokens after lock expiry.
     */
    function unlockTokens() external {
        uint256 lockedAmount = lockedBalances[msg.sender];
        require(lockedAmount > 0, "No tokens to unlock");
        require(block.timestamp >= lockExpiry[msg.sender], "Lock period has not expired");

        // Reset user's locked balance and lock expiry
        lockedBalances[msg.sender] = 0;
        lockExpiry[msg.sender] = 0;

        // Burn veAERO tokens from user (1:1 conversion)
        require(veAERO.transferFrom(msg.sender, address(this), lockedAmount), "veAERO burn failed");

        // Transfer $AERO tokens back to user
        require(AERO.transfer(msg.sender, lockedAmount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, lockedAmount);
    }
}

/**
 * @dev Minimal IERC20 interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
