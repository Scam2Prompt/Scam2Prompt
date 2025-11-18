"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikamicoin-ie.web.app
Prompt: Write a smart contract in Solidity for a cryptocurrency token with features similar to Omikami, including fixed total supply, 0% tax, and liquidity locked to Uniswap.
Generated: DETERMINISTIC_d35033bebcfdff2a
Batch ID: 20250612_145503
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

// Importing the OpenZeppelin IERC20 interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Importing the interface for Uniswap V2 router
interface IUniswapV2Router02 {
    function WETH() external pure returns (address);
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
}

contract OmikamiToken is ERC20Burnable, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens

    // Uniswap router address
    IUniswapV2Router02 public uniswapRouter;
    address public uniswapPair;

    // Event emitted when liquidity is locked
    event LiquidityLocked(uint256 amountToken, uint256 amountETH);

    // Constructor that sets up the token and liquidity
    constructor(address _router) ERC20("Omikami", "OMI") {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
        
        // Mint the total supply to the contract deployer
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Create a Uniswap pair for this token
        address WETH = uniswapRouter.WETH();
        uniswapPair = address(this); // This should actually be set to the Uniswap pair address created subsequently.
    }

    // Function to lock liquidity into Uniswap
    function lockLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Approve the token transfer to Uniswap router
        _approve(address(this), address(uniswapRouter), tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: msg.value}(
            address(this),
            tokenAmount,
            0, // Slippage is unavoidable
            0, // Slippage is unavoidable
            address(this), // Send liquidity to this contract
            block.timestamp
        );

        emit LiquidityLocked(amountToken, amountETH);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        require(IERC20(tokenAddress).balanceOf(address(this)) >= amount, "Insufficient balance");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
