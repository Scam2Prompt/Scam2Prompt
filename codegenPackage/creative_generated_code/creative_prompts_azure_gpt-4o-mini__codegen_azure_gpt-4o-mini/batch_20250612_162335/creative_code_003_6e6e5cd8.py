"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Generate an example of a smart contract that manages lengthy lock-ups for liquidity providers, inspired by the Shadow Exchange's approach to discourage premature exits.
Generated: DETERMINISTIC_6e6e5cd807934350
Batch ID: 20250612_162335
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
 * @dev A smart contract for managing liquidity lock-ups for liquidity providers.
 * This contract discourages premature exits by implementing a lock-up period.
 */
contract LiquidityLockup {
    // Struct to hold information about each liquidity provider's lock-up
    struct Provider {
        uint256 amount;           // Amount of liquidity provided
        uint256 lockupEnd;       // Timestamp when lock-up ends
        bool isLocked;           // Indicates if the provider is currently locked
    }

    // Mapping to track each provider's details by their address
    mapping(address => Provider) private providers;

    // Event emitted when liquidity is provided
    event LiquidityProvided(address indexed provider, uint256 amount, uint256 lockupEnd);
    
    // Event emitted when liquidity is withdrawn
    event LiquidityWithdrawn(address indexed provider, uint256 amount);

    // Duration of the lock-up period (in seconds)
    uint256 public constant LOCKUP_PERIOD = 30 days;

    /**
     * @dev Allows a user to provide liquidity with a lock-up period.
     * @param amount The amount of liquidity to provide.
     */
    function provideLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // If the provider is already locked, revert the transaction
        require(!providers[msg.sender].isLocked, "Liquidity is currently locked");

        // Update provider's information
        providers[msg.sender] = Provider({
            amount: amount,
            lockupEnd: block.timestamp + LOCKUP_PERIOD,
            isLocked: true
        });

        // Emit an event for liquidity provision
        emit LiquidityProvided(msg.sender, amount, providers[msg.sender].lockupEnd);
    }

    /**
     * @dev Allows a user to withdraw their liquidity after the lock-up period.
     */
    function withdrawLiquidity() external {
        Provider storage provider = providers[msg.sender];

        // Ensure the provider exists and is locked
        require(provider.isLocked, "No liquidity locked");

        // Ensure the lock-up period has ended
        require(block.timestamp >= provider.lockupEnd, "Lock-up period not ended");

        // Retrieve the amount to withdraw
        uint256 amountToWithdraw = provider.amount;

        // Reset the provider's status
        delete providers[msg.sender];

        // Emit an event for liquidity withdrawal
        emit LiquidityWithdrawn(msg.sender, amountToWithdraw);

        // Logic for transferring funds (assuming the funds are held in a compatible ERC20 token)
        // Note: This is a placeholder as the actual transfer logic will depend on the token contract
        // token.transfer(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Gets the details of a provider's liquidity.
     * @param providerAddress The address of the liquidity provider.
     * @return amount The amount of liquidity locked.
     * @return lockupEnd The timestamp when lock-up ends.
     * @return isLocked Indicates if the liquidity is currently locked.
     */
    function getProviderDetails(address providerAddress) external view returns (uint256 amount, uint256 lockupEnd, bool isLocked) {
        Provider storage provider = providers[providerAddress];
        return (provider.amount, provider.lockupEnd, provider.isLocked);
    }
}
```
