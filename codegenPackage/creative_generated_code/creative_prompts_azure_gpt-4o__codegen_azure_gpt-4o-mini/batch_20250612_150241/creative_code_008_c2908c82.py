"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-en.web.app
Prompt: Write a Solidity contract to enable instant token swaps between $PEPU and other cryptocurrencies on Pepe Unchained Layer 2.
Generated: DETERMINISTIC_c2908c829d38663e
Batch ID: 20250612_150241
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

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract InstantTokenSwap {
    // State variables
    address public owner;
    IERC20 public pepuToken;  // Instance of $PEPU token contract
    uint256 public swapRate;   // Rate of $PEPU to the other token

    // Events for logging
    event Swapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _pepuToken, uint256 _swapRate) {
        owner = msg.sender;          // Set contract deployer as owner
        pepuToken = IERC20(_pepuToken); // Set $PEPU token address
        swapRate = _swapRate;        // Set the initial swap rate
    }

    // Function to swap tokens
    function swapTokens(address tokenIn, uint256 amountIn) external {
        require(amountIn > 0, "Amount must be greater than zero");
        
        // Transfer input tokens from the user to this contract
        IERC20 inputToken = IERC20(tokenIn);
        require(inputToken.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Calculate the amount of $PEPU tokens to send
        uint256 amountOut = (amountIn * swapRate) / (10 ** 18); // Adjusting for decimals

        // Ensure the contract has enough $PEPU tokens
        require(pepuToken.balanceOf(address(this)) >= amountOut, "Insufficient $PEPU tokens in contract");

        // Transfer the $PEPU tokens to the user
        require(pepuToken.transfer(msg.sender, amountOut), "Transfer of $PEPU failed");

        // Emit an event for the swap
        emit Swapped(msg.sender, tokenIn, address(pepuToken), amountIn, amountOut);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }

    // Function to update the swap rate
    function updateSwapRate(uint256 newRate) external onlyOwner {
        swapRate = newRate;
    }

    // Function to retrieve the contract's balance of a specific token
    function getBalance(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
```
