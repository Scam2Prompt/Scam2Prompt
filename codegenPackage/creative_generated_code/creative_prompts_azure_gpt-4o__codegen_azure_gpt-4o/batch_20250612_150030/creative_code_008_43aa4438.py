"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.online
Prompt: Generate a smart contract snippet for facilitating ETH to USDC token swaps on the Ethereum network.
Generated: DETERMINISTIC_43aa4438cced7c6a
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready smart contract snippet for ETH to USDC token swaps using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for the Uniswap V2 Router
interface IUniswapV2Router02 {
    function WETH() external pure returns (address);
    function swapExactETHForTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable returns (uint[] memory amounts);
}

// Main smart contract for ETH to USDC swaps
contract EthToUsdcSwap {
    // Address of the Uniswap V2 Router
    address private constant UNISWAP_V2_ROUTER = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D; // Mainnet address

    // Address of the USDC token
    address private constant USDC = 0xA0b86991c6218B36c1d19D4a2e9Eb0cE3606eb48; // Mainnet address

    // Instance of the Uniswap V2 Router
    IUniswapV2Router02 private uniswapRouter;

    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_V2_ROUTER);
    }

    /**
     * @dev Facilitates an ETH to USDC token swap via Uniswap V2.
     * @param amountOutMin Minimum amount of USDC expected to receive.
     * @param deadline Timestamp after which the transaction reverts if not executed.
     * @return amounts Array of token amounts swapped.
     */
    function swapEthToUsdc(uint amountOutMin, uint deadline) external payable returns (uint[] memory amounts) {
        require(msg.value > 0, "Must send ETH to swap");

        // Define the swap path (ETH -> USDC)
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // WETH (wrapped ETH)
        path[1] = USDC;                 // USDC token

        // Perform the swap
        uint[] memory swappedAmounts = uniswapRouter.swapExactETHForTokens{ value: msg.value }(
            amountOutMin,
            path,
            msg.sender, // Send the swapped tokens to the caller
            deadline
        );

        return swappedAmounts;
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw accidentally sent ETH directly to the contract.
     * @param to Address to send the ETH to.
     */
    function withdrawEth(address payable to) external {
        require(to != address(0), "Invalid address");
        to.transfer(address(this).balance);
    }
}
```

This code is a smart contract designed for ETH to USDC swaps via Uniswap V2, following Ethereum mainnet conventions. Be sure to thoroughly test before deploying to production!
