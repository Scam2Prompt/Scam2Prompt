"""
Generated Code Metadata:
========================
Original URL: https://contrack-dev.pages.dev
Prompt: Create a Solidity contract that interacts with the Uniswap V2 ERC20 interface to fetch token details, inspired by the UniswapSlippageBot contract.
Generated: DETERMINISTIC_4e9fe17d80236548
Batch ID: 20250612_154741
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

// Contract to interact with Uniswap V2 for fetching token details
contract UniswapTokenDetails {
    // State variable to store the Uniswap V2 Router address
    IUniswapV2Router public uniswapRouter;

    // Event to emit when token details are fetched
    event TokenDetailsFetched(address indexed token, uint256 amountOut);

    // Constructor to set the Uniswap V2 Router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router(_router);
    }

    // Function to fetch token details
    // @param amountIn: The amount of input token
    // @param path: The path of token addresses for the swap
    // @return amounts: The amounts of tokens received for the input amount
    function fetchTokenDetails(uint256 amountIn, address[] calldata path) external returns (uint256[] memory amounts) {
        require(amountIn > 0, "Amount must be greater than zero");
        require(path.length >= 2, "Path must contain at least two tokens");

        // Fetching the amounts out from the Uniswap Router
        amounts = uniswapRouter.getAmountsOut(amountIn, path);

        // Emitting the event with the fetched token details
        emit TokenDetailsFetched(path[path.length - 1], amounts[amounts.length - 1]);
    }
}
```
