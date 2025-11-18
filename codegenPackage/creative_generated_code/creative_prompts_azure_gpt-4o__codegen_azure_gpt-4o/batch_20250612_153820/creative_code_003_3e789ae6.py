"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://store-uni-app.com
Prompt: Write a Solidity smart contract that integrates with the Uniswap protocol to automate token swaps based on predefined market conditions.
Generated: DETERMINISTIC_3e789ae645f93bc8
Batch ID: 20250612_153820
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

// Import the Uniswap interfaces
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IERC20.sol";

contract AutomatedTokenSwap {
    // Address of the Uniswap V2 Router
    address private constant UNISWAP_V2_ROUTER = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    // Instance of the Uniswap Router
    IUniswapV2Router02 private uniswapRouter;

    // Owner of the contract
    address private owner;

    // Constructor sets the Uniswap Router and initializes owner
    constructor() {
        uniswapRouter = IUniswapV2Router02(UNISWAP_V2_ROUTER);
        owner = msg.sender;
    }

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Function to swap tokens based on predefined market conditions
    // _tokenIn: Token to swap from
    // _tokenOut: Token to swap to
    // _amountIn: Amount of the input token to swap
    // _amountOutMin: Minimum amount of output tokens to accept
    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOutMin
    ) external onlyOwner {
        // Transfer `_amountIn` from the contract owner to this contract
        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);

        // Approve the Uniswap router to spend `_amountIn`
        IERC20(_tokenIn).approve(UNISWAP_V2_ROUTER, _amountIn);

        // Define the path for the swap: _tokenIn -> _tokenOut
        address[] memory path = new address[](2);
        path[0] = _tokenIn;
        path[1] = _tokenOut;

        // Perform the token swap on Uniswap
        uniswapRouter.swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            path,
            msg.sender, // Send swapped tokens back to the owner
            block.timestamp // Deadline for the transaction
        );
    }

    // Withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner, _amount);
    }

    // Function to update the contract owner
    function updateOwner(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid address");
        owner = _newOwner;
    }
}
```
