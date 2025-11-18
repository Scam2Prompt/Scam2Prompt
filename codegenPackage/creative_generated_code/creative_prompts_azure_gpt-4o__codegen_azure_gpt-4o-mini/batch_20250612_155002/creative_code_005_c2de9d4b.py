"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet.de6k46fqs3775.amplifyapp.com
Prompt: Create a smart contract that utilizes Router Nitro for automated cross-chain swaps.
Generated: DETERMINISTIC_c2de9d4b8fba6de0
Batch ID: 20250612_155002
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

// Import Router Nitro interface
import "@routerprotocol/router-sdk/contracts/Router.sol";

contract CrossChainSwap {
    // State variable to hold Router contract address
    Router public router;

    // Event for successful swaps
    event SwapExecuted(address indexed user, uint256 amountIn, uint256 amountOut, string destinationChain);

    // Constructor to set the Router contract address
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        router = Router(_router);
    }

    /**
     * @dev Function to execute a cross-chain swap
     * @param amountIn The amount of tokens to swap
     * @param amountOutMin The minimum amount of tokens to receive
     * @param destinationChain The chain to which the tokens will be sent
     * @param tokenIn The address of the token being swapped
     * @param tokenOut The address of the token being received
     * @param to The address that will receive the output tokens
     * @param deadline The time by which the swap must be completed
     */
    function swapTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        string memory destinationChain,
        address tokenIn,
        address tokenOut,
        address to,
        uint256 deadline
    ) external {
        // Check for sufficient balance and allowance
        require(amountIn > 0, "Amount must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer tokens from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Router to spend tokens
        IERC20(tokenIn).approve(address(router), amountIn);

        // Execute the swap via Router
        try router.swap(
            tokenIn,
            tokenOut,
            amountIn,
            amountOutMin,
            to,
            destinationChain,
            deadline
        ) {
            emit SwapExecuted(msg.sender, amountIn, amountOutMin, destinationChain);
        } catch {
            revert("Swap execution failed");
        }
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any ERC20 tokens from the contract
     * @param token The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw ETH from the contract
     * @param amount The amount of ETH to withdraw
     */
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        payable(msg.sender).transfer(amount);
    }
}

// Interface for ERC20 Token
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
