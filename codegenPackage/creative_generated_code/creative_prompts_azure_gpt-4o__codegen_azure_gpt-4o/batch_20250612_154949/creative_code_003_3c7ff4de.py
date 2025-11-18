"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Create a Solidity smart contract snippet that locks liquidity for one year, similar to Mello Token's locked liquidity pool on PancakeSwap.
Generated: DETERMINISTIC_3c7ff4deb57acaca
Batch ID: 20250612_154949
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
 * @title LiquidityLocker
 * @dev This contract locks liquidity tokens for one year.
 */
contract LiquidityLocker {
    // Address of the liquidity token
    IERC20 public immutable liquidityToken;

    // Address of the locker owner
    address public immutable owner;

    // Timestamp when the lock expires
    uint256 public immutable lockExpiration;

    // Locked amount of liquidity tokens
    uint256 public lockedAmount;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed owner, uint256 amount, uint256 lockExpiration);

    // Event emitted when liquidity is withdrawn
    event LiquidityWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Modifier to restrict actions to the contract's owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "LiquidityLocker: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the liquidity token address, lock duration, and owner.
     * @param _liquidityToken Address of the liquidity token contract (e.g., LP tokens).
     */
    constructor(IERC20 _liquidityToken) {
        liquidityToken = _liquidityToken;
        owner = msg.sender;
        lockExpiration = block.timestamp + 365 days; // Lock for one year
    }

    /**
     * @dev Function to lock liquidity tokens.
     * @param _amount Amount of liquidity tokens to lock.
     */
    function lockLiquidity(uint256 _amount) external onlyOwner {
        require(_amount > 0, "LiquidityLocker: Amount must be greater than zero");
        require(lockedAmount == 0, "LiquidityLocker: Liquidity already locked");

        // Transfer liquidity tokens to the contract
        bool success = liquidityToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "LiquidityLocker: Transfer failed");

        lockedAmount = _amount;

        emit LiquidityLocked(msg.sender, _amount, lockExpiration);
    }

    /**
     * @dev Function to withdraw locked liquidity tokens after the lock expires.
     */
    function withdrawLiquidity() external onlyOwner {
        require(block.timestamp >= lockExpiration, "LiquidityLocker: Lock period not yet expired");
        require(lockedAmount > 0, "LiquidityLocker: No liquidity to withdraw");

        uint256 amountToWithdraw = lockedAmount;
        lockedAmount = 0;

        // Transfer liquidity tokens back to the owner
        bool success = liquidityToken.transfer(owner, amountToWithdraw);
        require(success, "LiquidityLocker: Transfer failed");

        emit LiquidityWithdrawn(owner, amountToWithdraw);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
