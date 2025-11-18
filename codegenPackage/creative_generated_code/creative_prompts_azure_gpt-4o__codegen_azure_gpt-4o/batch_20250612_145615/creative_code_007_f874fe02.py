"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kyberswaps.pages.dev
Prompt: Develop a smart contract that interacts with KyberSwap for swapping tokens and distributing rewards to multiple addresses.
Generated: DETERMINISTIC_f874fe02cc6af810
Batch ID: 20250612_145615
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
 * @title TokenSwapRewardDistributor
 * @dev A smart contract that interacts with KyberSwap for swapping tokens
 *      and distributing rewards to multiple addresses.
 */
interface IKyberSwap {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

interface IERC20 {
    function transfer(address recipient, uint amount) external returns (bool);
    function approve(address spender, uint amount) external returns (bool);
    function balanceOf(address account) external view returns (uint);
}

contract TokenSwapRewardDistributor {
    address public owner;
    IKyberSwap public kyberSwap;

    // Events for logging
    event TokensSwapped(address indexed tokenIn, address indexed tokenOut, uint amountIn, uint amountOut);
    event RewardsDistributed(address indexed token, uint totalAmount, address[] recipients);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to set the KyberSwap router address and owner.
     * @param _kyberSwap Address of the KyberSwap router contract.
     */
    constructor(address _kyberSwap) {
        require(_kyberSwap != address(0), "KyberSwap address cannot be zero");
        owner = msg.sender;
        kyberSwap = IKyberSwap(_kyberSwap);
    }

    /**
     * @dev Swaps tokens via KyberSwap.
     * @param tokenIn Address of the input token.
     * @param tokenOut Address of the output token.
     * @param amountIn Amount of input tokens to swap.
     * @param amountOutMin Minimum amount of output tokens expected.
     * @param path Path of token addresses for the swap.
     * @param deadline Timestamp by when the swap must be executed.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        uint deadline
    ) external onlyOwner {
        require(IERC20(tokenIn).balanceOf(address(this)) >= amountIn, "Insufficient token balance");
        
        // Approve KyberSwap to spend tokens
        IERC20(tokenIn).approve(address(kyberSwap), amountIn);

        uint[] memory amounts = kyberSwap.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            deadline
        );

        emit TokensSwapped(tokenIn, tokenOut, amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Distributes rewards (tokens) to a list of recipient addresses.
     * @param token Address of the reward token.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts to distribute.
     */
    function distributeRewards(
        address token,
        address[] calldata recipients,
        uint[] calldata amounts
    ) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        uint totalAmount = 0;

        for (uint i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            IERC20(token).transfer(recipients[i], amounts[i]);
            totalAmount += amounts[i];
        }

        emit RewardsDistributed(token, totalAmount, recipients);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint amount) external onlyOwner {
        uint balance = IERC20(token).balanceOf(address(this));
        require(balance >= amount, "Insufficient contract balance");

        IERC20(token).transfer(owner, amount);
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
