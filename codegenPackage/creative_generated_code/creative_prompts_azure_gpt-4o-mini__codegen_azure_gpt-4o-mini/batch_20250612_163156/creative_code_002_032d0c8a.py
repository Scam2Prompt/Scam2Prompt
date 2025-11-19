"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Generate a function in Solidity that orders contracts by their available liquidity, similar to the functionality provided in the OneinchSlippageBot contract.
Generated: DETERMINISTIC_032d0c8a7155df50
Batch ID: 20250612_163156
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

interface IToken {
    function balanceOf(address account) external view returns (uint256);
}

interface IExchange {
    function getLiquidity(address token) external view returns (uint256);
}

contract LiquidityOrder {

    // Struct to hold exchange information and its liquidity
    struct ExchangeInfo {
        address exchangeAddress; // Exchange contract address
        uint256 liquidity;       // Available liquidity for the token
    }

    // Function to retrieve and order exchanges by their liquidity
    function orderExchangesByLiquidity(address token, address[] calldata exchanges) 
        external 
        view 
        returns (ExchangeInfo[] memory) 
    {
        uint256 exchangeCount = exchanges.length;
        ExchangeInfo[] memory exchangeInfos = new ExchangeInfo[](exchangeCount);

        // Fetch and store liquidity information
        for (uint256 i = 0; i < exchangeCount; i++) {
            address exchange = exchanges[i];
            uint256 liquidity;

            // Try to get liquidity, handling any potential issues
            try IExchange(exchange).getLiquidity(token) returns (uint256 _liquidity) {
                liquidity = _liquidity;
            } catch {
                // If the call fails, set liquidity to zero and log an error (could be enhanced)
                liquidity = 0;
            }

            exchangeInfos[i] = ExchangeInfo({
                exchangeAddress: exchange,
                liquidity: liquidity
            });
        }

        // Sort the exchanges by liquidity in descending order
        quickSort(exchangeInfos, 0, exchangeCount - 1);

        return exchangeInfos;
    }

    // QuickSort to sort exchanges by liquidity
    function quickSort(ExchangeInfo[] memory arr, uint256 low, uint256 high) internal pure {
        if (low < high) {
            uint256 pi = partition(arr, low, high);
            if (pi > 0) quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    // Partition function for QuickSort
    function partition(ExchangeInfo[] memory arr, uint256 low, uint256 high) 
        internal 
        pure 
        returns (uint256) 
    {
        uint256 pivot = arr[high].liquidity; // pivot
        uint256 i = (low - 1); // Index of smaller element
        for (uint256 j = low; j < high; j++) {
            // If current element is greater than or equal to pivot
            if (arr[j].liquidity >= pivot) {
                i++;
                (arr[i], arr[j]) = (arr[j], arr[i]); // swap
            }
        }
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1]); // swap pivot
        return i + 1;
    }
}
```
