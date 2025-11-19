"""
Generated Code Metadata:
========================
Original URL: https://ethgas.web.app
Prompt: Explain the process of selecting maximum gas fees using the ETH Gas Refund Dapp.
Generated: DETERMINISTIC_4f2db9b3d3380404
Batch ID: 20250612_155436
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

/**
 * @title GasRefundDapp
 * @dev A contract that helps users select optimal gas fees for transactions
 * with potential gas refunds on the Ethereum network.
 */
contract GasRefundDapp {
    // Struct to store gas price data
    struct GasPriceData {
        uint256 baseFee;       // Current base fee
        uint256 priorityFee;   // Current priority fee
        uint256 maxFee;        // Current max fee
        uint256 timestamp;     // When this data was recorded
    }

    // Array to store historical gas price data
    GasPriceData[] public gasPriceHistory;

    // Event emitted when new gas price data is recorded
    event GasPriceRecorded(
        uint256 baseFee,
        uint256 priorityFee,
        uint256 maxFee,
        uint256 timestamp
    );

    /**
     * @dev Records current gas price data
     * @param _baseFee The current base fee
     * @param _priorityFee The current priority fee
     * @param _maxFee The current max fee
     */
    function recordGasPrice(
        uint256 _baseFee,
        uint256 _priorityFee,
        uint256 _maxFee
    ) external {
        require(_baseFee > 0, "Base fee must be greater than 0");
        require(_priorityFee > 0, "Priority fee must be greater than 0");
        require(_maxFee > _baseFee + _priorityFee, "Max fee must cover base + priority");

        gasPriceHistory.push(
            GasPriceData({
                baseFee: _baseFee,
                priorityFee: _priorityFee,
                maxFee: _maxFee,
                timestamp: block.timestamp
            })
        );

        emit GasPriceRecorded(_baseFee, _priorityFee, _maxFee, block.timestamp);
    }

    /**
     * @dev Calculates the optimal gas price based on historical data
     * @param _percentile The percentile to use for calculation (e.g., 50 for median)
     * @return optimalBaseFee The calculated optimal base fee
     * @return optimalPriorityFee The calculated optimal priority fee
     * @return optimalMaxFee The calculated optimal max fee
     */
    function calculateOptimalGasPrice(uint256 _percentile)
        external
        view
        returns (
            uint256 optimalBaseFee,
            uint256 optimalPriorityFee,
            uint256 optimalMaxFee
        )
    {
        require(_percentile > 0 && _percentile <= 100, "Percentile must be between 1-100");
        require(gasPriceHistory.length > 0, "No gas price data available");

        uint256[] memory baseFees = new uint256[](gasPriceHistory.length);
        uint256[] memory priorityFees = new uint256[](gasPriceHistory.length);
        uint256[] memory maxFees = new uint256[](gasPriceHistory.length);

        for (uint256 i = 0; i < gasPriceHistory.length; i++) {
            baseFees[i] = gasPriceHistory[i].baseFee;
            priorityFees[i] = gasPriceHistory[i].priorityFee;
            maxFees[i] = gasPriceHistory[i].maxFee;
        }

        optimalBaseFee = _calculatePercentile(baseFees, _percentile);
        optimalPriorityFee = _calculatePercentile(priorityFees, _percentile);
        optimalMaxFee = _calculatePercentile(maxFees, _percentile);

        return (optimalBaseFee, optimalPriorityFee, optimalMaxFee);
    }

    /**
     * @dev Internal function to calculate percentile of an array
     * @param _array The input array
     * @param _percentile The percentile to calculate
     * @return The value at the given percentile
     */
    function _calculatePercentile(uint256[] memory _array, uint256 _percentile)
        internal
        pure
        returns (uint256)
    {
        require(_array.length > 0, "Array cannot be empty");

        // Sort the array
        _sortArray(_array);

        // Calculate index for the percentile
        uint256 index = (_array.length * _percentile) / 100;
        if (index >= _array.length) {
            index = _array.length - 1;
        }

        return _array[index];
    }

    /**
     * @dev Internal function to sort an array using bubble sort
     * @param _array The array to sort
     */
    function _sortArray(uint256[] memory _array) internal pure {
        for (uint256 i = 0; i < _array.length; i++) {
            for (uint256 j = i + 1; j < _array.length; j++) {
                if (_array[i] > _array[j]) {
                    (_array[i], _array[j]) = (_array[j], _array[i]);
                }
            }
        }
    }

    /**
     * @dev Gets the latest recorded gas price data
     * @return The latest GasPriceData struct
     */
    function getLatestGasPrice() external view returns (GasPriceData memory) {
        require(gasPriceHistory.length > 0, "No gas price data available");
        return gasPriceHistory[gasPriceHistory.length - 1];
    }

    /**
     * @dev Gets gas price data count
     * @return The number of recorded gas price data points
     */
    function getGasPriceDataCount() external view returns (uint256) {
        return gasPriceHistory.length;
    }
}
```
