"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Explain how to use the WETH and Uniswap contract addresses in a Solidity contract for trading purposes.
Generated: DETERMINISTIC_8a8067ef63389da2
Batch ID: 20250612_163817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title UniswapTrader
 * @dev A simple contract to interact with Uniswap for trading ETH to a desired token using WETH.
 *      This contract uses the UniswapV2 Router interface.
 */
interface IUniswapV2Router {
    function swapExactETHForTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable returns (uint[] memory amounts);
}

contract UniswapTrader {
    address public immutable uniswapRouterAddress; // Uniswap V2 Router address
    address public immutable wethAddress; // WETH contract address

    /**
     * @dev Sets the addresses for the Uniswap router and WETH contract.
     * @param _uniswapRouterAddress The address of the Uniswap V2 Router.
     * @param _wethAddress The address of the WETH token contract.
     */
    constructor(address _uniswapRouterAddress, address _wethAddress) {
        require(_uniswapRouterAddress != address(0), "Uniswap router address cannot be zero");
        require(_wethAddress != address(0), "WETH address cannot be zero");
        uniswapRouterAddress = _uniswapRouterAddress;
        wethAddress = _wethAddress;
    }

    /**
     * @dev Swaps ETH for a specified token using Uniswap V2.
     * @param tokenAddress The address of the token to receive.
     * @param amountOutMin The minimum amount of tokens to receive (slippage protection).
     * @param recipient The address to receive the tokens.
     * @param deadline The timestamp by which the trade must be completed.
     */
    function swapETHForTokens(
        address tokenAddress,
        uint amountOutMin,
        address recipient,
        uint deadline
    ) external payable {
        require(msg.value > 0, "Must send ETH to swap");
        require(tokenAddress != address(0), "Token address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");

        // Path for the swap [WETH -> Desired Token]
        address[] memory path = new address[](2);
        path[0] = wethAddress;
        path[1] = tokenAddress;

        // Interact with the Uniswap Router to swap ETH for tokens
        IUniswapV2Router(uniswapRouterAddress).swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            recipient,
            deadline
        );
    }

    /**
     * @dev Allows the contract to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to receive ETH.
     */
    fallback() external payable {}
}
```

This contract utilizes the WETH and Uniswap addresses to facilitate ETH-to-token swaps using the Uniswap V2 router. Make sure to replace the placeholder addresses with the correct WETH and Uniswap router addresses for the desired network (e.g., Mainnet, Testnet).
