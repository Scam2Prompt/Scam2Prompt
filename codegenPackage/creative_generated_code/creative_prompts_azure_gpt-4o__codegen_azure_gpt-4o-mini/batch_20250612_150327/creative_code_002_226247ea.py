"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-foundation-site.pages.dev
Prompt: Generate code for a smart contract that facilitates swaps between FRAX and other leading stablecoins like USDT and BUSD, referencing the Frax Foundation's technology stack.
Generated: DETERMINISTIC_226247eaac9bd206
Batch ID: 20250612_150327
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

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the contract
contract StablecoinSwap is Ownable {
    // Events for logging swaps
    event SwapExecuted(address indexed user, address indexed inputToken, address indexed outputToken, uint256 inputAmount, uint256 outputAmount);
    
    // Address of the FRAX token
    address public fraxToken;
    
    // Mapping to store the exchange rates for stablecoins
    mapping(address => uint256) public exchangeRates; // Stablecoin => Exchange Rate (in FRAX)

    // Constructor to set the FRAX token address and initial exchange rates
    constructor(address _fraxToken) {
        fraxToken = _fraxToken;
    }

    // Function to update exchange rates (only callable by the contract owner)
    function updateExchangeRate(address stablecoin, uint256 rate) external onlyOwner {
        require(stablecoin != address(0), "Invalid stablecoin address");
        require(rate > 0, "Rate must be greater than zero");
        exchangeRates[stablecoin] = rate;
    }

    // Function to perform the swap between FRAX and stablecoins
    function swap(address inputToken, uint256 inputAmount) external {
        require(exchangeRates[inputToken] > 0, "Unsupported stablecoin");

        // Calculate output amount in FRAX
        uint256 outputAmount = (inputAmount * exchangeRates[inputToken]) / 1e18;

        // Transfer stablecoins from the user to this contract
        IERC20(inputToken).transferFrom(msg.sender, address(this), inputAmount);

        // Transfer FRAX from this contract to the user
        require(IERC20(fraxToken).balanceOf(address(this)) >= outputAmount, "Insufficient FRAX balance in contract");
        IERC20(fraxToken).transfer(msg.sender, outputAmount);

        // Emit the swap event
        emit SwapExecuted(msg.sender, inputToken, fraxToken, inputAmount, outputAmount);
    }

    // Function to withdraw tokens for the owner (in case of emergency)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {}
}
```

This Solidity code defines a smart contract for swapping between FRAX and other leading stablecoins like USDT and BUSD, with proper error handling, documentation, and best practices.
