"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlayer-57n.pages.dev
Prompt: Write a smart contract in Solidity that interacts with KyberSwap to perform swaps and distribute earnings to multiple addresses.
Generated: DETERMINISTIC_83f0534bdbe07e4a
Batch ID: 20250612_154542
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

/**
 * @title KyberSwapDistributor
 * @dev A smart contract to interact with KyberSwap for token swaps and distribute earnings to multiple addresses.
 */
 
interface IKyberSwap {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable returns (uint256[] memory amounts);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @dev Main contract to perform swaps and distribute earnings.
 */
contract KyberSwapDistributor {

    address public kyberSwapRouter;
    address public owner;

    // Events
    event TokensSwapped(address indexed sender, uint256 amountIn, uint256 amountOut, address[] path);
    event EarningsDistributed(address indexed sender, uint256 totalAmount, address[] recipients);

    /**
     * @dev Modifier to restrict access to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _kyberSwapRouter) {
        kyberSwapRouter = _kyberSwapRouter;
        owner = msg.sender;
    }

    /**
     * @dev Function to perform a token swap via KyberSwap.
     * @param tokenIn Address of the token to swap from.
     * @param tokenOut Address of the token to swap to.
     * @param amountIn Amount of tokenIn to swap.
     * @param amountOutMin Minimum acceptable amount of tokenOut.
     * @param path Swap path (token addresses).
     * @param deadline Transaction deadline (timestamp).
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external onlyOwner {
        IERC20(tokenIn).approve(kyberSwapRouter, amountIn);

        uint256[] memory amounts = IKyberSwap(kyberSwapRouter).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            deadline
        );

        emit TokensSwapped(msg.sender, amountIn, amounts[amounts.length - 1], path);
    }

    /**
     * @dev Function to distribute earnings to multiple recipients.
     * @param token Address of the token to distribute.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts to send (matching recipients).
     */
    function distributeEarnings(
        address token,
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        uint256 totalAmount = 0;

        for (uint256 i = 0; i < recipients.length; i++) {
            require(IERC20(token).transfer(recipients[i], amounts[i]), "Transfer failed");
            totalAmount += amounts[i];
        }

        emit EarningsDistributed(msg.sender, totalAmount, recipients);
    }

    /**
     * @dev Function to retrieve the balance of a token held by the contract.
     * @param token Address of the token.
     * @return Balance of the token in the contract.
     */
    function getTokenBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }

    /**
     * @dev Function to withdraw any leftover ETH in the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH balance");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
