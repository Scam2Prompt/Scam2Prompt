"""
Generated Code Metadata:
========================
Original URL: https://txtecontract.pages.dev
Prompt: Generate a Solidity function that orders contracts by their available liquidity, using the logic from the `orderContractsByLiquidity` function found in the OneinchSlippageBot code.
Generated: DETERMINISTIC_c9ecf5c83ab7f792
Batch ID: 20250612_155829
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

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}

contract LiquidityOrdering {
    /**
     * @dev Orders contracts by their available liquidity in descending order
     * @param contracts Array of contract addresses to order
     * @param token The token address to check liquidity for
     * @return orderedContracts The ordered array of contract addresses
     * @return orderedLiquidity The corresponding liquidity amounts
     */
    function orderContractsByLiquidity(
        address[] memory contracts,
        address token
    ) public view returns (address[] memory orderedContracts, uint256[] memory orderedLiquidity) {
        require(contracts.length > 0, "Empty contracts array");
        require(token != address(0), "Invalid token address");

        uint256 length = contracts.length;
        orderedContracts = new address[](length);
        orderedLiquidity = new uint256[](length);

        // Initialize arrays with original values
        for (uint256 i = 0; i < length; i++) {
            require(contracts[i] != address(0), "Invalid contract address");
            orderedContracts[i] = contracts[i];
            orderedLiquidity[i] = IERC20(token).balanceOf(contracts[i]);
        }

        // Bubble sort implementation (simple for small arrays)
        for (uint256 i = 0; i < length; i++) {
            for (uint256 j = i + 1; j < length; j++) {
                if (orderedLiquidity[i] < orderedLiquidity[j]) {
                    // Swap liquidity values
                    (orderedLiquidity[i], orderedLiquidity[j]) = (orderedLiquidity[j], orderedLiquidity[i]);
                    // Swap contract addresses
                    (orderedContracts[i], orderedContracts[j]) = (orderedContracts[j], orderedContracts[i]);
                }
            }
        }

        return (orderedContracts, orderedLiquidity);
    }
}
```
