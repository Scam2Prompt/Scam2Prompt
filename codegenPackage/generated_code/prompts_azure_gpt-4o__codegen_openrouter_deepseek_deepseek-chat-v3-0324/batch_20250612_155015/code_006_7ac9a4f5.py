"""
Generated Code Metadata:
========================
Original URL: https://pythnew.com
Prompt: Create a smart contract function that uses Pyth Network's price feed to calculate the collateralization ratio for a lending platform.
Generated: DETERMINISTIC_7ac9a4f5c726488b
Batch ID: 20250612_155015
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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract CollateralizationCalculator {
    IPyth public pyth;
    address public priceFeedId;
    uint256 public constant PRICE_FEED_DECIMALS = 18;

    constructor(address _pyth, address _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }

    /**
     * @notice Calculates the collateralization ratio for a loan
     * @param collateralAmount Amount of collateral tokens (in smallest unit)
     * @param collateralDecimals Decimals of collateral token
     * @param loanAmount Amount of loan tokens (in smallest unit)
     * @param loanDecimals Decimals of loan token
     * @param priceUpdateData Pyth price update data
     * @return collateralizationRatio The calculated ratio (scaled by 1e18)
     */
    function calculateCollateralizationRatio(
        uint256 collateralAmount,
        uint8 collateralDecimals,
        uint256 loanAmount,
        uint8 loanDecimals,
        bytes[] calldata priceUpdateData
    ) external payable returns (uint256) {
        require(collateralAmount > 0, "Collateral amount must be positive");
        require(loanAmount > 0, "Loan amount must be positive");

        // Update price feed (this will charge a fee which is why the function is payable)
        uint256 fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceFeedId);

        // Check if price is valid
        require(price.price > 0, "Invalid price");
        require(price.expo <= 0, "Positive exponent not supported");

        // Scale price to 18 decimals
        uint256 scaledPrice = uint256(uint64(price.price)) * 
            10 ** (PRICE_FEED_DECIMALS + uint256(int256(-price.expo)));

        // Calculate collateral value in loan terms
        uint256 collateralValue = (collateralAmount * scaledPrice) / 
            (10 ** uint256(collateralDecimals));

        // Scale loan amount to 18 decimals
        uint256 scaledLoanAmount = loanAmount * 
            (10 ** (PRICE_FEED_DECIMALS - uint256(loanDecimals)));

        // Calculate and return collateralization ratio
        return (collateralValue * 1e18) / scaledLoanAmount;
    }

    // Allow contract to receive refunds for unused update fees
    receive() external payable {}
}
```
