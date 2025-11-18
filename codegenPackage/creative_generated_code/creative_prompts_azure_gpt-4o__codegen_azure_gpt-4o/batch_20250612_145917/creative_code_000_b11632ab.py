"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoden.pages.dev
Prompt: Write a Solidity contract that uses Uniswap V2 interfaces (`IUniswapV2ERC20`, `IUniswapV2Factory`, `IUniswapV2Pair`) to find newly deployed contracts with specific liquidity requirements, similar to the functionality described in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_b11632ab88a64a7a
Batch ID: 20250612_145917
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

// Import necessary interfaces from Uniswap V2
interface IUniswapV2Factory {
    function allPairs(uint256) external view returns (address);
    function allPairsLength() external view returns (uint256);
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

interface IUniswapV2ERC20 {
    function decimals() external view returns (uint8);
}

contract LiquidityScanner {
    // Address of the Uniswap V2 Factory contract
    address public immutable uniswapFactory;

    // Minimum liquidity threshold for detection
    uint256 public constant MINIMUM_LIQUIDITY = 1 ether;

    // Event to notify when a pair with sufficient liquidity is found
    event PairFound(address indexed pair, address token0, address token1, uint256 liquidityToken0, uint256 liquidityToken1);

    /**
     * @dev Constructor to initialize the contract with the Uniswap V2 Factory address.
     * @param _uniswapFactory Address of the Uniswap V2 Factory contract.
     */
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Factory address cannot be zero");
        uniswapFactory = _uniswapFactory;
    }

    /**
     * @dev Scans all pairs in the Uniswap V2 Factory for sufficient liquidity.
     * @notice Emits PairFound for pairs that meet the liquidity criteria.
     */
    function scanPairsForLiquidity() external {
        uint256 pairCount = IUniswapV2Factory(uniswapFactory).allPairsLength();

        // Iterate through all pairs in the factory
        for (uint256 i = 0; i < pairCount; i++) {
            address pairAddress = IUniswapV2Factory(uniswapFactory).allPairs(i);
            IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

            // Get token addresses
            address token0 = pair.token0();
            address token1 = pair.token1();

            // Fetch reserves
            (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

            // Ensure reserves meet minimum liquidity threshold
            if (reserve0 >= MINIMUM_LIQUIDITY && reserve1 >= MINIMUM_LIQUIDITY) {
                emit PairFound(pairAddress, token0, token1, reserve0, reserve1);
            }
        }
    }

    /**
     * @dev Utility function to fetch the token decimals for a given ERC20 token.
     * @param token Address of the ERC20 token.
     * @return decimals The number of decimals used by the token.
     */
    function getTokenDecimals(address token) external view returns (uint8) {
        return IUniswapV2ERC20(token).decimals();
    }
}
```
