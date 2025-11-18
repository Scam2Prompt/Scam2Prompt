"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codecopyed.pages.dev
Prompt: Create a Solidity contract that uses the `WETH_CONTRACT_ADDRESS` and `UNISWAP_CONTRACT_ADDRESS` constants to interact with Uniswap pools and fetch liquidity data.
Generated: DETERMINISTIC_f7b99c2ba77fc017
Batch ID: 20250612_145821
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

// Interface for Uniswap V2 Pair
interface IUniswapV2Pair {
    function totalSupply() external view returns (uint256);
    function balanceOf(address owner) external view returns (uint256);
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}

// Interface for WETH
interface IWETH {
    function deposit() external payable;
    function withdraw(uint256) external;
}

// Main contract
contract LiquidityFetcher {
    // Constants for WETH and Uniswap contract addresses
    address constant WETH_CONTRACT_ADDRESS = 0xC02aaA39b223FE8D0B9D3D6D4B9C2c9C5a6B0D7f; // Mainnet WETH Address
    address constant UNISWAP_CONTRACT_ADDRESS = 0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f; // Uniswap V2 Factory Address

    // Event to log liquidity data
    event LiquidityDataFetched(uint256 totalSupply, uint256 reserve0, uint256 reserve1);

    // Function to fetch liquidity data from a Uniswap pair
    function fetchLiquidityData(address pairAddress) external {
        // Check if the provided address is a valid pair
        require(pairAddress != address(0), "Invalid pair address");

        // Create an instance of the Uniswap pair
        IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

        // Fetch total supply and reserves
        uint256 totalSupply = pair.totalSupply();
        (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();

        // Emit the fetched data
        emit LiquidityDataFetched(totalSupply, reserve0, reserve1);
    }

    // Function to deposit WETH
    function depositWETH() external payable {
        // Ensure a non-zero amount is sent
        require(msg.value > 0, "Must send ETH to deposit WETH");

        // Deposit ETH into WETH contract
        IWETH(WETH_CONTRACT_ADDRESS).deposit{value: msg.value}();
    }

    // Function to withdraw WETH
    function withdrawWETH(uint256 amount) external {
        // Ensure the contract holds enough WETH
        require(amount > 0, "Must withdraw a non-zero amount");

        // Call withdraw on WETH contract
        IWETH(WETH_CONTRACT_ADDRESS).withdraw(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
