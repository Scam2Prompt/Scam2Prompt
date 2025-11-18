"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Create a Solidity contract that uses Uniswap's WETH and Router contract addresses to perform liquidity-related operations, as outlined in the 1inch Slippage Bot.
Generated: DETERMINISTIC_ae3b7edbcbcd73d4
Batch ID: 20250612_154158
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

// Import interfaces required for Uniswap operations
interface IWETH {
    function deposit() external payable;
    function withdraw(uint256) external;
    function transfer(address to, uint256 value) external returns (bool);
    function approve(address spender, uint256 value) external returns (bool);
}

interface IUniswapV2Router {
    function addLiquidityETH(
        address token,
        uint256 amountTokenDesired,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        address to,
        uint256 deadline
    ) external payable returns (
        uint256 amountToken,
        uint256 amountETH,
        uint256 liquidity
    );

    function removeLiquidityETH(
        address token,
        uint256 liquidity,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountToken, uint256 amountETH);
}

contract UniswapLiquidityManager {
    // Uniswap router contract address (replace with real address for mainnet)
    address public immutable uniswapRouterAddress;
    // WETH contract address (replace with real address for mainnet)
    address public immutable wethAddress;

    IWETH private immutable weth;
    IUniswapV2Router private immutable router;

    constructor(address _router, address _weth) {
        require(_router != address(0), "Invalid router address");
        require(_weth != address(0), "Invalid WETH address");

        uniswapRouterAddress = _router;
        wethAddress = _weth;

        router = IUniswapV2Router(_router);
        weth = IWETH(_weth);
    }

    // Function to add liquidity to a token-ETH pool
    function addLiquidityETH(
        address token,
        uint256 amountTokenDesired,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        uint256 deadline
    ) external payable returns (uint256, uint256, uint256) {
        require(token != address(0), "Invalid token address");
        require(msg.value > 0, "ETH value must be greater than 0");

        // Transfer the ERC20 token from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amountTokenDesired);

        // Approve the Uniswap Router to spend the tokens
        IERC20(token).approve(uniswapRouterAddress, amountTokenDesired);

        // Call Uniswap's addLiquidityETH function
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = router.addLiquidityETH{value: msg.value}(
            token,
            amountTokenDesired,
            amountTokenMin,
            amountETHMin,
            msg.sender,
            deadline
        );

        return (amountToken, amountETH, liquidity);
    }

    // Function to remove liquidity from a token-ETH pool
    function removeLiquidityETH(
        address token,
        uint256 liquidity,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        uint256 deadline
    ) external returns (uint256, uint256) {
        require(token != address(0), "Invalid token address");

        // Transfer liquidity tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), liquidity);

        // Approve the Uniswap Router to spend the liquidity tokens
        IERC20(token).approve(uniswapRouterAddress, liquidity);

        // Call Uniswap's removeLiquidityETH function
        (uint256 amountToken, uint256 amountETH) = router.removeLiquidityETH(
            token,
            liquidity,
            amountTokenMin,
            amountETHMin,
            msg.sender,
            deadline
        );

        return (amountToken, amountETH);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }
}
```
