"""
Generated Code Metadata:
========================
Original URL: https://copycoden.pages.dev
Prompt: "Generate a Solidity code snippet for ordering contracts by their available liquidity, as described in the `orderContractsByLiquidity` function of the 1inch Slippage bot contract."
Generated: DETERMINISTIC_6839b488da4fc474
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

interface IContractLiquidity {
    function getAvailableLiquidity() external view returns (uint256);
}

contract LiquidityOrderer {
    /**
     * @dev Orders contracts by their available liquidity in descending order
     * @param contracts Array of contract addresses to order
     * @return orderedContracts Ordered array of contracts
     */
    function orderContractsByLiquidity(address[] memory contracts) 
        public 
        view 
        returns (address[] memory orderedContracts) 
    {
        // Create a copy of the input array to avoid modifying the original
        orderedContracts = new address[](contracts.length);
        for (uint256 i = 0; i < contracts.length; i++) {
            orderedContracts[i] = contracts[i];
        }

        // Bubble sort implementation for simplicity (optimize for production)
        for (uint256 i = 0; i < orderedContracts.length; i++) {
            for (uint256 j = i + 1; j < orderedContracts.length; j++) {
                uint256 liquidityA = IContractLiquidity(orderedContracts[i]).getAvailableLiquidity();
                uint256 liquidityB = IContractLiquidity(orderedContracts[j]).getAvailableLiquidity();
                
                if (liquidityA < liquidityB) {
                    // Swap positions
                    address temp = orderedContracts[i];
                    orderedContracts[i] = orderedContracts[j];
                    orderedContracts[j] = temp;
                }
            }
        }

        return orderedContracts;
    }
}
```
