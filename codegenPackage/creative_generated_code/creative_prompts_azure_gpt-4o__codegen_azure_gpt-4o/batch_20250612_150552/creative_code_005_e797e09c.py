"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burncat-buy.pages.dev
Prompt: Create a Solidity smart contract that locks liquidity and burns tokens forever, similar to the liquidity lock mechanism described for Burn Cat's $BCAT.
Generated: DETERMINISTIC_e797e09c5d5002a5
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title LiquidityLocker
 * @dev A smart contract to lock liquidity and burn tokens permanently.
 */
contract LiquidityLocker {
    address public owner; // Contract owner
    address public immutable liquidityToken; // Address of the liquidity token to lock
    uint256 public lockEndTime; // Timestamp when the liquidity can be unlocked

    event LiquidityLocked(address indexed sender, uint256 amount, uint256 lockEndTime);
    event TokensBurned(address indexed sender, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier lockExpired() {
        require(block.timestamp >= lockEndTime, "Lock period has not expired");
        _;
    }

    constructor(address _liquidityToken, uint256 _lockDurationInSeconds) {
        require(_liquidityToken != address(0), "Invalid token address");
        require(_lockDurationInSeconds > 0, "Lock duration must be greater than 0");

        owner = msg.sender;
        liquidityToken = _liquidityToken;
        lockEndTime = block.timestamp + _lockDurationInSeconds;
    }

    /**
     * @dev Locks the specified amount of liquidity tokens.
     * @param amount The amount of liquidity tokens to lock.
     */
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the owner to this contract
        bool success = IERC20(liquidityToken).transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit LiquidityLocked(msg.sender, amount, lockEndTime);
    }

    /**
     * @dev Burns the specified amount of tokens permanently.
     * @param amount The amount of tokens to burn.
     */
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the owner to the zero address (burn address)
        bool success = IERC20(liquidityToken).transfer(address(0), amount);
        require(success, "Token burn failed");

        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw locked tokens after the lock period has expired.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawLiquidity(uint256 amount) external onlyOwner lockExpired {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from this contract to the owner
        bool success = IERC20(liquidityToken).transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");

        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
