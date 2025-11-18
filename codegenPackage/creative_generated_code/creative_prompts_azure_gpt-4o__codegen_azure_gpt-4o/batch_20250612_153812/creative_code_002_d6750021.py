"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome-metamask.bravesites.com
Prompt: Generate code in Solidity to implement a smart contract that integrates with Metamask for token swaps on Ethereum-based decentralized exchanges.
Generated: DETERMINISTIC_d675002177308eb4
Batch ID: 20250612_153812
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
 * @title TokenSwap
 * @dev A smart contract for token swaps on Ethereum-based decentralized exchanges.
 *      This contract integrates with MetaMask and supports ERC20 token swaps.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenSwap {
    // Events for logging the swap process
    event SwapInitialized(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Address of the owner
    address public owner;

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "TokenSwap: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Swap tokens function. Integrates with any ERC20-compliant token.
     * @param tokenIn Address of the token being swapped.
     * @param tokenOut Address of the token to receive.
     * @param amountIn Amount of tokenIn to swap.
     * @param amountOutMin Minimum amount of tokenOut expected.
     * @param dexAddress Address of the decentralized exchange router.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address dexAddress
    ) external {
        require(tokenIn != address(0), "TokenSwap: Invalid tokenIn address");
        require(tokenOut != address(0), "TokenSwap: Invalid tokenOut address");
        require(amountIn > 0, "TokenSwap: AmountIn must be greater than 0");
        require(dexAddress != address(0), "TokenSwap: Invalid DEX address");

        // Transfer tokenIn from sender to contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the DEX to spend the tokenIn
        IERC20(tokenIn).approve(dexAddress, amountIn);

        // Interact with the DEX router (Uniswap-like)
        // Note: This assumes the DEX supports a `swapExactTokensForTokens` function.
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        try IDEXRouter(dexAddress).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            block.timestamp
        ) {
            // Emit a successful swap event
            emit SwapInitialized(msg.sender, tokenIn, tokenOut, amountIn, amountOutMin);
        } catch {
            // Revert transaction on failure
            revert("TokenSwap: Swap failed");
        }
    }

    /**
     * @dev Fallback function to receive Ether. Required for refunds from DEX routers.
     */
    receive() external payable {}

    /**
     * @dev Owner-only function to withdraw any stuck Ether from the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "TokenSwap: No ETH balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Owner-only function to withdraw any stuck ERC20 tokens from the contract.
     * @param token Address of the token to withdraw.
     */
    function withdrawTokens(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "TokenSwap: No token balance to withdraw");
        IERC20(token).transfer(owner, balance);
    }
}

/**
 * @dev Interface for a generic DEX router.
 *      This is meant to represent Uniswap-like routers.
 */
interface IDEXRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}
```
