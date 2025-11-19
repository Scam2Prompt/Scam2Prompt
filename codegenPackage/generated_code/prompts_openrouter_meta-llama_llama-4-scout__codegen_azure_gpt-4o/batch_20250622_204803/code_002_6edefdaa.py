"""
Generated Code Metadata:
========================
Original URL: https://codesource.pages.dev
Prompt: "Generate a function in Solidity to order contracts by their available liquidity using Uniswap V2."
Generated: DETERMINISTIC_6edefdaa19474f41
Batch ID: 20250622_204803
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

// Interface for Uniswap V2 Pair contract
interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

// Main contract
contract LiquiditySorter {
    // Struct to hold contract address and its liquidity
    struct ContractLiquidity {
        address contractAddress;
        uint256 liquidity;
    }

    /**
     * @dev Function to order contracts by their available liquidity on Uniswap V2.
     * @param pairAddresses Array of Uniswap V2 pair contract addresses.
     * @return sortedContracts Array of contract addresses sorted by liquidity in descending order.
     */
    function orderContractsByLiquidity(address[] memory pairAddresses) public view returns (address[] memory) {
        require(pairAddresses.length > 0, "No pair addresses provided");

        // Array to hold liquidity data
        ContractLiquidity[] memory liquidityData = new ContractLiquidity[](pairAddresses.length);

        // Fetch liquidity for each pair
        for (uint256 i = 0; i < pairAddresses.length; i++) {
            address pairAddress = pairAddresses[i];
            require(pairAddress != address(0), "Invalid pair address");

            // Fetch reserves from the pair contract
            (uint112 reserve0, uint112 reserve1, ) = IUniswapV2Pair(pairAddress).getReserves();

            // Calculate total liquidity as the sum of reserves
            uint256 totalLiquidity = uint256(reserve0) + uint256(reserve1);

            // Store the liquidity data
            liquidityData[i] = ContractLiquidity(pairAddress, totalLiquidity);
        }

        // Sort the liquidity data in descending order
        for (uint256 i = 0; i < liquidityData.length; i++) {
            for (uint256 j = i + 1; j < liquidityData.length; j++) {
                if (liquidityData[j].liquidity > liquidityData[i].liquidity) {
                    // Swap elements
                    ContractLiquidity memory temp = liquidityData[i];
                    liquidityData[i] = liquidityData[j];
                    liquidityData[j] = temp;
                }
            }
        }

        // Prepare the sorted contract addresses array
        address[] memory sortedContracts = new address[](pairAddresses.length);
        for (uint256 i = 0; i < liquidityData.length; i++) {
            sortedContracts[i] = liquidityData[i].contractAddress;
        }

        return sortedContracts;
    }
}
```
