"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.librafinance.org
Prompt: Explain how to set up a smart contract that leverages Libra Finance's stableswap features for efficient trading.
Generated: DETERMINISTIC_5cb78ce9c0bde8a4
Batch ID: 20250612_155554
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

// Import the necessary interfaces for the StableSwap functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Libra Finance StableSwap contract
interface ILibraStableSwap {
    function swap(uint256 amountIn, uint256 minAmountOut, address tokenOut) external returns (uint256 amountOut);
}

// Smart Contract for leveraging Libra Finance's StableSwap features
contract StableSwapTrader is Ownable {
    using SafeMath for uint256;

    // Address of the Libra Finance StableSwap contract
    ILibraStableSwap public stableSwap;

    // Event to log swaps
    event Swapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the StableSwap contract address
    constructor(address _stableSwapAddress) {
        require(_stableSwapAddress != address(0), "Invalid StableSwap address");
        stableSwap = ILibraStableSwap(_stableSwapAddress);
    }

    // Function to execute a swap
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(minAmountOut > 0, "Minimum amount out must be greater than 0");

        // Transfer the input tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the StableSwap contract to spend the tokens
        IERC20(tokenIn).approve(address(stableSwap), amountIn);

        // Execute the swap through the StableSwap contract
        uint256 amountOut = stableSwap.swap(amountIn, minAmountOut, tokenOut);

        // Ensure that the swap was successful
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer the output tokens back to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit the swap event
        emit Swapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to change the StableSwap contract address (only by the owner)
    function setStableSwapAddress(address _newStableSwapAddress) external onlyOwner {
        require(_newStableSwapAddress != address(0), "Invalid StableSwap address");
        stableSwap = ILibraStableSwap(_newStableSwapAddress);
    }
}
```
