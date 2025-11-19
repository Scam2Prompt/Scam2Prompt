"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://contrack-dev.pages.dev
Prompt: Generate a function in Solidity that finds newly deployed contracts on the Uniswap exchange, based on the liquidity provided in the contract.
Generated: DETERMINISTIC_b81e85b05d03df4e
Batch ID: 20250612_161041
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

// Interface for interacting with Uniswap liquidity pools
interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
    function token0() external view returns (address);
    function token1() external view returns (address);
}

contract UniswapLiquidityScanner {
    // Event to emit details of newly deployed contracts with liquidity
    event NewLiquidityContract(
        address indexed pairAddress,
        address indexed token0,
        address indexed token1,
        uint112 reserve0,
        uint112 reserve1
    );

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Only owner allowed");
        _;
    }

    // Function to scan pairs and find newly deployed contracts with liquidity
    function scanLiquidityPairs(address[] calldata pairAddresses) external onlyOwner {
        for (uint256 i = 0; i < pairAddresses.length; i++) {
            address pair = pairAddresses[i];
            
            // Ensure the pair address is a valid contract
            require(isContract(pair), "Invalid pair address: Not a contract");

            try IUniswapV2Pair(pair).getReserves() returns (uint112 reserve0, uint112 reserve1, uint32) {
                // Only emit event if liquidity is provided in the contract
                if (reserve0 > 0 || reserve1 > 0) {
                    address token0 = IUniswapV2Pair(pair).token0();
                    address token1 = IUniswapV2Pair(pair).token1();

                    emit NewLiquidityContract(pair, token0, token1, reserve0, reserve1);
                }
            } catch {
                // Handle errors gracefully, such as when the address is not a Uniswap pair
                continue;
            }
        }
    }

    // Helper function to check if an address is a contract
    function isContract(address addr) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(addr)
        }
        return size > 0;
    }

    // Owner-only function to update the owner of the contract
    function updateOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address: Cannot set zero address as owner");
        owner = newOwner;
    }
}
```
