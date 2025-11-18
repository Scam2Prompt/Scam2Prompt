"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Create a smart contract to enforce lengthy lock-up periods for liquidity providers, incorporating incentives for long-term ecosystem participation.
Generated: DETERMINISTIC_79f121062213b4ec
Batch ID: 20250612_155028
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
 * @title LiquidityLockup
 * @dev A smart contract to enforce lock-up periods for liquidity providers
 * and incentivize long-term participation in the ecosystem.
 */
contract LiquidityLockup {
    // Struct to represent each liquidity provider's information
    struct LiquidityProvider {
        uint256 amount;         // Amount of liquidity provided
        uint256 unlockTime;     // Timestamp when the liquidity can be withdrawn
        bool isParticipating;    // Status of the participation
    }

    // Mapping of liquidity provider addresses to their information
    mapping(address => LiquidityProvider) public liquidityProviders;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed provider, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed provider, uint256 amount);

    // Duration of the lock-up period in seconds (e.g., 30 days)
    uint256 public constant LOCKUP_PERIOD = 30 days;

    /**
     * @dev Locks liquidity for a provider
     * @param amount Amount of liquidity to lock
     */
    function lockLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(liquidityProviders[msg.sender].amount == 0, "Liquidity already locked");

        // Transfer the liquidity tokens to the contract (assumed to be implemented)
        // ERC20(token).transferFrom(msg.sender, address(this), amount);

        // Set the liquidity provider's information
        liquidityProviders[msg.sender] = LiquidityProvider({
            amount: amount,
            unlockTime: block.timestamp + LOCKUP_PERIOD,
            isParticipating: true
        });

        emit LiquidityLocked(msg.sender, amount, liquidityProviders[msg.sender].unlockTime);
    }

    /**
     * @dev Unlocks liquidity for a provider after the lock-up period
     */
    function unlockLiquidity() external {
        LiquidityProvider storage provider = liquidityProviders[msg.sender];
        
        require(provider.isParticipating, "No liquidity locked");
        require(block.timestamp >= provider.unlockTime, "Liquidity is still locked");

        uint256 amountToUnlock = provider.amount;

        // Reset the liquidity provider's information
        provider.amount = 0;
        provider.isParticipating = false;

        // Transfer the liquidity tokens back to the provider (assumed to be implemented)
        // ERC20(token).transfer(msg.sender, amountToUnlock);

        emit LiquidityUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Check the amount of liquidity locked by a provider
     * @param provider Address of the liquidity provider
     * @return The amount of liquidity locked
     */
    function getLockedLiquidity(address provider) external view returns (uint256) {
        return liquidityProviders[provider].amount;
    }

    /**
     * @dev Check if the liquidity can be unlocked for a provider
     * @param provider Address of the liquidity provider
     * @return True if liquidity can be unlocked, false otherwise
     */
    function canUnlockLiquidity(address provider) external view returns (bool) {
        LiquidityProvider storage lp = liquidityProviders[provider];
        return lp.isParticipating && block.timestamp >= lp.unlockTime;
    }
}
```
