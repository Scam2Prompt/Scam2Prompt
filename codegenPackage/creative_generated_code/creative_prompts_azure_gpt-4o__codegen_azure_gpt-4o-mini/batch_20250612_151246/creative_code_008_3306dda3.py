"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Generate a Solidity function to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's anti-rug pull measures.
Generated: DETERMINISTIC_3306dda3b478ee44
Batch ID: 20250612_151246
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityLocker is Ownable {
    // Struct to hold lock details
    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        bool isLocked;
    }

    // Mappings for liquidity and team token locks
    mapping(address => Lock) public liquidityLocks;
    mapping(address => Lock) public teamTokenLocks;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount, uint256 unlockTime);
    
    // Event emitted when team tokens are locked
    event TeamTokensLocked(address indexed locker, uint256 amount, uint256 unlockTime);

    /**
     * @dev Locks liquidity for 20 years (6300 days) and team tokens for 700 days.
     * @param tokenAddress The address of the token to lock.
     * @param amount The amount of tokens to lock.
     */
    function lockLiquidity(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(liquidityLocks[tokenAddress].isLocked == false, "Liquidity already locked");

        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set lock details for 20 years
        liquidityLocks[tokenAddress] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 20 * 365 * 24 * 60 * 60,  // 20 years in seconds
            isLocked: true
        });

        emit LiquidityLocked(msg.sender, amount, liquidityLocks[tokenAddress].unlockTime);
    }

    /**
     * @dev Locks team tokens for 700 days.
     * @param tokenAddress The address of the team token to lock.
     * @param amount The amount of team tokens to lock.
     */
    function lockTeamTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(teamTokenLocks[tokenAddress].isLocked == false, "Team tokens already locked");

        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set lock details for 700 days
        teamTokenLocks[tokenAddress] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 700 * 24 * 60 * 60,  // 700 days in seconds
            isLocked: true
        });

        emit TeamTokensLocked(msg.sender, amount, teamTokenLocks[tokenAddress].unlockTime);
    }

    /**
     * @dev Unlocks liquidity after the lock period has expired.
     * @param tokenAddress The address of the locked liquidity token.
     */
    function unlockLiquidity(address tokenAddress) external onlyOwner {
        require(block.timestamp >= liquidityLocks[tokenAddress].unlockTime, "Liquidity is still locked");
        require(liquidityLocks[tokenAddress].isLocked == true, "Liquidity is not locked");

        uint256 amount = liquidityLocks[tokenAddress].amount;
        liquidityLocks[tokenAddress].isLocked = false;

        IERC20 token = IERC20(tokenAddress);
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Unlocks team tokens after the lock period has expired.
     * @param tokenAddress The address of the locked team token.
     */
    function unlockTeamTokens(address tokenAddress) external onlyOwner {
        require(block.timestamp >= teamTokenLocks[tokenAddress].unlockTime, "Team tokens are still locked");
        require(teamTokenLocks[tokenAddress].isLocked == true, "Team tokens are not locked");

        uint256 amount = teamTokenLocks[tokenAddress].amount;
        teamTokenLocks[tokenAddress].isLocked = false;

        IERC20 token = IERC20(tokenAddress);
        token.transfer(msg.sender, amount);
    }
}
```
