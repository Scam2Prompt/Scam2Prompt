"""
Generated Code Metadata:
========================
Original URL: https://updatedcode.pages.dev
Prompt: Implement a function in Solidity that orders Uniswap contracts by their available liquidity, as described in the "orderContractsByLiquidity" function on the webpage.
Generated: DETERMINISTIC_7fe5c2181e476561
Batch ID: 20250612_150902
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

contract UniswapLiquiditySorter {
    // Struct to hold Uniswap contract information
    struct UniswapContract {
        address contractAddress;
        uint256 liquidity;
    }

    // Function to get the liquidity of a Uniswap pair
    function getLiquidity(address pairAddress) internal view returns (uint256) {
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);
        (uint256 reserve0, uint256 reserve1, ) = pair.getReserves();
        return reserve0 * reserve1;
    }

    // Function to order Uniswap contracts by their available liquidity
    function orderContractsByLiquidity(address[] memory contractAddresses, address routerAddress) public view returns (UniswapContract[] memory) {
        // Initialize array to hold Uniswap contracts with their liquidity
        UniswapContract[] memory contracts = new UniswapContract[](contractAddresses.length);

        // Get the router contract
        IUniswapV2Router02 router = IUniswapV2Router02(routerAddress);

        // Iterate over each contract address
        for (uint256 i = 0; i < contractAddresses.length; i++) {
            // Get the pair address for the contract
            address pairAddress = router.pairFor(contractAddresses[i], address(0)); // Assuming ETH as the second token

            try {
                // Get the liquidity of the pair
                uint256 liquidity = getLiquidity(pairAddress);

                // Store the contract information
                contracts[i] = UniswapContract(contractAddresses[i], liquidity);
            } catch Error(string memory error) {
                // Handle error if pair does not exist or other issues
                // For simplicity, we assume that if an error occurs, the contract will have 0 liquidity
                contracts[i] = UniswapContract(contractAddresses[i], 0);
            }
        }

        // Bubble sort to order contracts by liquidity in descending order
        for (uint256 i = 0; i < contracts.length; i++) {
            for (uint256 j = i + 1; j < contracts.length; j++) {
                if (contracts[i].liquidity < contracts[j].liquidity) {
                    UniswapContract temp = contracts[i];
                    contracts[i] = contracts[j];
                    contracts[j] = temp;
                }
            }
        }

        return contracts;
    }
}
```
