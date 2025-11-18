"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quickwasp.godaddysites.com
Prompt: Develop a Solidity implementation of a fee mechanism for a DEX, where 0.30% of each transaction is added to the reserves and later distributed to liquidity providers when they withdraw their shares.
Generated: DETERMINISTIC_4b14b3ee039fbe97
Batch ID: 20250612_152045
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
 * @title DEX Fee Mechanism
 * @dev Implements a fee mechanism where 0.30% of each transaction is collected as fees
 * and added to reserves. Fees are distributed to liquidity providers upon withdrawal.
 */
contract DexFeeMechanism {
    // Reserve balance for collected fees
    uint256 public feeReserves;

    // Mapping to track liquidity provider shares
    mapping(address => uint256) public liquidityProviderShares;

    // Total shares issued to liquidity providers
    uint256 public totalShares;

    // Fee percentage (0.30% = 0.003 in Solidity math)
    uint256 public constant FEE_PERCENTAGE = 30; // Represented as 1/10000 (30/10000)
    uint256 public constant FEE_DENOMINATOR = 10000;

    event FeesCollected(address indexed user, uint256 amount);
    event LiquidityWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Executes a trade and collects fees.
     * @param trader The address of the trader executing the trade.
     * @param amount The transaction amount.
     */
    function executeTrade(address trader, uint256 amount) external {
        require(amount > 0, "Trade amount must be greater than zero");

        // Calculate fee based on the transaction amount
        uint256 fee = (amount * FEE_PERCENTAGE) / FEE_DENOMINATOR;

        // Add the collected fee to the reserves
        feeReserves += fee;

        // Emit event for fee collection
        emit FeesCollected(trader, fee);
    }

    /**
     * @dev Adds liquidity to the DEX.
     * @param provider The address of the liquidity provider.
     * @param shares The number of shares to add for the provider.
     */
    function addLiquidity(address provider, uint256 shares) external {
        require(shares > 0, "Shares must be greater than zero");

        // Update the provider's shares
        liquidityProviderShares[provider] += shares;

        // Update the total shares
        totalShares += shares;
    }

    /**
     * @dev Withdraws liquidity and distributes a proportional share of the fee reserves.
     * @param provider The address of the liquidity provider.
     */
    function withdrawLiquidity(address provider) external {
        uint256 providerShares = liquidityProviderShares[provider];
        require(providerShares > 0, "Provider has no shares to withdraw");

        // Calculate the provider's proportional share of the fee reserves
        uint256 shareOfReserves = (feeReserves * providerShares) / totalShares;

        // Decrease reserves and total shares
        feeReserves -= shareOfReserves;
        totalShares -= providerShares;

        // Reset the provider's shares
        liquidityProviderShares[provider] = 0;

        // Transfer the proportional share of the reserves to the provider
        (bool success, ) = provider.call{value: shareOfReserves}("");
        require(success, "Failed to transfer fees to provider");

        // Emit event for liquidity withdrawal
        emit LiquidityWithdrawn(provider, shareOfReserves);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
