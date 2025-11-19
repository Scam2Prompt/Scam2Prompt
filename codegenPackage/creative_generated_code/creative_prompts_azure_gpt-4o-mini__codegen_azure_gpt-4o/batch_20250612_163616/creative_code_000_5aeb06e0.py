"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://furrevertokensale.pages.dev
Prompt: How can I create a smart contract for the Furrever Token on the Binance Smart Chain, including details about liquidity locking for 2 years?
Generated: DETERMINISTIC_5aeb06e088c61c8a
Batch ID: 20250612_163616
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
 * @title Furrever Token Smart Contract
 * @dev ERC20 token implementation with liquidity locking for 2 years
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FurreverToken is ERC20, Ownable {
    // Liquidity lock details
    address public liquidityPool;
    uint256 public lockEndTime;

    // Event to notify liquidity lock
    event LiquidityLocked(address indexed pool, uint256 lockEndTime);

    /**
     * @dev Constructor to initialize the token.
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial supply of the token (in smallest unit)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Function to lock liquidity for 2 years.
     * @param pool Address of the liquidity pool where tokens will be locked
     * @param amount Amount of tokens to lock
     */
    function lockLiquidity(address pool, uint256 amount) external onlyOwner {
        require(liquidityPool == address(0), "Liquidity pool is already locked");
        require(pool != address(0), "Invalid pool address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the liquidity pool
        _transfer(msg.sender, pool, amount);

        // Set liquidity pool and lock duration
        liquidityPool = pool;
        lockEndTime = block.timestamp + (2 * 365 days); // 2 years

        emit LiquidityLocked(pool, lockEndTime);
    }

    /**
     * @dev Function to withdraw liquidity when lock period ends.
     * This can only be called by the contract owner.
     */
    function withdrawLiquidity() external onlyOwner {
        require(liquidityPool != address(0), "Liquidity pool is not set");
        require(block.timestamp >= lockEndTime, "Liquidity is still locked");

        // Reset liquidity pool and lock duration
        liquidityPool = address(0);
        lockEndTime = 0;
    }

    /**
     * @dev Modifier to check if liquidity is locked.
     */
    modifier liquidityUnlocked() {
        require(block.timestamp >= lockEndTime, "Liquidity is locked");
        _;
    }
}
```
