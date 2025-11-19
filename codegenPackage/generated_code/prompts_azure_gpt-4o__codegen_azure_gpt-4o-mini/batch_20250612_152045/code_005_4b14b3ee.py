"""
Generated Code Metadata:
========================
Original URL: https://quickwasp.godaddysites.com
Prompt: Develop a Solidity implementation of a fee mechanism for a DEX, where 0.30% of each transaction is added to the reserves and later distributed to liquidity providers when they withdraw their shares.
Generated: DETERMINISTIC_4b14b3ee039fbe97
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DEXFeeMechanism
 * @dev A contract to implement a fee mechanism for a decentralized exchange (DEX).
 *      0.30% of each transaction is added to reserves and distributed to liquidity providers.
 */
contract DEXFeeMechanism is Ownable {
    // State variables
    IERC20 public token; // The token being traded
    uint256 public totalReserves; // Total reserves accumulated from fees
    uint256 public totalShares; // Total shares of liquidity providers
    mapping(address => uint256) public shares; // Shares of each liquidity provider

    // Events
    event FeeCollected(uint256 feeAmount);
    event SharesWithdrawn(address indexed provider, uint256 amount);

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to execute a trade and collect fees.
     * @param amount The amount of tokens being traded.
     */
    function trade(uint256 amount) external {
        require(amount > 0, "Trade amount must be greater than zero");

        // Calculate the fee (0.30%)
        uint256 fee = (amount * 30) / 10000; // 0.30% fee
        uint256 netAmount = amount - fee;

        // Update reserves
        totalReserves += fee;
        emit FeeCollected(fee);

        // Transfer tokens (assuming the contract has been approved to spend tokens)
        token.transferFrom(msg.sender, address(this), netAmount);
    }

    /**
     * @dev Function for liquidity providers to withdraw their shares.
     */
    function withdrawShares() external {
        uint256 userShares = shares[msg.sender];
        require(userShares > 0, "No shares to withdraw");

        // Calculate the amount of reserves to distribute
        uint256 withdrawAmount = (totalReserves * userShares) / totalShares;

        // Reset user's shares and total reserves
        shares[msg.sender] = 0;
        totalReserves -= withdrawAmount;

        // Transfer the calculated amount to the user
        token.transfer(msg.sender, withdrawAmount);
        emit SharesWithdrawn(msg.sender, withdrawAmount);
    }

    /**
     * @dev Function for liquidity providers to deposit liquidity and receive shares.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Update shares
        shares[msg.sender] += amount;
        totalShares += amount;
    }

    /**
     * @dev Function to get the total reserves.
     * @return The total reserves accumulated from fees.
     */
    function getTotalReserves() external view returns (uint256) {
        return totalReserves;
    }

    /**
     * @dev Function to get the shares of a specific provider.
     * @param provider The address of the liquidity provider.
     * @return The number of shares held by the provider.
     */
    function getShares(address provider) external view returns (uint256) {
        return shares[provider];
    }
}
```
