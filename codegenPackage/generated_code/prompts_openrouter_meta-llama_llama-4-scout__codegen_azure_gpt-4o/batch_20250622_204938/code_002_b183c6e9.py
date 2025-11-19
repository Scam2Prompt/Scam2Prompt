"""
Generated Code Metadata:
========================
Original URL: https://cdnsource.pages.dev
Prompt: "Generate Solidity code for a bot that orders Uniswap contracts by their available liquidity, inspired by the `orderContractsByLiquidity` function in the provided 1inch Slippage bot contract."
Generated: DETERMINISTIC_b183c6e978a2f853
Batch ID: 20250622_204938
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

// Importing interfaces for Uniswap V2
interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract LiquidityOrderingBot {
    // Struct to store contract address and its liquidity
    struct ContractLiquidity {
        address contractAddress;
        uint256 liquidity;
    }

    // Function to order Uniswap contracts by their available liquidity
    function orderContractsByLiquidity(address[] calldata uniswapContracts) external view returns (ContractLiquidity[] memory) {
        require(uniswapContracts.length > 0, "No contracts provided");

        // Array to store liquidity data
        ContractLiquidity[] memory liquidityData = new ContractLiquidity[](uniswapContracts.length);

        for (uint256 i = 0; i < uniswapContracts.length; i++) {
            address contractAddress = uniswapContracts[i];
            IUniswapV2Pair pair = IUniswapV2Pair(contractAddress);

            // Fetch reserves from the contract
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

            // Calculate total liquidity as the sum of reserves
            uint256 totalLiquidity = uint256(reserve0) + uint256(reserve1);

            // Store contract address and liquidity
            liquidityData[i] = ContractLiquidity({
                contractAddress: contractAddress,
                liquidity: totalLiquidity
            });
        }

        // Sort the liquidity data array in descending order of liquidity
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

        return liquidityData;
    }
}
```
