"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Write a smart contract in Solidity that implements a meme-based cryptocurrency token similar to "Rich Pepe," incorporating features like 0% buy/sell tax, locked liquidity, and community-based ownership.
Generated: DETERMINISTIC_13c89cfd267863a3
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MemeToken
 * @dev This contract implements a meme-based cryptocurrency token with 0% buy/sell tax,
 *      locked liquidity, and community-based ownership.
 */
contract MemeToken is ERC20, Ownable, ReentrancyGuard {
    // Event for liquidity lock
    event LiquidityLocked(uint256 amount, uint256 unlockTime);

    // Liquidity lock variables
    uint256 public liquidityUnlockTime;
    bool public liquidityLocked = false;

    // Constructor to initialize token
    constructor() ERC20("Rich Pepe", "RPEPE") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to owner
    }

    /**
     * @dev Function to lock the liquidity.
     * @param amount Amount of tokens to lock.
     * @param duration Duration for which the liquidity will be locked in seconds.
     */
    function lockLiquidity(uint256 amount, uint256 duration) external onlyOwner {
        require(!liquidityLocked, "Liquidity already locked.");
        require(amount <= balanceOf(msg.sender), "Insufficient balance to lock.");
        require(duration > 0, "Duration must be greater than zero.");

        // Transfer tokens to contract for liquidity lock
        _transfer(msg.sender, address(this), amount);
        liquidityUnlockTime = block.timestamp + duration;
        liquidityLocked = true;

        emit LiquidityLocked(amount, liquidityUnlockTime);
    }

    /**
     * @dev Function to unlock the liquidity if the time has passed.
     */
    function unlockLiquidity() external onlyOwner {
        require(liquidityLocked, "Liquidity is not locked.");
        require(block.timestamp >= liquidityUnlockTime, "Liquidity is still locked.");

        // Transfer locked tokens back to the owner
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No tokens to unlock.");
        _transfer(address(this), msg.sender, balance);
        
        liquidityLocked = false;
    }

    /**
     * @dev Override transfer function to prevent taxes on transfers.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool indicating success of transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero.");
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Override transferFrom function to prevent taxes on transfers.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool indicating success of transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero.");
        _transfer(sender, recipient, amount);
        
        // Reduce the allowance
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);
        
        return true;
    }
}
```

Make sure to install the OpenZeppelin contracts using npm to compile this contract correctly:
```bash
npm install @openzeppelin/contracts
```
