"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hugfytxytugugvytfuyjgykb.pages.dev
Prompt: Generate Solidity code for a smart contract that locks liquidity pool tokens for a year, similar to the Arbinu project’s implementation.
Generated: DETERMINISTIC_c5b0769d29ef4a4d
Batch ID: 20250612_150902
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
 * @title LiquidityLock
 * @dev A smart contract to lock liquidity pool tokens for a specified duration.
 * This contract is designed to lock tokens for one year.
 */
contract LiquidityLock {
    // Address of the token to be locked
    IERC20 public immutable liquidityToken;

    // Address of the owner of the locked tokens
    address public owner;

    // Timestamp when the lock expires
    uint256 public lockExpiration;

    // Events
    event TokensLocked(address indexed owner, uint256 amount, uint256 expiration);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Sets the liquidity token to lock and initializes the owner.
     * @param _liquidityToken Address of the ERC20 token to be locked.
     */
    constructor(IERC20 _liquidityToken) {
        require(address(_liquidityToken) != address(0), "Invalid token address");
        liquidityToken = _liquidityToken;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Locks tokens for one year. Tokens must be pre-approved for this contract.
     * @param amount Amount of tokens to lock.
     */
    function lockTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(lockExpiration == 0, "Tokens already locked");

        // Calculate lock expiration time (current time + 1 year)
        lockExpiration = block.timestamp + 365 days;

        // Transfer tokens from owner to this contract
        bool success = liquidityToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit TokensLocked(msg.sender, amount, lockExpiration);
    }

    /**
     * @dev Withdraws locked tokens after the lock period has expired.
     */
    function withdrawTokens() external onlyOwner {
        require(block.timestamp >= lockExpiration, "Lock period has not expired");
        require(lockExpiration != 0, "No tokens locked");

        // Reset lockExpiration to prevent re-locking
        uint256 balance = liquidityToken.balanceOf(address(this));
        lockExpiration = 0;

        // Transfer tokens back to the owner
        bool success = liquidityToken.transfer(owner, balance);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(owner, balance);
    }
}

/**
 * @dev Interface for ERC20 token contract.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
