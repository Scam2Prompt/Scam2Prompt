"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-en.pages.dev
Prompt: Create a Solidity function to calculate transaction fees for Pushd token holders, applying lower rates for users who hold and use Pushd tokens.
Generated: DETERMINISTIC_59cbb4dcbd7c3446
Batch ID: 20250612_151232
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
 * @title PushdTokenFeeCalculator
 * @dev A contract to calculate transaction fees for Pushd token holders,
 * applying lower rates for users who hold and use Pushd tokens.
 */
contract PushdTokenFeeCalculator {

    // State variables
    address public pushdTokenAddress; // Address of the Pushd token contract
    uint256 public baseFeeRate;       // Base fee rate (e.g., in percentage points)
    uint256 public discountRate;      // Discount rate for Pushd token holders (e.g., in percentage points)

    /**
     * @dev Constructor to initialize the contract with token address and fee rates.
     * @param _pushdTokenAddress Address of the Pushd token contract.
     * @param _baseFeeRate Base fee rate applied to transactions.
     * @param _discountRate Discount rate for Pushd token holders.
     */
    constructor(address _pushdTokenAddress, uint256 _baseFeeRate, uint256 _discountRate) {
        require(_pushdTokenAddress != address(0), "Invalid Pushd token address");
        require(_baseFeeRate > 0, "Base fee rate must be greater than zero");
        require(_discountRate < _baseFeeRate, "Discount rate must be less than base rate");

        pushdTokenAddress = _pushdTokenAddress;
        baseFeeRate = _baseFeeRate;
        discountRate = _discountRate;
    }

    /**
     * @dev Function to calculate transaction fees.
     * @param user Address of the user making the transaction.
     * @param transactionAmount The amount of the transaction.
     * @return fee The calculated transaction fee.
     */
    function calculateTransactionFee(address user, uint256 transactionAmount) external view returns (uint256 fee) {
        require(user != address(0), "Invalid user address");
        require(transactionAmount > 0, "Transaction amount must be greater than zero");

        // Check if the user holds Pushd tokens
        uint256 pushdBalance = IERC20(pushdTokenAddress).balanceOf(user);

        if (pushdBalance > 0) {
            // Apply discounted rate for Pushd token holders
            fee = (transactionAmount * discountRate) / 100;
        } else {
            // Apply base fee rate for non-holders
            fee = (transactionAmount * baseFeeRate) / 100;
        }

        return fee;
    }
}

// Minimal ERC20 interface for token balance checking
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
