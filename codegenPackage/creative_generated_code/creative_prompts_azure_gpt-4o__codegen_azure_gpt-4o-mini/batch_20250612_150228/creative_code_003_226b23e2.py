"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiaoulkqm54mkpjy5t7idjlc2wxddyj7a4cpdrpi4reejwkd4gphke.ipfs.dweb.link
Prompt: Create a smart contract snippet in Solidity for listing $Gou tokens on Uniswap, ensuring compatibility with Ethereum wallets like MetaMask.
Generated: DETERMINISTIC_226b23e2d1f33afe
Batch ID: 20250612_150228
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

// Importing the necessary interfaces from OpenZeppelin and Uniswap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract GouTokenListing is Ownable {
    // The address of the Uniswap V2 Router
    IUniswapV2Router02 public uniswapRouter;
    // The address of the $Gou token
    IERC20 public gouToken;

    // Event for successful liquidity provision
    event LiquidityAdded(uint tokenAmount, uint ethAmount);

    // Constructor to initialize the contract with the token address and Uniswap router
    constructor(address _gouToken, address _uniswapRouter) {
        gouToken = IERC20(_gouToken); // Initialize the Gou token address
        uniswapRouter = IUniswapV2Router02(_uniswapRouter); // Initialize the Uniswap router
    }

    // Function to add liquidity to Uniswap
    function addLiquidity(uint tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(msg.value > 0, "ETH amount must be greater than 0");

        // Approve the Uniswap router to spend the $Gou tokens
        gouToken.approve(address(uniswapRouter), tokenAmount);

        // Add liquidity to the Uniswap pool
        (uint amountToken, uint amountETH, uint liquidity) = uniswapRouter.addLiquidityETH{
            value: msg.value
        }(
            address(gouToken),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner(), // The liquidity will belong to the owner
            block.timestamp
        );

        // Emit an event for the liquidity addition
        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to withdraw tokens that were not used in the liquidity process
    function withdrawUnusedTokens() external onlyOwner {
        uint balance = gouToken.balanceOf(address(this));
        require(balance > 0, "No unused tokens to withdraw");
        gouToken.transfer(owner(), balance);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        uint balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
