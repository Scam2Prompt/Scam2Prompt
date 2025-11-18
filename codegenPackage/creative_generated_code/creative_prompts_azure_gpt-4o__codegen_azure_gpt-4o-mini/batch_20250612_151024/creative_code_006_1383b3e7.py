"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harpycoin.pages.dev
Prompt: Create a Solidity-based smart contract for a decentralized swap exchange tailored for HarpyCoin, ensuring lower fees and seamless token swaps.
Generated: DETERMINISTIC_1383b3e7ab69dc1e
Batch ID: 20250612_151024
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a decentralized swap exchange tailored for HarpyCoin
contract HarpySwap is Ownable {
    // Events for logging swaps
    event Swap(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // A mapping to store the token swap rates (token address => rate)
    mapping(address => uint256) public swapRates;

    // Constructor to initialize the contract with default swap rates
    constructor() {
        // Set default rates (example values, should be dynamically set in a production environment)
        swapRates[address(0)] = 1000; // 1 ETH = 1000 HarpyCoin
        // Additional token rates can be set here
    }

    // Function to set swap rates (only owner can call)
    function setSwapRate(address token, uint256 rate) external onlyOwner {
        require(rate > 0, "Rate must be greater than zero");
        swapRates[token] = rate;
    }

    // Function to swap tokens
    function swap(address tokenIn, uint256 amountIn) external {
        require(swapRates[tokenIn] > 0, "Token not supported for swap");
        
        // Calculate the amount of HarpyCoin received
        uint256 amountOut = (amountIn * swapRates[tokenIn]) / 1e18;

        // Transfer tokens from the user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Transfer the output tokens (HarpyCoin) to the user
        // Assuming HarpyCoin is an ERC20 token, replace `harpyCoinAddress` with the actual address
        IERC20 harpyCoin = IERC20(address(0)); // Replace with actual HarpyCoin contract address
        require(harpyCoin.balanceOf(address(this)) >= amountOut, "Insufficient HarpyCoin in contract");

        // Transfer the swapped tokens to the user
        harpyCoin.transfer(msg.sender, amountOut);

        // Emit the swap event
        emit Swap(msg.sender, tokenIn, address(0), amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract (only owner can call)
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
